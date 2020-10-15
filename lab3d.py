#!/usr/bin/env python3

# Author ID: mjvelota

import subprocess 

p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return str(stdout)

print(free_space())

