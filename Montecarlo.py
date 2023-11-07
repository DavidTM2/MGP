import numpy as np
import random
import matplotlib.pyplot as plt
import itertools 

def Main(num):
    m1=np.asarray(np.random.uniform(size=num, low=0.08, high=100))
    mask1 = np.where((0.08 < m1) & (m1 < 0.5))[0] 
    mask2=np.where(m1>0.5)[0]
    alpha_1=1.3
    alpha_2=2.3
    mb=m1[mask1]
    mu=m1[mask2]
    c1=(2*mb**(-alpha_1))*np.log(10*mb)
    c2=(mu**(-alpha_2))*np.log(10*mu)

    inicio=10000000000/num
    birth=np.asarray(np.linspace(inicio, 10000000000, num).astype(int)) 
    np.asarray(np.random.shuffle(birth)) #tiempo en años
    #tb=birth[mask1]
    #tu=birth[mask2]

    t=np.asarray((10**10)/(m1**(2.5)))
    Msm=[]
    rem=[]
    Mst=[]
    ret=[]
    tf=[]

    for i,v in enumerate(t):
        if v<birth[i]:
            Msm.append(m1[i])
            Mst.append(birth[i])
        elif v>birth[i]:
            rem.append(m1[i])
            ret.append(birth[i])
            tf.append(v)

    rem=np.asarray(rem)
    ret=np.asarray(ret)
    tf=np.asarray(tf)

    #clasificacion de remanente

    #WD

    maskwd=np.where((rem>=0.08)&(rem<9))[0]
    wd=rem[maskwd]
    wdf=0.109*wd+0.394
    wdt=ret[maskwd]
    #neutron star6.5


    maskns1=np.where((rem>=9)&(rem<=13))[0]
    ns1=np.asarray(rem[maskns1])
    ns1f=2.24+0.508*(ns1-14.75)+0.125*(ns1-14.75)**2 +0.0110*(ns1-14.75)**3
    ns1t=ret[maskns1]

    maskns2=np.where((rem>13)&(rem<15))[0]
    ns2=np.asarray(rem[maskns2])
    ns2f=0.123 + 0.112*ns2
    ns2t=ret[maskns2]

    maskns3=np.where((rem>=15)&(rem<=17.8))[0]  
    ns3=np.asarray(rem[maskns3])
    ns3f=0.996 + 0.0384*ns3
    ns3t=ret[maskns3]   

    maskns4=np.where((rem>17.8)&(rem<18.5))[0]
    ns4=np.asarray(rem[maskns4])
    ns4f= -0.020 + 0.10*ns4
    ns4t=ret[maskns4]
    NSt=list(itertools.chain(ns1t,ns2t,ns3t,ns4t))


    Nsf = list(itertools.chain(ns1f,ns2f,ns3f,ns4f))
    #black hole
    maskBH1=np.where((rem>=18.5)&(rem<=40))[0]
    bh1=np.asarray(rem[maskBH1])
    bh1f=0.9*(-2.049 + 0.4140*bh1)+(1-0.9)*(15.52 - 0.3294 *(bh1 - 25.97)- 0.02121 *(bh1 - 25.97)**2+ 0.003120 *(bh1 - 25.97)**3)
    bh1t=ret[maskBH1]   
    bh1i=rem[maskBH1]

    maskBH2=np.where((rem>40)&(rem<120))[0]
    bh2=np.asarray(rem[maskBH2])
    bh2f=5.697+7.8598*(10**8)*(bh2)**(-4.858)
    bh2t=ret[maskBH2]
    bh2i=rem[maskBH2]   
    BHf = list(itertools.chain(bh1f,bh2f))
    BHfi=list(itertools.chain(bh1i,bh2i))
    BHt=list(itertools.chain(bh1t,bh2t))




    return mb , mu ,c1 ,c2 ,birth, t, wdf,Nsf,BHf,Msm,rem,BHfi,Mst,wdt,NSt,BHt

num=1000000
mb,mu,c1,c2,birth,t, wdf,Nsf,BHf,Msm,rem,BHfi,Mst,wdt,NSt,BHt=Main(num)

#IMF plot
plt.scatter(mb,c1,c='#000000',s=3,label='0.08<m<0.5')
plt.scatter(mu, c2,c='r',s=3,label='m>0.5')
plt.yscale('log')
plt.xscale('log')
plt.legend(loc='best')
plt.xlabel(r'$log_{10}(m)[M_\odot]$')
plt.ylabel(r'$log_{10}(\xi_L(log_{10}(m)))$')
plt.savefig('imf.png',dpi=400)
plt.show()

#star formation rate
plt.hist(birth,alpha=0.7, bins=100, color='black')
plt.xlabel('Time of Birth[yr]')
plt.savefig('timebirth.png',dpi=400)
plt.show()


#Histrograma de masa
alpha=0.7
plt.hist(wdf,alpha=alpha, bins=100, color='#990099',density=True,label='WD')
plt.hist(Nsf,alpha=alpha, bins=100, color='#0000FF',density=True,label='NS')
plt.hist(BHf,alpha=alpha, bins=100, color='#330033',density=True,label='BH')
plt.hist(Msm,alpha=alpha, bins=100, color='#990000',density=True,label='MS')
plt.yscale('log')
plt.xlabel(r'$Masa\ final [M_{\odot}]$')
plt.legend(loc='best')
plt.savefig('masafinal.png',dpi=400)
plt.show()
#histogramas de tiempo
plt.hist(wdt,alpha=alpha, bins=100, color='#990099',density=True,label='WD')
plt.hist(NSt,alpha=alpha, bins=100, color='#0000FF',density=True,label='NS')
plt.hist(BHt,alpha=alpha, bins=100, color='#330033',density=True,label='BH')
plt.hist(Mst,alpha=alpha, bins=100, color='#990000',density=True,label='MS')
plt.yscale('log')
plt.xlabel('Tiempo [yr]')
plt.legend(loc='best')
plt.savefig('time.png',dpi=400)
plt.show()

plt.hist(wdt,alpha=alpha, bins=100, color='#990099',density=True,label='WD')
plt.hist(NSt,alpha=alpha, bins=100, color='#0000FF',density=True,label='NS')
plt.hist(BHt,alpha=alpha, bins=100, color='#330033',density=True,label='BH')
plt.hist(Mst,alpha=alpha, bins=100, color='#990000',density=True,label='MS')
plt.yscale('log')
plt.xlabel('Tiempo [yr]')
plt.xlim(0,0.002e10)
plt.legend(loc='best')
plt.savefig('timezoom.png',dpi=400)
plt.show()



fraccns=len(NSt)/num  *100
fraccbh=(len(BHt)/num)*100
fraccms=(len(Mst)/num)     *100
fraccwd=(len(wdt)/num)     *100
fraccre=(len(rem)/num)     *100
print('fraccion de estrella de neutrones ',fraccns,', fraccion de agujeros negros ',fraccbh,' fraccion de enanas blancas',fraccwd,' fraccion de secuencia principal',fraccms)

#desde 0.08 a 100
