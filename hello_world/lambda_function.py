
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': "success!"
    }
    return awsgi.response(app, event, context)