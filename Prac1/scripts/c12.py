import sys
sys.path.insert(0, '/home/pi/3096-Pracs-CHKKHA006/Prac1/scripts')
import optlib

print("*"*50)
print("Preparing C heterodyning benchmark")
optlib.run_cmd("make")
print("*"*50)

ave = 0.0
f = open(optlib.c12, "w")
for i in range(optlib.samples):
    dur = float(optlib.run_cmd("make run").split()[17].decode("utf-8"))
    print("Test "+ str(i+1) +" took "+ str(dur)+" ms")
    f.write(str(dur)+",")
    ave = ave + dur
ave = ave/optlib.samples
f.close()

print("*"*50)
print("C heterodyning benchmark completed, average time is ",ave)
print("*"*50)