import socket
from lib import driver
from time import sleep
from PIL import Image, ImageDraw

def getIPAddress():
    ip = 'default'
    test_server = "google.com"
    port = 80
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.settimeout(10)
    try:
        sck.connect((test_server, port))
        ip = sck.getsockname()[0]
    except socket.error:
        ip = 'No connect to the network'
    finally:
        sck.close()
    return (ip)

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
