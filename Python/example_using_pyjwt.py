import jwt
import time
import sys
from datetime import datetime, timedelta

subject='test'
aud='test'
issuer='ASecuritySite'
id="123456"
signer='HS256'
password='my-secret'

if (len(sys.argv)>1):
  subject=str(sys.argv[1])
if (len(sys.argv)>2):
  aud=str(sys.argv[2])
if (len(sys.argv)>3):
  issuer=str(sys.argv[3])
if (len(sys.argv)>4):
  id=str(sys.argv[4])
if (len(sys.argv)>5):
  signer=str(sys.argv[5])
if (len(sys.argv)>6):
  password=str(sys.argv[6])

timeout = datetime.utcnow() + timedelta(seconds=3600)
print(f"Subject:\t{subject}")
print(f"Timeout:\t{timeout}")
print(f"Audience:\t{aud}")
print(f"Issuer:\t\t{issuer}")
print(f"ID:\t\t{id}")
print(f"Signer:\t\t{signer}")
print(f"Password:\t{password}\n")

token = jwt.encode({'aud':aud, 'exp':timeout, 'iss':issuer,'jti':id, 'sub':subject}, password, algorithm=signer)
print(f"Token: {token}\n")
rtn=jwt.decode(token, password, algorithms=signer,audience=aud)
print(f"Decoded: {rtn}")