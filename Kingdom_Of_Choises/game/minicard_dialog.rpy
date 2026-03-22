label card1: 
    show tukan at tukan_poz
    "Eğer bana istediğim ödemeyi yaparsan seni özel bir yuvarlak masa şövalyeleri teşkilatı ile tanıştırırım."
    menu:
        "Sende kimsin":
            $ check_bars()
        "Ödemeyi kabul ediyorum":
            $ Economy -= 4
            $ unlock_level(22)
            $ mnc_info[0]["val"] = 1
            $ mnc_chng("kosc_mnc", 1)
            $ check_bars() #knight of the swan minikart
            hide image tukan
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Sevgili Efendim, Satın almış olduğunuz Kinght Of The Swan Klanı sizi Askeri , Siyaset, Halk ve Din değeri biter yada dolarsa bu Klan sizi ölümden koruyacaktır." 
            $ unlock_level(25)
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image Kraliçe
            hide image kosc_mnc
    hide image tukan
    $ main_story_count += 1
    jump random_dialog
    return

label card2:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var elimdeki sağlık iksirini seninle paylaşabilirim ne dersin."
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ unlock_level(22)
            $ Religion -= 1 # Sağlık iksiri mini kartı
            $ mnc_info[1]["val"] = 1
            $ mnc_chng("hp_mnc",1)
            $ check_bars()
            hide image Büyücü
            show Kraliçe at kraliçe_poz
            show hp_mnc at hp_mnc_poz
            Kraliçe "Kralım, satın almış olduğunuz bu Sağlık iksiri sizi Sağlık değeri biter yada dolarsa bu iksir sizin ölmenize engel olacak." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image hp_mnc
        "İksirlere inanmıyorum":
            $ check_bars()
    hide image Kraliçe
    hide image Büyücü
    $ main_story_count += 1
    jump random_dialog
    return

label card3:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var sana zor zamanlarda yardım edecek bir şeyler öğretebilirim"
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ unlock_level(22)
            $ Religion -= 2
            $ mnc_info[2]["val"] = 1
            $ mnc_chng("bm_mnc",1)
            $ check_bars() #Kara büyü kartı
            hide image Büyücü
            show Kraliçe at kraliçe_poz
            show bm_mnc at bm_mnc_poz
            Kraliçe "Efendim, aldığınız bu kitap asker değeri bittiğinde veya dolduğunda yada siyaset sigmenti dolduğunda sizi ölümden korur."
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image bm_mnc
        "Benim büyü ile işim olmaz":
            $ check_bars()
    hide image Kraliçe
    hide image Büyücü
    $ main_story_count += 1
    jump random_dialog
    return
label card4:
    show Soylu at soylu_poz
    Soylu "Aquila Kralı elinizdeki mevcut hazine ile zor zamanlar için bir tahıl ambarı açmalısınız. "
    menu:
        "Mantıklı açıyorum":
            $ Economy -= 3
            $ unlock_level(22)
            $ mnc_chng("gw_mnc",1)
            $ mnc_info[3]["val"] = 1
            $ check_bars()
            hide image Soylu
            show Kraliçe at kraliçe_poz
            show gw_mnc at gw_mnc_poz
            Kraliçe "Satın aldığınız bu ambar sizi ekonomi değeri bittiğinde veya dolduğunda yada halk değeri dolduğunda ölümden korur."
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image gw_mnc
        "Hazineyi kullanmak istemiyorum":
            $ check_bars()
    hide image Kraliçe 
    hide image Soylu
    $ main_story_count += 1
    jump random_dialog
    return

label card5:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim bir grup iyi asker sizin hizmetinize girmek istiyor. Belli bir ücret karşılığında tabii."
    menu:
        "Evet çağır onları":
            $ Economy -= 3
            $ unlock_level(22)
            $ mnc_chng("al_mnc",1)
            $ mnc_info[4]["val"] = 1
            $ check_bars()
            hide image Muhafız_Başı
            show Kraliçe at kraliçe_poz
            show al_mnc at al_mnc_poz
            Kraliçe "Efendim, Suikastçi birliğiniz hazır bu birlik sizi askeri, siyaset ve din değeri dolduğunda sizi ölümden korur." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image al_mnc
        "Hayır ihtiyacım yok":
            $ check_bars()
    hide image Kraliçe
    hide image Muhafız_Başı
    $ main_story_count += 1
    jump random_dialog
    return

label card6:
    show Baş_İmam at bas_imam_poz
    Baş_İmam "Ne vakittir aradığımız kutsal emanetlerin yerini buldum bir ordu ile onları kurtaralım."
    menu:
        "Ordumla yola çıkıyorum hemen":
            $ Military -= 2
            $ unlock_level(22)
            $ mnc_chng("hr_mnc",1)
            $ mnc_info[5]["val"] = 1
            $ check_bars()
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show hr_mnc at hr_mnc_poz
            Kraliçe "Sahip olduğunuz bu emanetler sizi din değeri bittiğinde yada dolduğunda ölümden korur." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image hr_mnc
        "Yeterli gücüm yok maalesef":
            $ check_bars()
    hide image Kraliçe
    hide image Baş_İmam
    $ main_story_count += 1
    jump random_dialog
    return

label card7:
    show Kütüphaneci at kutuphaneci_poz
    Kütüphaneci "Kralım babanızın kütüphanesinde eski bir kitap buldum belki işinize yarayabilir."
    menu:
        "Ver bakalım":
            $ mnc_chng("spcb_mnc",1)
            $ mnc_info[6]["val"] = 1
            $ unlock_level(22)
            $ check_bars()
            hide image Kütüphaneci
            show Kraliçe at kraliçe_poz
            show spcb_mnc at spcb_mnc_poz
            Kraliçe "Bu kitap Üstün Siyaset Bilmi Kitabı, bu kitap sizi siyaset değeri bittiğinde yada dolduğunda sizi ölümden korur." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image spcb_mnc
            $ check_bars()
        "Gerek yok istemiyorum.":
            $ check_bars()

    hide image Kraliçe
    hide image Kütüphaneci
    $ main_story_count += 1
    jump random_dialog
    return

label card8:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim Krallığınız Yargea ile olan savaşı kazandı gelen ganimeti ne yapalım"
    menu:
        "Zor günler için ayıralım":
            $ mnc_chng("sow_mnc",1)
            $ mnc_info[7]["val"] = 1
            $ unlock_level(22)
            $ check_bars()
            hide image Muhafız_Başı
            show Kraliçe at kraliçe_poz
            show sow_mnc at sow_mnc_poz
            Kraliçe "Efendim Ganimetleri hazinenize ekledik ekonomi ve halk değeri bittiğinde sizi ölümden koruyacaktır." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image sow_mnc
        "Bir kısmını orduya bir kısmını hazineye dağıt":
            $ Military += 1
            $ Economy += 1
            $ Politics += 1
            $ check_bars()
    hide image Kraliçe
    hide image Muhafız_Başı
    $ main_story_count += 1
    jump random_dialog
    return

label card9:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim bana bağlı bir grup askeri sizin emrinize vermek istiyorum can güvenliğinizi arttırmak için."
    menu:
        "Tamam ücretlerini ben karşılayacağım":
            $ Economy -= 3
            $ mnc_chng("rg_mnc",1)
            $ unlock_level(22)
            $ mnc_info[8]["val"] = 1
            $ check_bars()
            hide image Muhafız_Başı
            show Kraliçe at kraliçe_poz
            show rg_mnc at rg_mnc_poz
            Kraliçe "Kraliyet Muhafızları emrinizde askeri değeri bittiğinde yada dolduğunda yada halk ve siyaset dolduğunda sizi ölümden korur." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image rg_mnc
        "Şuan böyle bir tehdit yok":
            $ check_bars()
    hide image Kraliçe
    hide image Muhafız_Başı
    $ main_story_count += 1
    jump random_dialog
    return

label card10:
    show Zengin_Tüccar at zengin_tuccar_poz
    Zengin_Tüccar "Sizinle bir anlaşma yapmak istiyorum eğer bana koruma ve maddi destek sağlarsanız Donovia ile ipek ticareti yapalım, kârın bir kısmınıda size vereceğim."
    menu:
        "Kabul ediyorum destek vereceğim.":
            $ Economy -= 2
            $ Military -= 2
            $ mnc_chng("sti_mnc",1)
            $ unlock_level(22)
            $ mnc_info[9]["val"] = 1
            $ check_bars()
            hide image Zengin_Tüccar
            show Kraliçe at kraliçe_poz
            show sti_mnc at sti_mnc_poz
            Kraliçe "Efendim bu gelirler sizi ekonomi değeri bittiğinde yönetime devam etmenizi sağlayacaktır."
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image sti_mnc
        "Ben bir Kralım sana ihtiyacım yok":
            $ check_bars()
    hide image Kraliçe
    hide image Zengin_Tüccar
    $ main_story_count += 1
    jump random_dialog
    return

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
            $ unlock_level(22)
            $ mnc_chng("bcm_mnc",1)
            $ mnc_info[10]["val"] = 1
            $ check_bars()
            hide image Çiftçi
            show Kraliçe at kraliçe_poz
            show bcm_mnc at bcm_mnc_poz
            Kraliçe "Efendim bu mantarlar sizi ekonomi ve sağlık değeri bittiğinde yönetime devam etmenizi sağlayacaktır." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image bcm_mnc
    hide image Kraliçe
    hide image Çiftçi
    $ main_story_count += 1
    jump random_dialog
    return

label card12:
    show Büyücü at buyucu_poz
    Büyücü "Biraz paraya ihtiyacım var elimdeki sadakat iksirini seninle paylaşabilirim ne dersin. "
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2
            $ mnc_chng("lp_mnc",1)
            $ unlock_level(22)
            $ mnc_info[11]["val"] = 1
            $ check_bars()
            hide image Büyücü
            show Kraliçe at kraliçe_poz
            show lp_mnc at lp_mnc_poz
            Kraliçe "Aldığınız bu iksiri sizi siyaset ve din değeri dolduğunda yönetime devam etmenizi sağlayacaktır." 
            Kraliçe "Bu kartı yukarıdaki menüden görüntüleyebilirsin."
            hide image lp_mnc
        "İksirlere inanmıyorum renkli su!":
            $ Religion += 1
            $ check_bars()
    hide image Kraliçe
    hide image Büyücü
    $ main_story_count += 1
    jump random_dialog
    return
