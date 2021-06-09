import json

def lambda_handler(event, context):
    name_list = ['Alison', 'John', 'Mike']
    email_list = ['alison@example.com', 'john@example.com', 'ross@example.com']
    payment_list = ['Done', "Pending"]
    
    Name = event[0]
    Email = event[1]
    Payment = event[2]

    if Name in name_list and Email in email_list and Payment in payment_list:
        return "Records are present in the Database, User can enroll for the Course"
    else:
        return "Records are not present in the Database, User cannot enroll for the Course"
