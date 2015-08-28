from PIL import Image, ImageDraw,ImageFont

im = Image.open('base.png').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .66666666

venueName = "University of Texas"
addressDetails = "2317 Speedway, Austin, TX 78712"

venueSize = MaxSize
addressSize = MaxSize/2

venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
address = ImageFont.truetype('fonts/OpenSansRegular.ttf', 100)


draw = ImageDraw.Draw(im)

wVenue, hVenue = draw.textsize(venueName,font=venue)

while (wVenue > maxFontW):
    print venueSize
    venueSize = venueSize - 10
    venue = ImageFont.truetype('fonts/Outage.ttf', venueSize)
    wVenue, hVenue = draw.textsize(venueName,font=venue)

wAddress, hAddress = draw.textsize(addressDetails,font=address)

while (wAddress > maxFontW):
    print addressSize
    addressSize = addressSize - 10
    address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
    wAddress, hAddress = draw.textsize(addressDetails,font=address)


draw.text(((W-wVenue)/2,(H-hVenue)/2), venueName,font=venue, fill="white")
draw.text(((W-wAddress)/2,((H-hAddress)/2)+hVenue+10), addressDetails,font=address, fill="white")


im.show()
