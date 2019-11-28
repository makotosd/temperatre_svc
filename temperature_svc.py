#!/usr/bin/env python3

from flask import Flask
import wiringpi
import os
import struct
from time import sleep


app = Flask(__name__)

@app.route('/')
def index():
    (t, h) = get_temperature()
    return 'Hello: ' + t + " " + h


def get_temperature():
    wiringpi.wiringPiSetup()  # setup wiringpi
    i2c = wiringpi.I2C()  # get I2C
    dev = i2c.setup(0x40)  # setup I2C device
    i2c.write(dev, 0x02)  # HDC1000 CONFIGURATION POINTER
    i2c.write(dev, 0x10)  # send 1byte
    i2c.write(dev, 0x00)  # send 1byte
    sleep((6350.0 + 6500.0 + 500.0) / 1000000.0)
    dataAry = struct.unpack("BBBB", os.read(dev, 4))
    os.close(dev)
    temp = (dataAry[0] << 8) | (dataAry[1])
    hudi = (dataAry[2] << 8) | (dataAry[3])
    temp = ((temp / 65535.0) * 165 - 40)
    hudi = ((hudi / 65535.0) * 100)
    return temp, hudi



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
