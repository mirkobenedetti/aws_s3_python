import boto3
 
 
s3 = boto3.client('s3')
 
all_buckets = s3.list_buckets()
 
for bucket in all_buckets['Buckets']:
    print (bucket['Name'])