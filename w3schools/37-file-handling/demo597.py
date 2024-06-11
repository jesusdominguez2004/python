# W3Schools, Python Delete Files
# Note: You can only remove empty folders
import os
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder 'myfolder' does not exist")
