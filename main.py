import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

# factory reset
ser.write(bytearray([0x5A, 0x04, 0x10, 0x00]))

# set address (change 4th byte)
ser.write(bytearray([0x5A, 0x05, 0x0B, 0x0B, 0x00]))

# save settings
ser.write(bytearray([0x5A, 0x04, 0x11, 0x00]))

while True:
    if ser.in_waiting > 0:
        line = ser.readline()
        print([hex(x) for x in list(line)])

ser.close()
