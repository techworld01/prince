# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")
 
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		
 
##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER TECHWORLD>
 \033[1;96m
▀█▀ █▀▀ █▀▀ █░█
░█░ ██▄ █▄▄ █▀█
\033[1;91m  _ 
\033[1;92m 
╭╮╭╮╭┳━━━┳━━━┳╮╱╱╭━━━╮
┃┃┃┃┃┃╭━╮┃╭━╮┃┃╱╱╰╮╭╮┃
┃┃┃┃┃┃┃╱┃┃╰━╯┃┃╱╱╱┃┃┃┃
┃╰╯╰╯┃┃╱┃┃╭╮╭┫┃╱╭╮┃┃┃┃
╰╮╭╮╭┫╰━╯┃┃┃╰┫╰━╯┣╯╰╯┃
╱╰╯╰╯╰━━━┻╯╰━┻━━━┻━━━╯
           \033[1;93m  ____    _    ____    _                                           
\033[1;93m        IT'S A TRICKER, MR PRINCE
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : MR PRINCE KUMAR
 FACEBOOK   : https://www.facebook.com/profile.php?id=100009761892563
 YOUTUBE    : https://www.youtube.com/channel/UCncclGZ6Kex00G0UHRF670Q?view_as=subscriber
 GITHUB     : GITHUB.COM/TECHWORLD01
\033[1;32m
--------------------------------------------------
                                """
 
cusr = "techprince"
cpwd = "techprince"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCncclGZ6Kex00G0UHRF670Q?view_as=subscriber')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : techprince (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : techprince (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCncclGZ6Kex00G0UHRF670Q?view_as=subscriber')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : techprince (correct)")
    print(" TOOL PASSWORD : techprince (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Chacking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
 
