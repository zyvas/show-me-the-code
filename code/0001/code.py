
import uuid

for var in range(200):
    code = str(uuid.uuid1())
    print code.split('-')[0]

