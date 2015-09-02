from PIL import Image, ImageDraw,ImageFont
import csv

im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .90

with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        im = Image.open('base.jpg').convert('RGBA')

        venueSize = MaxSize
        addressSize = MaxSize/2

        venueName = row[0]
        addressDetails = row[1]

        venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
        address = ImageFont.truetype('fonts/Lato.ttf', addressSize)

        draw = ImageDraw.Draw(im)

        wVenue, hVenue = draw.textsize(venueName,font=venue)

        while (wVenue > maxFontW):
            venueSize = venueSize - 10
            venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
            wVenue, hVenue = draw.textsize(venueName,font=venue)

        wAddress, hAddress = draw.textsize(addressDetails,font=address)

        while (wAddress > maxFontW):
            addressSize = addressSize - 10
            address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
            wAddress, hAddress = draw.textsize(addressDetails,font=address)


        draw.text(((W-wVenue)/2,(H-hVenue)/2 + 100), venueName,font=venue, fill="white")
        draw.text(((W-wAddress)/2,((H-hAddress)/2)+hVenue+125), addressDetails,font=address, fill="white")

        filename = 'output/' + venueName.strip() + '.png'
        filename = filename.replace (" ", "_")
        print filename
        im.save(filename,'PNG')
