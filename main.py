import os
import shutil
import sys
import subprocess
sys.path.append('./')

import inquirer
from pyfiglet import Figlet
f = Figlet(font="slant")
msg = f.renderText("Amethyst")
print(msg)
print("")
print("利用は自己責任であり製作者は一切の責任を負いません")
print("")
print("製作者: rusklabo")
print("")

while True: 

    questions = [
        inquirer.List(
            "size",
            choices=["CreateServer","exit"],
            carousel=True,
        )
    ]

    temp = inquirer.prompt(questions)

    s = temp.get("size")

    if s == 'exit':
        quit()

    #if s == 'CreateServer':


