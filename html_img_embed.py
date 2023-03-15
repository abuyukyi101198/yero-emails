import re
import base64

def getHTML(filename):
    with open(f'{filename}', 'r') as FILE:
        html = FILE.read()
    return re.split(r'(<img [^>]*>)', html)


def getImg(elem):
    elem = re.split(r'(src=\"[^\"]*\")', elem)
    img = elem[1][5:-1]
    if img[:4] != 'data':
        with open(img, 'rb') as IMG:
            enc = base64.b64encode(IMG.read())
        elem[1] = 'src=\"data:image/png;base64,' + enc.decode('utf-8') + '\"'

    return ''.join(elem)


if __name__ == "__main__":
    filename = input("Enter HTML file: ")

    html_text = getHTML(filename)

    for i, elem in enumerate(html_text):
        if elem[:4] == '<img':
            html_text[i] = getImg(elem)

    with open(f'mails/{filename}', 'w') as MAIL:
        MAIL.write(''.join(html_text))