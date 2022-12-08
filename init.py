import subprocess

try:

    subprocess.call(['sh', './init.sh'])

except IOError:   

    print("Hata")
