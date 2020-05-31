import os
import subprocess
import os.path as path


eMail = input("\nEnter E-Mail ID for SSH Key\n> ")
sshPass = input("\nSSH Key PassPhrase\n> ")

sshDir = path.join(path.expanduser("~"), ".ssh/")

sshFile = path.join(sshDir, "id_rsa")

try:
    os.mkdir(sshDir)
except FileExistsError:
    print("SSH Directory already exists.")

sshCmd = [
    "ssh-keygen",
    "-q",
    "-t",
    "rsa",
    "-b",
    "4096",
    "-N",
    sshPass,
    "-C",
    eMail,
    "-f",
    sshFile,
]

sshExit = subprocess.run(sshCmd)

if sshExit.returncode != 0:
    quit()

publicKey = ""
with open(f"{sshFile}.pub", "r") as f:
    publicKey = f.read()

# Copy Public key to clipboard using tk
try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(publicKey)
r.update()  # now it stays on the clipboard after the window is closed
r.destroy()

input("Press any key to Exit...")


# subprocess.run(f"clip < {sshFile}.pub")
# ['xclip', '-sel', 'clip', '<', sshFile] for Linux
