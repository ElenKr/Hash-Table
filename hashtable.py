from random import randint
import random
import time
count=0
load_factor=0.5

#######################################   δημιουργία πρώτου αριθμού για μήκος πίνακα

def primeGreaterThan1(num):
    while True:
        isPrime = True
        for x in range(2, num):
            if num % x == 0:
                isPrime = False
                break
        if isPrime:
            return num
        num -= 1

######################################     hash function
        
def hashing_func(key,leng):
    z=33
    code=0
    for c in key:
        code=z*code+ord(c)
    return code % leng


####################################      instert

def insert(hash_table,hash_key, customer,day1,collisions):
    found=False
    global count    
    #global collisions
    #θέλω να ελέγχω εάν υπάρχει ο ίδιος πελάτης
    #αν βρω τον ίδιο προσθέτω το ποσό στην αντίστοιχη ημέρα
    #και αυξάνω τον αριθμό των επισκέψεων
    #η δομή της καταχώρησης ειναι customer=(key,val,day)
    #print("πληθος εγγραφων=",count)
    hash_key_init = hash_key
    while hash_table[hash_key] !=None:
        
        if hash_table[hash_key][0]==customer[0]:
           hash_table[hash_key][1][day1]+=customer[1][day1]
           hash_table[hash_key][2][day1]+=customer[2][day1]
           #print("Βρέθηκε ίδιος πελάτης ",hash_table[hash_key])
           
           found=True
           break
        
        # collisions+=1
        hash_key+=1
        
        if hash_key==len(hash_table):
            hash_key=0        
        
    if found==False:    
        hash_table[hash_key]=customer        
        count+=1
        
        if hash_table[hash_key_init] !=None:
            collisions += 1

    n=count/len(hash_table)
    
    if n>=load_factor:
        
        #hash_table,collisions =rehashing(hash_table,collisions)  
        hash_table,collisions=new_rehashing(hash_table,collisions)
        #print(collisions)    
    return hash_table,collisions;

############################################# κάρτα με μεγαλύτερο ποσό πληρωμών

def maxposo(hash_table):
    li1=[]
    li2=[]
    #η δομή της καταχώρησης ειναι customer=(key,val,day)
    plousios1="Kaneis"
    plousios2="kaneis"
    pos=0
    maxx_poso=0
    maxx_visit=0
    aa=0
    temp1=0
    temp2=0
    meraa=" "   
    dayy=6*[0]
    visits=0
    
    dayy=hash_table[pos][2]
    while hash_table[pos]==None:
        pos+=1
    for i in range (0,6):
        maxx_poso=maxx_poso+hash_table[pos][1][i]
        maxx_visit+=hash_table[pos][2][i]
        
    plousios1=hash_table[pos][0]
    plousios2=hash_table[pos][0]
    dayy=hash_table[pos][2]
    
    for j in range(pos,len(hash_table)):
        temp1=0
        temp2=0
        
        if hash_table[j]!=None:
            
            for i in range (0,6):
                temp1=temp1+hash_table[j][1][i]
                temp2+=hash_table[j][2][i]                     
                dayy[i]+=hash_table[j][2][i]

    
        
     
            if temp2>maxx_visit:
                maxx_visit=temp2
                li2=[]
                plousios2=hash_table[j][0]
                li2.append(plousios2)
                
            elif temp2==maxx_visit:
                plousios2=hash_table[j][0]
                li2.append(plousios2)
                
            if temp1>maxx_poso:
                li1=[]
                maxx_poso=temp1
                plousios1=hash_table[j][0]
                li1.append(plousios1)
            elif temp1==maxx_poso:
               plousios1=hash_table[j][0]
               li1.append(plousios1)
               
    visits=dayy[0]
    max_day=0           
    for i in range (0,6):
        if dayy[i]>visits:
            visits=dayy[i]
            max_day=i
            
    meraa=hmera(max_day)
    
    print("η ημέρα με τις περισσότερες επισκέψεις είναι ",meraa," με αριθμό επισκέψεων ",visits)          
    print("η κάρτα με το μεγαλύτερο ποσό πληρωμών ειναι ",li1,"και πλήρωσε συνολικά ",maxx_poso)
    print("οι καρτες με τις περισσότερες επίσκεψεις ειναι ",li2,"και πήγε συνολικά ",maxx_visit)
############################################## κάρτα με τις περισσότερες επισκέψεις

def maxvisit(hash_table):
    
    #η δομή της καταχώρησης ειναι customer=(key,val,day)
    li=[]
    plousios="Kaneis"
    pos=0
    meg=0
    aa=0
    while hash_table[pos]==None:
        pos+=1
    for i in range (0,6):
        meg=meg+hash_table[pos][2][i]
    plousios=hash_table[pos][0] 
        
    for j in range(pos,len(hash_table)):
        ps=0
        if hash_table[j]!=None:
            for i in range (0,6):
                ps=ps+hash_table[j][2][i]
            if ps>meg:
                meg=ps
                li=[]
                plousios=hash_table[j][0]
                li.append(plousios)
            elif ps==meg:
                plousios=hash_table[j][0]
                li.append(plousios)
   

    print("οι καρτες με τις περισσότερες επίσκεψεις ειναι ",li,"και πήγε συνολικά ",meg)
    
################################################ συνολικές επισκέψεις για συγκεκριμένη μέρα

def day_with_max_visit(hash_table):
    
    #η δομή της καταχώρησης ειναι customer=(key,val,day)
    meraa=" " 
    pos=0   
    dayy=6*[0]
    visits=0
    while hash_table[pos]==None:
        pos+=1
    dayy=hash_table[pos][2]
    
    for i in range(pos+1,len(hash_table)):
       if hash_table[i]!=None: 
           for j in range(0,6):
               dayy[j]+=hash_table[i][2][j]

    visits=dayy[0]
    max_day=0
    for i in range (0,6):
        if dayy[i]>visits:
            visits=dayy[i]
            max_day=i
    meraa=hmera(max_day)       
    print("η ημέρα με τις περισσότερες επισκέψεις είναι ",meraa," με αριθμό επισκέψεων ",visits)
    
#############################################
    
def hmera(i):
    if i==0:
        mera="Δευτέρα¨"
    elif i==1:
        mera="Τρίτη"
    elif i==2:
        mera="Τετάρτη"
    elif i==3:
        mera="Πέμπτη"
    elif i==4:
        mera="Παρασκευή"
    else:
        mera="Σάββατο" 
        
    return mera  

    
#############################################   αλλαγή των θέσεων κατα το rehashing
        
def insert_rehas(hash_table,hash_key, customer,collisions):
    
    if hash_table[hash_key] !=None:
        collisions += 1

    while hash_table[hash_key] !=None:
        hash_key+=1
        # collisions+=1
        
        if hash_key==len(hash_table):
            hash_key=0               
                
    hash_table[hash_key]=customer
    
    return hash_table,collisions;

############################################       rehashing
        
def rehashing(hash_table,collisions):
    
    collisions=0
    
    temp=[]
    new_length=primeGreaterThan1(2*len(hash_table))
    temp=new_length*[None]
    
    #print("rehasing new length",new_length)
    for x in hash_table:
        if x==None :continue
        else:
            hash_key=hashing_func(x[0],len(temp))
            temp,collisions=insert_rehas(temp,hash_key,x,collisions)
    
    #print("rehashing->",temp)        
    return temp,collisions;

############################################# διπλασιαζω καθε φορα το μηκος

def new_rehashing(hash_table,collisions):
    temp=[]
    
    new_length=2*len(hash_table)
    
    temp=new_length*[None]
    #print("rehasing new length",new_length)
    for x in hash_table:
        if x==None :continue
        else:
            hash_key=hashing_func(x[0],len(temp))
            insert_rehas(temp,hash_key,x,collisions)
            
            
    return temp,collisions
    
    


###########################################       customers
    
def card(hash_table):
    collisions=0
    string='1234567890123456'
    random.seed(1059438)    
    val=6*[0]
    day=6*[0] #-> κάθε θέση του day αντιστοιχεί
    #σε μία μερά και σε κάθε μια απο αυτες τι θέσεις
    #θα βάζουμε τον αντίστοιχο αριθμό επισκέψεων
    
    for i in range(0,1000000):
        val=6*[0]
        day=6*[0]
        customer=()
        string='1234567890123456'
        for char in ['X','Y','Z','W']:
                        
            pos = randint(0, len(string) - 1)  # pick random position to insert char
            while string[pos].isdigit()==False:
                pos = randint(0, len(string) - 1)
            string = "".join((string[:pos], char, string[pos+1:]))  # insert char at pos
        key=string         
        
        #0->Δευτέρα
        #1->Τρίτη
        #2->Τετάρτη
        #3->Πέμπτη
        #4->Παρασκευή
        #5->Σάββατο
        
        poso=randint(10,100) #ποσό πληρωμής
        day1=randint(0,5) #ημέρα αγοράς
        
        val[day1]=poso
        day[day1]+=1
        customer=(key,val,day)
        
        position=hashing_func(key,len(hash_table))
        hash_table,collisions=insert(hash_table,position,customer,day1,collisions)
        
    print("οι συγκρουσεις ειναι",collisions)
    return hash_table 

###################################################
        
def main():
    
    #leng=primeGreaterThan1(1000) #μήκος του hash table
    leng=1000
    
    hash_table=leng*[None] #δημιουργία του hash table
    to=time.time()
    hash_table=card(hash_table)
    to=time.time()-to  
    #print("main->",hash_table)    
    #maxposo(hash_table)
    #maxvisit(hash_table)
    #day_with_max_visit(hash_table)
    
    #print("Οι συνολικες εγγραφές είναι: ",count,"το τελικό μήκος του πίνακα είναι: ",len(hash_table)," load_factor=",load_factor ) 

    print("running time - Hash_Table :",to)
    
if __name__=="__main__":
    main()
