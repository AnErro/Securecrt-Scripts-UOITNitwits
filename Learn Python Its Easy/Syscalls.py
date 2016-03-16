import subprocess

def runBash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out  #This is the stdout from the shell command

subprocess.call("ls -a", shell=True)
print ("\n \n \n this is the other ls:", runBash("ls"))
