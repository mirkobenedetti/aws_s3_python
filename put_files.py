import boto3
 
 
s3 = boto3.client('s3')
 
bucket_name = input("Please enter the name of your Bucket: ")
file_name = input("Please enter the name of your file: ")
 
file_handler = open(file_name, "rb") 
 
response = s3.put_object(
    ACL = 'private',
    Body = file_handler,
    Bucket = bucket_name,
    Key = file_name
)