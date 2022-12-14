import sys
sys.path.insert(0, '/home/pi/3096-Pracs-CHKKHA006/Prac1/scripts')
import optlib

nFlags = ["-O0", "-O1", "-O2", "-O3"]
sFlags = ["-Ofast", "-Os", "-Og", "-funroll-loops"]

optlib.change_thread(1)

f = open(optlib.c16, "w")

def run_bench(flag):
    optlib.change_flag(flag)
    optlib.run_cmd("make threaded")

    data = []
    data.append(flag+',')
    ave = 0.0
    for i in range(optlib.samples):
        dur = float(optlib.run_cmd("make run_threaded").split()[19].decode("utf-8"))
        data.append(str(dur)+',')
        ave = ave + dur
        print("Test "+str(i+1)+" took "+str(dur)+" ms")

    ave = ave/optlib.samples
    data.append(str(ave)+',')
    print("Average over "+str(optlib.samples)+" is ",ave)
    f.writelines(''.join(data)+"\n")

for nFlag in nFlags:
    run_bench(nFlag)

for sFlag in sFlags:
    run_bench(sFlag)

for nFlag in nFlags:
    for sFlag in sFlags:
        run_bench(nFlag+" "+sFlag)

f.close()