from serial import Serial, SerialException


port = 'COM3'


print(f"Opening {port}")

try:
    with Serial(port, 9600):
        print('How did it open??')
except SerialException as e:
        print(e)
        print(dir(e))


