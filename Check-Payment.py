import json

def lambda_handler(event, context):
    print('Received Message from Step Function')
    Payment = event['Payment']
    print(Payment)
    
    return event['Payment']
