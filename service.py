# -*- coding: utf-8 -*-
#pyblic to acess aws
import boto3
#random number (0/1)
import random
#json lib
import json

def handler(event, context):
	#serviço rekognition
    client=boto3.client('rekognition')

    #s3 das imagens
    bucket='hackadasa'
    #imagem salva a ser analisada
    photo='guia_1.png'

    #analise OCR
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    #lendo todos os textos encontros
    textDetections=response['TextDetections']
        
    result = {"data":[]}

    for text in textDetections:
	    #print( 'Detected text:' + text['DetectedText'][3:] + ' Value: ' + str(random.randint(0,1)))
	    result["data"].append({'exam':text['DetectedText'],
	                           'chk':random.randint(0,1)})

    json_data = json.dumps(result)

    return {
        "statusCode": 200,
        "headers": { "content-type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json_data
    }