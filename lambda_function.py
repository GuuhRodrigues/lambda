import json
from log import function_log

def lambda_handler(event, context):
    function_log('Log de execução '+ json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


