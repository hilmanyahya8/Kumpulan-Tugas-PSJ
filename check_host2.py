import subprocess
import multiprocessing

def ipcheck(ip):
    status = subprocess.getstatusoutput("ping -c1 -w2 " + str(ip))
    if status == 0:
        ini = "UP"
    else:
        ini = "DOWN"
    return ("%s;%s\n" %(ip,ini))
def main():
    listIp = ["192.168.1.1", "192.168.1.2", "8.8.8.8", "8.8.4.4"]
	for lis in listIp:
        p = multiprocessing.Process(target=ipcheck, args=(lis,))
        p.start()
        p.join()
		print(p)
   
main()