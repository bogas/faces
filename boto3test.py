import boto3
from PIL import Image
import math
import time

if __name__ == "__main__":

    bucket = 'pinkiimozgbucket'
    sourceFile = 'allen3.png'
    targetFile = 'allen2.png'

    client = boto3.client('rekognition', 'us-east-1')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'S3Object': {'Bucket': bucket, 'Name': sourceFile}},
                                    TargetImage={'S3Object': {'Bucket': bucket, 'Name': targetFile}})

    s3 = boto3.resource('s3')
    localImg1 = 'img1'
    s3.Bucket(bucket).download_file(sourceFile, localImg1)
    img1 = Image.open(localImg1)
    w1,h1 = img1.size

    localImg2 = 'img2'
    s3.Bucket(bucket).download_file(targetFile, localImg2)
    img2 = Image.open(localImg2)
    img2.show()
    w2,h2 = img2.size

    for faceMatch in response['FaceMatches']:
        position1 = faceMatch['Face']['BoundingBox']
        position2 = response['SourceImageFace']['BoundingBox']
        area1 = (math.floor(position1['Left']*w1), math.floor(position1['Top']*h1), math.floor((position1['Left'] + position1['Width'])*w1), math.floor((position1['Top'] + position1['Height'])*h1))
        cropped_img1 = img1.crop(area1)
        cropped_img1.show()
        cropped_img1.save("allenface{0}.png".format(str(time.time())))

        area2 = (math.floor(position2['Left']*w2), math.floor(position2['Top']*h2), math.floor((position2['Left'] + position2['Width'])*w2), math.floor((position2['Top'] + position2['Height'])*h2))
        cropped_img2 = img2.crop(area2)
        cropped_img2.show()
        cropped_img2.save("allenface2.png")






