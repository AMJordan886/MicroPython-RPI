import machine
import utime
sensor_temp = machine.ADC(26)
conversion_factor = 3.3/(65535)
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    break;
print(temperature)
print(sensor_temp)
utime(27)