# Script Name		    : main.py
# Author			    : Shy Ruparel
# Created			    : September 8 2015

# Pulls in data from "data.csv" which is 2 columns wide
# Uses a base image as the background
# Uses the data - school name, and venue address -
# and prints onto the base image
# and saves every image as a .PNG

from PIL import Image, ImageDraw,ImageFont
import csv

# Main image from base.jpg
im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .90

# Text writing onto image
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        im = Image.open('base.jpg').convert('RGBA')

        venueSize = MaxSize
        addressSize = MaxSize/2

        # Grab name and address
        venueName = row[0]
        addressDetails = row[1]

        # Set font and size
        venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
        address = ImageFont.truetype('fonts/Lato.ttf', addressSize)

        draw = ImageDraw.Draw(im)

        # Find size of text
        wVenue, hVenue = draw.textsize(venueName,font=venue)

        # Make size smaller until width is less than size of maxFontW
        while (wVenue > maxFontW):
            venueSize = venueSize - 10
            venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
            wVenue, hVenue = draw.textsize(venueName,font=venue)

        wAddress, hAddress = draw.textsize(addressDetails,font=address)

        while (wAddress > maxFontW):
            addressSize = addressSize - 10
            address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
            wAddress, hAddress = draw.textsize(addressDetails,font=address)

        # Put text onto the image
        draw.text(((W-wVenue)/2,(H-hVenue)/2 + 100), venueName,font=venue, fill="white")
        draw.text(((W-wAddress)/2,((H-hAddress)/2)+hVenue+125), addressDetails,font=address, fill="white")

        # Save out the image
        filename = 'output/' + venueName.strip() + '.png'
        filename = filename.replace (" ", "_")
        print filename
        im.save(filename,'PNG')
