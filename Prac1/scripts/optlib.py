import os
import subprocess

p_CHeterodyning_threaded = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/CHeterodyning_threaded.h"
p_CHeterodyning_threaded_bak = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/CHeterodyning_threaded.h.bak"
temp_file = "/home/pi/EEE3096S-2022/WorkPackage1/C/src/"

p11 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/p11.cvs"
c12 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/c12.cvs"
c14 = "/home/pi/3096-Pracs-CHKKHA006/Prac1/data/c12.cvs"

samples = 10


# Run a bash command 
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    if(err!=''):
        print("Something went wrong")
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
        mod.writelines(line)
        i = i + 1
    
    ori.close()
    ori.close()

    swap_file(p_CHeterodyning_threaded_bak, p_CHeterodyning_threaded)
    f_done("Thread", thread)

# Change flags
def change_flag(flag):

    f_done("Flag", flag)

