import logging
from unittest import result

import azure.functions as func
from PIL import Image
import io
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os
import tempfile
import base64
import json
import uuid

def main(imagein: func.InputStream, imageresult: func.Out[str], context: func.Context):
   
    region = os.environ['ACCOUNT_REGION']
    key = os.environ['ACCOUNT_KEY']
    credentials = CognitiveServicesCredentials(key)
    visionClient = ComputerVisionClient(
        endpoint="https://" + region + ".api.cognitive.microsoft.com/",
        credentials=credentials
    )

    image = Image.open(imagein)

    #image.thumbnail((128,128))

    img_byte_arr = io.BytesIO()
    
    image.convert('RGB').save(img_byte_arr, format='JPEG')

    fp = tempfile.TemporaryFile()
    fp.write(img_byte_arr.getvalue())
    fp.seek(0)

    description_result  = visionClient.describe_image_in_stream(fp)    

    summarized_captions_arr = []
    if (len(description_result.captions) == 0):
        print("No description detected.")
    else:
        for caption in description_result.captions:
            summarized_captions_arr.append("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
            
    summarized_captions = ',\n'.join(summarized_captions_arr)

    image.thumbnail((256,256))
    img_byte_arr_resized = io.BytesIO()
    
    image.convert('RGB').save(img_byte_arr_resized, format='JPEG')

    imageBase64 = base64.b64encode(img_byte_arr_resized.getvalue()).decode("utf-8")

    rowKey = str(uuid.uuid4())

    data = {
        "image": imageBase64,
        "name": imagein.name,
        "description": summarized_captions,
        "PartitionKey": "imageresults",
        "RowKey": rowKey
    }

    imageresult.set(json.dumps(data))

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {imagein.name}\n"
                 f"Blob Size: {imagein.length} bytes")
