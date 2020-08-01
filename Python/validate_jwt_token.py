################################################################################
# Validate a JWT token                                                         #
################################################################################

import sys
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
    
def validate_jwt_token(token, secret):
    pos = token.rfind('.')
    if pos < 0:
        return False
    
    header_plus_payload = token[:pos]
    signature = token[pos+1:]
    
    m = hmac.new(secret.encode('utf-8'), digestmod=hashlib.sha256)
    m.update(header_plus_payload.encode('utf-8'))
    d = m.digest()
    
    signature_derived = base64_encode(d)
    
    return signature_derived == signature
    
def decode_jwt_token(token):
    strs = token.split('.')
    header = base64_decode(strs[0])
    payload = base64_decode(strs[1])
    return header, payload
    
def print_usage(script_name):
    print(f'Usage: python {script_name} <token> <secret>')
  
################################################################################
# Main                                                                         #
################################################################################

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage(sys.argv[0])
        sys.exit(-1)

    token = sys.argv[1]
    secret = sys.argv[2]
    
    #token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmdW4td2l0aC1qd3RzIiwic3ViIjoiQXp1cmVEaWFtb25kIiwianRpIjoiZjZjMTA5N2YtY2M0OC00OTQ5LWE2MjctOGI5NGZjNWUzN2JhIiwiaWF0IjoxNTk2MTg1MDAxLCJleHAiOjE1OTYxODUwNjF9.UXvXY97CNcHv7LobrBagePBPeGiW2F-Z-nuINSmUy5k'
    #secret = 'my-secret'

    is_valid = validate_jwt_token(token, secret)
    print(f'** is_valid: {is_valid} **')
    if is_valid:
        header, payload = decode_jwt_token(token)
        print(header)
        print(payload)
