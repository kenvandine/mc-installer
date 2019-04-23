#!/usr/bin/env python3

import os.path
from urllib.request import urlretrieve 
import subprocess
import os
import re


def main():
    urlretrieve("https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_2.1.2482.tar.gz", "minecraft-launcher.tar.gz")
    
    subprocess.call(['tar','-xzf','minecraft-launcher.tar.gz'])
    
main()

