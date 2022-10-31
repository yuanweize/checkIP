import requests

def checkip(uid):
    
    l=[]
    loca={datainput!!!!!}
    lid=[]
    f = open('access.log','r')
    lines = f.readlines()
    for line1 in lines:
        k=line1.split()
        if 'email' in k[-1].split(':'):
            if k[2].split(':')[0]=='tcp':
                l.append(k[2].split(':')[1])
                lid.append(k[-1].split(':')[1].split('@')[0])
            else:
                l.append(k[2].split(':')[0])
                lid.append(k[-1].split(':')[1].split('@')[0])
    l=list(set(l))
    # loca=ipcache(l)
    lid=list(set(lid))
    
    if uid =='':
        for uid in lid:
            file = open(uid+'.txt','w')
            for line2 in lines:
                if uid in line2:
                    k=line2.split()
                    if k[2].split(':')[0]=='tcp':
                        file.write(k[0]+' '+k[1]+' IP: '+k[2].split(':')[1]+' City:'+loca.get(k[2].split(':')[1])+'        '+k[4].split(':',1)[1]+'\n')
                    else:
                        file.write(k[0]+' '+k[1]+' IP: '+k[2].split(':')[0]+' City:'+loca.get(k[2].split(':')[0])+'        '+k[4].split(':',1)[1]+'\n')
            file.close()
    else:
        file = open(uid+'.txt','w')
        for line3 in lines:
            if uid in line3:
                k=line3.split()
                if k[2].split(':')[0]=='tcp':
                    file.write(k[0]+' '+k[1]+' IP: '+k[2].split(':')[1]+' City:'+loca.get(k[2].split(':')[1])+'        '+k[4].split(':',1)[1]+'\n')
                else:
                    file.write(k[0]+' '+k[1]+' IP: '+k[2].split(':')[0]+' City:'+loca.get(k[2].split(':')[0])+'        '+k[4].split(':',1)[1]+'\n')
        file.close()
    f.close()

def ipcache(l):
    loca={}
    st={}
    for i in l:
        response = requests.get('http://ipinfo.io/'+i+'?token=1b39e3c666cb4a')
        st=response.json()
        loca[i]=st.get('city')
    return loca

if __name__ == "__main__":
    checkip('')






