import json

def lambda_handler(event, context):
    print('Received Message from Step Function')
    Email = event['Email']
    print(Email)
    
    return event['Email']
