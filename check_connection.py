import requests

def check_connection(addr:str):
  try:
    response = requests.get(addr, timeout=2.5)
    print('OK')
  except Exception:
    print('Bad connection!')

if __name__ == '__main__':
  addr = 'http://77.94.121.29:82'
  check_connection(addr)
