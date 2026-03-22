label dialog1:
    show Demirci at demirci_poz       
    Demirci "Kralım elime kaliteli bir maden geçti bununla ne yapmalıyım?"
    $ daily_visitors += 1
    menu:
        "Tarım aletleri yapabiliriz.":
            $ People += 1
            $ Economy += 1
            Demirci "Halk memnun olacaktır."
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Madeni satabiliriz.":
            $ Economy += 2
            Demirci "Güzel kar ettik."
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog2:
    show Ozan at ozan_poz
    Ozan "Kralım bu mutsuz ahali için hazinenizden bir eğlence..."
    $ daily_visitors += 1
    menu:
        "Çok güzel olur, hadi yapalım.":
            $ People += 1
            $ Economy -= 2
            Ozan "Harika!"
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Ülkenin parasını çarçur edemeyiz.":
            Ozan "Ufff..."
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog3:
    show Muhafız_Başı at muhafiz_basi_poz    
    Muhafız_Başı "Ordumuzun gücünü artırmak için yeni askerler toplamalıyız"
    $ daily_visitors += 1
    menu:
        "Evet, ordumuzu güçlendirelim.":
            $ Military += 2
            $ Economy -=1
            $ People -=1
            Muhafız_Başı "Halk hoşnut olmayacak ama ordumuz güçlenecek." 
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Hayır, halkın tepkisini çekebiliriz.":
            $ People += 1
            Muhafız_Başı "Peki."
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)      
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1) 
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog4:
    show Asker at asker_poz      
    Asker "Saygıdeğer Kralım talimler çok fazla sayısını azaltmalısınız."
    $ daily_visitors += 1
    menu: 
        "Muhafız Başı ile konuşacağım":
            $ Military -=1
            Asker "Çok yaşayın efendimiz"
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Gerek yok":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1) 
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog5:
    show Çiftçi at ciftci_poz    
    Çiftçi "saygıdeğer Kralım Köyümüzü fareler bastı lütfen yardım edin"
    $ daily_visitors += 1
    menu:
        "Ordudan bir bölük gönderiyorum":
            $ Military -= 2
            $ People +=2
            Çiftçi "Teşekkür ederim efendimiz"
            $ check_bars()
            $ chr_chng("çiftçi","+",1)

        "Başınızın çaresine bakın":
            $ People -= 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog6:
    show Baş_İmam at bas_imam_poz
    Baş_İmam "Ülkedeki camiler yetersiz halkımız dışarda kalıyor destek talep ediyorum"
    $ daily_visitors += 1
    menu:
        "Tamam vereceğim":
            $ Economy -= 2 
            $ Religion += 2
            $ check_bars()
            $ chr_chng("baş_imam","+",1)

        "Lüzumu yok":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog7:
    show Zengin_Tüccar at zengin_tuccar_poz
    Zengin_Tüccar "Eğer vergilerde indirim yaparsanız kendi halkımdan gelen tacirleri  ülkenize yönlendiririm kazan kazan ne dersiniz"
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum":
            $ Economy += 1
            $ Politics += 2
            Zengin_Tüccar "Doğru karar verdiniz efendim"
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)

        "Herkese nasıl davranılıyorsa sanada öyle davranılacak":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog8:
    show Yerel_Bakan at yerel_bakan_poz        
    Yerel_Bakan "Kralım ülkenin bütçesinin büyük bir kısmı askeriye ye harcanıyor inşaatları arttıralım."
    $ daily_visitors += 1
    menu:
        "Ordunun bütçesine dokunamayız":
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)

        "Olur ülkeyi kalkındıralım":
            $ Military -= 2
            $ Economy += 1
            $ People += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog9:
    show Soylu at soylu_poz      
    Soylu "Yeterli sayıda kölem yok yenilerini nerden bulabilirim"
    $ daily_visitors += 1
    menu:
        "Benim kölelerimin birazını satın alabilirsin":
            $ Economy += 2
            $ Politics -= 1
            Soylu "Teşekkürler"
            $ check_bars()
            $ chr_chng("soylu","+",1)

        "Bu benim sorunum değil":
            Soylu "Doğru, değil."
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog10:
    show Kadı at kadi_poz        
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor."
    $ daily_visitors += 1
    menu:
        "Arazi Soylunun hakkı":
            $ Politics += 1 
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("kadı","+",1)

        "Arazi Tacirin hakkı":
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog11:
    show Şifacı at sifaci_poz
    Şifacı "Tıp için bir araştırma yapmam gerekiyor bütçeyi nasıl oluşturayım?"
    $ daily_visitors += 1
    menu: 
        "Ben vereceğim":
            $ Economy -= 2
            $ Health += 1
            Şifacı "Teşekkür ederim efendim"
            $ check_bars()
            $ chr_chng("şifacı","+",1)

        "Bu araştırma gereksiz":
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog12:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Kralım, mutfağınızda kullanılan malzemeler bayat ve kalitesiz. Daha iyi ve taze malzemeler almak için bütçemizi artırmalıyız, yoksa hastalıklar baş gösterebilir."
    $ daily_visitors += 1
    menu:
        "Tamam, bütçeyi arttıracağım.Temizlik önemli.":
            $ Economy -= 1
            $ Health += 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)

        "Yemeklerimiz yeterince iyi.Gereksiz şeyler sorma!!":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog13:
    show Büyücü at buyucu_poz        
    Büyücü "Efendim, son zamanlarda kıtlık arttı. Bunun doğal sebeplerle mi, yoksa bir lanet yüzünden mi olduğunu belirlemem için sizden destek istiyorum."
    $ daily_visitors += 1
    menu:
        "Tamam destek olucağım.":
            $ Economy -= 3
            $ check_bars()
            $ chr_chng("büyücü","+",1)

        "Sana inanmıyorum.":
            $ Religion += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog14:
    show Otacı at otaci_poz      
    Otacı "Yeni bir iksir geliştirdim, hastalıklara karşı çok etkili ama içeriği biraz… alışılmadık."
    $ daily_visitors += 1
    menu:
        "Deneyin, işe yarıyorsa sorun yok.":
            $ Religion -= 2
            $ Health += 2
            Otacı "Majesteleri, sağduyunuz her derde deva!"
            $ check_bars()
            $ chr_chng("otacı","+",1)

        "Hayır, halk arasında huzursuzluk çıkarır.":
            $ Religion += 1
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog15:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Halk kütüphanemiz depremde zarar görmüştü hala tamir edilmedi"
    $ daily_visitors += 1
    menu:
        "Şuan ki durumu iyi":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)

        "Onarım başlasın":
            $ Politics += 1
            $ People += 1
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog16:
    show Demirci at demirci_poz
    Demirci "Kralım malzemeler yetersiz sağlık için ayrılına bütçeden madenler için biraz kullanılmasını talep ediyorum"
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum":
            $ Health -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Reddediyorum":
            $ People -= 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog17:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2,4)
    Demirci "Kralım askerler talimlerde kılıçlara zarar veriyor buda daha çok kılıç üretmemize neden oluyor"
    $ daily_visitors += 1
    menu :
        "Talimleri azaltıyorum":
            $ Military -= 2
            $ Economy += 1
            Demirci "Minnettarım kralım"
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "düzeni bozma":
            $ People -= 1
            $ check_bars ()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog18:
    show Demirci at demirci_poz
    Demirci "Kralım elime değerli bir maden geçti bununla ne yapayım"
    $ daily_visitors += 1
    menu:
        "Sat":
            $ Economy += 2
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Silah yap":
            $ Military += 2
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog19:
    show Demirci at demirci_poz
    Demirci "Kralım imam camilerde süs için iyi çelik kullanmak istiyor ne yapalım"
    $ daily_visitors += 1
    menu:
        "Kullan":
            $ Economy -= 2
            $ Religion += 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Gerek yok":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog20:
    show Demirci at demirci_poz
    Demirci "Kralım daha çok demir ocağı yapmamız gerek tarım aletleri üretemiyoruz"
    $ daily_visitors += 1
    menu:
        "İnşaat başlasın":
            $ Economy -= 2
            $ People += 1
            Demirci "Çok doğru karar."
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Lüzum yok":
            $ People -= 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog21:
    show Demirci at demirci_poz
    Demirci "Köylülerden biri sinirlenip sabanı kırdı ne ceza verelim?"
    $ daily_visitors += 1
    menu:
        "Onu affedelim":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Para cezası verelim":
            $ People -= 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog22:
    show Demirci at demirci_poz
    Demirci "Kralım ülkenizdeki askeri gücü arttırmak için bir fikrim var, bana gereken desteği sağlarsanız bunu yaparım"
    $ daily_visitors += 1
    menu:
        "Hazineden alabilirsin":
            $ Economy -= 3
            $ Military += 2
            Demirci "Bana güvenebilirsiniz."
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Askeri gücümüz yeterli":
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog23:
    show Demirci at demirci_poz
    Demirci "Kralım, soyluların evinde çok fazla değerli maden var. Bunları eritip tarım aleti yapmalıyız."
    $ daily_visitors += 1
    menu:
        "Haklısın, tüm izinleri veriyorum":
            $ Politics -= 2
            $ Economy += 2
            $ People += 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Soyluların şahsi mallarına dokunamayız":
            $ Politics += 1
            Demirci "Sanırım haklısınız."
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog24:
    show Demirci at demirci_poz
    Demirci "Elimde bazı değerli madenler var. Ne yapayım Kralım?"
    $ daily_visitors += 1
    menu:
        "Ameliyat aletleri yapalım":
            $ Health += 2
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Satalım":
            $ Economy += 2
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog25:
    show Demirci at demirci_poz
    Demirci "Kralım, sizdeki iyi bir zırh takımını Bertrumlu bir tacir istiyormuş. Ne yapmak istersiniz?"
    $ daily_visitors += 1
    menu:
        "Tamam, satıyorum":
            $ Economy += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Benim küçük tacirlerle işim olmaz":
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog26:
    show Demirci at demirci_poz
    Demirci "Kralım, halkın silahları eskidi ve düşman sınırlarda geziyor. Yeni silahlar yapmam için bana daha fazla demir ve kömür tahsis edin."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum, ordumuzun güçlenmesi önemli":
            $ Military += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Reddediyorum, şu an kaynaklarımız kısıtlı":
            $ Military -= 1
            $ People += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog27:
    show Demirci at demirci_poz
    Demirci "Kralım, tapınakların kutsal kılıçlarını yenilemek istiyorum. Din adamları bana altın ve gümüş verilmesini talep ediyor."
    $ daily_visitors += 1
    menu:
        "Kutsal işlere kaynak ayırmak elbette önemli":
            $ Religion += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Şu an devletin hazinesi dini işlere yetecek kadar dolu değil":
            $ Religion -= 1
            $ Politics += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog28:
    show Demirci at demirci_poz
    Demirci "Kralım, köylülerin sabanları kırık. Tarım verimi düşecek. Onlara yeni aletler yapmam için bana destek olun!"
    $ daily_visitors += 1
    menu:
        "Halkın refahı önemli, hemen kaynak ayır":
            $ People += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Önce askeri ihtiyaçlar bitmeli":
            $ People -= 1
            $ Military += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog29:
    show Demirci at demirci_poz
    Demirci "Kralım, sarayın korumaları için daha sağlam zırhlar yapabilirim, ancak bu iş için fazla çalışmam gerekecek. Bana ek ücret ödenmeli."
    $ daily_visitors += 1
    menu:
        "Sarayın güvenliği önceliğim, kabul":
            $ Politics += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Şimdilik mevcut zırhlar yeterli":
            $ Politics -= 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog30:
    show Demirci at demirci_poz
    Demirci "Kralım, vebadan kırılan kasabalar için tıbbi aletler yapmak istiyorum. Bana yardımcı olacak birkaç çırak verin."
    $ daily_visitors += 1
    menu:
        "Sağlık her şeyden önemli, hemen çırakları gönderin":
            $ Health += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Başka bölgelerde daha acil ihtiyaçlar var":
            $ Health -= 2
            $ Military += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog31:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Kralım, sınırda görev yapan askerlerimizin erzakları tükenmek üzere. Yeni ikmal için emir verir misiniz?"
    $ daily_visitors += 1
    menu:
        "Derhal erzak gönderin":
            $ Economy -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şehirdeki stoklarımızı zorlamayalım":
            $ Military -= 1
            $ Economy += 1
            Muhafız_Başı "Aç bir asker, zayıf bir sınır demektir, majesteleri…"
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog32:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Son zamanlarda askerler arasında hoşnutsuzluk var. Daha iyi şartlar için şikayet ediyorlar."
    $ daily_visitors += 1
    menu:
        "Maaşlarını artırın":
            $ Economy -= 3
            $ Military += 2
            $ People += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Onlara sadakatlerini hatırlatın":
            $ Military -= 1
            $ Politics += 1
            Muhafız_Başı "Umarım bu kararınız, askerlerin sadakatini sarsmaz, majesteleri…"
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog33:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Sarayınızı koruyan muhafızların sayısını artırmayı öneriyorum. Güvenliğiniz her şeyden önemli."
    $ daily_visitors += 1
    menu:
        "Haklısınız, daha fazla muhafız alın":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şu an için yeterli olduklarını düşünüyorum":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog34:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Komşu topraklardan gelen çapulcular, sınır kasabalarımıza saldırıyor. Ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Ek asker gönderin, halkı koruyun!":
            $ Military -= 2
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Önceliğimiz büyük şehirlerdir":
            $ People -= 2
            $ Economy += 1
            Muhafız_Başı "Sınırdaki halkımız kendini yalnız hissedecek, majesteleri…"
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog35:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Ordumuzun silahları eskiyor. Yeni kılıç ve zırhlar için yatırım yapmalıyız."
    $ daily_visitors += 1
    menu:
        "Demircilere emir verin, yeni silahlar yapılsın!":
            $ Economy -= 3
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Mevcut silahları onarıp kullanın":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog36:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Halk arasında huzursuzluk çıkaran bazı kişiler var. Onları gözaltına alalım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, huzuru bozacak kimseye izin vermeyin!":
            $ People -= 2
            $ Politics += 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Önce onları dinleyelim":
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog37:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Askerlerimizi formda tutmak için büyük bir tatbikat düzenlemeyi öneriyorum."
    $ daily_visitors += 1
    menu:
        "Harika fikir, derhal düzenleyin!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şimdilik gereksiz bir masraf":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog38:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Bazı soylular, ordunun desteğini almaya çalışıyor. Bu bir darbe hazırlığı olabilir."
    $ daily_visitors += 1
    menu:
        "Şüpheli soyluları gözaltına alın!":
            $ Politics -= 1
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Onlarla bir toplantı yapalım":
            $ Politics += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog39:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Bazı muhafızlar rüşvet almakla suçlanıyor. Araştırmamı emreder misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, suçlu olanları cezalandırın":
            $ People += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Göz ardı edin, bunlar küçük meselelerdir":
            $ People -= 2
            Muhafız_Başı "Adaletin zayıflaması, krallığın çöküşüne sebep olabilir…"
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog40:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Yeni savaş stratejileri geliştirmek için daha fazla vakit ve kaynak ayırmalıyız."
    $ daily_visitors += 1
    menu:
        "Bu işe zaman ve para ayırın":
            $ Economy -= 3
            $ Military += 3
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şimdilik mevcut taktiklere güvenelim":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog41:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Şehirde suç oranı artıyor. Daha fazla devriye görevlendirelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın güvenliği her şeyden önemli!":
            $ Economy -= 2
            $ People += 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Halk kendi güvenliğini sağlamalı":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog42:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Sarayda bir suikast girişimi oldu. Soruşturma başlatılsın mı?"
    $ daily_visitors += 1
    menu:
        "Derhal başlatın, hainler bulunmalı!":
            $ Politics += 1
            $ Military += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Bu bir söylenti olabilir, önemsemeyin":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog43:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Kale duvarlarımızın bazı bölümleri eskiyor. Onları güçlendirelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, krallığımızı koruyalım":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şimdilik bir tehdit yok, erteleyin":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog44:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Düşman casuslarının sarayımıza sızdığına dair bilgiler var."
    $ daily_visitors += 1
    menu:
        "Derhal casusları tespit edin ve tutuklayın!":
            $ Military += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Önce onların amaçlarını öğrenelim":
            $ Politics += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog45:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim Narga Krallığı sınırlarımızı ihlal ediyor buna bir son vermemiz gerek."
    $ daily_visitors += 1
    menu:
        "Savaş açalım hadlerini aşmasınlar":
            $ Economy -= 1
            $ People -= 2
            $ Military -= 2
            $ Politics += 2
            Muhafız_Başı "Efendim, savaş ilan edildi."
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Barış imzalayalım, şartlarını kabul edelim":
            $ Economy -= 3
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog46:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim askerler arasında bir husumet çıktı bu sorunu çözmeliyiz."
    $ daily_visitors += 1
    menu:
        "Bölükleri ayıralım, husumet dağılsın":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Komutan sen değil misin, bastır onları":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog47:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim Kuzey bölgesinden bir grup haydut bir köyü basıp insanları rehin almış."
    $ daily_visitors += 1
    menu:
        "Ben haydutlarla pazarlık yapmam, orduyu üzerlerine sür":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Ne istiyorlarsa verip köylüleri kurtarın":
            $ Economy -= 2
            $ People += 1
            Muhafız_Başı "Efendim, köylüler kurtarıldı."
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog48:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim ordu için ekipman yetersiz, sağlıkçıların aletlerini eritip silah yapalım mı?"
    $ daily_visitors += 1
    menu:
        "Olur, demircilere talimat verin":
            $ Military += 1
            $ Health -= 2
            Muhafız_Başı "Efendim, silahlar hazır."
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şu anki durum yeterli":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog49:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim ordudaki askerlerin sayısı az, buna bir çözüm bulalım."
    $ daily_visitors += 1
    menu:
        "Köylerden asker toplamaya çıkın":
            $ Military += 1
            $ People -= 2
            Muhafız_Başı "Efendim, köylerden askerler toplandı."
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Paralı asker alalım":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog50:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim asker sayımız çok fazla, bazılarını size koruma olarak verebilirim."
    $ daily_visitors += 1
    menu:
        "Yeterli muhafızım var":
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
        "Olur, ver bakalım":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog51:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Bir grup haydut yolumuzu kesmişti, hepsini öldürüp silahlarını aldık. Bunları ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Eritip tarım aletleri yapalım":
            $ Economy += 1
            $ People += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Askerlerimiz kullansınlar":
            $ Military += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog52:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Askerlerimiz savaş ganimetleri arasında bir takım sıhhiye aletleri buldu. Kime verelim?"
    $ daily_visitors += 1
    menu:
        "Otacılara verelim":
            $ Health += 1
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
        "Şifacılara verelim":
            $ Health += 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog53:
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim, askerler aileleri için ayrıcalık talep ediyorlar."
    $ daily_visitors += 1
    menu:
        "Herkes eşit haklara sahip olmalı":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","-",1)
        "Ayrıcalıkları verelim":
            $ Military += 1
            $ People -= 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("mhf_baş","+",1)
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog54:
    show Kadı at kadi_poz   
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor. Adaletin tecelli etmesi için kararınızı bekliyorum."
    $ daily_visitors += 1
    menu:
        "Bu topraklar Tacir'e ait. ":
            $ Economy += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Bu topraklar Soylu'ya ait.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog55:
    show Kadı at kadi_poz
    Kadı "Efendim, şehirdeki zengin bir tüccar, ödediği vergilerin haksız olduğunu iddia ediyor. Eğer bu konu çözülemezse, diğer tacirler de aynı yola başvurabilir."
    $ daily_visitors += 1
    menu:
        "O da herkes gibi vergisini ödemeli.":
            $ People += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Ona ayrıcalık tanıyabiliriz.":
            $ Economy -= 1
            $ People -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog56:
    show Kadı at kadi_poz
    Kadı "Majesteleri, köylüler genç bir kadını büyücülükle suçluyor. Kadının suçlu olup olmadığına karar vermek için sizden bir hüküm beklenmektedir."
    $ daily_visitors += 1
    menu:
        "Büyü saçmalıklarına inanmam.": 
            $ People -= 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Büyü mü? O zaman idam edilsin.":
            $ People += 1
            $ Religion += 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog57:
    show Kadı at kadi_poz
    Kadı "Kralım, muhafızlardan biri düşman krallıkla gizlice haberleşmekle suçlanıyor. Kanıtlar yetersiz ama halk idam edilmesini istiyor. Adaletin sağlanması için kesin bir emir vermelisiniz."
    $ daily_visitors += 1
    menu:
        "İdam edelim, şüphe kalmasın.":
            $ Military -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
        "Hapis cezası verelim.":
            $ check_bars()
            $ chr_chng("kadı","+",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog58:
    show Kadı at kadi_poz
    Kadı "Kralım, adaletin doğru ve hızlı bir şekilde yerine getirilebilmesi için yeni bir mahkeme binasına ihtiyacımız var. Eski bina küçük ve yetersiz kaldı."
    $ daily_visitors += 1
    menu:
        "Yeni bir mahkeme binası yapalım.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Gerek yok, eski bina yeterli.":
            $ Politics -= 1
            $ People -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog59:
    show Kadı at kadi_poz
    Kadı "Efendim, yargıçlar ve mahkeme personelinin maaşları çok düşüktür. Onların maaşlarında bir artış yapılmasını talep ediyorum."
    $ daily_visitors += 1
    menu:
        "Maaşlara zam yapalım.":
            $ Economy -= 1
            $ People -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Maaşlarınız yeterli.":
            $ Economy += 1
            $ People += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog60:
    show Kadı at kadi_poz
    Kadı "Bazı suçlar, halk arasında büyük tartışmalara yol açıyor. Bu durumu önlemek için belirli suçların cezalarında değişiklik yapmamız gerekiyor."
    $ daily_visitors += 1
    menu:
        "Sorunlu cezalar hafiflesin.":
            $ People += 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Cezalar caydırıcı olmalıdır.":
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog61:
    show Kadı at kadi_poz
    Kadı "Ülkemizin büyüklüğü ve adalet talepleri göz önüne alındığında, daha fazla kadı ve yargıç atanmasına ihtiyaç var."
    $ daily_visitors += 1
    menu:
        "Hemen işlemleri başlatıyorum.":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Daha fazla alım yapamayız.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog62:
    show Kadı at kadi_poz
    Kadı "Kralım, halk arasında eşitlik ve adaletin sağlanması adına, köylerde ve kasabalarda da düzenli olarak duruşmalar yapılmalıdır."
    $ daily_visitors += 1
    menu:
        "Köylülerin de hakkını koruyalım.":
            $ Economy -= 1
            $ People += 2
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Alt tabaka insanlarla uğraşmayalım.":
            $ People -= 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog63:
    show Kadı at kadi_poz
    Kadı "Büyük Kralım, kadınların ve çocukların korunması hususunda daha fazla önlem alınmasını rica ediyorum. Bu, toplumda adalete olan güveni pekiştirecek ve halkın huzurunu sağlayacaktır."
    $ daily_visitors += 1
    menu:
        "Kadın ve çocukların korunması için yeni yasalar çıkaralım.":
            $ People += 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("kadı","+",1)
        "Bunu ancak toplum düzeltebilir.":
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kadı","-",1)
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog64:
    show Çiftçi at ciftci_poz
    Çiftçi "Majesteleri, fareler bir tür veba taşıyor ve insanlarımız ölüyor lütfen yardım edin!"
    $ daily_visitors += 1
    menu:
        "Otacıları köyünüze yolluyorum.":
            $ People += 2
            $ Health -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Askerleri yolluyorum tüm hastalar yakılacak!":
            $ People -= 3
            $ Military -= 1
            $ Health += 2
            $ check_bars()
            Çiftçi "Bunu yapmayın efendim."
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog65:
    show Çiftçi at ciftci_poz
    Çiftçi "Majesteleri, bu yılın hasadı çok iyi olacak gibi görünüyor. Vergileri biraz hafifletebilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın yükünü azaltın!":
            $ People += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Hayır, güçlü bir ekonomi için vergiler aynı kalmalı!":
            $ People -= 2
            $ Economy += 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog66:
    show Çiftçi at ciftci_poz
    Çiftçi "Topraklarımız kuruyor, sulama kanalları yapamaz mıyız?"
    $ daily_visitors += 1
    menu:
        "Evet, su yolları inşa edin!":
            $ Economy -= 3
            $ People += 2
            Çiftçi "Sağ olun, majesteleri. Topraklarımız size minnettar olacak!"
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu yıl idare edin, şimdilik bütçe yok.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog67:
    show Çiftçi at ciftci_poz
    Çiftçi "Köyümüzde veba var! Doktorlar gönderir misiniz?"
    $ daily_visitors += 1
    menu:
        "Derhal şifacıları yollayın!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Köyü karantinaya alın, ama daha fazla uğraşmayın.":
            $ People -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog68:
    show Çiftçi at ciftci_poz
    Çiftçi "Yabancı tüccarlar mallarımızı ucuza alıyor, onlara karşı bir şey yapacak mısınız?"
    $ daily_visitors += 1
    menu:
        "Tüccarlarla görüşüp fiyatları adil hale getirin!":
            $ Politics -= 1
            $ Economy += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Serbest ticaret böyle işler, alışmalısınız.":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog69:
    show Çiftçi at ciftci_poz
    Çiftçi "Vergi memurları haksız yere fazladan para alıyor!"
    $ daily_visitors += 1
    menu:
        "Onları cezalandırın, halkı koruyun!":
            $People += 2
            $Politics -= 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Memurlar işini bilir, boşuna şikayet etmeyin!":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog70:
    show Çiftçi at ciftci_poz
    Çiftçi "Sürüdeki koyunlarımız kayboldu, hırsızlar mı aldı bilemiyoruz…"
    $ daily_visitors += 1
    menu:
        "Birkaç asker gönderin, hırsızları bulun!":
            $ Military -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Çiftlik işlerine karışamayız, kendi başınızın çaresine bakın.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog71:
    show Çiftçi at ciftci_poz
    Çiftçi "Yeni araziler açarsak daha fazla mahsul yetiştirebiliriz."
    $ daily_visitors += 1
    menu:
        "Toprak genişletme projelerine başlayın!":
            $ Economy -= 3
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şimdilik elimizdekilerle idare edin.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog72:
    show Çiftçi at ciftci_poz
    Çiftçi "Baş İmam, kutsal dualarla hasadın bereketli olacağını söylüyor. Bir ayin düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, ayini düzenleyin!":
            $ Religion += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Dualarla mahsul artmaz, çalışmaya devam edin!":
            $ Religion -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog73:
    show Çiftçi at ciftci_poz
    Çiftçi "Ürünlerimizin çoğu şehre gidiyor, köydekiler aç kalıyor!"
    $ daily_visitors += 1
    menu:
        "Şehirden köylere daha fazla yiyecek gönderin.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şehir halkı önceliklidir, köylüler sabretsin.":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog74:
    show Çiftçi at ciftci_poz
    Çiftçi "Askerlerimiz eğitim yaparken ekinlerimizi eziyor, buna bir çözüm bulunabilir mi?"
    $ daily_visitors += 1
    menu:
        "Eğitim alanlarını başka bir yere taşıyın!":
            $ Military -= 1
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Tarla her yıl büyür, askerlerimiz daha önemli!":
            $ People -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog75:
    show Çiftçi at ciftci_poz
    Çiftçi "Gençlerimiz köyleri terk edip şehre gidiyor, tarım zayıflıyor…"
    $ daily_visitors += 1
    menu:
        "Köylere teşvik verin, daha fazla kişi tarımla uğraşsın!":
            $ Economy -= 3
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şehirde daha çok insana ihtiyaç var, bu doğal bir süreç.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog76:
    show Çiftçi at ciftci_poz
    Çiftçi "Tohum bulmak zorlaştı, ekim yapamazsak kıtlık başlar!"
    $ daily_visitors += 1
    menu:
        "Tohum desteği sağlayın!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Çiftçiler kendi yollarını bulmalı.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog77:
    show Çiftçi at ciftci_poz
    Çiftçi "Geleneksel hasat festivalimizi düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın morale ihtiyacı var!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Festival gereksiz harcamadır, iptal edin.":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog78:
    show Çiftçi at ciftci_poz
    Çiftçi "Şiddetli bir fırtına yüzünden tarlalarımız mahvoldu!"
    $ daily_visitors += 1
    menu:
        "Çiftçilere yardım edin!":
            $ Economy -= 3
            $ People += 2
            Çiftçi "Bizi unutmadığınız için minnettarız, majesteleri!"
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu yıl kaybı kabullenmek zorundayız.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog79:
    show Çiftçi at ciftci_poz
    Çiftçi "Kendimizi haydutlara karşı koruyabilmek için silah taşıyabilir miyiz?"
    $ daily_visitors += 1
    menu:
        "Evet, köylülere basit silahlar verin!":
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Hayır, ordu varken köylülerin silaha ihtiyacı yok.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog80:
    show Çiftçi at ciftci_poz
    Çiftçi "saygıdeğer Kralım bana güneydeki arsalarınızı verirseniz onları sizin için ekebilirim."
    $ daily_visitors += 1
    menu:
        "Tamam, kârın bir kısmını alabilirsin.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Benim arsam senin gibi bir çiftçinin insafına bırakılamaz.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
            Çiftçi "Haklısınız efendim."
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog81:
    show Çiftçi at ciftci_poz
    Çiftçi "saygıdeğer Kralımız, biz vergilerimizi ödeyen köylüler askerlerden gereken korumayı alamıyoruz."
    $ daily_visitors += 1
    menu:
        "Bir bölük askeri köyünüze yollayacağım.":
            $ People += 2
            $ Military -= 2
            $ Politics -= 1
            Çiftçi "Minnettarım efendim."
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Size savaşmayı öğretmesi için bir komutanımı göndereceğim.":
            $People += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog82:
    show Çiftçi at ciftci_poz
    Çiftçi "saygıdeğer Kralımız, köylüler olarak taleplerimizi bildirmek için sizinle bir görüşme yapmak istiyoruz."
    $ daily_visitors += 1
    menu:
        "Gerekli önlemleri alıp görüşmeyi yapacağım.":
            $ People += 3
            $ Economy -= 1
            $ Politics -= 1
            $ Military -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Halka bizzat benim görüşmem tehlikeli olacaktır.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog83:
    show Çiftçi at ciftci_poz
    Çiftçi "saygıdeğer Kralımız, köyümüze hiç yağmur yağmadı. Çok zarar ettik, lütfen bu sene vergi almayın."
    $ daily_visitors += 1
    menu:
        "Vergilerinizi azaltıyorum.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Herkes vergisini ödeyecek.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog84:
    show Çiftçi at ciftci_poz
    Çiftçi "saygıdeğer Kralımız, köyümüzde yeterli insan gücü kalmadı. Tarım yaparken zorlanıyoruz. Bize hayvan desteği verir misiniz?"
    $ daily_visitors += 1
    menu:
        "10 baş hayvanı size hibe ediyorum.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu benim sorunum değil.":
            $ People -= 2
            Çiftçi "Haklısınız efendim."
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog85:
    show Çiftçi at ciftci_poz
    Çiftçi "Majesteleri, bu yıl kuraklık hasatlarımızı mahvetti. Vergileri azaltmazsanız ailelerimiz aç kalacak. Lütfen bizden alınan vergiyi bu yıl için düşürün."
    $ daily_visitors += 1
    menu:
        "Vergiler aynı kalacak.":
            $ People -= 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
        "Vergilerinizi ben ödeyeceğim.":
            $ Economy -= 3
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog86:
    show Çiftçi at ciftci_poz
    Çiftçi "Kralım, yıllardır lordumun topraklarında çalışıyorum ama kendi ailem için hiçbir şeyim yok. Bana ve aileme işleyebileceğimiz küçük bir arazi bağışlamanızı dilerim."
    $ daily_visitors += 1
    menu:
        "Sana ve ailene arazi veriyorum.":
            $ Politics -= 3
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu kabul edilemez.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog87:
    show Çiftçi at ciftci_poz
    Çiftçi "Efendimiz, köyümüzden çok fazla genç erkek askere alındı. Tarlalarımızı ekecek kimse kalmadı. Daha fazla adam almamanız için yalvarıyorum."
    $ daily_visitors += 1
    menu:
        "Asker alımlarını azaltıyorum.":
            $ People += 2
            $ Military -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Sanmıyorum.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog88:
    show Çiftçi at ciftci_poz
    Çiftçi "Efendim, haydutlar ve paralı askerler köylerimizi talan ediyor. Kadınlarımız ve çocuklarımız korku içinde yaşıyor. Bizi koruyacak bir grup asker gönderir misiniz?"
    $ daily_visitors += 1
    menu:
        "Köyünüze bir bölük asker gönderiyorum.":
            $ Military -= 1
            $ People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Köyünüzü korumak için bir de asker mi göndereceğim, git başımdan!":
            $ People -= 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog89:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Kralım su baskınında zarar gören evleri onarmamız gerekiyor."
    $ daily_visitors += 1
    menu:
        "Tamam onaralım":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Şuan yeterli maliyemiz yok.":
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog90:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Ülkedeki camiler yetersiz, destek talep ediyorum."
    $ daily_visitors += 1
    menu:
        "Tamam, câmi yapımı için destek vericem.":
            $ Economy -= 2
            $ Religion += 2
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Câmi'lerin yeterli olduğunu düşünüyorum, talebinizi reddediyorum.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog91:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Camilerde topladığımız yardımlar arttı, bu kadarına ihtiyacımız yok. Ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Halka yemek dağıtalım.":
            $ People += 1
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Orduya yemek dağıtalım.":
            $ Military += 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog92:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Gençlerimizin gereken eğitimi alması için medreseler açalım."
    $ daily_visitors += 1
    menu:
        "Gençlerin gelişimi için gerekli buluyorum.":
            $ Economy -= 2
            $ Politics += 2
            $ People += 1
            $ Religion += 1
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Gençlerimizin zaten bilinçli olduğunu düşünüyorum.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog93:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Vergilerin bir kısmı ile başıboş kişilere eğitim verelim."
    $ daily_visitors += 1
    menu:
        "Çok iyi fikir.":
            $ Economy -= 2
            $ Religion += 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Zaten işlerim var, bir de bunlara para veremem.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog94:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Efendimiz, şehirlerimizde kumar, içki ve sefahat artıyor. Bu günahları önlemek için daha sert yasalar getirmenizi rica ediyorum."
    $ daily_visitors += 1
    menu:
        "Yeni yasalar getirilsin.":
            $ People -= 2
            $ Religion += 3
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Burası laik bir krallık, isteyen istediğini yapar.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog95:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Kralım, halkın inancını güçlendirmek için kutsal bir günü kraliyet kararıyla resmî bayram ilan edelim."
    $ daily_visitors += 1
    menu:
        "Tamam, hangi günler olsun?":
            $ Economy -= 1
            $ Religion += 2
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Böyle bir şey olmayacak.":
            $ Religion -= 2
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog96:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Baş_İmam "Majesteleri, kararlarınıza rehberlik etmesi için yanınıza bir din bilgini almanızı öneririm."
    $ daily_visitors += 1
    menu:
        "Mantıklı, ben de arıyordum. Sen olmak ister misin?":
            $ Politics -= 1
            $ Religion += 2
            $ check_bars()
            $ chr_chng("baş_imam","+",1)
        "Siyaset bilmezsin, hâlâ diyorsun yanıma din adamı alayım.":
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog97:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Daha fazla hizmetçi ve köle istiyorum."
    $ daily_visitors += 1
    menu:
        "Olmaz.":
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "İstediğini alacaksın.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog98:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Evimin yanındaki inşaat yıkıldı ve evimin duvarı zarar gördü karşılanmasını talep ediyorum."
    $ daily_visitors += 1
    menu:
        "Tüm zararın benim tarafımdan ödenecek.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Git inşaat sahibinden al zararını.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog99:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Pazarlarda büyük tüccarlar çok kar ederken küçük tüccarlar zarara uğruyor bunun önüne geçmemiz gerek."
    $ daily_visitors += 1
    menu:
        "Vergileri adaletli yapalım.":
            $ Politics += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Vergileri eşit yapalım.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog100:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Komutanlar çok kazanıyor maaşlarını azaltıp başka alanlara yöneltelim."
    $ daily_visitors += 1
    menu:
        "İnşaatları arttıralım.":
            $ Economy += 1
            $ Military -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Komutanlarımın sadakatini sorgulama.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

    label dialog101:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Ülke zor durumda, bazı Soylular elindeki değerli eşyaları size vermek istiyor."
    $ daily_visitors += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Askeri harcamalar yapalım.":
            $ Military += 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog102:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Efendim bazı köyler eksik vergi ödemişler ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Kalan borçlarını ödesinler.":
            $ Economy += 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Cezalandırılacaklar.":
            $ Economy += 3
            $ People -= 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog103:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Tavernada bir eğlence düzenlemek istiyorum bu sayede tacirler ülkemize daha çok uğrar."
    $ daily_visitors += 1
    menu:
        "Mantıklı, ücretini karşılıyorum.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Böyle şeylere para harcamak mantıklı değil.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog104:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Kralım kölelerim çok fazla, size satmak istiyorum."
    $ daily_visitors += 1
    menu:
        "Tamam hepsini satın alıyorum. Askeriyede getir götür için çalışacaklar.":
            $ Economy -= 2
            $ Military += 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Kölelerin çoksa onlara el koyuyorum, tarlalarda çalışacaklar.":
            $ Economy += 2
            $ People += 1
            $ Politics -= 3
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog105:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Daha fazla para için köleleri su kenarlarına götürelim, balık yakalasınlar."
    $ daily_visitors += 1
    menu:
        "Kölelerinizi balıkçılık yapmaları için götürelim.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Kölelerinizi balıkçılık yapmaları için götürmeyin, köleler de insan.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog106:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Köylerden gelen vergileri arttıralım."
    $ daily_visitors += 1
    menu:
        "Vergileri arttıralım.":
            $ Economy += 2
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Vergiler ideal.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog107:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Daha fazla para için köleleri inşaatlarda çalıştıralım."
    $ daily_visitors += 1
    menu:
        "Köleleri inşaatlarda çalıştıralım.":
            $ Economy += 2
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Köleler de insan, zaten çok çalışıyorlar.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog108:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Majesteleri, bana bir toprak bağışlamanızı talep ediyorum. Böylece hem krallığınıza daha fazla vergi ödeyebilir hem de sınırları koruyabilirim."
    $ daily_visitors += 1
    menu:
        "Toprak bağışlıyorum.":
            $ Politics -= 3
            $ Economy += 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Kendi alabiliyorsa alsın, benden toprak yok.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog109:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Efendim, danışmanlarınız arasında daha fazla söz hakkına sahip olmalıyım. Kraliyet konseyinizde bana bir yer verirseniz, tecrübemle kararlarınıza rehberlik edebilirim."
    $ daily_visitors += 1
    menu:
        "Kraliyet konseyine alıyorum.":
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Kraliyet konseyine almam söz konusu bile olamaz.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog110:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Majesteleri, güçlü bir ittifak ve sizin otoritenizi güçlendirmek için beni bir başka asille evlendirmenizi rica ediyorum."
    $ daily_visitors += 1
    menu:
        "İttifak için evlendiriyorum.":
            $ Politics += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Gerek yok, ittifaklarım zaten güçlü.":
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog111:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Majesteleri, kraliyet sarayında daha görkemli balolar düzenleyerek halkın gözündeki ihtişamınızı artırabiliriz. Ne dersiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, büyük bir şölen düzenleyin!":
            $ Economy -= 2
            $ Politics += 2
            Soylu "Halkınıza ihtişamınızı göstermek her zaman iyi bir fikirdir, majesteleri!"
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Şu an gereksiz masraflardan kaçınmalıyız.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog112:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Köylüler, biz soyluların ayrıcalıklarını sorgulamaya başladı. Bu durum düzeni bozabilir!"
    $ daily_visitors += 1
    menu:
        "Halkın şikayetlerini dikkate alıp onlarla uzlaşmalıyız.":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Soylular krallığın temelidir, köylüler haddini bilmeli!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog113:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Soyluların güvenliği için daha fazla saray muhafızı istiyoruz."
    $ daily_visitors += 1
    menu:
        "Tamam, güvenlik artırılsın.":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Şu an böyle bir bütçemiz yok.":
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog114:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Soylular için büyük bir av partisi düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Elbette, eğlence de lazım!":
            $ Economy -= 2
            $ Politics += 2
            Soylu "Neşeli bir av partisi, herkesin moralini yükseltecektir!"
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Şu an böyle bir şeye zaman ve para harcayamam.":
            $ Economy += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog115:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Yabancı prenslerden biri, kraliyet ailesinden biriyle evlenmek istiyor."
    $ daily_visitors += 1
    menu:
        "Bu evlilik ittifaklarımızı güçlendirebilir, kabul edin.":
            $ Politics += 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Kraliyet ailesinin yabancılarla evlenmesine izin vermem.":
            $ Politics -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog116:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Sanat ve edebiyat gelişmeli! Saraya yeni şairler ve ressamlar alalım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, kültürümüz gelişmeli!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Şu an daha önemli meselelerimiz var.":
            $ Economy += 1
            $ People -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog117:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Soylular üzerindeki vergi yükü çok fazla. Vergilerimizi azaltmayı düşünür müsünüz?"
    $ daily_visitors += 1
    menu:
        "Hayır, herkes adil şekilde vergi ödeyecek.":
            $ Politics -= 2
            $ Economy += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Haklısınız, soylular vergiden muaf olsun.":
            $ Politics += 2
            $ Economy -= 2
            Soylu "Ne kadar bilge bir karar, majesteleri!"
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog118:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Krallığın bazı topraklarını soylulara tahsis etsek yönetimi daha kolay olur."
    $ daily_visitors += 1
    menu:
        "Hayır, kraliyet toprakları halka aittir.":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Mantıklı bir öneri, topraklarınızı genişletebilirsiniz.":
            $ People -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog119:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Halkın bize daha fazla saygı duyması için soyluların yetkilerini artırmalıyız."
    $ daily_visitors += 1
    menu:
        "Yetkileriniz yeterli, halkın çıkarlarını da korumalıyız.":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Soylular her zaman üstün olmalıdır!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog120:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Yabancı elçiler için büyük bir ziyafet verelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, diplomatik ilişkiler için bu önemli.":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Gerek yok, böyle masrafları kısmalıyız.":
            $ Economy += 1
            $ Politics -= 1
            Soylu "Çok iyi bir karar, majesteleri! Yabancı elçiler bundan memnun kalacak."
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog121:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Halk, giderek daha fazla lüks tüketim talep ediyor. Bu durum ticaretimizi etkiliyor."
    $ daily_visitors += 1
    menu:
        "Lüks malların vergisini artırın.":
            $ Economy += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Ticaret serbesttir, isteyen istediğini alır.":
            $ People += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog122:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Krallığın gücünü göstermek için büyük bir askeri geçit töreni düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, bu halkın moralini yükseltir!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Şu an buna bütçemiz yok.":
            $ Economy += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog123:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Saraydaki bazı soylular arasında ciddi anlaşmazlıklar var. Müdahale etmeli misiniz?"
    $ daily_visitors += 1
    menu:
        "Tarafları barıştırmaya çalışın.":
            $ Politics += 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Bu onların sorunu, beni ilgilendirmez.":
            $ Politics -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog124:
    show Soylu at soylu_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Soylu "Soylulara özel yeni ayrıcalıklar içeren kanunlar çıkarmayı düşünür müsünüz?"
    $ daily_visitors += 1
    menu:
        "Hayır, herkes eşit olmalı.":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("soylu","+",1)
        "Soylular her zaman ayrıcalıklı olmalı!":
            $ Politics += 2
            $ People -= 2
            Soylu "Bu karar, krallığın güçlü kalmasını sağlayacaktır, majesteleri!"
            $ check_bars()
            $ chr_chng("soylu","-",1)
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog125:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Majesteleri, geceler çok soğuk. Nöbetçiler için daha kalın pelerinler verilebilir mi?"
    $ daily_visitors += 1
    menu:
        "Askerler üşümemeli, yeni pelerinler dikin!":
            $ Economy -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Savaşta konfor olmaz, dayanmalılar!":
            $ Military -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog126:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Majesteleri, yemeğimiz azaldı. Aç karnına savaşamayız…"
    $ daily_visitors += 1
    menu:
        "Askerlerin yiyeceğini artırın!":
            $ Economy -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Tüm halk sıkıntı çekiyor, sabredin!":
            $ Military -= 1
            $ People += 1
            Asker "Haklısınız Kralım."
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog127:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Bazı komutanlar bizi fazla zorluyor, bazen dayak bile atıyorlar…"
    $ daily_visitors += 1
    menu:
        "Hemen soruşturma açın, adaleti sağlayın!":
            $ People += 1
            $ Military -= 1
            Asker "Gerçekten adil bir kral olduğunuza inanıyorum, majesteleri!"
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Ordu disiplinsiz olmaz, böyle şeyler normaldir.":
            $ People -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog128:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Sınırda savaş çıkacağı konuşuluyor. Bu doğru mu?"
    $ daily_visitors += 1
    menu:
        "Henüz kesin bir şey yok, ama hazırlıklı olun.":
            $ check_bars()
            $ asker_relationship += 0
        "Evet, yakında sefere çıkacağız!":
            $ Military += 2
            $ Economy -= 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog129:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Bazı köylüler, askerlerin tarlalarına zarar verdiğini söylüyor."
    $ daily_visitors += 1
    menu:
        "Zararı karşılayın, halkın güvenini kaybetmeyelim.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Bunu büyütmesinler, ordu her şeyden önemli!":
            $ People -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog130:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Ordumuz yeni asker alımı yapıyor. Daha fazla kişi alalım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, güçlü bir ordu her şeydir!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Şimdilik yeterince askerimiz var.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog131:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Nöbetteyken ormanda garip sesler duyduk. Bir grup gönderelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, derhal araştırın!":
            $ Military -= 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Boşuna vakit harcamayın.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog132:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Moralimizi yükseltmek için şölen düzenleyebilir miyiz?"
    $ daily_visitors += 1
    menu:
        "Evet, bir şölen düzenleyin!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Savaşçı eğlence istemez, çalışmaya devam edin!":
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog133:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kamp alanımızın yakınında temiz su yok. Daha iyi bir yer seçelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, su kaynağı olan bir bölgeye geçin.":
            $ Military -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Su bulun, ama kampı değiştirmeyin.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog134:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Yolculuk sırasında birkaç yağmacı gördük, saldırı emri verelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, derhal yok edin!":
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Önce ne istediklerini öğrenin.":
            $ People += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog135:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Zırhlarımız çok ağır, daha hafif malzemelerden yapılabilir mi?"
    $ daily_visitors += 1
    menu:
        "Evet, yeni bir tasarım deneyelim!":
            $ Economy -= 3
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Savaşçılar güçlü olmalı, böyle devam edin!":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog136:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Halk bize pek güvenmiyor gibi. Onlarla daha fazla ilgilenelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, askerler halkla daha çok vakit geçirmeli.":
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Halk bizi sevmese de olur, görevimizi yapalım!":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog137:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Eskiden muhafız olan yaşlı bir adam, tekrar savaşa katılmak istiyor."
    $ daily_visitors += 1
    menu:
        "Onun tecrübesi işe yarayabilir, kabul edin!":
            $ Military += 1
            $ People -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Yaşı ilerlemiş, geri çevirin.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog138:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Birkaç asker firar etti. Onları arayalım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, kaçakları bulun ve cezalandırın!":
            $ Military += 1
            $ People -= 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Peşlerinden gitmeyin, onları unutun.":
            $ Military -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog139:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Saray nöbeti çok sıkıcı, bize başka görevler verilebilir mi?"
    $ daily_visitors += 1
    menu:
        "Görev değişiklikleri yapın.":
            $ Military += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Göreviniz bu, şikayet etmeyin!":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog140:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "saygıdeğer Kralım savaş ganimetlerinin çoğu komutanlarımıza gidiyor adalet istiyoruz."
    $ daily_visitors += 1
    menu:
        "Düzenleme yapacağım.":
            $ Military += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Mevcut düzen iyi.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog141:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "saygıdeğer Kralım silahlarımız eskidi yenilerine ihtiyaç var."
    $ daily_visitors += 1
    menu:
        "Demircilere talimat vericem.":
            $ Military += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Elinizdekilerle yetinin.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog142:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kralım yemekler yeterince iyi değil değişmesini talep ediyoruz."
    $ daily_visitors += 1
    menu:
        "Yemeklerin kalitesini arttıracağım.":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Yemeklerin kalitesi yeterli.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog143:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kralım yatakhaneler çok berbat daha iyilerini hak ediyoruz."
    $ daily_visitors += 1
    menu:
        "Haklısın düzenlemeleri yapacağım.":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "İdare etmeye çalışın.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog144:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kralım askerler size minnetlerini sunmak için sizi kışlaya davet ediyorlar."
    $ daily_visitors += 1
    menu:
        "Kışlaya gideceğim.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Askerleri saraya davet ediyorum.":
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog145:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Majesteleri, savaş meydanında gösterdiğim kahramanlıklar nedeniyle bana ve aileme küçük bir arazi bağışlamanızı rica ederim."
    $ daily_visitors += 1
    menu:
        "Yaptığın kahramanlıklar için minnettarız arazi bağışlıyoruz.":
            $ Politics -= 1
            $ Economy -= 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Hayır sende herkes gibi eşit pay alacaksın.":
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog146:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Efendim, uzun yıllardır ordunuza sadakatle hizmet ettim. Bana şövalyelik unvanı ve komuta edebileceğim küçük bir birlik bahşetmenizi dilerim."
    $ daily_visitors += 1
    menu:
        "Artık yeni bir komutanımız var.":
            $ Politics -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Bunun için çok erken.":
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog147:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Majesteleri, askerlerimiz zor şartlar altında görev yapmaktadır. Orduya daha fazla destek sağlamanızı arz ederim."
    $ daily_visitors += 1
    menu:
        "Haklısın!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Şimdilik bu kadarı yeter.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog148:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kralım, yıllardır seferden sefere koşuyorum. Eşim ve çocuklarım beni görmeyi özledi. Kısa bir süreliğine köyüme dönmem için izin vermenizi istiyorum."
    $ daily_visitors += 1
    menu:
        "Aileni görmek seninde hakkın tabiki gidebilirsin,izin veriyorumm.":
            $ Military -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("asker","-",1)
        "Hayır bölüğünden ayrılamassın.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog149:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Yabancı tüccarlar, bizim sattığımız malların fiyatlarını düşürerek pazarı ele geçiriyor. Müdahale edecek misiniz?"
    $ daily_visitors += 1
    menu:
        "Vergileri artırarak yerli tüccarları koruyun!":
            $ Economy += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Serbest piyasa böyle işler, rekabet iyidir!":
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog150:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Asilzadeler için özel tasarlanmış lüks eşyalar satmayı planlıyoruz. Bunun için özel izin verebilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Soyluların statüsü korunmalı, izin veriyorum!":
            $ Politics += 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Herkes eşittir, böyle ayrıcalık olmaz!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog151:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Majesteleri, tüccarlarımız haydutlar tarafından soyuluyor. Yolların güvenliği artırılsın mı?"
    $ daily_visitors += 1
    menu:
        "Daha fazla muhafız görevlendirin!":
            $ Economy -= 2
            $ Military += 2
            Zengin_Tüccar "Sizin gibi bir kral sayesinde güven içinde ticaret yapabiliriz, majesteleri!"
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Tüccarlar kendi güvenliklerini sağlasın!":
            $ Economy += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)

    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog152:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Büyük bir ticaret festivali düzenleyerek krallığın ekonomisini canlandırabiliriz."
    $ daily_visitors += 1
    menu:
        "Harika fikir, festival düzenlensin!":
            $ Economy += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Böyle etkinlikler gereksiz masraftır!":
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)

    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog153:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Piyasada sahte paralar dolaşıyor, bu durum tüccarları zora sokuyor!"
    $ daily_visitors += 1
    menu:
        "Sahte para basanları ağır şekilde cezalandırın!":
            $ Politics += 2
            $ People -= 1
            Zengin_Tüccar "Sert ama adil bir karar, majesteleri!"
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Serbest piyasa kendi dengesini bulur!":
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)

    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog154:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Yeni bir liman inşa edersek denizaşırı ticaretimizi artırabiliriz."
    $ daily_visitors += 1
    menu:
        "İnşaata başlayın, ekonomi büyüsün!":
            $ Economy += 3
            $ People -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Bu kadar büyük bir harcamaya gerek yok!":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)

    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog155:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Krallığımızdaki kaçakçılar, tüccarların işini zorlaştırıyor. Daha sıkı denetim talep ediyoruz!"
    $ daily_visitors += 1
    menu:
        "Kaçakçılıkla mücadeleyi artırın!":
            $ Politics += 3
            $ People -= 2
            Zengin_Tüccar "Sert ama adil bir karar, majesteleri!"
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Küçük kaçakçılar sorun yaratmaz, görmezden gelelim!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)

    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog156:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Kraliyet ailesine özel tasarlanmış lüks kıyafetler ve mücevherler sunmak isteriz."
    $ daily_visitors += 1
    menu:
        "Saray şanına yakışır, alın!":
            $ Politics += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "İsraf etmeyelim, gereksiz harcama!":
            $ Economy += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
            
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog157:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Majesteleri, tüccarları bir lonca çatısı altında birleştirmek istiyoruz. Bize resmi yetki verebilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, ticaret organize olmalı!":
            $ Economy += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Loncalar zamanla tekel olur, hayır!":
            $ Politics += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog158:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Daha güvenli ticaret için yeni kervan yolları açmayı öneriyoruz."
    $ daily_visitors += 1
    menu:
        "Yol yapımı başlasın!":
            $ Economy += 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Mevcut yollar yeterli, masrafa gerek yok!":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog159:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Küçük tüccarlar büyük borçlar içinde. Borçlarının bir kısmını silebilir miyiz?"
    $ daily_visitors += 1
    menu:
        "Evet, tüccarlara destek olalım!":
            $ People += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Herkes borcunu ödemeli!":
            $ People -= 2
            $ Economy += 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog160:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Sarayın aldığı vergiler çok yüksek, bunları azaltmayı düşünür müsünüz?"
    $ daily_visitors += 1
    menu:
        "Evet, vergileri hafifletelim!":
            $ Economy += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Hayır, sarayın gelirleri azalmaz!":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog161:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Krallık genelinde yeni pazar alanları açarak ticareti genişletebiliriz."
    $ daily_visitors += 1
    menu:
        "Evet, pazar alanları açılsın!":
            $ Economy += 2
            $ People -= 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Şu an için buna gerek yok!":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog162:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Yabancı yatırımcılar krallığımıza büyük paralar getirebilir, onları teşvik edelim mi?"
    $ daily_visitors += 1
    menu:
        "Yatırımcıları teşvik edin!":
            $ Economy += 3
            $ People -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Yabancılar ülkemizi sömüremez!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog163:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Elimde çok değerli bir tarihi eser var bunu almak isteyebilirsiniz."
    $ daily_visitors += 1
    menu:
        "Tamam alıyorum.":
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Ben böyle şeylere para harcamam.":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog164:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Kiralık asker arıyorum ordunuzdan bir bölük alabilirmiyim."
    $ daily_visitors += 1
    menu:
        "Tamam senin için bir bölük hazırlayacağım.":
            $ Politics -= 1
            $ Economy += 3
            $ Military -= 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Ben Kraliyet ordusunu para için savaştırtmam seninle işim yok.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog165:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Demirci "Kralım şahsi atlarınızın eğerleri eskimiş yenileyelim mi?"
    $ daily_visitors += 1
    menu:
        "Olur yapalım.":
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("demirci","+",1)
            
        "Gereksiz harcama olur.":
            $ People += 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog166:
    show Asker at asker_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Asker "Kralım dağ çobanlarından birinin sürüsüne kurtlar dadanmış."
    $ daily_visitors += 1
    menu:
        "Yardım edelim.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("asker","+",1)
        "Kendi sorunu.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("asker","-",1)
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog167:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Kralım, eğer bana ve loncalarıma özel bir vergi indirimi sağlarsanız, size her yıl bol miktarda altın ve mal göndermeye söz veririm."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum Kadı'ya söyleyin.":
            $ Politics -= 3
            $ Economy += 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Bu kabul edilemez.":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog168:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Majesteleri, tuz ve baharat ticaretinin tek yetkilisi ben olayım. Karşılığında size her yıl belirli bir miktar gelir aktarırım."
    $ daily_visitors += 1
    menu:
        "Ben rüşvet kabul etmem.":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
        "Kulağa harika geliyor.":
            $ Politics -= 3
            $ Economy += 2
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog169:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Kralım, ticaretin gelişmesi için yeni bir pazar yeri ya da liman açılmasını öneriyorum. Böylece, yabancı tüccarlar gelip daha fazla vergi ödeyebilirler."
    $ daily_visitors += 1
    menu:
        "İnşaat için köleleri kullanalım ve yeni bir liman açalım.":
            $ Economy += 2
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Pazar yerleri yeterli.":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog170:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Zengin_Tüccar "Efendim, soylular ve Baş imam çok fazla güce sahip. Bana daha fazla yetki verirseniz, ticareti ve dolayısıyla krallığın ekonomisini sizin için büyütürüm."
    $ daily_visitors += 1
    menu:
        "Tamamdır! istediğin olsun.":
            $ Politics -= 2
            $ Religion -= 2
            $ Economy += 3
            $ check_bars()
            $ chr_chng("zng_tcr","+",1)
        "Olmaz!":
            $ check_bars()
            $ chr_chng("zng_tcr","-",1)
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog171:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Majesteleri, devletin gelirlerini artırmak için yeni bir vergi reformu öneriyoruz."
    $ daily_visitors += 1
    menu:
        "Evet, zenginlerden daha fazla vergi alın!":
            $ People += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Hayır, tüccarların yükünü artırmamalıyız!":
            $ People -= 2
            $ Economy += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog172:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Bazı soylular, bölgesel yönetimde daha fazla söz sahibi olmak istiyor. Ne yapmalıyız?"
    $ daily_visitors += 1
    menu:
        "Onlara daha fazla yetki verin!":
            $ Politics += 2
            $ People -= 2
            Yerel_Bakan "Soylular bunu hoş karşılamayacaktır, majesteleri."
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Güç kraldadır, yetkilerini sınırlandırın!":
            $ Politics -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog173:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Halk, yerel yöneticilerin seçimle belirlenmesini talep ediyor."
    $ daily_visitors += 1
    menu:
        "Halkın sesi duyulmalı, seçimlere izin verin!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Monarşi güçlü kalmalı, halk yönetemez!":
            $ People -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog174:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Komşu krallık ile önemli bir diplomatik görüşme yapacağız. Sert mi yoksa ılımlı mı olalım?"
    $ daily_visitors += 1
    menu:
        "Sert olun, gücümüzü gösterelim!":
            $ Military += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Ilımlı olun, diplomasi önemlidir!":
            $ Politics += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog175:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Krallık için bazı yeni yasalar çıkarmalıyız. Adalet sistemini güçlendirelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, daha adil bir yönetim istiyorum!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Kanunları sıkılaştırın, disiplini sağlayın!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog176:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Bazı danışmanlar, sizin yetkilerinizin bir kısmını bakanlara devretmenizi öneriyor."
    $ daily_visitors += 1
    menu:
        "Hayır, güç kraldadır!":
            $ Politics -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
        "Yetkileri paylaşalım, yönetimi kolaylaştıralım!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog177:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Sarayın harcamalarını azaltmayı öneriyorum, hazinemiz zorlanıyor."
    $ daily_visitors += 1
    menu:
        "Evet, tasarruf yapmalıyız!":
            $ Economy += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Hayır, sarayın ihtişamı korunmalı!":
            $ Economy -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog178:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Baş İmam, dini liderlerin daha fazla yetkiye sahip olması gerektiğini söylüyor."
    $ daily_visitors += 1
    menu:
        "Evet, din önemli bir unsurdur!":
            $ Religion += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Devlet ve din ayrı olmalı!":
            $ Religion -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog179:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Yeni bir şehir kurarak nüfusu ve ekonomiyi genişletebiliriz."
    $ daily_visitors += 1
    menu:
        "Harika fikir, şehir kurulsun!":
            $ Economy += 3
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Böyle büyük bir yatırım riskli olur!":
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog180:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Soylular ve köylüler arasındaki gerilim artıyor. Bir çözüm üretmeli miyiz?"
    $ daily_visitors += 1
    menu:
        "Soyluların yetkilerini azaltın!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Soyluların otoritesini koruyun!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog181:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Komşu krallık bize casuslar gönderiyor. Ne yapmalıyız?"
    $ daily_visitors += 1
    menu:
        "Kendi casuslarımızı gönderin!":
            $ Military += 2
            $ Politics -= 2
            Yerel_Bakan "Düşmanlarımıza aynı şekilde cevap vereceğiz, majesteleri."
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Diplomasiyi kullanarak olayı büyütmeyin!":
            $ Politics += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog182:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Halkın sizi daha fazla görmesi için saraydan çıkıp halk arasına karışmanız öneriliyor."
    $ daily_visitors += 1
    menu:
        "Harika fikir, halka yakın olmalıyım!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Kral mesafesini korumalıdır!":
            $ People -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog183:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Yargıçları siz mi atayacaksınız yoksa halk mı seçsin?"
    $ daily_visitors += 1
    menu:
        "Ben atayacağım, adalet sağlam kalmalı!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Halk seçim yapabilmeli!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog184:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Farklı grupları birleştirerek krallık içinde daha büyük bir birlik sağlayabiliriz."
    $ daily_visitors += 1
    menu:
        "Birlik güçtür, herkesi kucaklayın!":
            $ People += 2
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Herkes uyum sağlayamaz, sıkı kurallar koyun!":
            $ Politics += 2
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog185:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Krallığın birliğini simgeleyecek yeni bir arma tasarlamayı öneriyoruz."
    $ daily_visitors += 1
    menu:
        "Harika fikir, halkın da katılımını sağlayın!":
            $ People += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Gereksiz bir çaba, zaten sembollerimiz var!":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog186:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Kralım soyluların elinde çok fazla değerli eşya var bunları eritip ordunun harcamaları için kullanalım."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum gerekenleri yap!":
            $ Politics -= 1
            $ People -= 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Soyluların şahsi mallarına dokunamayız.":
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog187:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Efendim batıdaki köyler sınırlarımıza çok yakın onlar için tehlike arz ediyor."
    $ daily_visitors += 1
    menu:
        "Köylüleri daha güvenli yerlere taşıyalım.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Sınır bölgelerini boşaltırsak o toprakları sahipsiz bırakırız.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog188:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Kralım hazinemiz tükeniyor bir çare bulmamız gerek."
    $ daily_visitors += 1
    menu:
        "Askerleri yağmaya gönderelim.":
            $ Military -= 3
            $ Economy += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Kölelerimizi geceleri de çalıştıralım.":
            $ People -= 2
            $ Economy += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog189:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Efendim hazineden bir miktar altın artırdım bunu ne için kullanalım."
    $ daily_visitors += 1
    menu:
        "Sağlıkçıların eşyalarını yeniliyelim.":
            $ Health += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Ordunun ihtiyaçlarını karşılayalım":
            $ Military += 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog190:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Kralım Zemorvia Krallığı ile barış antlaşmamızın süresi bitiyor yenisini imzalayıp sulhe devam edelim mi?"
    $ daily_visitors += 1
    menu:
        "Olur ticaretteki becerileri ekonomimizi iyileştirecektir.":
            $ Economy += 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Savaşalım orduları bizden zayıf yağma yaparak daha çok ganimet elde edebiliriz.":
            $ Economy += 3
            $ Military -= 3
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog191:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Soyluların çok fazla değerli eşyaları var onlara el koyup hazineye ekleyebiliriz."
    $ daily_visitors += 1
    menu:
        "Ülkenin paraya ihtiyacı var,yapalım.":
            $ People -= 2
            $ Politics -= 2
            $ Economy += 3
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Bu zalimlik olur.":
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog192:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Yonkur Krallığı bize savaş açtığını iletti ne yapacağız."
    $ daily_visitors += 1
    menu:
        "Muhafız başına haber ver savaşalım.":
            $ Military -= 3
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Bu işi masada çözebiliriz.":
            $ Politics += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog193:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Donovia'dan elçi geldi bizden borç istiyorlar karşılığında bize paralı askerler verecekler."
    $ daily_visitors += 1
    menu:
        "Tamam hazineden verelim":
            $ Economy -= 4
            $ Politics += 2
            $ Military += 3
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Bu kadar yüklü bir borcu veremeyiz.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog194:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Majesteleri, hazinemiz zayıflıyor. Soyluların ve büyük tüccarların daha fazla vergi ödemesi için yeni bir düzenleme yapmalıyız."
    $ daily_visitors += 1
    menu:
        "Soylular ve Büyük Tüccarlardan alalım vergiyi.":
            $ Economy += 3
            $ Politics -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Köylülerden alalım vergiyi.":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog195:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Efendim, sarayda ve taşrada bazı memurlar rüşvet alıyor, halk arasında huzursuzluk artıyor."
    $ daily_visitors += 1
    menu:
        "Haklısın hemen işe koyul.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Yiyin birbirinizi.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog196:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Kralım, halkımız giderek daha fazla açlık ve kıtlık içinde."
    $ daily_visitors += 1
    menu:
        "Halka erzak dağıtalım.":
            $ Economy -= 3
            $ Politics -= 1
            $ People += 3
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Bu işe girmeyelim.":
            $ People -= 2
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog197:
    show Yerel_Bakan at yerel_bakan_poz
    $ visitors_today = renpy.random.randint(1, 4)
    Yerel_Bakan "Krallığınızda farklı bölgelerde kanunlar farklı işliyor, bazı lordlar kendi hukukunu uyguluyor."
    $ daily_visitors += 1
    menu:
        "Yeni yasalar çıkaralım.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)
        "Aynı düzen devam etsin.":
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5    
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog198:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Canım biraz para istiyor istersen meclisindekilere kısa süreli bir büyü yapıp  Meclistekilerin kafasını karıştırabilirim."
    $ daily_visitors += 1
    menu:
        "Tamam sana paranı vereceğim":
            $ Religion -= 2
            $ Economy -= 2
            $ Politics += 3
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Büyü zırvalıklarına inanmıyorum":
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog199:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Eğer bana biraz ödeme yaparsan sana büyü yaparım ve herşeyi önceden fark edersin."
    $ daily_visitors += 1
    menu:
        "Tamam hemen para veriyorum":
            $ Religion -= 2
            $ Economy -= 2
            Büyücü "(hiç birşey olmuyor)"
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Böyle bir şeyin olması mümkün değil sana inanmıyorum":
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog200:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Majesteleri, Diyanet'in bazı mensupları benim karanlık sanatlarla uğraştığımı iddia ediyor ve beni yakarak cezalandırmak istiyor. Oysa ki ben sadece bitkilerden ilaçlar yapıyor ve yıldızları okuyorum. Lütfen, bilgeliğinizle benim kaderimi belirleyin."
    $ daily_visitors += 1
    menu:
        "Para cezasına çevirdim":
            $ Economy += 1
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Onlar haksız, bunu konuşacağım":
            $ Religion -= 2
            $ check_bars()
            $ chr_chng("büyücü","+",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog201:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Efendim, son zamanlarda krallıkta kıtlık, salgın ve huzursuzluk arttı. Bunların doğal sebeplerle mi, yoksa bir lanet yüzünden mi olduğunu belirlemem için bana izin verin. Eğer karanlık bir büyü varsa, onu bozmam için sizden destek istiyorum."
    $ daily_visitors += 1
    menu:
        "Tamam destek olacağım":
            $ Economy -= 3
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "İnanmıyorum":
            $ Religion += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog202:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Kralım, kuzey ormanlarında karanlık bir varlık köylüleri korkutuyor. Büyüyle onu uzaklaştırabilirim, ancak bunun için nadir iksir malzemelerine ihtiyacım var."
    $ daily_visitors += 1
    menu:
        "Gerekli altını ver, büyüyü hazırlayayım.":
            $ Economy -= 2
            $ People += 1
            $ Religion += 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Köylüler kendi başlarının çaresine baksın.":
            $ People -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog203:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Majesteleri, kutsal tapınakta bir kehanet keşfedildi: Taç giyenin gücü, halkın duasıyla beslenir. Ayin düzenlememi ister misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, görkemli bir ayin yapılsın!":
            $ Religion += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Şimdi zamanı değil, hazinemiz boş.":
            $ Religion -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return
label dialog204:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Büyü kitaplarımızda yasaklı bir büyü var; düşman ordusunu bir gecede çürütebilir... Ancak ruhlar bize darılabilir."
    $ daily_visitors += 1
    menu:
        "Kullan, ne pahasına olursa olsun!":
            $ Military += 3
            $ Religion -= 2
            $ Health -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Yasaklı büyüye dokunmayın, başka çözüm bulalım.":
            $ Politics += 1
            $ Religion += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog205:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Kralım, sarayınızın duvarlarına koruma büyüleri işleyebilirim, ancak bu işlem aylar sürer ve büyücülerin tüm enerjisini alır."
    $ daily_visitors += 1
    menu:
        "Hemen başlayın, güvenlik önemli.":
            $ Military += 2
            $ Health -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Şimdilik askerlerin nöbet tutması yeterli.":
            $ Economy += 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog206:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Majesteleri, halk arasında veba yayılıyor. İlaç yapabilirim, ama bunun için kraliyet şifalı otlarını kullanmamız gerekecek."
    $ daily_visitors += 1
    menu:
        "Tüm otları kullan, halk kurtulsun!":
            $ Health += 3
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Sadece ağır hastalara yetecek kadar ver.":
            $ Health += 1
            $ People -= 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog207:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Kralım, düşman krallık büyücüleri sınırlarımızda tuhaf işaretler bırakıyor. Karşı büyü yapmamı ister misiniz?"
    $ daily_visitors += 1
    menu:
        "Hemen karşılık verin!":
            $ Military += 1
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Önce casuslarımızla durumu araştıralım.":
            $ Politics += 2
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog208:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Majesteleri, kraliyet kütüphanesindeki büyü kitapları çalınıyor. Büyülü tuzaklar kuralım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, hırsızlar dersini alsın!":
            $ Religion -= 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Hayır, kitapları başka yere taşıyalım.":
            $ Economy -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog209:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Kralım, bir grup köylü büyücülüğün şeytani olduğunu iddia edip büyücüleri linç etmek istiyor. Müdahale edelim mi?"
    $ daily_visitors += 1
    menu:
        "Büyücüleri koru, asılsız iddialara izin verme!":
            $ People -= 2
            $ Religion += 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Halkın öfkesini yatıştırmak için büyücüleri geçici sürgün edelim.":
            $ People += 1
            $ Health -= 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog210:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Majesteleri, düşmanın büyücüsü size bir barış elçisi göndermek istiyor. Ancak bu bir tuzak olabilir."
    $ daily_visitors += 1
    menu:
        "Elçiyi kabul et, barış şansını değerlendir.":
            $ Politics += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Reddet, düşmana güven olmaz.":
            $ Military += 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog211:
    show Büyücü at buyucu_poz       
    $ visitors_today = renpy.random.randint(1, 4)
    Büyücü "Kralım, bir meteor düştü ve içinden tuhaf bir taş çıktı. Büyü enerjisiyle dolu! Ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Büyücülere ver, güçlü silahlar yapsınlar!":
            $ Military += 2
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("büyücü","+",1)
        "Tapınağa koyalım, kutsal bir emanet olsun.":
            $ Religion += 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("büyücü","-",1)
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog212:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı " Yeni bir iksir geliştirdim, hastalıklara karşı çok etkili ama içeriği biraz… alışılmadık."
    $ daily_visitors += 1
    menu:
        "Deneyin, işe yarıyorsa sorun yok.":
            $ Health += 2
            $ Religion -= 2
            $ check_bars()
            $ chr_chng("otacı","+",1)
            Otacı "Majesteleri, sağduyunuz her derde deva!"
        "Hayır, halk arasında huzursuzluk çıkarır.":
            $ Religion += 1
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog213:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Bazı şifalı karışımlar için nadir ve zehirli yaratıkların parçalarına ihtiyacım var."
    $ daily_visitors += 1
    menu:
        "Gerekirse sağlayın, iyileşmek için her yol mübah.":
            $ Health += 2
            $ Military -= 2
            $ check_bars()
            $ chr_chng("otacı","+",1)            
        "Hayır, bu tür uygulamalar yasaklanmalı.":
            $ Religion += 2
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog214:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Halk, kullandığım yöntemleri büyücülük sanıyor. Beni koruyacak mısınız?"
    $ daily_visitors += 1
    menu:
        "Seni destekliyorum, gerçek şifa önemlidir.":
            $ Health += 2
            $ Religion -= 2
            $ check_bars()
            $ chr_chng("otacı","+",1) 
            Otacı "Majesteleri, bilgelikle hükmediyorsunuz!"           
        "Halkın korkularını göz ardı edemem.":
            $ Religion += 2
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog215:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Doğal şifa sanatlarını öğreteceğim bir kurum kurmak istiyorum."
    $ daily_visitors += 1
    menu:
        "Harika fikir, halk sağlığı artar.":
            $ Health += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("otacı","+",1) 
            Otacı "Bu harika olacak!"           
        "Gereksiz masraf, başka önceliklerimiz var.":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog216:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Kraliyet ailesi için gençleştirici bir iksir hazırlayabilirim."
    $ daily_visitors += 1
    menu:
        "Bu deneyin ilgimi çekti.":
            $ Health += 2
            $ Economy -= 1
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("otacı","+",1)                    
        "Saçmalık, buna kaynak ayıramam.":
            $ Health -= 2
            $ Economy += 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog217:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Rüyalar yoluyla mesajlar aldım, bu bazı kararlarızı etkileyebilir."
    $ daily_visitors += 1
    menu:
        "Dinleyelim, bilgi her kaynaktan gelebilir.":
            $ Religion -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("otacı","+",1)                    
        "Mantıksız, rüyalarına göre hükmedemem.":
            $ Religion += 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog218:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Sarayın arkasına özel bir bitki bahçesi kurmak istiyorum."
    $ daily_visitors += 1
    menu:
        "Elbette, ilaç için gerekli.":
            $ Economy -= 1
            $ Health += 2
            $ check_bars()
            $ chr_chng("otacı","+",1)  
            Otacı "Her yaprak, bir umut taşıyacak!"                  
        "Hayır, şimdilik uygun değil.":
            $ Economy += 1
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog219:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Bazı din adamları beni kara büyü yapmakla suçluyor."
    $ daily_visitors += 1
    menu:
        "Seni koruyacağım, otacılık ta önemlidir.":
            $ Religion -= 2
            $ Health += 2
            $ check_bars()
            $ chr_chng("otacı","+",1)                  
        "Bu suçlamalar araştırılmalı.":
            $ Religion += 2
            $ Health -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog220:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Kıtlık zamanında halkın hayatta kalması için bazı yenilebilir otlar öneriyorum."
    $ daily_visitors += 1
    menu:
        "Uygulayalım, hayat kurtarır.":
            $ Economy -= 1
            $ People += 2
            $ check_bars()
            $ chr_chng("otacı","+",1)                    
        "İnsanlara yabani ot yedirmem.":
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog221:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Efsanelerde geçen eski bir büyü kitabına ulaştım. Denememe izin verir misiniz?"
    $ daily_visitors += 1
    menu:
        "Elbette, büyük bir fırsat olabilir. ":
            $ Religion -= 2
            $ Politics += 2
            $ check_bars()
            $ chr_chng("otacı","+",1)                            
        "Hayır, bu çok tehlikeli.":
            $ Religion += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog222:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Saraydaki bazı kişilerin size zehirle suikast planladığını düşünüyorum."
    $ daily_visitors += 1
    menu:
        "Araştır, eğer doğruysa hayat kurtarabilir.":
            $ Politics -= 1
            $ Military += 2
            $ check_bars()
            $ chr_chng("otacı","+",1)  
            Otacı "Gerçekler görünmeyen zehirden bile daha keskindir!"                  
        "Elinde kanıt olmadan kimseyi suçlayamazsın.":
            $ Politics += 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog223:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Halk için küçük tılsımlar hazırlayabilirim, onlara umut olur."
    $ daily_visitors += 1
    menu:
        "Güzel fikir, deneyelim.":
            $ Economy -= 1
            $ People += 2
            $ Religion -= 2
            $ check_bars()
            $ chr_chng("otacı","+",1)  
            Otacı "Bu küçük taşlar, büyük umutlar taşıyacak!"                  
        "Saçma şeylerle vakit kaybetmeyelim.":
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog224:
    show Otacı at otaci_poz     
    $ visitors_today = renpy.random.randint(1, 4)
    Otacı "Sarayı kötü enerjilerden arındırmak için bir ritüel yapmam gerek."
    $ daily_visitors += 1
    menu:
        "Peki, düzenleyin.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("otacı","+",1)  
            Otacı "Temiz hava, temiz kader getirir majesteleri!"                 
        "Bu saçmalıklara izin veremem.":
            $ Religion += 1
            $ check_bars()
            $ chr_chng("otacı","-",1)
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog225:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Başkentimize yeni bir kütüphane açmak istiyorum destek olurmusunuz?"
    $ daily_visitors += 1
    menu:
        "Ekonomimiz bunu kaldırmaz ":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Evet, halkın bilgiye ihtiyacı var":
            $ Politics += 1
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog226:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Büyük Kralım, halkımıza daha iyi eğitim ve kültür sunabilmek adına kütüphanemize yeni kitaplar ve kaynaklar eklememiz gerekiyor. Bu, halkımızın bilgiyi daha geniş bir yelpazede edinmesini sağlayacak ve ülkenin eğitim seviyesini artıracaktır."
    $ daily_visitors += 1
    menu:
        "Yeni kitaplar eklensin!":
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Elimizdekiler yeterli, tutumlu olalım.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog227:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Sayın Kralım, kütüphanenin rafları aşırı eskidi, kitap koyduğumuz gibi raflar düşüyor yenileyebilir miyiz?"
    $ daily_visitors += 1
    menu:
        "Tabi raflar önemli. ":
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
            Kütüphaneci "Rafa koyduğumuz kitaplar artık düşmeyecek. "
        "Gereği yok sanırım.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog228:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Kralım, kütüphanemizin daha verimli çalışabilmesi ve daha fazla insanın erişebilmesi için binamızın genişletilmesi gerekmektedir. "
    $ daily_visitors += 1
    menu:
        "İnşaat başlasın!":
            $ People += 1
            $ Economy -= 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Gerek yok.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog229:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Sayın kralım kütüphaneye gelip insanları rahatsız eden bir grup saygısız insan var yardım edebilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Tamam askerlerim halledecek.":
            $ People += 1
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Üzgünüm askerlerimi bu iş için yoramam.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog230:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Sayın kralım en yeni çıkan kitaplar uzun zamandır kütüphanemize gelmedi bunun için biraz bütçe ayırır mısınız?"
    $ daily_visitors += 1
    menu:
        "Tabi kitaplar bizim için herşeydir.":
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Elimizdekiler ile idare edelim.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog231:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Büyük Kralım, kütüphanemizdeki değerli kitapları ve el yazmalarını koruyabilmek için güvenlik önlemlerini artırmamız gerekiyor. Bunlar halkımızın kültür mirasıdır."
    $ daily_visitors += 1
    menu:
        "Bir grup yönlendireceğim.":
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
            Kütüphaneci "Bu çok değerli Efendim."
        "Hayır.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog232:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Kralım, gençlerin okuma alışkanlığı kazanabilmesi için okuma programları düzenlemeliyiz. Bu, halkımızın kültür seviyesini artıracaktır."
    $ daily_visitors += 1
    menu:
        "Onaylıyorum!":
            $ People += 2
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Olmaz.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog233:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Efendim , halkımıza dünya literatürünü sunabilmek adına yabancı dillerde kitaplar temin etmemiz gerekir. Bu, uluslararası alandaki gelişmeleri takip etmemizi sağlayacaktır."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum.":
            $ People += 1
            $ Religion += 1
            $ Economy -= 2
            $ Politics += 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
            Kütüphaneci "Çok yerinde bir karar Efendim."
        "Reddediyorum.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog234:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Kralım, halkımıza kitapları daha iyi tanıtabilmek için bir eğitimci atanmasını rica ediyorum. Bu kişi, halkı kitaplar konusunda bilinçlendirecek ve okuma oranlarını artıracaktır"
    $ daily_visitors += 1
    menu:
        "Peki, atayalım.":
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Yeterli eğitimcimiz var.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog235:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Kralım, halktan kitap bağışları almak için bir kampanya başlatalım. Bu, hem halkın kitaplara olan ilgisini artırır hem de kütüphanemize yeni kaynaklar kazandırır."
    $ daily_visitors += 1
    menu:
        "Olur yapalım.":
            $ People += 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Gerek yok":
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog236:
    show Kütüphaneci at kutuphaneci_poz     
    Kütüphaneci "Kralım, halkımızın ruhsal gelişimini desteklemek için kütüphanemizde ruhsal eğitim programları düzenlememiz gerekebilir."
    $ daily_visitors += 1
    menu:
        "Düzenleyelim.":
            $ People += 1
            $ Religion += 1
            $ check_bars()
            $ chr_chng("ktpnc","+",1)
        "Gerek yok":
            $ check_bars()
            $ chr_chng("ktpnc","-",1)
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog237:
    show Yerel_Bakan at yerel_bakan_poz        
    Yerel_Bakan "Kralım ekonomimizi güçlendirmek için askerlerimizin kullanmadıkları silahlarını satalım mı?"
    $ daily_visitors += 1
    menu:
        "Satalım! hazineye para girer.":
            $ Economy += 2
            $ Military -= 1
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("yrl_bkn","+",1)

        "Muhafız Başından habersiz yapmamız doğru olmaz.":
            $ Military += 1
            $ check_bars()
            $ chr_chng("yrl_bkn","-",1)
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog238:
    show Demirci at demirci_poz       
    Demirci "Kralım kalenin duvarlarında çatlaklar olduğunu fark ettik, bu çatlakları tamir etmemizi ister misiniz?"
    $ daily_visitors += 1
    menu:
        "Hemen tamir edin, herhangi bir düşmanın çatlakları kullanarak içeri girmesini istemiyorum.":
            $ People += 1
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ chr_chng("demirci","+",1)
        "Boşa masraf yapmaya gerek yok.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("demirci","-",1)
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog239:
    show Ozan at ozan_poz
    Ozan "İlmin ve hikmetin bekçisi padişahım, kütüphanemizdeki nadide eserler nemin pençesinde. Onları koruyacak yeni bir çatı..."
    $ daily_visitors += 1
    menu:
        "Hemen en marifetli mimarlar görevlendirilsin!":
            $ People += 1
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Bu masraf, şu an lüks sayılır. Mürekkep ve ciltler biraz daha sabretsin.":
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog240:
    show Ozan at ozan_poz
    Ozan "Ulu Hakanım, tarlalar bereketsiz, çiftçilerimizin yüzü gülmez oldu. Ambar kapıları bir nebze aralansa... "
    $ daily_visitors += 1
    menu:
        "Ambarlarımızı onlar için sonuna kadar açın!":
            $ People += 1
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Duâ etsinler.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog241:
    show Ozan at ozan_poz
    Ozan "Yüce Sultanım, sarayın arslanları nöbetten ayakta uyur oldu. Yorgun bedenlere bir soluk..."
    $ daily_visitors += 1
    menu:
        "Nöbetler hafifletilsin, dinlenme sıraları yapılsın!":
            $ Military -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Nöbetçinin uyuduğu nerde görülmüş.":
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog242:
    show Ozan at ozan_poz
    Ozan "Yeryüzünün güneşi padişahım, hapishanelerdeki bazı mahkûmlar masum. Bir af rüzgârı esse de..."
    $ daily_visitors += 1
    menu:
        "Hemen araştırılsın, masumlar serbest bırakılsın!":
            $ Politics -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "O kapılar bir kere kapanınca bir daha açılmaz.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog243:
    show Ozan at ozan_poz
    Ozan "İhtişamlı Hükümdarım, çarşıdaki esnaf ağır vergilerden dermanını yitirmiş. Biraz merhamet..."
    $ daily_visitors += 1
    menu:
        "Vergiler bu yıl için yarıya indirilsin!":
            $ Economy -= 2
            $ People += 2
            $ check_bars()
            $ chr_chng("ozan","+",1)
            Ozan "Siz efendim, tacın tek sahibi..."
        "O kapılar bir kere kapanınca bir daha açılmaz.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog244:
    show Ozan at ozan_poz
    Ozan "Yüce Efendim, halk sokağa çıkamaz oldu. Gece olunca eşkıya türer. Sokaklara daha çok fener ve muhafız..."
    $ daily_visitors += 1
    menu:
        "Hemen sokaklar aydınlatılsın, devriyeler iki katına çıkarılsın!":
            $ Economy -= 1
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Eşkıya, eşkıyalığını her yerde yapar. Her sokağa asker mi dikelim?":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog245:
    show Ozan at ozan_poz
    Ozan "Merhamet Timsali Hünkârım, kuraklık su kaynaklarını kuruttu. Yeni kuyular ve sarnıçlar..."
    $ daily_visitors += 1
    menu:
        "İşçiler seferber edilsin, su yolları yapılsın!":
            $ Economy -= 1
            $ People += 2
            $ check_bars()
            $ chr_chng("ozan","+",1)
        "Büyük bir masraf!":
            $ People -= 1
            $ check_bars()
            $ chr_chng("ozan","-",1)
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog246:
    show Şifacı at sifaci_poz
    Şifacı "Sayın kralım üretimini yaptığımız şifalı otlar kuraklık nedeniyle bitmek üzere, Altrum krallığından bu otları ucuza temin edebiliriz yardım edebilir misiniz?"
    $ daily_visitors += 1
    menu: 
        "İnsanlarımın sağlığı her şeyden değerli.":
            $ Economy -= 1
            $ Health += 1
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)

        "Şimdilik elindekiyle yetinmeni istiyeceğim":
            $ People -= 1
            $ Health -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog247:
    show Şifacı at sifaci_poz
    Şifacı "Sayın kralım tüm askerlerinizi etkileyen bir hastalık var, bu hastalığın tedavisini bulmam için bana imkan sağlar mısınız?"
    $ daily_visitors += 1
    menu: 
        "Ordumu etkileyen hastalık neymiş öğren bakalım":
            $ Economy -= 1
            $ Health += 1
            $ Military += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Yardım etmeyeceğim.":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog248:
    show Şifacı at sifaci_poz
    Şifacı "Kralım, halkımız şifacılara karşı saldırgan bir tutum sergiliyor, bize yardım etmenizi istiyoruz."
    $ daily_visitors += 1
    menu: 
        "Şifacılarımız olmazsa halkımız da olmaz onları durdurucaz.":
            $ Health += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Yardım edemem.":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog249:
    show Şifacı at sifaci_poz
    Şifacı "Kralım yeni bir ilaç keşfettik bunu diğer krallıklara iyi fiyatlara satabiliriz, satalım mı?"
    $ daily_visitors += 1
    menu: 
        "Olur ekonomimize yardımı dokunacaktır.":
            $ Health -= 1
            $ Economy += 2
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Olmaz halkımızın daha fazla ihtiyacı var.":
            $ Health += 1
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog250:
    show Şifacı at sifaci_poz
    Şifacı "Kralım yeni şifaccılar yetiştirmek için sizden izin ve destek istiyorum."
    $ daily_visitors += 1
    menu: 
        "Tamam gerekeni yapalım.":
            $ Health += 1
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Yeterince şifacımız olduğundan eminim":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog251:
    show Şifacı at sifaci_poz
    Şifacı "Efendim yıllardır sizin hizmetinizdeyim biraz dinlenmek istiyorum."
    $ daily_visitors += 1
    menu: 
        "Tüm bu işlere ara vermek iyi gelebilir.":
            $ Health -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Üzgünüm ama biraz daha çalışman gerek.":
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog252:
    show Şifacı at sifaci_poz
    Şifacı "Efendim krallığın en büyük şifahenisinde yangın çıktı çok büyük zarar ettik şifahaneyi eski haline getirmek için sizden yardım istiyoruz."
    $ daily_visitors += 1
    menu: 
        "Hemen şifahanenin nin yeniden inşaatına başlansın":
            $ Economy -= 2
            $ People += 1
            Şifacı "Ucuz atlattık efendim."
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Şuan böyle bir yükü kaldıracak kadar iyi bir ekonomimiz yok":
            $ Health -= 3
            $ People -= 2
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog253:
    show Şifacı at sifaci_poz
    Şifacı "Sayın kralım halkın büyük çoğunluğu kıtlık getiren böcekler yüzünden hayatını kaybediyor, bu böceklerin yokedilmesi için bazı ekipmanlara ihtiyaç var ekipmanları karşılar mısınız?"
    $ daily_visitors += 1
    menu: 
        "Tabii halkımın hayatı çok değerli.":
            $ Economy -= 2
            $ People += 2
            $ Health += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Bunu karşılayamam bütün yiyecekleri yakın ":
            $ Health += 1
            $ People -= 3
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog254:
    show Şifacı at sifaci_poz
    Şifacı "Değerli kralım soylular kendilerine daha fazla ilaç satılmasını istiyorlar ne yapalım?"
    $ daily_visitors += 1
    menu: 
        "İlaçları insanların hastalıklarına uygun şekilde dağıtın.":
            $ People += 1
            $ Health += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Tamam soylulara fazladan ilaç satın.":
            $ Health -= 1
            $ Economy += 2
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog255:
    show Şifacı at sifaci_poz
    Şifacı "Efendim askerler köylülerle aynı şifahaneye gitmeyi reddediyor askeri sağlık çadırı yapmaya ne dersiniz?"
    $ daily_visitors += 1
    menu: 
        "Tamam inşaata başlansın.":
            $ Military += 2
            $ Health += 1
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Elimizdeki imkanları idareli kullanalım.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog256:
    show Şifacı at sifaci_poz
    Şifacı "Değerli kralım ülkemizde çıkan ölümcül salgın çok şiddetlendi durdurmak için ilaç tedariğine ihtiyacımız var."
    $ daily_visitors += 1
    menu: 
        "İlaçları tedarik etmesi için bir tüccarı yolluyorum.":
            $ Health += 2
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "İlaçları kendimiz üretmeliyiz.":
            $ Politics += 2
            $ Health -= 2
            $ People += 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return


label dialog257:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Efendim soylu ve tüccar arasında büyük bir anlaşmazlık olduğunu işittim, size haber vermek istedim."
    $ daily_visitors += 1
    menu:
        "Teşekkür ederim bununla ilgileneceğim.":
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Senden sadece işini yapmanı bekliyorum dedikodu değil!":
            $ People -= 1
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog258:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Değerli kralım sarayın etrafını temizlemek için yeterince temizlikçiniz yok daha fazla temizlikçi işe alabilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Tamam yeni temizlikçiler işe alıncak":
            $ Economy -= 1
            $ Health += 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Sen ne işe yarıyorsun peki?":
            Şifacı "Affedersiniz efendim çok haklısınız"
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog259:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Kralım çok yakın bir dostumun kızının acil işe ihtiyacı var sarayda temizlikçilik yapabilir onu işe alabilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Az bir maaşla işe başlayabilir. ":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Sarayda daha fazla hizmetliye ihtiyaç yok.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog260:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Kralım Baş İmam'ın sizin ülkeyi iyi yönetemediğinizi söylediğini duydum."
    $ daily_visitors += 1
    menu:
        "Onunla ilgileneceğim teşekkürler. ":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Böyle bir şey dediğine inanmıyorum":
            $ Religion += 1
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog261:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Efendim Muhafız başı'nın biz hizmetlilere bağırması hoşumuza gitmiyor buna bir çözüm bulabilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Muhafız başı bundan sonra sizlere bağırmayacak. ":
            $ Military -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Bunda bir sorun göremedim.":
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog262:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    Hizmetçi_Başı "Kralım büyücünüzün kara büyü yaptığını öğrendim size haber vermek istedim."
    $ daily_visitors += 1
    menu:
        "Bi sorun göremedim ":
            $ check_bars()
        "Dedikodu yapmayı kes.":
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog263:
    show Komutan at komutan_poz        
    Komutan "Majesteleri, kuzey sınırında hareketlilik var. Henüz saldırı yok ama askerlerim huzursuz. Önlem almak ister misiniz?"
    $ daily_visitors += 1
    menu:
        "Hazırlık yap":
            $ Military += 1
            $ Politics += 1
            $ Economy -= 1
            $ check_bars()
        "Bekleyelim bakalım.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog264:
    show Komutan at komutan_poz        
    Komutan "Bazı birliklerde disiplin zayıfladı. Sert cezalar düzeni geri getirebilir… ama hoş karşılanmaz."
    $ daily_visitors += 1
    menu:
        "Cezaları arttıralım ve uygulayalım":
            $ Military += 2
            $ People -= 1
            $ check_bars()
        "Uyarılara devam edelim.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog265:
    show Hizmetçi_Başı at hizmetci_basi_poz    
    Hizmetçi_Başı "Kralım Haznedarın hazineden altın kaçırdığı hakkında dedikodular duydum. Bu konuda birşeyler yapmanızı öneririm."
    $ daily_visitors += 1
    menu:
        "Bu konu hakkında haznedarla görüşüceğim":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("hzmt_baş","+",1)
        "Derhal işin başına dön!":
            $ check_bars()
            $ chr_chng("hzmt_baş","-",1)
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog266:
    show Şifacı at sifaci_poz
    Şifacı "Kralım ordumuzda yaralıları iyileştirmek için kullandığımız bitkinin tamamı zararlı böcekler tarafından yokedilmek üzere yardım edebilir misiniz?"
    $ daily_visitors += 1
    menu: 
        "Ne gerekiyorsa yap.":
            $ Health += 2
            $ Economy -= 2
            $ Military += 1
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Buna ayırabilecek ödeneğimiz maalesef yok.":
            $ Health -= 1
            $ Military -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog267:
    show Şifacı at sifaci_poz
    Şifacı "Efendim Zemorvia dan sipariş ettiğimiz tıbbi ekipmanlar elimize ulaşmadı ne yapalım?"
    $ daily_visitors += 1
    menu: 
        "Yeni aletler için ödenek hazırlansın.":
            $ Health += 2
            $ Economy -= 2
            $ check_bars()
            $ chr_chng("şifacı","+",1)
        "Siparişler gelene kadar bekleyelim.":
            $ Health -= 1
            $ check_bars()
            $ chr_chng("şifacı","-",1)
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog268:
    show Baş_İmam at bas_imam_poz
    Baş_İmam "Kütüphanelerdeki dini kitapların sayısını arttırmalıyız."
    $ daily_visitors += 1
    menu:
        "Tabiki yapalım.":
            $ Economy -= 1 
            $ Religion += 1
            $ check_bars()
            $ chr_chng("baş_imam","+",1)

        "Şuanlık elimizdekiler yeterli.":
            $ Religion -= 1
            $ check_bars()
            $ chr_chng("baş_imam","-",1)
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog269:
    show Komutan at komutan_poz        
    Komutan "Sayın kralım ordumuzda asker sayımız yetersiz halktan gönüllü asker toplayalım."
    $ daily_visitors += 1
    menu:
        "Alım yapılsın.":
            $ Military += 2
            $ People -= 1
            $ Economy -= 1
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Askerlerimiz yeterli.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog270:
    show Komutan at komutan_poz        
    Komutan "Efendim Yonkur krallığından bir soylu bizden paralı asker satın almak istiyor."
    $ daily_visitors += 1
    menu:
        "Verelim, güzel para.":
            $ Military -= 3
            $ People -= 1
            $ Economy += 3
            Komutan "Askerlerimiz satıldı, efendim umarım buna değer."
            $ check_bars()
        "Kendi askerlerimizi satmak mantıklı değil.":
            $ check_bars()
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog271:
    show Komutan at komutan_poz        
    Komutan "Kralım duvarlarımızdaki okçu sayılarını arttırmamız gerekli surların dışındaki tehdit artıyor."
    $ daily_visitors += 1
    menu:
        "Tabiki, sarayımızın surları önemli.":
            $ Military += 2
            $ People += 1
            $ Economy -= 2
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Burçlardaki okçular yeterli.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog272:
    show Komutan at komutan_poz        
    Komutan "Efendim güney sınırlarındaki gözcülerimiz için gözetleme kulesi inşa etmeyi öneriyorum."
    $ daily_visitors += 1
    menu:
        "Mantıklı, edelim.":
            $ Military += 1
            $ Economy -= 1
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Gerek yok.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog273:
    show Komutan at komutan_poz        
    Komutan "Kralım kışlalarımız oldukça yetersiz, yeni ve daha büyüklerini yaptırmamız gerekli."
    $ daily_visitors += 1
    menu:
        "Yeni kışlalar için hazineden para harcayalım.":
            $ Military += 1
            $ People += 1
            $ Economy -= 1
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Şuanlık böyle bir ihtiyaç yok":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog274:
    show Komutan at komutan_poz        
    Komutan "Donovia'lı başıbozuklar sınır köylerimizi talan etti!!"
    $ daily_visitors += 1
    menu:
        "Karşı saldırı için hazırlanalım.":
            $ Military -= 2
            $ People -= 1
            $ Economy -= 1
            $ Politics += 3
            Komutan "Bunun sonuçları ağır olabilir."
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Bu sorunu masada çözelim ve tazminat isteyelim.":
            $ Politics -= 3
            $ Economy += 2
            Komutan "Siyasetinizle bu sorunu çözmeniz farklı soruçlar doğurabilir."
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog275:
    show Komutan at komutan_poz        
    Komutan "Majesteleri, sınırlardaki öncü birliklerimiz uzun süredir Narga Krallığının sınırlarını kontrol ediyor. Biraz dinlenmek onlarında hakkı."
    $ daily_visitors += 1
    menu:
        "Halısın bir süre ara verebiliriz.":
            $ Military += 1
            $ Politics -= 1
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Güvenliğimiz için devam etmeleri şart.":
            $ Military += 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog276:
    show Komutan at komutan_poz        
    Komutan "Keşif birliklerinin sayısı az ordudan bir kaç askeri o birliklere takviye edelim."
    $ daily_visitors += 1
    menu:
        "Düzenleme yapılsın.":
            $ Military -= 1
            $ Politics += 1
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Garnizonu dağıtmak çokmantıklı değil.":
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog277:
    show Komutan at komutan_poz        
    Komutan "Ordunun kullandığı silahlar eskiyor Efendim. Demirciler yeni silahlar yapmalı."
    $ daily_visitors += 1
    menu:
        "Gerekli zinleri veriyorum. Üretim başlasın.":
            $ Military += 2
            $ Economy -= 2
            $ chr_chng("kmtn","+",1)
            $ check_bars()
        "Şimdilik idare edin.":
            $ Military -= 1
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog278:
    show Komutan at komutan_poz        
    Komutan "Bazı soylular kendi özel muhafızlarını topluyor. Bu, ordunun otoritesini zayıflatıyor."
    $ daily_visitors += 1
    menu:
        "Bu işe derhal müdahale et, tek güç Kraliyet Ordu olsun.":
            $ Military += 2
            $ Politics -= 3
            $ chr_chng("kmtn","+",1)
            Komutan "Soylulara ağır bi darbe vuracağız."
            $ check_bars()
        "Soylularla çatışma istemiyorum, şimdilik dokunma.":
            $ check_bars()
            $ chr_chng("kmtn","-",1)
    hide image Komutan
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog279:
    show Elçi at elci_poz   
    Elçi "Kralım, Zemorvia dan elçi geldi. Ticaret yollarının güvenliği için bizden sınır geçişlerinde ayrıcalık talep ediyorlar."
    $ daily_visitors += 1
    menu:
        "Ayrıcalıklar vereceğim. Zemorvia gibi bir ülke ile ilişkimizin iyi olmasını isterim.":
            $ Economy -= 1
            $ Military -= 2
            $ Politics += 3
            Elçi "Zemorvia ile iyi ilişkiler geliştireceğinize eminim."
            $ check_bars()
        "Sınırlarmızda kimseye ayrıcalık yok.":
            $ Politics -= 1
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog280:
    show Elçi at elci_poz   
    Elçi "Kralım zemorvia dan ticaret kervanları geldi narga krallığına geçiş için izin istiyorlar."
    $ daily_visitors += 1
    menu:
        "İzin verelim.":
            $ Economy += 1
            $ check_bars()
        "Hayır bu çok riskli.":
            $ Politics -= 2
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog281:
    show Elçi at elci_poz   
    Elçi "Efendim Yargea Krallışından bir elçi geldi bizden ürettiğimiz tahıllardan istiyorlar. Halkları zor durumdaymış."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum.":
            $ Economy -= 2
            $ People -= 2
            $ Politics += 3
            Elçi "Bu sayede Yargea ile ilişkilerimiz daha iyiye gidicek."
            $ check_bars()
        "Reddediyorum.":
            $ Politics -= 1
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog282:
    show Elçi at elci_poz   
    Elçi "Kralım Narga krallığı bizden savaş aletleri almak istiyor."
    $ daily_visitors += 1
    menu:
        "Satalım paraya ihtiyacımız var.":
            $ Economy += 2
            $ Military -= 1
            $ Politics -= 2
            $ check_bars()
        "Hayır düşmanlarımıza silah vermeyeceğiz.":
            $ Politics += 1
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog283:
    show Elçi at elci_poz   
    Elçi "Efendim elçilerin daha güvenli gelip gidebilmesi için sizden ek koruma talep ediyorum."
    $ daily_visitors += 1
    menu:
        "Tabiki.":
            $ Military -= 1
            $ chr_chng("elçi","+",1)
            $ check_bars()
        "Gerek yok.":
            $ chr_chng("elçi","-",1)
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog284:
    show Elçi at elci_poz   
    Elçi "Saygıdeğer efendim Donovia dan bir gemi geldi bize balık satmak istiyorlar halkımızın buna ihtiyacı olabilir."
    $ daily_visitors += 1
    menu:
        "Haklısın alalım":
            $ Economy -= 1
            $ People += 2
            $ check_bars()
        "Gerekli değil.":

            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog285:
    show Elçi at elci_poz   
    Elçi "Kralım Yargea Krallığından bir grup asker zemorvia Krallığına gitmek istediklerini söyledi."
    $ daily_visitors += 1
    menu:
        "İzin verelim geçsinler.":
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
        "Çok güvensiz reddedelim.":
            $ Politics -= 1
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog286:
    show Elçi at elci_poz   
    Elçi "Efendim ihtarinli bir büyük tüccar pazarda size hakaret etti ne yapalım diplomatik bir sorun çıkarmı?"
    $ daily_visitors += 1
    menu:
        "Cezasını verin yollayın ülkeden.":
            $ Politics -= 1
            $ check_bars()
        "Sınır dışı edin.":
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog287:
    show Elçi at elci_poz   
    Elçi "Narga Krallığı ile imzaladığımız ateşkes anlaşması sona erdi."
    $ daily_visitors += 1
    menu:
        "Yeniden imzalayalım.":
            $ Economy -= 1
            $ Politics += 2
            $ check_bars()
        "Gerek yok sınırlara asker koyalım":
            $ Military -= 2
            $ Economy += 1
            $ check_bars()
    hide image Elçi
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog288:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım güney köylerindeki vergileri getirdim hazineye mi koyayım yoksa ordunun ihtiyaçlarınamı harcayayım?"
    $ daily_visitors += 1
    menu:
        "Hazineye koy.":
            $ Economy += 2
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Komutana teslim et.":
            $ Military += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog289:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım kentin surlarının tamiri için ayırdığınız bütçe arttı yeni yatırımlar için ayıralım mıyoksa hazineye geri mi koyalım?"
    $ daily_visitors += 1
    menu:
        "Hazineye geri koyalım.":
            $ Economy += 1
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Halkımıza yatırımlara devam edelim.":
            $ People += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog290:
    show Haznedar at Haznedar_poz      
    Haznedar "Efendim kütüphaneci bir tüccarın kendisine yüklü bir miktar parayı hibe ettiğini söyledi kütüphanenin ihtiyacı olmadığı için hazineye teslim etmemi söyledi."
    $ daily_visitors += 1
    menu:
        "Hazineye koy ozaman":
            $ Economy += 2
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Kütüphaneye hibe edilen parayı kütüphaneye harcayalım.":
            $ Politics += 1
            $ People += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog291:
    show Haznedar at Haznedar_poz      
    Haznedar "Efendim Baş imam camilerde toplanan paranın artanını getirip hazineye teslim etti ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 2
            $ Religion -= 1
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Cami için toplanan parayla yeni  camiler açalım.":
            $ Religion += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog292:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım, inşaatlardan artan bir miktar paramız var ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 1
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Çeşme yaptıralım.":
            $ People += 1
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog293:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım madenden çıkan silah yapımına elverişsiz bazı madenleri demirci bize teslim etti."
    $ daily_visitors += 1
    menu:
        "Satıp parasını hazineye koyalım.":
            $ Economy += 2
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Madenleri soylulara teslim edelim.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog294:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım ,toplanan vergileri getirdim."
    $ daily_visitors += 1
    menu:
        "Hazineye koy.":
            $ Economy += 2
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Komutana teslim et orduya yeni ekipmanlar alsın.":
            $ Military += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog295:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım, ismini vermek istemeyen biri yüklü bir miktar para teslim etti."
    $ daily_visitors += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 3
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Halka dağıtalım.":
            $ People += 3
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog296:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım ülkemizde yapılan ticaret vergilerini getirdim."
    $ daily_visitors += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 2
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Şifacıya teslim et yeni aletler alması gerekiyordu.":
            $ Health += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog297:
    show Haznedar at Haznedar_poz      
    Haznedar "Kralım, Komutan haber göndertmiş ordu için hazineden para istiyor"
    $ daily_visitors += 1
    menu:
        "Şuanlık gerek yok.":
            $ Military -= 1
            $ chr_chng("hznc","+",1)
            $ check_bars()
        "Orduya gerekli yatırımı yapalım.":
            $ Military += 2
            $ check_bars()
            $ chr_chng("hznc","-",1)
    hide image Haznedar
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog298:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman ""
    $ daily_visitors += 1
    menu:
        "":
            $ Economy += 2
            $ People -= 3
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog299:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Kralım meclis üyeleri daha fazla ayrıcalık istiyor."
    $ daily_visitors += 1
    menu:
        "Verelim":
            $ Politics += 1
            $ People -= 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Aynı kalsın":
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog300:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Efendim, halkın büyük bir kesmi çok fazla vergi aldığımızdan bahsediyor. Vergileri azaltalım mı ?"
    $ daily_visitors += 1
    menu:
        "Azaltalım halk rahatlasın.":
            $ Economy -= 2
            $ People += 2
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Vergiler aynı kalacak.":
            $ People -= 1
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog301:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Kralım ateşkes anlaşması devam eden ülkelerle görüşmelere sizin yerinize benim gitmem daha güvenli olur."
    $ daily_visitors += 1
    menu:
        "Haklısın":
            $ Politics += 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Onlara göz dağı vermek için benim gitmem gerek":
            $ Military += 1
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog302:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Efendim, ülkenin ana ticaret yolunda hırsızlıklar artmış oraya bir asker birliği gönderelim mi?"
    $ daily_visitors += 1
    menu:
        "Gönderelim.":
            $ Economy += 1
            $ Military -= 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Hayır gerek yok.":
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog303:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Efendim, Bazı saray çalışanlarının saray hazinesine girdiğini öğrendik onlara ne yapalım"
    $ daily_visitors += 1
    menu:
        "Hemen tutuklayın ve zindana atın.":
            $ People -= 1
            $ check_bars()
        "Onları sorgulayalım.":
            $ People += 1
            $ check_bars()
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog304:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Kralım, Eterna Krallığındaki ajanlarımız büyük bir hastalık çıktığını ve yakın zamanda buraya da hastalığın gelebiliceğinden bahsetti tedbir alalım mı?"
    $ daily_visitors += 1
    menu:
        "Alalım tabikide.":
            $ Economy -= 2
            $ Health += 2
            $ People += 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Gerek yok Eterna ile kara sınırımız yok.":
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog305:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Efendim, soylular mecliste kendilerine daha fazla hak talep ediyorlar."
    $ daily_visitors += 1
    menu:
        "Gereken hakları verelim.":
            $ Politics += 2
            $ People -= 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Şuanki meclis dengesine dokunmayalım.":
            $ People += 1
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog306:
    show Baş_Danışman at bas_danisman_poz     
    Baş_Danışman "Efendim meclis üyelerinin güvenliğini arttırmalıyız."
    $ daily_visitors += 1
    menu:
        "Haklısın.":
            $ Politics += 2
            $ Military -= 1
            $ chr_chng("baş_dnş","+",1)
            $ check_bars()
        "Meclisimiz zaten güvenli.":
            $ Politics -= 1
            $ check_bars()
            $ chr_chng("baş_dnş","-",1)
    hide image Baş_Danışman
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog307:
    show Tacir at tacir_poz     
    Tacir "Kralım, tanıdığım bir tacir grubu ülkemize insan gücü almak karşılığında yatırım yapmak istediğini söyledi."
    $ daily_visitors += 1
    menu:
        "Olur kabul edelim.":
            $ Economy += 2
            $ People -= 2
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Gerek yok.":
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog308:
    show Tacir at tacir_poz     
    Tacir "Efendim, çok zengin bir tüccar dostum ülkemizden toprak alıp toprak sahibi olmak istiyor."
    $ daily_visitors += 1
    menu:
        "Tamam olur.":
            $ Economy += 2
            $ People -= 1
            $ Politics -= 1
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Toprak satmak istemiyorum.":
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog309:
    show Tacir at tacir_poz     
    Tacir "Sayın kralım, ülkenin ticaret işlerinde daha fazla yetki istiyorum bunun ekonomimize yardımı dokunabilir."
    $ daily_visitors += 1
    menu:
        "Olur yetkilerini arttırdım":
            $ Economy += 1
            $ Politics -= 2
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Böyle bir şeye ihtiyacım yok.":
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog310:
    show Tacir at tacir_poz     
    Tacir "Sayın kralım, Bertrum dan gelen bir kaç hizmetçi var onları size almanız için öneririm."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum.":
            $ Economy -= 1
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Reddediyorum":
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog311:
    show Tacir at tacir_poz     
    Tacir "Değerli kralım ülkemizdeki tacirleri haydutlardan korumak için askeri destek istiyorum."
    $ daily_visitors += 1
    menu:
        "Tamam vereceğim.":
            $ Economy += 1
            $ Military -= 1
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Gerek yok.":
            $ Economy -= 1
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return

label dialog312:
    show Tacir at tacir_poz     
    Tacir "Kralım elime değerli bir vazo geçti almak istermisiniz."
    $ daily_visitors += 1
    menu:
        "Tabi":
            $ Economy -= 1
            $ chr_chng("tcr","+",1)
            $ check_bars()
        "Gereksiz harcama.":
            $ check_bars()
            $ chr_chng("tcr","-",1)
    hide image Tacir
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            show aa:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show bb:
                size (config.screen_width, config.screen_height)
            pause 0.5
            show cc:
                size (config.screen_width, config.screen_height) 
            pause 0.5
            show dd:
                size (config.screen_width, config.screen_height)  
            pause 0.5
            show ee:
                size (config.screen_width, config.screen_height)
            pause 0.5      
            $ daily_visitors = 0
            $ visitors_today = renpy.random.randint(1, 4)
            $ advance_date(1)
    $ main_story_count += 1
    scene startbcg
    jump random_dialog
    return
