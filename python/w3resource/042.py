# Write a Python program that calls an external command.
# import os
# print(os.system('ls -l'))

# import psutil
# print(psutil.cpu_count())

from subprocess import call
call(["ls", "-l"])
