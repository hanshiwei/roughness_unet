"""
    Updated on 2025/03/07
    This script has to be saved in the same directory as these inp files.

    -------------------------------------------------------------------------
    This script can submit multiple abaqus jobs one by one automatically.
    Here, abaqus functions will be used.

    According to the advice of ChatGPT, subprocess can be used to run 'abaqus job' command.

    programmed on 2025/01/23

    calling this script in cmd window as:
    abaqus cae nogui=PythonScriptName.py
"""


from odbAccess import *
from abaqusConstants import *
import job
import os
import sys
import time
from datetime import datetime

full_length = 636

half_crop_grids = 0

sub_times = 1

id_job_start = 10000
id_job_end = 10001

abqinp_dir = "C:\\Abaqus_Works\\roughness_simulation\\abaqus_inp_files"
# change working directory to the directory where the inp files are located
os.chdir(abqinp_dir)

for job_id in range(id_job_start, id_job_end, 1):
	
    os.write(1, b'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    job_name = "abq_surface_L{:03d}um_C{:d}_S{:d}_ID{:05d}".format(full_length, half_crop_grids, sub_times, job_id)  # 
    inp_name = job_name + ".inp"
    inp_path = os.path.join(abqinp_dir, inp_name)
    os.write(1, b'Abaqus inp [%s]\n' % (inp_path))

    odb_name = job_name + ".odb"    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.write(1, b'Current time: %s\n' % current_time.encode())

	#    Parallel Compute with Domains  userSubroutine='UmtPlsFGH96.f',
    job = mdb.JobFromInputFile(name=job_name, inputFileName=inp_path, numCpus=2, numDomains=2)
    job.submit()
    job.waitForCompletion()

    # Print the current time after job completion
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.write(1, b'Job is finished at %s.\n' % (current_time.encode()))
    
    os.write(1, b'Job [%s] is finished.\n' % (job_name))
    os.write(1, b'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')

os.write(1, b'All jobs are finished.\n')

"""
import subprocess
import os
import time

#
input_dir = '/path/to/your/input/files'

# 
input_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.inp')])

# Abaqus
abaqus_command = "abaqus job={} interactive"

#
for input_file in input_files:
    # 
    input_path = os.path.join(input_dir, input_file)
    
    # 
    print(f": {input_file} ...")
    
    # 
    try:
        subprocess.run(abaqus_command.format(input_path), check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f" {input_file} : {e}")
        continue
    


"""