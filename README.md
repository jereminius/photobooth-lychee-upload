
# Photobooth - Lychee gallery upload

Based on 



- [@Chostakovitch/pychee](https://github.com/Chostakovitch/pychee)


## How to use?

#### When installing the pychee pip package, make sure to install as root.

Copy the lychee_upload.py file to your private folder:
```bash
/var/www/html/private
```

Replace the gallery URL, user and password in the `lychee_upload.py` file.

In your admin settings, under commands, add this to your Post-photo script / command:

```bash
python3 /var/www/html/private/lychee_upload.py "YOUR_LYCHEE_GALLERY_ID" /var/www/html/data/images/%s
```
Replace `"YOUR_LYCHEE_GALLERY_ID"` with your gallery ID.







