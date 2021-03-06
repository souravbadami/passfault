#Written by Bernardo Rodrigues (bernardoaraujor@gmail.com)
#Based on Luminoso Insight's wordfreq module (https://github.com/LuminosoInsight/wordfreq/)

from wordfreq import word_frequency
from wordfreq import zipf_frequency
from wordfreq import top_n_list
#import matplotlib.pyplot as plt

dest = "./wordlists/"

ar = top_n_list('ar', 1e5, wordlist='large')
de = top_n_list('de', 1e5, wordlist='large')
en = top_n_list('en', 1e5, wordlist='large')
es = top_n_list('es', 1e5, wordlist='large')
fi = top_n_list('fi', 1e5)
fr = top_n_list('fr', 1e5, wordlist='large')
hi = top_n_list('hi', 1e5)
it = top_n_list('it', 1e5, wordlist='large')
ja = top_n_list('ja', 1e5)
nl = top_n_list('nl', 1e5, wordlist='large')
sv = top_n_list('sv', 1e5)
pt = top_n_list('pt', 1e5, wordlist='large')
zh = top_n_list('zh', 1e5)

#---------------------------------------------------------------
arPopular = open(dest + '/arPopular.txt', 'w')
arLongTail = open(dest + '/arLongTail.txt', 'w')

integral100 = 0
for i in range(len(ar)):
    integral100 += word_frequency(ar[i], 'ar')

integral80 = 0
for i in range(len(ar)):
    integral80 += word_frequency(ar[i], 'ar')
    if (integral80 <= 0.80*integral100):
        arPopular.write(ar[i] + '\n')
    else:
        arLongTail.write(ar[i] + '\n')

arPopular.close()
arLongTail.close()


#---------------------------------------------------------------
dePopular = open(dest + '/dePopular.txt', 'w')
deLongTail = open(dest + '/deLongTail.txt', 'w')

integral100 = 0
for i in range(len(de)):
    integral100 += word_frequency(de[i], 'de', wordlist='large')

integral80 = 0
for i in range(len(de)):
    integral80 += word_frequency(de[i], 'de', wordlist='large')
    if (integral80 <= 0.80*integral100):
        dePopular.write(de[i] + '\n')
    else:
        deLongTail.write(de[i] + '\n')

dePopular.close()
deLongTail.close()

#---------------------------------------------------------------
enPopular = open(dest + '/enPopular.txt', 'w')
enLongTail = open(dest + '/enLongTail.txt', 'w')

integral100 = 0
for i in range(len(en)):
    integral100 += word_frequency(en[i], 'en', wordlist='large')

integral80 = 0
for i in range(len(en)):
    integral80 += word_frequency(en[i], 'en', wordlist='large')
    if (integral80 <= 0.80*integral100):
        enPopular.write(en[i] + '\n')
    else:
        enLongTail.write(en[i] + '\n')

enPopular.close()
enLongTail.close()

#---------------------------------------------------------------
esPopular = open(dest + '/esPopular.txt', 'w')
esLongTail = open(dest + '/esLongTail.txt', 'w')

integral100 = 0
for i in range(len(es)):
    integral100 += word_frequency(es[i], 'es', wordlist='large')

integral80 = 0
for i in range(len(es)):
    integral80 += word_frequency(es[i], 'es', wordlist='large')
    if (integral80 <= 0.80*integral100):
        esPopular.write(es[i] + '\n')
    else:
        esLongTail.write(es[i] + '\n')

esPopular.close()
esLongTail.close()

#---------------------------------------------------------------
fiPopular = open(dest + '/fiPopular.txt', 'w')
fiLongTail = open(dest + '/fiLongTail.txt', 'w')

integral100 = 0
for i in range(len(fi)):
    integral100 += word_frequency(fi[i], 'fi')

integral80 = 0
for i in range(len(fi)):
    integral80 += word_frequency(fi[i], 'fi')
    if (integral80 <= 0.80*integral100):
        fiPopular.write(fi[i] + '\n')
    else:
        fiLongTail.write(fi[i] + '\n')

fiPopular.close()
fiLongTail.close()

#---------------------------------------------------------------
frPopular = open(dest + '/frPopular.txt', 'w')
frLongTail = open(dest + '/frLongTail.txt', 'w')

integral100 = 0
for i in range(len(fr)):
    integral100 += word_frequency(fr[i], 'fr', wordlist='large')

integral80 = 0
for i in range(len(fr)):
    integral80 += word_frequency(fr[i], 'fr', wordlist='large')
    if (integral80 <= 0.80*integral100):
        frPopular.write(fr[i] + '\n')
    else:
        frLongTail.write(fr[i] + '\n')

frPopular.close()
frLongTail.close()

#---------------------------------------------------------------
hiPopular = open(dest + '/hiPopular.txt', 'w')
hiLongTail = open(dest + '/hiLongTail.txt', 'w')

integral100 = 0
for i in range(len(hi)):
    integral100 += word_frequency(hi[i], 'hi')

integral80 = 0
for i in range(len(hi)):
    integral80 += word_frequency(hi[i], 'hi')
    if (integral80 <= 0.80*integral100):
        hiPopular.write(hi[i] + '\n')
    else:
        hiLongTail.write(hi[i] + '\n')

hiPopular.close()
hiLongTail.close()

#---------------------------------------------------------------
itPopular = open(dest + '/itPopular.txt', 'w')
itLongTail = open(dest + '/itLongTail.txt', 'w')

integral100 = 0
for i in range(len(it)):
    integral100 += word_frequency(it[i], 'it', wordlist='large')

integral80 = 0
for i in range(len(it)):
    integral80 += word_frequency(it[i], 'it', wordlist='large')
    if (integral80 <= 0.80*integral100):
        itPopular.write(it[i] + '\n')
    else:
        itLongTail.write(it[i] + '\n')

itPopular.close()
itLongTail.close()

#---------------------------------------------------------------
jaPopular = open(dest + '/jaPopular.txt', 'w')
jaLongTail = open(dest + '/jaLongTail.txt', 'w')

integral100 = 0
for i in range(len(ja)):
    integral100 += word_frequency(ja[i], 'ja')

integral80 = 0
for i in range(len(ja)):
    integral80 += word_frequency(ja[i], 'ja')
    if (integral80 <= 0.80*integral100):
        jaPopular.write(ja[i] + '\n')
    else:
        jaLongTail.write(ja[i] + '\n')

jaPopular.close()
jaLongTail.close()

#---------------------------------------------------------------
nlPopular = open(dest + '/nlPopular.txt', 'w')
nlLongTail = open(dest + '/nlLongTail.txt', 'w')

integral100 = 0
for i in range(len(nl)):
    integral100 += word_frequency(nl[i], 'nl', wordlist='large')

integral80 = 0
for i in range(len(nl)):
    integral80 += word_frequency(nl[i], 'nl', wordlist='large')
    if (integral80 <= 0.80*integral100):
        nlPopular.write(nl[i] + '\n')
    else:
        nlLongTail.write(nl[i] + '\n')

nlPopular.close()
nlLongTail.close()

#---------------------------------------------------------------
ptPopular = open(dest + '/ptPopular.txt', 'w')
ptLongTail = open(dest + '/ptLongTail.txt', 'w')

integral100 = 0
for i in range(len(pt)):
    integral100 += word_frequency(pt[i], 'pt', wordlist='large')

integral80 = 0
for i in range(len(pt)):
    integral80 += word_frequency(pt[i], 'pt', wordlist='large')
    if (integral80 <= 0.80*integral100):
        ptPopular.write(pt[i] + '\n')
    else:
        ptLongTail.write(pt[i] + '\n')

ptPopular.close()
ptLongTail.close()

#---------------------------------------------------------------
svPopular = open(dest + '/svPopular.txt', 'w')
svLongTail = open(dest + '/svLongTail.txt', 'w')

integral100 = 0
for i in range(len(sv)):
    integral100 += word_frequency(sv[i], 'sv')

integral80 = 0
for i in range(len(sv)):
    integral80 += word_frequency(sv[i], 'sv')
    if (integral80 <= 0.80*integral100):
        svPopular.write(sv[i] + '\n')
    else:
        svLongTail.write(sv[i] + '\n')

svPopular.close()
svLongTail.close()

#---------------------------------------------------------------
zhPopular = open(dest + '/zhPopular.txt', 'w')
zhLongTail = open(dest + '/zhLongTail.txt', 'w')

integral100 = 0
for i in range(len(zh)):
    integral100 += word_frequency(zh[i], 'zh')

integral80 = 0
for i in range(len(zh)):
    integral80 += word_frequency(zh[i], 'zh')
    if (integral80 <= 0.80*integral100):
        zhPopular.write(zh[i] + '\n')
    else:
        zhLongTail.write(zh[i] + '\n')

zhPopular.close()
zhLongTail.close()

#---------------------------------------------------------------
#uncomment the following lines and change the language to plot

#integralList = []
#integral = 0
#f = []
#for i in range(0, len(pt)):
#    f.insert(i, word_frequency(pt[i], 'pt', wordlist='large')/word_frequency(de[0], 'pt', wordlist='large'))
#    integral += word_frequency(pt[i], 'pt', wordlist='large')
#    integralList.insert(i, integral)

#plt.plot(integralList)
#plt.plot(f)
#plt.xscale('log')
#plt.yscale('log')
#plt.show()


