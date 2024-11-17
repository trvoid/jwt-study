################################################################################
# Create a JWT token                                                           #
################################################################################

import base64
import hashlib
import hmac

################################################################################
# Functions                                                                    #
################################################################################

def base64_encode(input_as_bytes):
    b = base64.urlsafe_b64encode(input_as_bytes).decode('utf-8')
    return b.rstrip('=')

def base64_decode(input_as_string):
    padding = 4 - len(input_as_string) % 4
    input_as_string = input_as_string + '=' * padding
    return base64.urlsafe_b64decode(input_as_string.encode('utf-8')).decode('utf-8')

def create_jwt_token(header_obj_str, payload_obj_str, secret):
    header = base64_encode(header_obj_str.encode('utf-8'))
    payload = base64_encode(payload_obj_str.encode('utf-8'))
    header_plus_payload = f'{header}.{payload}'
    
    m = hmac.new(secret.encode('utf-8'), digestmod=hashlib.sha256)
    m.update(header_plus_payload.encode('utf-8'))
    d = m.digest()
    signature = base64_encode(d)
    print('** Signature (algorithm: HS256) **')
    print(f'Byte size: {len(d)}')
    print(f'Base64 encoded: {signature}')

    jwt_token = f'{header_plus_payload}.{signature}'
    return jwt_token

header_obj_str = '{\
"typ":"JWT",\
"alg":"HS256"\
}'

payload_obj_str = '{\
"iss":"fun-with-jwts",\
"sub":"AzureDiamond",\
"jti":"f6c1097f-cc48-4949-a627-8b94fc5e37ba",\
"iat":1596185001,\
"exp":1596185061\
}'

secret = 'my-secret'

jwt_token = create_jwt_token(header_obj_str, payload_obj_str, secret)
print('** JWT token (structure: header.payload.signature) **')
print(jwt_token)
