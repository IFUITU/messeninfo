from datetime import datetime
import random

def upload_file_name(instance, filename): #from where i recieve filename
    ext = filename.split(".")[-1]
    # folders = {"jpg":'img',"jpeg":"img","png":"img","svg":'img'}
    return "{:%Y}/{:%Y-%m-%d-%H-%M-%S}--{}.{}".format(
        # folders.get(ext[1:],"upload"), #get funct of dict if 1_argument exists do or upload
        datetime.now(),datetime.now(),random.randint(1000,9999),ext
    )