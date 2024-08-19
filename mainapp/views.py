from django.shortcuts import render,redirect

# Create your views here.
from django.template import loader
from django.http import HttpResponse
import qrcode
import base64
from PIL import Image
from io import BytesIO

def index(request):

    return render(request,'index.html') 

def counter(request):
    text = request.POST['text']
    img = qrcode.make(text)
    qr_image = img.get_image() # get_image() is a function that stores img in variable qr_img
    stream = BytesIO() # provides an in-memory binary stream, which is stores in stream
    qr_image.save(stream,format='PNG') #it saves the pil image to stream as a png
    qr_image_data = stream.getvalue()
    qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
    context = { 'qr_image_base64':qr_image_base64}

    return render(request,'counter.html',context)