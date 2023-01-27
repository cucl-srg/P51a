from useful import local_cmd, ssh_cmd, ssh_connect

def getdeltas(exp,crsid,num):
    local_cmd('tshark -r /home/l51/'+crsid+'/P51aLab3/'+exp+'.erf -V | grep "previous captured" > '
              '/home/l51/'+crsid+'/P51aLab3/'+exp+'_d.txt')
    deltas = []
    with open('/home/l51/'+crsid+'/P51aLab3/'+exp+'_d.txt') as f:
        f.next()
        for i in range(2,num+1):
            delta = f.next()[46:57]
            deltas.append(float(delta)*1000000)
    return deltas
