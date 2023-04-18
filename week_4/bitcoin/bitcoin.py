import requests
import sys

def main():

    len_argv = len(sys.argv)

    if len_argv == 1:
        sys.exit('Missing command-line argument')
    elif len_argv >= 3:
        sys.exit('Too much command-line argument')
    else:
        try:
            bitcoin = float(sys.argv[1])
        except ValueError:
            sys.exit('Missing command-line argument')

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        pass

    json_file = r.json()
    rate_string = json_file['bpi']['USD']['rate']
    rate = float(rate_string.replace(',',''))

    dollar = bitcoin * rate
    print(f'${dollar:,.4f}')


if __name__ == "__main__":
    main()