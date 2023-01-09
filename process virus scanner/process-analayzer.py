import threading
import subprocess
import psutil
from time import sleep
from virustotal import *
 
class thread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)

 
        # helper function to execute the threads

    def get_processes():
        processes_names = []
        processes_id = []

        for proc in psutil.process_iter():
            try:
                # if proc.status() == "running":
                    processes_id.append(proc.pid)
                    processes_names.append(proc.name())
            except psutil.Error:
                pass
        return processes_id,processes_names

    def run(self):
        report={}
        # processes_id,processes_names = get_processes
        while(True):
            processes_names = []
            processes_id = []

            for proc in psutil.process_iter():
                try:
                    # if proc.status() == "running":
                        processes_id.append(proc.pid)
                        processes_names.append(proc.name())
                except psutil.Error:
                    pass


            print("The process of the local memory:\n")
            for i in range(len(processes_id)):
                print(processes_id[i],"---"+processes_names[i])


            # The path to the Bash script you want to execute
            script_path = 'dumping.sh'
            # Read the contents of the script into a string
            with open(script_path, 'r') as f:
                script_contents = f.read()

                # Modify the script contents as desired
            for i in processes_id:
                script_contents='sudo gcore -o cores/core process'
                with open(script_path, 'w') as f:
                    f.write(script_contents)
                            
                # print(processes_id[i],"---"+processes_names[i])
                script_contents = script_contents.replace('process', str(i))
                # print(script_contents)
                
                # Write the modified script contents back to the file
                with open(script_path, 'w') as f:
                    f.write(script_contents)
                # Execute the script using the bash command
                print("start dumping the process: ",i)
                subprocess.run(['bash', script_path])
                print("start scanning the process: ",i)

                results = scan_file("cores/core."+str(i))
                report[i]=results
                print(report)

            print("re-analyze after 20 secondes ")
            sleep(20)
        print("Report of the processes status:\n",report)



    
thread2 = thread();
 
thread2.start()
 
