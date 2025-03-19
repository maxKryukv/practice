import shlex
import subprocess

res = subprocess.Popen(["sleep", "10", "&&", "exit", "1"])