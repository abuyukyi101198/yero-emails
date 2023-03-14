import re as regex
import base64

if __name__ == "__main__":
    directory = input("Enter working directory: ")
    filename = input("Enter HTML file: ")
    print(directory, filename)

    FILE = open(directory + '/' + filename, "r")
    html_text = FILE.read()
    FILE.close()

    html_split = regex.split(r'(<img [^>]*>)', html_text)
    for index, section in enumerate(html_split):
        if section[:4] == '<img':
            section_split = regex.split(r'(src=\"[^\"]*\")', section)
            img_file = section_split[1][5:-1]
            with open(directory + '/' + img_file, "rb") as IMG:
                img_enc = base64.b64encode(IMG.read())
            src = 'src=\"data:image/png;base64,' + img_enc.decode('utf-8') + '\"'
            section_split[1] = src
            img_tag = ''.join(section_split)
            html_split[index] = img_tag
    html_text = ''.join(html_split)

    html_split = regex.split(r'(background-image: url\([^\)]*\))', html_text)
    for index, section in enumerate(html_split):
        if section[:16] == 'background-image':
            section_split = regex.split(r'(url\([^\)]*\))', section)
            img_file = section_split[1][5:-2]
            with open(img_file, "rb") as IMG:
                img_enc = base64.b64encode(IMG.read())
            src = 'url(data:image/png;base64,' + img_enc.decode('utf-8') + ')'
            section_split[1] = src
            img_tag = ''.join(section_split)
            html_split[index] = img_tag
    html_text = ''.join(html_split)

    FILE = open(directory + '/' + 'new_' + filename, "w")
    FILE.write(html_text)
    FILE.close()
