import boto3
 
 
s3 = boto3.client('s3')
 
bucket_name = input("Please enter the name of your Bucket: ")
 
objects_list = s3.list_objects(
    Bucket = bucket_name
)
 
if 'Contents' in objects_list:
 
    object_keys = []
     
    for object in objects_list['Contents']:
        object_keys.append({'Key': object['Key']})
     
    response = s3.delete_objects(
        Bucket = bucket_name,
        Delete = {
            'Objects': object_keys
        }
    )
 
response = s3.delete_bucket(
    Bucket = bucket_name
)