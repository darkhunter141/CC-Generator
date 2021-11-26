import  os , random
from typing import Counter 

try :
    import pyfiglet
except  :
    os.system ("pip install pyfiglet")
totaldigits = 16
def banner ():
    os.system ("clear")
    banner1 = pyfiglet.figlet_format("Credit Card")
    banner2 = pyfiglet.figlet_format("       Generator")
    print ("\033[91m"+banner1)
    print("\033[95m"+banner2)

def formula  () :
    inputcvc = int (input("\033[90m Bin : "))
    totalcc = int (input(" QUANTITY : "))
    lapart = str (inputcvc)
    if len(lapart)==0:
        count = 16
    count = len (str (inputcvc))
    totalbin =  int (count)
    genbin = totaldigits-totalbin
    firstnum =  "1"*genbin
    lastnum = "9"*genbin
    binf =  int (firstnum)
    binl = int (lastnum)
    b = 0
    for i in range (totalcc):
        rancc=str(random.randint(binf,binl))
        cc=lapart+rancc
        ranmonth = str (random.randint (1,12))
        smon =str (ranmonth)
        if len(smon)==1:
            month = "0"+smon
            b = month
        else  :
            month =smon
            b = month
        ranyear = str (random.randint(2022,2025))
        cvc = str (random.randint(111,999))
        validcc=cc+"|"+month+"|"+ranyear+"|"+cvc
        open ("cc.txt","a").write(validcc+"\n")
    print (" Done ")
banner()
formula  ()
