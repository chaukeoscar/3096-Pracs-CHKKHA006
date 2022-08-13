import os
import subprocess

make_file = "/home/pi/EEE3096S-2022/WorkPackage1/C/makefile"
make_file_bak = "/home/pi/EEE3096S-2022/WorkPackage1/C/make_temp"

p_CHeterodyning_threaded = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/CHeterodyning_threaded.h"
p_CHeterodyning_threaded_bak = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/CHeterodyning_threaded.h.bak"
temp_file = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/temp"

p11 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/p11.csv"
c12 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/c12.csv"
c14 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/c14.csv"
c16 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/c16.csv"

samples = 10


# Run a bash command 
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    if(err.decode("utf-8")!=''):
        print("Something went wrong \n"+err.decode("utf-8"))
    return out

# Print status
def f_done(param, input):
    print("*"*50)
    print(param + " changed to "+str(input))


# Swap file name
def swap_file(file1, file2):
    os.rename(file1, temp_file)
    os.rename(file2, file1)
    os.rename(temp_file, file2)


# Change thread count
def change_thread(thread):
    ori = open(p_CHeterodyning_threaded, "r")
    mod = open(p_CHeterodyning_threaded_bak, "w")

    i = 0
    for line in ori.readlines():
        if i==14:
            mod.writelines("#define Thread_Count "+str(thread)+"\n")
        else:
            mod.writelines(line)
        i = i + 1
    
    ori.close()
    mod.close()

    swap_file(p_CHeterodyning_threaded_bak, p_CHeterodyning_threaded)
    f_done("Thread", thread)

# Change flags
def change_flag(flag):

    ori = open(make_file,"r")
    mod = open(make_file_bak,"w")

    i = 0
    for line in ori.readlines():
        if(i == 2):
            mod.writelines("CFLAGS = -lm -lrt "+flag+"\n")
        else:
            mod.writelines(line)
        i = i + 1
    ori.close()
    mod.close()
    swap_file(make_file, make_file_bak)
    f_done("Flag", flag)

