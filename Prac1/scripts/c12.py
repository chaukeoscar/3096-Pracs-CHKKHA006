import optlib

print("*"*50)
print("Preparing C heterodyning benchmark")
print("*"*50)

f = open(optlib.c12, "w")
for i in range(optlib.samples):
    dur = float(optlib.run_cmd("python3 PythonHeterodyning.py").split()[17].decode("utf-8"))
    print("Test "+ str(i+1) +" took "+ str(dur)+" secs")
    f.write(str(dur)+",")
    ave = ave + dur
ave = ave/optlib.samples
f.close()

print("*"*50)
print("C heterodyning benchmark completed, average time is ",ave)
print("*"*50)