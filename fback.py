import json
import argparse
from urllib.parse import urlparse
import os
def Fback():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', required=True, default=False, metavar="Full url eg.: api.v1.apple.com [!]Note: you should use this oprtion even if you declare a list of urls", type=str)
    parser.add_argument('-l', required=False, default=False, metavar='url list. [!]The output of this list will be saved in a file named urdomain.backs', type=str)
    parser.add_argument('-w', required=False, default=False, metavar='words to use', type=str)
    parser.add_argument('-d', required=False, default=False, metavar='Specify the range of date to use eg.: 2020-2023', type=str)

    args = parser.parse_args()
    #I hardcoded this words cus its easier, try to use a wordlist and make it dynamic
    ext = ("back", "backup", "bak", "bck", "bkup", "bckp", "bk", "backupdb", "old", "swp", "tmp", "backup1", "bak2", "bak3", "bdb", "log", "save", "sav", "orig", "copy", "sh", "bash", "new","zip", "rar", "tar.gz", "7z", "bz2", "tar", "gzip", "bzip", "bz")
    sen_words = ("web","fullbackup","backup","data","site","assets","logs","web","debug","install")
    dir = os.path.expanduser('~/scopes/backup')
    if args.u.find('https')==-1:
       url = 'https://'+args.u
    else:
       url = args.u
    parsedurl = urlparse(url)
    full_domain = parsedurl.netloc
    domain = full_domain.split('.')[-2]+'.'+full_domain.split('.')[-1]
    subdomain = full_domain.replace('.'+domain,'')
    host = full_domain.split('.')[-2]
          #Read list of urls V               
    if args.l:
      urlist=[]
      f = open(f"{domain}.backs","a+")
      line = open(args.l,"r")
      while True:
        w = line.readline()
        if len(w) == 0:
          break
        w = w.replace('\n','')
        if w.endswith('/'):
          continue
        urlist.append(w)
      for l in urlist:
        for m in ext:
          f.write(f"{l}.{m}\n")
      f.close()  
    #print(f"full domain:{full_domain}\ndomain:{domain}\nsubdomain:{subdomain}")  
    backs = []

    #with open(f"{dir}/{domain}.backup", "a+") as file:
    for ext in ext:
      
      backs.append(f"{full_domain}.{ext}")
      backs.append(f"{domain}.{ext}")
      backs.append(f"{subdomain}.{ext}")
      backs.append(f"{host}.{ext}")
      backs.append(f"{subdomain}{host}.{ext}")
      for w in sen_words:
        backs.append(f"{full_domain}.{w}.{ext}")
        backs.append(f"{domain}.{w}.{ext}")
        backs.append(f"{subdomain}.{w}.{ext}")
        backs.append(f"{host}.{w}.{ext}")
        backs.append(f"{subdomain}{host}.{w}.{ext}")
        backs.append(f"{w}.{ext}")
        backs.append(f"{w}{full_domain}.{ext}")
        backs.append(f"{w}{domain}.{ext}")
        backs.append(f"{w}{subdomain}.{ext}")
        backs.append(f"{w}{host}.{ext}")
        backs.append(f"{w}{subdomain}.{ext}")
        for i in range(1,11):
          backs.append(f"{full_domain}.{w}{i}.{ext}")
          backs.append(f"{domain}.{w}{i}.{ext}")
          backs.append(f"{subdomain}.{w}{i}.{ext}")
          backs.append(f"{host}.{w}{i}.{ext}")
          backs.append(f"{subdomain}{host}.{w}{i}.{ext}")
      for i in range(1,11):
        backs.append(f"{full_domain}{i}.{ext}")
        backs.append(f"{domain}{i}.{ext}")
        backs.append(f"{subdomain}{i}.{ext}")
        backs.append(f"{host}{i}.{ext}")
        backs.append(f"{subdomain}{host}{i}.{ext}")
      #Using Dates V
      if args.d:
         date = args.d.split('-')
         for y in range(int(date[0]),int(date[1])):                             
          backs.append(f"{domain}.{y}.{ext}")
          for m in range(1,13):
             for d in range(1,31): 
              backs.append(f"{y}-{m}-{d}.{ext}")
              backs.append(f"{full_domain}.{y}-{m}-{d}.{ext}")
              backs.append(f"{full_domain}.{y}{m}{d}.{ext}")
              backs.append(f"{domain}.{y}-{m}-{d}.{ext}")
      #Read list of words V
      if args.w:
        line = open(args.w, "r")
        while True:
          if len(line.readline()) == 0:
            break
          w = line.readline().replace('\n','')
          backs.append(f"{w}.{ext}") 



    for i in backs:
       print(f"{i}")
if __name__ == '__main__':
    Fback()