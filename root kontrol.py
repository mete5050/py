

if os.geteuid() != 0:
    print("sudo olarak çalıştır ")
else:
    print("Sen root kulanıcısın")


