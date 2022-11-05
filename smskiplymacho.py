import requests, os

def logo():
  print("""

            | 📨 Sms-Kiplymacho 📩
              Admin +6285751032225

""")

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Di Awali (8xxx)")
  nomor = input("Nomer Target : 0")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get ("https://ainxbot-sms.herokuapp.com/api/Spamsms",params={"phone":nomor}).text
      if 'terkirim' in req:
           print("\nSpam Terkirim")
      else:
           print("\nSpam Gagal")
           os.system('clear')

menu()
