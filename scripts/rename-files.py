import os
import re
import shutil

os.chdir("----firefox screenshot pictures' directory path----")

for f in os.listdir():
    new_name = re.sub('^Screenshot_\d{4}-\d{2}-\d{2} ', '', f)  # or new_name = f[22:]
    os.rename(f, new_name)
    shutil.move(new_name, "----processed screenshot pictures' directory path----")
