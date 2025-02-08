# import os
# import platform
# print("name of the operating system :",os.system)
# print("name of os system :",platform.system())
# print("version of the operating system :",platform.release())
import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())
