# Script Name       : main.py
# Author            : Shy Ruparel
# Created           : September 8 2015

# Pulls in data from "data.csv" which is 2 columns wide
# Uses a base image as the background
# Uses the data - school name, and venue address -
# and prints onto the base image
# and saves every image as a .PNG

from PIL import Image, ImageDraw,ImageFont
import os.path
import csv
import urllib

# Main image from base.jpg
im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .80

# Text writing onto image
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        im = Image.open('base.jpg').convert('RGBA')

        venueSize = MaxSize
        addressSize = MaxSize/2
        urlSize = MaxSize/2

        # Grab name and address
        venueName = row[0].decode('utf-8')
        addressDetails = row[1].decode('utf-8')
        urlDetails = row[2].decode('utf-8').replace(" ", "+")

        # Set font and size
        venue = ImageFont.truetype('fonts/OpenSansBold.ttf', venueSize)
        address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
        url = ImageFont.truetype('fonts/OpenSansRegular.ttf', urlSize)

        draw = ImageDraw.Draw(im)

        #Check if file already exists.
        filename = 'output/' + venueName.strip().replace ("/", "_") + '.png'
        filename = filename.replace (" ", "_")
        
        if os.path.isfile(filename) == True:
            print filename + " exists."
        else:
            # Find size of text
            wVenue, hVenue = draw.textsize(venueName,font=venue)

            # Make size smaller until width is less than size of maxFontW
            while (wVenue > maxFontW):
                venueSize = venueSize - 10
                venue = ImageFont.truetype('fonts/OpenSansBold.ttf', venueSize)
                wVenue, hVenue = draw.textsize(venueName,font=venue)

            wAddress, hAddress = draw.textsize(addressDetails,font=address)

            while (wAddress > maxFontW):
                addressSize = addressSize - 10
                address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
                wAddress, hAddress = draw.textsize(addressDetails,font=address)

            wUrl, hUrl = draw.textsize(urlDetails,font=url)

            while (wUrl > maxFontW):
                urlSize = urlSize - 10
                url = ImageFont.truetype('fonts/OpenSansRegular.ttf', urlSize)
                wUrl, hUrl = draw.textsize(urlDetails,font=url)

            # Put text onto the image
            draw.text(((W-wVenue)/2,(H-hVenue)/2 ), venueName,font=venue, fill="black")
            draw.text(((W-wAddress)/2,((H-hAddress)/2)+hVenue), addressDetails,font=address, fill="black")
            draw.text(((W-wUrl)/2,H-550), urlDetails,font=url, fill="blue")

            # Save out the image
            im.save(filename,'PNG')
            print filename + " created."