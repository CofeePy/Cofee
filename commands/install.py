import os
import platform

if platform.system() == "Windows":
    if os.getcwd() != "C:\\Python27\Lib\cofee":
        if os.path.exists("C:\\Python27\Lib\cofee"):
            os.system("rd C:\\Python27\Lib")
        os.system("move "+os.getcwd()+"")
