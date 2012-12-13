import random, os
fh = open("emulator-arm", "r+b")
fh.seek(2373833,0)
fh.write(str(int(random.random()*1000000000000000)))
fh.close()
#os.system("./emulator -avd andy")

