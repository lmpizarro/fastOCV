from celery import Celery
from pyzbar.pyzbar import decode
from PIL import Image, ImageSequence
import numpy as np
import cv2 as cv

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def decode_qr(context):
    filename = context['filename']
    index = context['index']

    seqimg = Image.open(filename)


    img = ImageSequence.Iterator(seqimg)[index]

    page_cv = np.array(img.convert('L'))
    height = page_cv.shape[0]
    width = page_cv.shape[1]

    img_roi = page_cv[0:int(height/4), int(width/2):width]
    # cv.imwrite(f'image{index}.tiff', img_roi)

    barcodes = decode(img_roi)

    objeto = {"page": index,
              "type": str(barcodes[0].type) if len(barcodes) > 0 else "",
              "barcode": (str(barcodes[0].data)).replace("'", "")[1:]
              if len(barcodes) > 0 else ""}

    return objeto
