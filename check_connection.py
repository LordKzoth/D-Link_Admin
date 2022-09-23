import requests
import base64

def get_addr(b64_data:str) -> str:
  addr_bytes = base64.b64decode(b64_data.encode('ascii'))
  return addr_bytes.decode('ascii')

def check_connection(addr:str):
  try:
    response = requests.get(addr, timeout=2.5)
    print('OK')
  except Exception:
    print('Bad connection!')

if __name__ == '__main__':
  addr = 'aHR0cDovLzc3Ljk0LjEyMS4yOTo4Mg=='
  check_connection(get_addr(addr))
