"""çoklu yorum satırı oluşturma
bu şekilde yapılır
"""
#bu bir yorum satırıdır.tek satırdır.

#değişken adları alt çizgi veya harfle başlamalı.değişkenin içinde sayı,harf,alt çizgiden başka bi şey bulunamaz.

myvar=2
MyVar=2
myvar3=2
_myvar=2


"""hatalı değişken isimleri:
2myvar
my-var
my var
"""


#deve değişken ismi:ilk kelime küçük harfle başlar:
deveDeğişkenİsmi=5
#pascal davası:hepsi büyük harfle başlar.
PascalDavaDeğişkeni=6
#yılan değişken ismi:her sözcük alt çizgi ile ayrılır.
yılan_değişken_ismi=10

#birden çok değer atama:x=seni y=çok z=seviyorum şeklinde çıktı verir.
x,y,z="seni","çok","seviyorum"
print(x)
print(y)
print(z)

#liste verildiyse:
liste=["mine","kalp","burak"]
a,b,c=liste
print(a)
print(b)
print(c)


m="iyi "
i="ki "
n="benimsin "
e="aşkım"

print(m,i,n,e)#ya da aynı şekilde sonuç alınan başka yol var ama bunu sadece aynı veri tiplerinde kullanabilirsin int ve float toplanmaz mesela aynı tür olmalı:

print(m+i+n+e)

#global değişkenler bi değişkeni fonk içinde ve dışında aynı değer olarak gösterir:
q="harika"

def fonk():
    global q
    q="çok güzel"
fonk() #global olmasaydı çıktılarımız: çok güzel ve harika şeklinde olcaktı ama global ile artık q değeri her yerde çok güzel şeklinde oldu.
print(q)


sayı1=10
sayı2=2.6
sayı3=1j
sayı4=35e4
print(type(sayı1))#int
print(type(sayı2))#float
print(type(sayı3))#complex
print(type(sayı4))#float


#sayı türlerini dönüştürme:

sayi1=5
sayi2=10e5


dönüşüm1=float(sayi1)
dönüşüm2=int(sayi2)
print(dönüşüm1) #5.0
print(dönüşüm2)#1000000

#rastgele sayı üretme:
import random
print(random.randrange(1,100))


#string,indexler 0 dan başlar.
stringler="sana çok aşığım"
print(stringler[3]) #a

print(len(stringler))#uzunluğunu verir:15


# kelime bulma 
print("sevgi"in stringler)#false olur çünkü o kelime yok .

if "sana" in stringler:
    print("sana kelimesi bu cümlede var")



for i in "burak kalp mine":
    print(i)#tek tek hafrleri yazcak .


#dilimleme:
örnek="her şey güzel olacak"
print(örnek[3:10]) #çıktısı: şey gü
print(örnek[-5:-2])#çıktısı:lac olacak kelimesinin -5. indexi l dir,-2 ise k den önceki a dır.


#büyük harf küçük harf:
örnek2="Elma"
print(örnek2.upper())#ELMA
print(örnek2.lower())#elma

#baştaki ve sondaki boşluğu kaldırır
örnek3=" armut "
print(örnek3.strip())

#yerleri değiştirme:
print(örnek3.replace("a","k"))#krmut

örnek4="merhaba,burak"
print(örnek4.split("b"))#b harfini kaldırıp cümleyi liste haline getirdi.


#stringe sayı eklemek için kullanılan komut:format
yas=20
örnek5="benim adım mine,yaşım:{}"
print(örnek5.format(yas))


#kaçış karakterleri:
örnek6="mesleğim \"yazılım mühendisliği\"olarak bilinir"  #\"
örnek7="seni \nçok seviyorum"#yeni satır:\n
örnek8="seni \bçok seviyorum" #aradaki boşluğu siler:seniçok seviyorum
örnek9="seni \rçok seviyorum"#satır başı artık çok kelimesi oldu.
örnek10="hayat \fçok güzel"
print(örnek10)#çok güzel kısmı diğer satıra geçti
print(örnek9)
print(örnek8)
print(örnek6)
print(örnek7)


"""
Method Description
capitalize() İlk karakteri büyük harfe dönüştürür
casefold() Dizeyi küçük harfe dönüştürür
center() Ortalanmış bir dize döndürür
count() Bir dizede belirtilen bir değerin kaç kez oluştuğunu döndürür
encode() Dizenin kodlanmış bir sürümünü döndürür
endswith() Dize belirtilen değerle biterse true döndürür
expandtabs() Dizenin sekme boyutunu ayarlar
find() Dizeyi belirtilen bir değer için arar ve bulunduğu konumu döndürür
format() Bir dizede belirtilen değerleri biçimlendirir
format_map() Bir dizede belirtilen değerleri biçimlendirir
r
isalnum() Dizedeki tüm karakterler alfasayısal ise True döndürür
isalpha() Dizedeki tüm karakterler alfabedeyse True döndürür
isdecimal() Dizedeki tüm karakterler ondalık ise True döndürür
isdigit() Dizedeki tüm karakterler rakam ise True döndürür
isidentifier() Dize bir tanımlayıcıysa True döndürür
islower() Dizedeki tüm karakterler küçük harf ise True döndürür
isnumeric() Dizedeki tüm karakterler sayısal ise True döndürür
isprintable() Dizedeki tüm karakterler yazdırılabilirse True döndürür
isspace() Dizedeki tüm karakterler boşluksa True döndürür
istitle() Dize bir başlığın kurallarına uyuyorsa True döndürür
isupper() Dizedeki tüm karakterler büyük harf ise True döndürür
join() Bir yinelenebilir öğenin öğelerini dizenin sonuna birleştirir
ljust() Dizenin sola dayalı bir sürümünü döndürür
lower() Bir dizeyi küçük harfe dönüştürür
lstrip() Dizenin sol kırpılmış sürümünü döndürür
maketrans() Çevirilerde kullanılacak bir çeviri tablosu döndürür
partition() Dizenin üç parçaya ayrıldığı bir tanımlama grubu döndürür
replace() Belirtilen bir değerin belirtilen bir değerle değiştirildiği bir dize döndürür
find() Dizeyi belirtilen bir değer için arar ve bulunduğu yerin son konumunu
döndürür
index() Dizeyi belirtilen bir değer için arar ve bulunduğu yerin son konumunu
döndürür
just() Dizenin sağa yaslanmış bir sürümünü döndürür
partition() Dizenin üç parçaya ayrıldığı bir tanımlama grubu döndürür
split() Dizeyi belirtilen ayırıcıda böler ve bir liste döndürür
strip() Dizenin sağ trim sürümünü döndürür
split() Dizeyi belirtilen ayırıcıda böler ve bir liste döndürür
splitlines() Dizeyi satır sonlarında böler ve bir liste döndürür
startswith() Dize belirtilen değerle başlarsa true döndürür
strip() Dizenin kırpılmış bir sürümünü döndürür
swapcase() Durumları değiştirir, küçük harf büyük harf olur ve tam tersi
title() Her kelimenin ilk karakterini büyük harfe dönüştürür
translate() Çevrilmiş bir dize döndürür
upper() Bir dizeyi büyük harfe dönüştürür
zfill() Dizeyi başlangıçta belirtilen sayıda 0 değerle doldurur


"""



#python operatörleri:
k=15
l=2
print(k//l) #7
print(2**5)#üs alma:32


#listeler:
liste1=["köşeli","parantez","kullanılır"]
liste2=["string",2,"sayı","içerebilir"]
print(type(liste1)) #liste çıktısı verir.
print(len(liste2))#4
print(liste1[2])#kullanılır kelimesi çıktı olarak gelir.
#ögeleri değiştirme:
liste1[0]="köşesiz"
print(liste1)#çıktı:['köşesiz', 'parantez', 'kullanılır']

liste2.insert(3,"falan")
print(liste2)#insert ekleme metodudur.
liste2.append("bence")#listenin sonuna ekleme:append
print(liste2)


liste1.extend(liste2)
print(liste1) #listeleri birbirine ekleme


liste3=["muz","elma","kivi"]
liste3.remove("muz")
print(liste3)#remove silme işlemi yapar.
liste3.pop() #son ögeyi kaldırır. 
print(liste3)

liste3.clear()#tüm liste silinir.

print(liste3)



#liste ve döngüler:
liste4=["armut","şeftali","üzüm"]
for r in liste4:
    print(r)#tek tek yazdırdı.

i=0
while i<len(liste4):
    print(i)
    i+=1    #0,1,2 çıktısı verdi.


liste5=["ananas","karpuz","kiraz"]
liste6=[]

for x in liste5:
    if "a" in x:
        liste6.append(x)
print(liste6)

liste7=["ananas","karpuz","kiraz"]
yeniliste=[x for x in liste7 if x!="karpuz"]
print(yeniliste)

#listeyi  alfabetik  ve sayısal sıralama:sort

liste8=["artık","kelime","bulamıyorum"]
liste8.sort()
print(liste8)
liste9=[10,57860,8,78]
liste9.sort()
print(liste9) #küçükten büyüğe ve a dan z ye sıraladı tam tersi yapsın istenirse reverse=true yapılır:
liste9.sort(reverse=True)
print(liste9)

#liste birleştirme:
liste10=[1,2,3]
liste11=["mine","kalp","burak"]
liste10.extend(liste11)
print(liste10)
#diğer yol:
for x in liste11:
    liste10.append(x)
print(liste10)

"""append() Listenin sonuna bir öğe ekler
clear() Tüm öğeleri listeden kaldırır
copy() Listenin bir kopyasını döndürür
count() Belirtilen değere sahip öğelerin sayısını döndürür
extend() Geçerli listenin sonuna bir listenin öğelerini (veya herhangi bir yinelenebilir) ekleyin
index() Belirtilen değere sahip ilk öğenin dizinini döndürür
insert() Belirtilen konuma bir eleman ekler
pop() Belirtilen konumdaki öğeyi kaldırır
remove() Belirtilen değere sahip öğeyi kaldırır
reverse() Listenin sırasını tersine çevirir
sort() Listeyi sıralar"""



#tuple:liste indexleme ile aynıdır.çoğu şey aynıdır.
tuple1=("normal","parantez","kullanılır")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)#yıldız işareti ile liste yapma


meyve=("elma","kiraz","muz")
tuple2=meyve*2
print(tuple2)#iki defa yazdırır 


tuple3=(1,2,4,5,2,4,3,7,8,3,4,5)
x=tuple3.count(3)#kaç tane var=count
print(x)


#set:
set1={"şekilli","parantezle","oluşturulur"}
set1.add("mine")
print(set1)#ekleme işlemi

set2={"armut","elma"}
set3={"kiraz","üzüm"}
set2.update(set3)
print(set2) #iki seti birleştirme.
setyeni=set2.union(set3)#tuple ve seti de birleştirebilirsin
print(setyeni)#birleştirme,üçüncü yöntem:
_set1={"mine","burak"}
_set2={"kalp"}
_set3=_set1|_set2
print(_set3)

set4={"artık","meyve","bulamıyorum."}
set4.remove("meyve")
print(set4)#öge kaldırma

set4.discard("artık")
print(set4)#discard ve remove arasındai fark eğer silinecek kelime sette yoksa remove hata verir ama discard vermez.

#rastegele öge kaldırma:pop
set5={"elma","armut","portakal"}
set5.pop()
print(set5)


set6={"selam","canım"}
set7={"seviyorum","canım"}
set8=set6.intersection(set7)#iki sette ortak ögeyi yazdırır.bunun yerine & da kullanılır
_set8=set6&set7
print(_set8)
print(set8)

set9=set6.difference(set7)
print(set9)#sadece ilk sette bulunanı yazdırır.bunun yerine - kullanabilirsin
set10=set6-set7
print(set10)
 #difference ,symmetric_difference ve intersection kullanılırken yeni bir küme oluşrumak yerine difference_update ya da intersection_update kullanabilirsin:

set11={"seni","çok","seviyorum"}
set12={"seni","özlüyorum"}
set11.difference_update(set12)
print(set11)

set13={"kedi","köpek"}
set14={"kedi","insan","ağaç"}
set15=set13.symmetric_difference(set14)
print(set15)#iki sette de ortak olanı kaldırdı tek kümede diğerlerini yazdırdı.


#dictionary:

sözlük1={"adı":"mine",
         "soyadı":"eryılmaz"

         }


print(sözlük1)
print(sözlük1.get("adı"))
#yeni öge ekleme:key
x=sözlük1.keys()
sözlük1["yaşı"]="20"
print(x)

#değişiklik yapmak için :1.yol

y=sözlük1.values()
sözlük1["soyadı"]="diner"
print(y)


#2. yol
sözlük2={"marka":"ford",
         "renk":"pembe",
        "yıl":"2000"}

sözlük2["yıl"]="2003"
print(sözlük2)

#3.yol
sözlük2.update({"marka":"ferrari"})
print(sözlük2)


#öge silme için:
sözlük2={"marka":"ford",
         "renk":"pembe",
        "yıl":"2000"}

sözlük2.pop("renk")
print(sözlük2)

#son ögeyi kaldırma:

sözlük2.popitem()
print(sözlük2)

#silme diğer yol:
del sözlük2["marka"]
print(sözlük2)
#sözlüğü tamamen boşaltmak için clear kullanılır.


#içiçe sözlük:
çocuk1={"adı":"mine",
        "soyadı":"eryılmaz"}
çocuk2={"adı":"burak",
        "soyadı":"diner"}
aile={"çocuk1":çocuk1,
      "çocuk2":çocuk2}
print(aile)


"""Liste, sıralı ve değiştirilebilir bir koleksiyondur. Yinelenen üyelere
izin verir.
Tuple, sıralı ve değişmez bir koleksiyondur. Yinelenen üyelere izin
verir.
Set, sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Çift
üye yok.
Sözlük, sıralı** ve değiştirilebilir bir koleksiyondur. Çift üye yok.
"""

#fonksiyonlar

def fonksiyon1(isim):
    print(isim +" diner")
fonksiyon1("mine")
fonksiyon1("burak")

def fonksiyon2(cocuk1,cocuk2):
    print("en küçük çocuk:" + cocuk1)
fonksiyon2(cocuk1="mine",cocuk2="burki")


#lambda:

x=lambda a:a +10
print(x(5))

def fonk1(n):
    return lambda a:a*n
m=fonk1(2)
print(m(11))


#class oluşturma:

class class1:
    x=5


class insan:
    def __init__(kişi,isim,yaş):
        kişi.isim=isim
        kişi.yaş=yaş
kişi1=insan("mine",20)
print(kişi1.isim)
print(kişi1.yaş)

#tarih:şu anki saati yazmak için:

import datetime
x=datetime.datetime.now()
print(x)
#yıl ve günü de eklemek için:
print(x.year)
print(x.strftime("%A"))

#matematik:min max değeri için:

x=min(72389,263478,2643782)
y=max(82904,7,84390)
print(x)
print(y)

#mutlak değer:
sayii=abs(-23758.249) 
print(sayii)   

#üs alma:
sayii1=pow(2,5)
print(sayii1)

#karekök:
import math

sayii2=math.sqrt(64)
print(sayii2)


a=math.ceil(2.6)#yukarıya yuvarlama
b=math.floor(2.4)#aşağıya yuvarlama
print(a)
print(b)




