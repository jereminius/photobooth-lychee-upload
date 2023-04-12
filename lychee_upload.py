#!/usr/bin/env python
# coding=utf-8
from pychee import pychee
from urllib.request import url2pathname
from urllib.parse import urlparse
import sys

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 3:
    print("Error: Please provide an album ID and the path of your photo.")
    print("Usage: python lychee.py album_ID path")
    sys.exit(1)

# Get command line arguments
album_ID = sys.argv[1]
arg_path = sys.argv[2]

# Initialize instance (your Lychee instance URL)
client = pychee.LycheeClient('https://gallery.example.com')

# Login (your user and password
client.login('user', 'password')

# Add a photo in the album

p = urlparse(arg_path)
path_to_your_photo = url2pathname(p.path)
with open(path_to_your_photo, 'rb') as f:
    photo_id = client.add_photo(f, 'photo.jpg', album_ID)['id']

# Logout
client.logout()