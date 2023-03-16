import re
import base64

def get_html(f):
    with open(f'{f}', 'r') as FILE:
        html = FILE.read()
    return re.split(r'(<img [^>]*>)', html)


def get_img(e):
    e = re.split(r'(src=\"[^\"]*\")', e)
    img = e[1][5:-1]
    if img[:4] != 'data':
        with open(img, 'rb') as IMG:
            enc = base64.b64encode(IMG.read())
        e[1] = 'src=\"data:image/png;base64,' + enc.decode('utf-8') + '\"'

    return ''.join(e)


if __name__ == "__main__":
    filename = input("Enter HTML file: ")

    html_text = get_html(filename)

    for i, elem in enumerate(html_text):
        if elem[:4] == '<img':
            html_text[i] = get_img(elem)

    with open(f'mails/{filename}', 'w') as MAIL:
        MAIL.write(''.join(html_text))