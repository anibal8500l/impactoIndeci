import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('suceso')

id              = "00001"
fenomeno        = "temblor"
fecha           = "2019-11-30T00:39:57+00:00"
afectados       = "1"
fallecidos      = "0"
departamento    = "La isla"
distrito        = "Funi"
direccion       = "Fula"

response = table.put_item(
   Item={
        'id': id,
        'fenomeno': fenomeno,
        'fecha': fecha,
        'afectados': afectados,
        'fallecidos': fallecidos,
        'departamento': departamento,
        'distrito': distrito,
        'direccion': direccion
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))