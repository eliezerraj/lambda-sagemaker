import boto3
import json

def lambda_handler(event, context):

    # Create a Boto3 client for SageMaker
    client = boto3.client('sagemaker-runtime')

    # Set the name of the SageMaker endpoint to invoke
    endpoint_name = 'xgboost-serverless-ep-fraud-model-v3-2024-04-23-00-41-40'


    # Set the content type of the input data
    content_type = 'application/json'
    # Set the input data
    input_data = {
        'data': ['9.0','23.0','7.0','90.0','4.0','365.0','17.0','263.0','28.0','238.0','97582.0']
    }
    # Convert the input data to JSON format
    payload = json.dumps(input_data)
    print(payload)
        
    content_type = 'text/csv'
    input_data = '9.0,23.0,7.0,90.0,4.0,365.0,17.0,263.0,28.0,238.0,97582.0'

    # Invoke the SageMaker endpoint
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=input_data
    )

    # Get the response from the SageMaker endpoint
    result = response['Body'].read().decode('utf-8')

    # Return the result
    return {
        'statusCode': 200,
        'body': result
    }