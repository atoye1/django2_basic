from django.http import HttpResponse
from io import StringIO, BytesIO
from urllib.parse import quote
from django.http import HttpResponse
import pandas as pd

def response_csv(request):
    df = pd.DataFrame([
        [100, 110, 120],
        [200, 210, 220],
        [300, 310, 320]
    ])


    io = StringIO()
    df.to_csv(io)
    io.seek(0)
    encoded_filename = 'django_csv_test.csv'
    response = HttpResponse(io, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    return response

def response_excel(request):

    df = pd.DataFrame([
        ['a','b','c'],
        ['d','e','f']
            ])
    
    io = BytesIO()
    df.to_excel(io)
    io.seek(0)

    encoded_filename = quote('pandas.xlsx')
    response = HttpResponse(io, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    return response


import requests
from PIL import Image, ImageDraw, ImageFont

def response_pillow(request):
    ttf_path = 'C:/Windows/Fonts/malgun.ttf'

    image_url = 'http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg'
    res = requests.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)

    canvas = Image.open(io).convert('RGBA')

    font = ImageFont.truetype(ttf_path, 40)
    draw = ImageDraw.Draw(canvas)

    text = 'Test for Djang and PIL'
    left, top = 10, 10
    margin =10
    width, height = font.getsize(text)
    right = left+width+margin
    bottom = top+height+margin

    draw.rectangle((left, top, right, bottom), (255,255,244))
    draw.text((15,15), text, font=font, fill=(20,20,20))
    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')
    return response