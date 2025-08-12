label card1: 
    show Gizemli_Adam at gizemli_adam_poz
    Gizemli_Adam "Eğer bana istediğim ödemeyi yaparsan sana bağlı bir şövalye teşkilatı oluştururum."
    menu:
        "sende kimsin":
            $ check_bars()
        "Ödemeyi kabul ediyorum":
            $ Economy -= 4
            $ mnc_chng("kosc_mnc", 1)
            $ check_bars() #knight of the swan minikart
    hide image Gizemli_Adam
    jump random_dialog
label card2:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var elimdeki sağlık iksirini seninle paylaşabilirim ne dersin."
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2 # Sağlık iksiri mini kartı
            $ mnc_chng("hp_mnc",1)
            $ check_bars()
        "İksirlere inanmıyorum":
            $ check_bars()
    hide image Büyücü
    jump random_dialog
label card3:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var sana zor zamanlarda yardım edecek bir şeyler öğretebilirim"
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2
            $ mnc_chng("bm_mnc",1)
            $ check_bars() #Kara büyü kartı
        "Benim büyü ile işim olmaz":
            $ check_bars()
    hide image Büyücü
    jump random_dialog
label card4:
    show Soylu at soylu_poz
    Soylu "Aquila Kralı elinizdeki mevcut hazine ile zor zamanlar için bir tahıl ambarı açmalısınız."
    menu:
        "Mantıklı açıyorum":
            $ Economy -= 3
            $ mnc_chng("gw_mnc",1)
            $ check_bars()
        "Hazineyi kullanmak istemiyorum":
            $ check_bars()
    hide image Soylu
    jump random_dialog
label card5:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim bir grup iyi asker sizin hizmetinize girmek istiyorlar. Belli bir ücret karşılığında tabii."
    menu:
        "Evet çağır onları":
            $ Economy -= 3
            $ mnc_chng("al_mnc",1)
            $ check_bars()
        "Hayır ihtiyacım yok":
            $ check_bars()
    hide image Muhafız_Başı
    jump random_dialog
label card6:
    show Baş_İmam at bas_imam_poz
    Baş_İmam "Ne vakittir aradığımız kutsal emanetlerin yerini buldum bir ordu ile onları kurtaralım."
    menu:
        "Ordumla yola çıkıyorum hemen":
            $ Military -= 2
            $ mnc_chng("hr_mnc",1)
            $ check_bars()
        "Yeterli gücüm yok maalesef":
            $ check_bars()
    hide image Baş_İmam
    jump random_dialog
label card7:
    show Kütüphaneci at kutuphaneci_poz
    Kütüphaneci "Kralım babanızın kütüphanesinde eski bir kitap buldum belki işinize yarayabilir."
    menu:
        "Ver bakalım":
            $ mnc_chng("spcb_mnc",1)
            $ check_bars()
        "Sende kalsın":
            $ check_bars()
    hide image Kütüphaneci
    jump random_dialog
label card8:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim Krallığınız Yargea ile olan savaşı kazandı gelen ganimeti ne yapalım"
    menu:
        "Zor günler için ayıralım":
            $ mnc_chng("sow_mnc",1)
            $ check_bars()
        "Bir kısmını orduya bir kısmını hazineye dağıt":
            $ Military += 1
            $ Economy += 1
            $ Politics += 1
            $ check_bars()
    hide image Muhafız_Başı
    jump random_dialog
label card9:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim bana bağlı bir grup askeri sizin emrinize vermek istiyorum can güvenliğinizi arttırmak için."
    menu:
        "Tamam ücretlerini ben karşılayacağım":
            $ Economy -= 3
            $ mnc_chng("rg_mnc",1)
            $ check_bars()
        "Şuan böyle bir tehdit yok":
            $ check_bars()
    hide image Muhafız_Başı
    jump random_dialog
label card10:
    show Zengin_Tüccar at zengin_tuccar_poz
    Zengin_Tüccar "Sizinle bir anlaşma yapmak istiyorum eğer bana koruma ve maddi destek sağlarsanız Donovia ile ipek ticareti yapalım, karın bir kısmınıda size vereceğim."
    menu:
        "Kabul ediyorum destek vereceğim.":
            $ Economy -= 2
            $ Military -= 2
            $ mnc_chng("sti_mnc",1)
            $ check_bars()
        "Ben bir Kralım sana ihtiyacım yok":
            $ check_bars()
    hide image Zengin_Tüccar
    jump random_dialog
label card11:
    show Çiftçi at ciftci_poz
    Çiftçi "Saygı değer Kralım bir mağranın içinde mavi şapkalı mantar bulduk bize ekonomik destek sağlarsanız onları sizin için toplayabiliriz."
    menu:
        "Böyle saçma işlerle huzuruma bir daha çıkma":
            $ People -= 1
            $ check_bars()
        "Tamam destek veriyorum":
            $ Economy -= 1
            $ People += 1
            $ mnc_chng("bcm_mnc",1)
            $ check_bars()
    hide image Çiftçi
    jump random_dialog
label card12:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var elimdeki sadakat iksirini seninle paylaşabilirim ne dersin. "
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2
            $ mnc_chng("lp_mnc",1)
            $ check_bars()
        "İksirlere inanmıyorum renkli su":
            $ Religion += 1
            $ check_bars()
    hide image Büyücü
    jump random_dialog
