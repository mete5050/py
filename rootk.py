import os

if os.geteuid() != 0:
    print("Sen root kullanıcısı değilsin")
else:
    print("Sen root kulanıcısın")


