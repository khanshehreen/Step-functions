import json

def lambda_handler(event, context):
    print('Received Message from the Step Function')
    Name = event['Name']
    print(Name)
    
    return event['Name']
