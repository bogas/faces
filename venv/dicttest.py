# mydic = {}
# mydic['karolcia'] = 'laseczka'
# mydic['misia'] = 'pysia'
#
# for key, value in mydic.iteritems():
#     print key, value
import json, ast

slownik = [{u'eventVersion': u'2.0', u'eventTime': u'2018-05-01T16:19:24.876Z',
            u'requestParameters': {u'sourceIPAddress': u'95.155.115.24'},
            u's3': {u'configurationId': u'4fcb1604-6b60-4834-b61a-0e7150c03709',
                    u'object': {u'eTag': u'b5a410a1a3865c91a616fc2fb00f9abf', u'sequencer': u'005AE8938CD3DE8A55',
                                u'key': u'edgar-allen-bro-13577-1286384941-17.jpg', u'size': 72564},
                    u'bucket': {u'arn': u'arn:aws:s3:::pinkiimozgbucket', u'name': u'pinkiimozgbucket',
                                u'ownerIdentity': {u'principalId': u'AUGIRD5O0PFU'}}, u's3SchemaVersion': u'1.0'},
            u'responseElements': {
                u'x-amz-id-2': u'fny1kDRLQ9Gzk2WF27GKPkhJZBJ9xDUDlq7fvvj64hTqA5+OqpI7dsupdCi3gp4bHAUZ/5iBlgc=',
                u'x-amz-request-id': u'2276C930B4E38675'}, u'awsRegion': u'us-east-1',
            u'eventName': u'ObjectCreated:Put',
            u'userIdentity': {u'principalId': u'AUGIRD5O0PFU'}, u'eventSource': u'aws:s3'}]

zmienna = ast.literal_eval(json.dumps(slownik))
print zmienna[0]['s3']['object']['key']
