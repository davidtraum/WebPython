#Returns the current CPU temperature in degrees (celsius)
#Works only under linux. Tested on raspberry pi.
with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
	print(float(file.read())/1000);
	file.close();
