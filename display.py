from lib import driver
from time import sleep
from PIL import Image, ImageDraw

# def getIPaddress
def getIPAddress():
    return 'default'


def main():
    display = driver.OLED_0in95_rgb()
    img = Image.new('RGB', (96, 64), 0)
    canvas = ImageDraw.Draw(img)
    ip = 'default'

    print("Initializing the display")
    display.Init()
    display.clear()
    canvas.text((0,0), 'Current IP address:', fill = "GREEN")
    while True:
        ip = getIPAddress()
        canvas.text((0, 20), ip, fill="WHITE")
        display.ShowImage(display.getbuffer(img))
        sleep(100)

main()
