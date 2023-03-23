import re
import base64


# Function which returns the contents of the index.html
# file as list split at <img> tags, separators included
def get_html():
    with open('index.html', 'r') as FILE:
        html = FILE.read()
    return re.split(r'(<img [^>]*>)', html)


# Function which reads the <img> src, gets the contents
# of the source .png file, and replaces the src attribute
# with the embedded base 64 data of the file
def get_img(e):
    e = re.split(r'(src=\"[^\"]*\")', e)
    img = e[1][5:-1]
    if img[:4] != 'data':
        with open(img, 'rb') as IMG:
            enc = base64.b64encode(IMG.read())
        e[1] = 'src=\"data:image/png;base64,' + enc.decode('utf-8') + '\"'

    return ''.join(e)


if __name__ == "__main__":
    filename = input("Enter HTML file name: ")

    html_text = get_html()

    for i, elem in enumerate(html_text):
        if elem[:4] == '<img':
            html_text[i] = get_img(elem)

    with open(f'templates/samples/{filename}', 'w') as MAIL:
        MAIL.write(''.join(html_text))