############################################
# Users should be advised that this is not #
# a production ready code.                 # 
############################################
import json
import boto3

def lambda_handler(event, context):
    name=event['body']['name']
    version=event['body']['version']
    vpc=event['body']['vpc']
    subnets=getsubnets(vpc)
    
    client= boto3.client('eks',region_name='us-east-1')
    
    response = client.create_cluster(
        name=name,
        version=version,
        roleArn='arn:aws:iam::856426095413:role/eksclusterrole',
        resourcesVpcConfig={
            'subnetIds':subnets,
        }
    )


def getsubnets(vpc):
    region='us-east-1'
    client = boto3.client('ec2',region_name=region)
    subnets = client.describe_subnets(
        Filters=[
            {
                'Name':'vpc-id',           
                'Values':[vpc],
            },
            {
                'Name':'availabilityZone',
                'Values':['us-east-1a','us-east-1b']
            },
        ],
    )
        
    data=[]
    for subnet in subnets['Subnets']:
        data.append(subnet['SubnetId'])
        
    return data