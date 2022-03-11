from operator import length_hint
import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

def send_with_checksum(arr: bytearray):
    s = sum(arr)
    checksum = s & 0xFF
    arr.append(checksum)
    print([hex(i) for i in arr])
    ser.write(arr)

# # disable checksum
# ser.write(bytearray([0x5A, 0x05, 0x08, 0x00, 0x67]))

# factory reset
send_with_checksum(bytearray([0x5A, 0x04, 0x10]))

# set address (change 4th byte)
send_with_checksum(bytearray([0x5A, 0x05, 0x0B, 0x11]))

# save settings
send_with_checksum(bytearray([0x5A, 0x04, 0x11]))

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline()
            # data = [hex(x) for x in list(line)]
            i = 0
            while i < len(data):
                if data[i] == 0x5a:
                    length = data[i + 1]
                    print(length)
                i += 1
except:    
    ser.close()
