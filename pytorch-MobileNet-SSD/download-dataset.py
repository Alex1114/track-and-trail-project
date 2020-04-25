import gdown
import os
import logging
from zipfile import ZipFile

dataset_url = "https://drive.google.com/u/1/uc?id=1NrsDefKZECw6fhPx52-H9d2WCZEjdHTB&export=download"
dataset_name = "dataset"
if not os.path.isdir(dataset_name):
    gdown.download(dataset_url, output=dataset_name + '.zip', quiet=False)
    zip1 = ZipFile(dataset_name + '.zip')
    zip1.extractall(dataset_name)
    zip1.close()
    os.remove("dataset.zip")

print("Finished downloading dataset.") 