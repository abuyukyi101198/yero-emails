# YERO E-mails

This repository contains the HTML contents for automated standard e-mails to be sent to clients.

The `images` directory contains all the images to be embedded in the e-mails in `PNG` format.

The `mails` directory contains the created e-mail HTML files. These files are usage-ready and have all their images
embedded as `base64` using the `html_img_embed.py` Python script.

The `html_img_embed.py` Python script is used to embed the images found in an HTML file. The script is designed to
read `index.html`, locate the `<img>` tags, find the `src` attribute, and read the source image file in binary. Then,
the binary code is encoded in `base64`, and is prepended the prefix `"data:image/png;base64,"`. This `data` is then
placed in the `src` attribute of the `<img>`. The resulting HTML is written to a new file with name provided to the
script under the `mails` directory.

The `index.html` is not tracked by `git`, as it is simply a generator file acting as the template for changing e-mail
contents.

The e-mails have inline-styling using CSS, and contain basic, table-oriented features. Since e-mail clients lack the
CSS rendering capabilities of modern browsers, `<table>` elements are used for layouts, and simple CSS is used for
styling.