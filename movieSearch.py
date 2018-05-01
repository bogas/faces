import boto3

bucket = 'ka-movies'
client = boto3.client('rekognition', 'us-east-1')
collections = client.list_collections(
    MaxResults=123
)
image_to_be_found = 'pacino.jpeg' #keaton.jpg pacino.jpeg
for name in collections['CollectionIds']:
    str(name)
    search = client.search_faces_by_image(
    CollectionId=str(name),
    Image={ 'S3Object': {'Bucket': bucket,'Name': image_to_be_found}},
    MaxFaces=123,
    FaceMatchThreshold=90
    )
    if len(search['FaceMatches']) > 0 :
        print("Face from {0} found in the {1} collection".format(image_to_be_found, str(name)))

