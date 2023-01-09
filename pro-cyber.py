import subprocess



import psutil

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

processes_id,processes_names = get_processes()

for i in range(len(processes_id)):
    print(processes_id[i],"---"+processes_names[i])



# The path to the Bash script you want to execute
script_path = 'dumping.sh'



    # Read the contents of the script into a string
with open(script_path, 'r') as f:
    script_contents = f.read()

    # Modify the script contents as desired
for i in processes_id:
    script_contents='sudo gcore -o Desktop/cores/ process'
    with open(script_path, 'w') as f:
        f.write(script_contents)
                
    # print(processes_id[i],"---"+processes_names[i])
    script_contents = script_contents.replace('process', str(i))
    print(script_contents)
    
    # Write the modified script contents back to the file
    with open(script_path, 'w') as f:
        f.write(script_contents)
    # Execute the script using the bash command
    subprocess.run(['bash', script_path])