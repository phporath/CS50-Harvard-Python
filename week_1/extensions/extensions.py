def main():
    file = input('File name: ').lower().strip()
    type = type_extensions(file)
    print(type)


def type_extensions(x):
    if x.endswith('.gif'):
        return 'image/gif'
    elif x.endswith('.jpg'):
        return 'image/jpeg'
    elif x.endswith('.jpeg'):
        return 'image/jpeg'
    elif x.endswith('.png'):
        return 'image/png'
    elif x.endswith('.pdf'):
        return 'application/pdf'
    elif x.endswith('.txt'):
        return 'text/plain'
    elif x.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'


main()