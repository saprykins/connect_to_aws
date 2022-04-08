import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='region')
text = "It is raining today in Seattle"

#     s3 = boto3.resource('s3',
        # aws_access_key_id=ACCESS_ID,
         # aws_secret_access_key= ACCESS_KEY)


print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectEntities\n')
