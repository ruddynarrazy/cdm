from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest
from time import sleep
import json,re,sys,os,requests,asyncio

c = requests.Session()

if not os.path.exists("session"):
    os.makedirs("session")
   
if len(sys.argv)<2:
   print ("\n\n\n\033[1;32mUsage : python main.py +62")
   sys.exit(1)

banner = f"""\033[1;35m
                                              
eeeee  eeeee e    e eeee eeeee       e  eeeee 
8   8  8   8 8    8 8    "   8       8  8   8 
8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 
88   8 88  8   88   88   88          88 88  8 
88   8 88  8   88   88ee 88ee8       88 88ee8 
                               eeeee
\033[1;36m=============================================
\033[1;32m ~ anthesphong1998@gmail.com ( +201064497134)
\033[1;36m=============================================          
"""
def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m[\033[1;32m+\033[1;30m]\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)
       
def bentar(z):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(z, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m[\033[1;33m!\033[1;30m]\033[1;0m{:2d} \033[1;33mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)
       
ua={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
api_id = 800812
api_hash = "db55ad67a98df35667ca788b97f771f5"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  client.send_code_request(phone_number)
  me = client.sign_in(phone_number, input('\n\n\n\033[1;0mEnter Your Code Code : '))
  
myself = client.get_me()

os.system('clear')
print(banner)

try:
 channel_entity=client.get_entity('@cdm_doge_bot')
 channel_target=client.get_entity('@MathCalcBot')
 for i in range(5000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write("\033[1;30m[\033[1;33m!\033[1;30m] \033[1;33mSending a command")
  sys.stdout.flush()
  client.send_message(entity=channel_entity,message="⏱ Get 0.2 DOGE")
  bentar(17)
  posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
  msg_id = posts.messages[0].message
  msg_eg = msg_id.strip("🔠 Solve the captcha: =❓")
  if posts.messages[0].message.find("You've got") != -1:
    sys.stdout.write("\r\033[1;30m[\033[1;32m+\033[1;30m] \033[1;32mCongratulation! You've got D 0.2 DOGE!\n")
    tunggu(int(17))
  elif posts.messages[0].message.find("you robot") != -1:
    client.send_message(entity=channel_entity,message="I AM NOT A ROBOT")
    sys.stdout.write("\r\033[1;30m[\033[1;33m!\033[1;30m] \033[1;33mI Am not A Robot\n")
    tunggu(int(17))
  elif posts.messages[0].message.find("Solve the captcha") != -1:
    client.send_message(entity=channel_target,message=msg_eg)
    sleep(4)
    conan = client(GetHistoryRequest(peer=channel_target,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    haibara = conan.messages[1].message
    sleep(3)
    client.send_message(entity=channel_entity,message=haibara)
    sys.stdout.write(f"\r\033[1;30m[\033[1;33m-\033[1;30m] \033[1;33m{msg_id}{haibara}\n")
    tunggu(int(10))
  else:
    sys.exit()
    
finally:
   client.disconnect()
