import subprocess

def run(cmd):
	p = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(out, err) = p.communicate()
	return out

print("Starting Python Heterodyning benchmarking")
ave = 0.0
f = open("PyBan.csv", "w")
for i in range(10):
	t = float(run("python3 PythonHeterodyning.py").split()[23].decode("utf-8").split(':')[2])
	print("Test "+ str(i+1) +" took "+ str(t)+" ms")
	f.write(str(t)+",")
	ave = ave + t

ave = ave/10
f.write(str(ave))
f.close()
print("Data ready, Avarege over 10 samples is "+str(ave))
print('*'*40)
run("mv PyBan.csv /home/pi/3096-Pracs-CHKKHA006/Prac1/data")
run("mv pythondata.py /home/pi/3096-Pracs-CHKKHA006/Prac1/scripts")
print("Data and script added to github folder")

