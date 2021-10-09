import glob
import subprocess
from threading import Thread


path = "X:\PATH\TO\TOP\FOLDER"

bad_word = 'sync_all'
bat_files = ""
text_files = glob.glob(path + "/**/*.bat", recursive = True)
threads = []


for line in text_files:
    if bad_word not in line and 'sync' in line:
        print(line)
        try:
            # STDOUT is not thread safe. 
            # So, the lines will be on top of each other etc.

            t = Thread(target=subprocess.call, args=(line,))
            t.start()
            threads.append(t)
        except:
            print("[failed_threading][File:" + __file__)

print(bat_files)

for t in threads:
    t.join()

input() # Wait for user input before closing
