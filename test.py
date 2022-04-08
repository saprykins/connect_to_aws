import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
text = "William leaves in Seattle"

# print('Calling DetectEntities')
dict = comprehend.detect_entities(Text=text, LanguageCode='en')
entities = dict["Entities"]

array_of_named_entities = []

for entity in entities: 
    if entity["Type"] == 'PERSON':
        array_of_named_entities.append(entity["Text"])

print(array_of_named_entities)
