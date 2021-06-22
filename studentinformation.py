SINIF_SAY = 4
NOT_ARALIK_SAY = 10

def verileri_al(lise_isim,aralik_liste): #ogrenciden bilgilerini alan fonksiyon
    devam = 'e'
    while devam == 'e' or devam == 'E':
        sinif_no = int(input('Şu an kaçıncı sınıfta okuduğunuzu giriniz(1-4): '))
        while sinif_no not in range (1,5):
            sinif_no = int(input('Lütfen yalnızca 1-4 arasında tamsayı giriniz: '))

        not_ort = int(input('Genel not ortalamanızı giriniz (0-100): ' ))
        while not_ort not in range (0,101):
            not_ort = int(input('Lütfen yalnızca 0-100 arasında tamsayı giriniz: '))
        lise = input('Mezun olduğunuz lisenin adını giriniz: ') 

        #not araliklarina gore ogrencini sayini bulmak icin dongu
        if not_ort in range (91,101):
            aralik_liste[sinif_no-1][9] += 1
        elif not_ort == 90:
            aralik_liste[sinif_no - 1][8] += 1
        else:
            aralik_liste[sinif_no - 1][not_ort // 10 - not_ort // 10 // 10] += 1

        if not lise_isim.get(lise):
            lise_isim[lise] = {}

        lise_isim.get(lise)["ogrenci_sayi"] = lise_isim.get(lise).get("ogrenci_sayi",0) + 1
        lise_isim.get(lise)["top_not"] = lise_isim.get(lise).get("top_not",0) + not_ort

        devam = input('Başka öğrenci var mı(e/E/h/H)?: ')
        while devam not in ['e','E','h','H']:
            devam = input('Lütfen yalnızca e/E/h/H karakterlerini giriniz: ')

def verileri_yazdir(lise_isim):  #okullardan mezun olan ogrenci sayi ve not ortalamasi icin fonksiyon
    print('\nMezun Olunan Lise Adı                                  Bölümdeki Öğrenci Say                     Not Ortalamaları')
    print('-------------------------------------------           -----------------------                   ------------------' )
    for lise,say in lise_isim.items():
        print(lise,(" ")*(73-len(lise)),say["ogrenci_sayi"],  format(say["top_not"]/say["ogrenci_sayi"],'37.2f'))


def siniflara_gore_not_yazdir(aralik_liste):  #not araliklarina gore ogrenci bilgilerini bulan fonksiyon
    not_araliklari = ['0-10 %','11-20 %','21-30 %','31-40 %','41-50 %','51-60 %','61-70 %','71-80 %','81-90 %','91-100 %']        
    print('Bölümümüzdeki her sınıftaki öğrencilerin sayıları ve 10 puanlık genel not ortalaması aralıklarına göre dağılımları:')
    print('                                                          Not Aralıkları                                   ')
    print('Sınıflar',end = '         ')
    for notlar in range (len(not_araliklari)):
        print(not_araliklari[notlar],end = '          ')
    print('Öğrenci Say')
    print("--------- ",end="    ")
    for say in not_araliklari:   
        print('----------',end='       ')
    print("-------------")
    sutun_top = [0] * NOT_ARALIK_SAY    #her alaliklara gore toplam ogrenci orani
    ogr_top = 0   #bolumdeki toplam ogrenci sayini bulmak icindir
    for no in range (SINIF_SAY):
        print(format(no+1,'2'),end = '       ')
        for index in range (len(aralik_liste[no])):
            try:
                not_aralik = (aralik_liste[no][index]*100)/sum(aralik_liste[no])
            except ZeroDivisionError:
                not_aralik = 0
            print(format(not_aralik,'13.2f'),end='    ')
            sutun_top[index] += not_aralik
        print("                ",format(sum(aralik_liste[no]),'.0f'))

        ogr_top += sum(aralik_liste[no])  #bolumdeki toplam ogrenci sayi
    print('Tüm Bölüm',end=("    "))
    for say in range (len(not_araliklari)):
        print(format(sutun_top[say],'9.2f'),end = '        ')
    print("            ",ogr_top)


def main():  #tum fonksiyonlar buradan cagriliyor
    try:
        lise_isim = {}     #ogrencilerin mezun olduklari liseni ve ortalama puan icin dict
        aralik_liste = []  #ogrencilerin not araliklarini yazdirmak icin liste
        for no in range (SINIF_SAY):   #her sinif icin uzunlugu 10 olan liste, burada not araliklarina gore ogrenci sayi toplanacak
            not_aralik_say = [0]*NOT_ARALIK_SAY
            aralik_liste.append(not_aralik_say)
        verileri_al(lise_isim,aralik_liste)
        verileri_yazdir(lise_isim)
        bir_tus = input("Devam etmek için bir tuşa ve enter'a basınız...")
        siniflara_gore_not_yazdir(aralik_liste)

    except IOError:
        print("Veri dosyası açılamadı ya da okunamadı!")
main()

#GIRILEN LISE ISMINE GORE SATIR UZUNLUGU KAYABILIR
