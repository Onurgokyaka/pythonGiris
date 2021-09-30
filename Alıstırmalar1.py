#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ekrana merhaba dünya yazdırma
print("Merhaba Dünya")


# In[2]:


isim=input("Adınızı giriniz")
print("Hoşgeldin",isim)


# In[5]:


#Klavyeden girilen iki sayıyı toplayan ve sonucu ekranda gösteren python kodunu yazınız.
a=int(input("1. sayiyi giriniz"))
b=int(input("2. sayiyi giriniz"))
print("Girilen iki sayinin toplami",a+b)


# In[6]:


#Klavyeden girilen iki sayıyının ortalamasını bulan ve sonucu ekranda gösteren python kodunu yazınız.
a=int(input("1. sayiyi giriniz: "))
b=int(input("2. sayiyi giriniz: "))
print("Girilen iki sayinin ortalamasi",(a+b)/2)


# In[7]:


#Klavyeden girilen vize ve final notuna göre vizenin %40 ve
#finalin %60 ını alan ve sonucu ekranda gösteren python kodunu yazınız.

vize=int(input("Vize notunu giriniz"))
final=int(input("Final notunu giriniz"))
sonuc=vize*0.4+final*0.6
print("Ögrenci ders notu: ", sonuc)





# In[8]:


#Klavyeden girilen üç yazılı notunun ortalamasını bulan ekranda gösteren python kodunu yazınız.
sayi1=int(input("1.sayiyi giriniz"))
sayi2=int(input("2. sayiyi giriniz"))
sayi3=int(input("3. sayiyi giriniz"))
ort=(sayi1+sayi2+sayi3)/3
print("Nor ortalamasi: ", ort)


# In[9]:


#Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodunu yazınız. (50den büyükse geçti değilse kaldı yazdıran örnek python kodu)
vize=int(input("Vize notunu giriniz"))
final=int(input("Final notunu giriniz"))
sonuc=vize*0.4+final*0.6
if sonuc>=50:
    print("Dersi geçtiniz ortalamaniz: ",sonuc)
else:
    print("Dersi gecemediniz,seneye görüsürüz,ortalamaniz: ",sonuc)


# In[10]:


#Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod örneğini yapınız.
a=int(input("Sayiyi giriniz: "))
if a%2==0:
    print("sayi cift")
else:
    print("sayi tek")


# In[11]:


#Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu bulan python kodunu yazınız
sayi=int(input("Sayiyi giriniz: "))
if sayi<0:
    print(sayi ," sayisi negatiftir")
elif sayi==0:
    print(sayi, " sayisi 0'a eşittir")
else:
    print(sayi, "sayisi pozitiftir")


# In[12]:


#Klavyeden girilen yaşa göre ehliyet alıp alamayacağını bulan python kodunu yazınız.
yas=int(input("Aday'ın yaşını giriniz: "))
if yas>18:
    print("Aday ehliyet alabilir")
else:
    print("Aday ehliyet alamaz")


# In[13]:


#1 den 10 a kadar olan sayıları alt alta yazdıran python kodunu yazınız.
for i in range (1,11,1):
    print(" ",i)


# In[14]:


#1 den 20 ye kadar olan çift sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,21):
    if i%2==0:
        print(i)


# In[16]:


#1 den 20 ye kadar olan tek sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,21):
   if i%2==1:
       print(i)


# In[17]:


#1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)


# In[18]:


#Klavyeden girilen sayıya kadar olan sayıları alt alta yazdıran python kodunu yazınız.
a=int(input("Bir sayı giriniz: "))
for i in range(1,a+1):
    print(i)


# In[19]:


###### Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.
kk=int(input("kısa kenar: "))
uk=int(input("uzun kenar: "))
alan=kk*uk
cevre=2*(kk+uk)
print("alan: ",alan,"cevre: ", cevre)


# In[20]:


#Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
metin= input("metni giriniz: ")
sayac=0
while sayac<len(metin):
    print(metin[sayac])
    sayac=sayac+1


# In[21]:


#Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
metin= input("metni giriniz: ")
sayac=0
for sayac in range(len(metin)):
    print(metin[sayac])
    sayac=sayac+1


# In[22]:


#Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.
sayi1=int(input("Sayi1 i giriniz: "))
sayi2=int(input("Sayi2 yi giriniz: "))
toplam=0
for i in range (sayi1+1,sayi2):
    toplam=i+toplam
print(" ",sayi1, " ile",sayi2,"arasındaki sayıların toplamı ="  , toplam)
    


# In[23]:


#Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.
sayi=int(input("sayiyi giriniz"))
sayac=0
for i in range(1,sayi+1):
   if sayi%i==0:
       sayac=sayac+1
if sayac==2:
   print(sayi,"sayisi asaldır")
else:
   print(sayi,"sayisi asal degildir")


# In[24]:


#Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.
sayi=int(input("sayiyi giriniz"))
sayac=0
for i in range(2,sayi):
    if sayi%i==0:
        sayac=sayac+1
if sayac==0:
    print(sayi,"sayisi asaldır")
else:
    print(sayi,"sayisi asal degildir")


# In[25]:


#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
sayi=int(input("Sayıyı giriniz"))
tektoplam=0
cifttoplam=0
for i in range (1,sayi+1):
   if i%2==0:
       cifttoplam+=i
   else:
       tektoplam+=i
print("tek toplam= " ,tektoplam,"cift toplam = ", cifttoplam)


# In[ ]:





# In[ ]:





# In[ ]:




