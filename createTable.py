import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='suceso',
    KeySchema=[
        {
            'AttributeName': 'fenomeno',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'fecha',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'fenomeno',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'fecha',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)