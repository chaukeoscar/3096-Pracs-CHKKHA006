import sys
sys.path.insert(0, '/home/pi/3096-Pracs-CHKKHA006/Prac1/scripts')
import optlib

optlib.change_flag("-O3 -Ofast")
optlib.change_thread(1)

f = open(optlib.c18, "w")
data = []
for i in range(optlib.samples):
    for i in range(optlib.samples):
        dur = float(optlib.run_cmd("make run_threaded").split()[19].decode("utf-8"))
        data.append(str(dur)+',')
        ave = ave + dur
        print("Test "+str(i+1)+" took "+str(dur)+" ms")

    ave = ave/optlib.samples
    data.append(str(ave)+',')
    print("Average over "+str(optlib.samples)+" is ",ave)
    f.writelines(''.join(data)+"\n")

f.close()
