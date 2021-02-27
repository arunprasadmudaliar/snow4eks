############################################
# Users should be advised that this is not #
# a production ready code.                 # 
############################################
import json
import boto3

def lambda_handler(event, context):
    region= event['body']['region']
    client = boto3.client('ec2',region_name=region)
    vpcs = client.describe_vpcs()

    data=[]
    for vpc in vpcs['Vpcs']:
        data.append({'vpc':vpc['VpcId'],'cidr':vpc['CidrBlock']})
    return data
