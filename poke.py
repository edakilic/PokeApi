import requests

def main():
    req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    print(req.status_code)

if __name__ == '__main__':
    main()