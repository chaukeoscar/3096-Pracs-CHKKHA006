import optlib

print("*"*50)
print("Preparing python heterodyning benchmark")
print("*"*50)

f = open(optlib.p11, "w")
for i in range(optlib.samples):
    dur = float(optlib.run_cmd("python3 PythonHeterodyning.py").split()[23].decode("utf-8").split(':')[2])
    print("Test "+ str(i+1) +" took "+ str(dur)+" secs")
    f.write(str(dur)+",")
    ave = ave + dur
ave = ave/optlib.samples
f.close()

print("*"*50)
print("Python heterodyning benchmark completed average time is ",ave)
print("*"*50)