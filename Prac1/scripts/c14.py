import sys
sys.path.insert(0, '/home/pi/3096-Pracs-CHKKHA006/Prac1/scripts')
import optlib

threads = [1, 2, 4, 8, 16, 32]
f = open(optlib.c14, "w")
for thread in threads:
    optlib.change_thread(thread);
    optlib.run_cmd("make threaded")

    ave = 0.0
    data = []
    data.append("Thread "+str(thread)+',')
    for i in range(optlib.samples):
        dur = float(optlib.run_cmd("make run_threaded").split()[19].decode("utf-8"))
        data.append(str(dur)+',')
        ave = ave + dur
        print("Test "+str(i+1)+"took "+str(dur)+" ms")
    ave = ave/optlib.samples
    f.writelines(''.join(data)+"\n")
    
f.close()