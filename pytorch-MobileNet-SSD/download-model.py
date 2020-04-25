import gdown
import os
import logging
from zipfile import ZipFile

model_url = "https://drive.google.com/a/g2.nctu.edu.tw/uc?id=1uEzOLHiOYycHFO0XKQTyLtH3pOwIC4HA&export=download"
model_name = "models"
if not os.path.isdir(model_name):
    gdown.download(model_url, output=model_name + '.zip', quiet=False)
    zip1 = ZipFile(model_name + '.zip')
    zip1.extractall(model_name)
    zip1.close()
    os.remove("models.zip")

print("Finished downloading model.") 