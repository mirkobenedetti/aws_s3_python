import boto3
 
 
s3 = boto3.client('s3')
 
bucket_name = input("Please enter a name for your Bucket: ")
 
response = s3.create_bucket(
    ACL = 'private',
    Bucket = bucket_name,
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-central-1'
    }
)
