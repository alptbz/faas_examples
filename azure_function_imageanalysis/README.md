# Azure function example - image analysis

This example uses [Azure function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python) (Python programming model v1), [Pillow](https://pypi.org/project/Pillow/) to resize the image, and [Azure Cognitive Services Computer Vision SDK for Python](https://pypi.org/project/azure-cognitiveservices-vision-computervision/) to create a description of the image and [Azure tables](https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme) to store the results. 

The azure function provides a http endpoint to retrieve the stored data. 

The results can be view using the Tkinker example [tkinker_gui_imagealalysis](../tkinker_gui_imagealalysis). 

# Requirements

This example is best tested with Visual Studio Code. 

 - Python 3.10.x
 - Visual Studio Code with extensions:
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Azure functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
   - [Azure account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)
   - [Azure Resources](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureresourcegroups)
   - [Azurite](https://marketplace.visualstudio.com/items?itemName=Azurite.azurite)
 - Azure Computer vision set up in Azure.
 - [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer)

# Steps
 - Install *Visual Studio Code* with extensions
 - The Azure function extension will show a pop up asking to setup azure function, acknowledge and confirm
 - Open this folder with *Visual Studio Code*
 - Rename `local.settings.json.example` to `local.settings.json`
 - Create Computer Vision Resource
 - Define ACCOUNT_KEY and ACCOUNT_REGION in `local.settings.json`
 - Start Azurite `Ctrl+Shift+P` -> `Azurite: Start`
 - Run Function with `F5`
 - Upload file into blob `images` into folder `input` (Storage Account => Emulator) using `Azure Storage Explorer`

# Links
 - [Quickstart: Create a function in Azure with Python using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators)
 - [cognitive-services-quickstart-code - ImageAnalysisQuickstart.py](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py)
 - [yokawasa/azure-functions-python-samples - blob-trigger-watermark-blob-out-binding](https://github.com/yokawasa/azure-functions-python-samples/blob/master/v2functions/blob-trigger-watermark-blob-out-binding/__init__.py)