import boto3
 
 
s3 = boto3.client('s3')
 
bucket_name = input("Please enter the name of your Bucket: ")
file_name = input("Please enter the name of your file: ")
 
response = s3.delete_object(
    Bucket = bucket_name,
    Key = file_name
)