#json is best for pulling data out of a system and sending it btwn 2 systems with minimum fuzz
#python process json

import json
data = '''{
  "name" : "Dan",
  "phone" : {
     "type" : "huawei",
     "number" : "0713455678"
   },
   "email" : {
      "hide" : "yes"
      }
   }'''
   
   
info=json.loads(data)
print('name:',info["name"])
print('Hide:',info["email"]["hide"])
