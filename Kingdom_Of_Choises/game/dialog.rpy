
label dialog1:
    show Demirci at demirci_poz       
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım elimde kaliteli bir maden geçti bununla ne yapmalıyım?"
    $ daily_visitors += 1
    menu:
        "Tarım aletleri yapabiliriz.":
            $ People += 1
            $ Economy += 1
            Demirci "Halk memnun olacaktır."
            $ check_bars()
            $ demirci_relationship += 1
        "Madeni satabiliriz.":
            $ Economy += 2
            Demirci "Güzel kar ettik."
            $ check_bars()
            $ demirci_relationship -= 1
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog2:
    show Ozan at ozan_poz        
    $ visitors_today = renpy.random.randint(2, 4)
    Ozan "Kralım saray ahalisi çok mutsuz bir eğlence düzenleyelim"
    $ daily_visitors += 1
    menu:
        "Çok güzel olur, hadi yapalım.":
            $ People += 1
            $ Economy -= 2
            Ozan "Harika!"
            $ check_bars()
            $ ozan_relationship += 1
        "Ülkenin parasını çarçur edemeyiz.":
            Ozan "Ufff..."
            $ check_bars()
            $ ozan_relationship -= 1
    hide image Ozan
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1) 
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog3:
    show Muhafız_Başı at muhafiz_basi_poz    
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Ordumuzun gücünü artırmak için yeni askerler toplamalıyız"
    $ daily_visitors += 1
    menu:
        "Evet, ordumuzu güçlendirelim.":
            $ Military += 2
            $ Economy -=1
            $ People -=1
            Muhafız_Başı "Halk hoşnut olmayacak ama ordumuz güçlenecek." 
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Hayır, halkın tepkisini çekebiliriz.":
            $ People += 1
            Muhafız_Başı "Peki."
            $ check_bars()
            $ muhafızbaşı_relationship -= 1      
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1) 
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog4:
    show Asker at asker_poz      
    $ visitors_today = renpy.random.randint(2, 4)
    Asker "Saygı değer Kralım talimler çok fazla sayısını azaltmalısınız."
    $ daily_visitors += 1
    menu: 
        "Muhafız Başı ile konuşacağım":
            $ Military -=1
            Asker "Çok yaşayın efendimiz"
            $ check_bars()
            $ asker_relationship += 1
        "Gerek yok":
            $ check_bars()
            $ asker_relationship -= 1
    hide image Asker
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1) 
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog5:
    show Çiftçi at ciftci_poz    
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralım Köyümüzü fareler bastı lütfen yardım edin"
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
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog6:
    show Baş_İmam at bas_imam_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Baş_İmam "Ülkedeki camiler yetersiz halkımız dışarda kalıyor destek talep ediyorum"
    $ daily_visitors += 1
    menu:
        "Tamam vereceğim":
            $ Economy -= 2 
            $ Religion += 2
            $ check_bars()
            $ başimam_relationship += 1

        "Lüzumu yok":
            $ Religion -= 1
            $ check_bars()
            $ başimam_relationship -= 1
    hide image Baş_İmam
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog7:
    show Zengin_Tüccar at zengin_tuccar_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Zengin_Tüccar "Eğer vergilerde indirim yaparsanız kendi halkımdan gelen tacirleri  ülkenize yönlendiririm kazan kazan ne dersiniz"
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum":
            $ Economy += 1
            $ Politics += 2
            Zengin_Tüccar "Doğru karar verdiniz efendim"
            $ check_bars()
            $ zengintüccar_relationship += 1

        "Herkese nasıl davranılıyorsa sanada öyle davranılacak":
            $ check_bars()
            $ zengintüccar_relationship -= 1
    hide image Zengin_Tüccar
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog8:
    show Yerel_Bakan at yerel_bakan_poz        
    $ visitors_today = renpy.random.randint(2, 4)
    Yerel_Bakan "Kralım ülkenin bütçesinin büyük bir kısmı askeriye ye harcanıyor inşaatları arttıralım."
    $ daily_visitors += 1
    menu:
        "Ordunun bütçesine dokunamayız":
            $ check_bars()
            $ yerelbakan_relationship += 1

        "Olur ülkeyi kalkındıralım":
            $ Military -= 2
            $ Economy += 1
            $ People += 1
            $ check_bars()
            $ yerelbakan_relationship -= 1
    hide image Yerel_Bakan
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog9:
    show Soylu at soylu_poz      
    $ visitors_today = renpy.random.randint(2, 4)
    Soylu "Yeterli sayıda kölem yok yenilerini nerden bulabilirim"
    $ daily_visitors += 1
    menu:
        "Benim kölelerimin birazını satın alabilirsin":
            $ Economy += 2
            $ Politics -= 1
            Soylu "Teşekkürler"
            $ check_bars()
            $ soylu_relationship += 1

        "Bu benim sorunum değil":
            Soylu "Doğru, değil."
            $ check_bars()
            $ soylu_relationship -= 1
    hide image Soylu
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog10:
    show Kadı at kadi_poz        
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor."
    $ daily_visitors += 1
    menu:
        "Arazi Soylunun hakkı":
            $ Politics += 1 
            $ Economy -= 1
            $ check_bars()
            $ kadı_relationship += 1

        "Arazi Tacirin hakkı":
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog11:
    show Şifacı at sifaci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Şifacı "Tıp için bir araştırma yapmam gerekiyo bütçeyi nasıl oluşturayım"
    $ daily_visitors += 1
    menu: 
        "Ben vereceğim":
            $ Economy -= 2
            $ Health += 1
            Şifacı "Teşekkür ederim efendim"
            $ check_bars()
            $ şifacı_relationship += 1

        "Bu araştırma gereksiz":
            $ check_bars()
            $ şifacı_relationship -= 1
    hide image Şifacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog12:
    show Hizmetçi_Başı at hizmetci_basi_poz        
    $ visitors_today = renpy.random.randint(2, 4)
    Hizmetçi_Başı "Kralım, mutfağınızda kullanılan malzemeler bayat ve kalitesiz. Daha iyi ve taze malzemeler almak için bütçemizi artırmalıyız, yoksa hastalıklar baş gösterebilir."
    $ daily_visitors += 1
    menu:
        "Tamam, bütçeyi arttıracağım.Temizlik önemli.":
            $ Economy -= 1
            $ Health += 1
            $ check_bars()
            $ hizmetci_basi_relationship += 1

        "Yemeklerimiz yeterince iyi.Gereksiz şeyler sorma!!":
            $ Health -= 1
            $ check_bars()
            $ hizmetci_basi_relationship -= 1
    hide image Hizmetçi_Başı
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog13:
    show Büyücü at buyucu_poz        
    $ visitors_today = renpy.random.randint(2, 4)
    Büyücü "Efendim, son zamanlarda kıtlık arttı. Bunun doğal sebeplerle mi, yoksa bir lanet yüzünden mi olduğunu belirlemem için sizden destek istiyorum."
    $ daily_visitors += 1
    menu:
        "Tamam destek olucağım.":
            $ Economy -= 3
            $ check_bars()
            $ büyücü_relationship += 1

        "Sana inanmıyorum.":
            $ Religion += 1
            $ check_bars()
            $ büyücü_relationship -= 1
    hide image Büyücü
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog14:
    show Otacı at otaci_poz      
    $ visitors_today = renpy.random.randint(2, 4)
    Otacı "Yeni bir iksir geliştirdim, hastalıklara karşı çok etkili ama içeriği biraz… alışılmadık."
    $ daily_visitors += 1
    menu:
        "Deneyin, işe yarıyorsa sorun yok.":
            $ Religion -= 2
            $ Health += 2
            Otacı "Majesteleri, sağduyunuz her derde deva!"
            $ check_bars()
            $ otacı_relationship += 1

        "Hayır, halk arasında huzursuzluk çıkarır.":
            $ Religion += 1
            $ Health -= 1
            $ check_bars()
            $ otacı_relationship -= 1
    hide image Otacı
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog15:
    show Kütüphaneci at kutuphaneci_poz     
    $ visitors_today = renpy.random.randint(2, 4)
    Kütüphaneci "Halk kütüphanemiz depremde zarar görmüştü hala tamir edilmedi"
    $ daily_visitors += 1
    menu:
        "Şuan ki durumu iyi":
            $ People -= 1
            $ check_bars()
            $ kütüphaneci_relationship += 1

        "Onarım başlasın":
            $ Politics += 1
            $ People += 1
            $ Economy -= 2
            $ check_bars()
            $ kütüphaneci_relationship -= 1
    hide image Kütüphaneci
    if daily_visitors >= visitors_today:
            $ managed_day += 1  
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return
label dialog16:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım malzemeler yetersiz sağlık için ayrılına bütçeden madenler için biraz kullanılmasını talep ediyorum"
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum":
            $ Health -= 1
            $ People += 1
            $ check_bars()
            $ demirci_relationship += 1
        "Reddediyorum":
            $ People -= 1
            $ check_bars()
            $ demirci_relationship -= 1
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
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
            $ demirci_relationship +=1
        "düzeni bozma":
            $ People -= 1
            $ check_bars ()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
            $ managed_day += 1
            $ daily_visitors = 0
            $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog18:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım elime değerli bir maden geçti bununla ne yapayım"
    $ daily_visitors += 1
    menu:
        "Sat":
            $ Economy += 2
            $ check_bars()
            $ demirci_relationship += 1
        "Silah yap":
            $ Military += 2
            $ check_bars()
            $ demirci_relationship -= 1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog19:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım imam camilerde süs için iyi çelik kullanmak istiyor ne yapalım"
    $ daily_visitors += 1
    menu:
        "Kullan":
            $ Economy -= 2
            $ Religion += 1
            $ check_bars()
            $ demirci_relationship += 1
        "Gerek yok":
            $ Religion -= 1
            $ check_bars()
            $ demirci_relationship -= 1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog20:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım daha çok demir ocağı yapmamız gerek tarım aletleri üretemiyoruz"
    $ daily_visitors += 1
    menu:
        "İnşaat başlasın":
            $ Economy -= 2
            $ People += 1
            Demirci "Çok doğru karar."
            $ check_bars()
            $ demirci_relationship += 1
        "Lüzum yok":
            $ People -= 1
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog21:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Köylülerden biri sinirlenip sabanı kırdı ne ceza verelim?"
    $ daily_visitors += 1
    menu:
        "Onu affedelim":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ demirci_relationship += 1
        "Para cezası verelim":
            $ People -= 1
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog22:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım ülkenizdeki askeri gücü arttırmak için bir fikrim var, bana gereken desteği sağlarsanız bunu yaparım"
    $ daily_visitors += 1
    menu:
        "Hazineden alabilirsin":
            $ Economy -= 3
            $ Military += 2
            Demirci "Bana güvenebilirsiniz."
            $ check_bars()
            $ demirci_relationship += 1
        "Askeri gücümüz yeterli":
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog23:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, soyluların evinde çok fazla değerli maden var. Bunları eritip tarım aleti yapmalıyız."
    $ daily_visitors += 1
    menu:
        "Haklısın, tüm izinleri veriyorum":
            $ Politics -= 2
            $ Economy += 2
            $ People += 1
            $ check_bars()
            $ demirci_relationship += 1
        "Soyluların şahsi mallarına dokunamayız":
            $ Politics += 1
            Demirci "Sanırım haklısınız."
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog24:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Elimde bazı değerli madenler var. Ne yapayım Kralım?"
    $ daily_visitors += 1
    menu:
        "Ameliyat aletleri yapalım":
            $ Health += 2
            $ check_bars()
            $ demirci_relationship += 1
        "Satalım":
            $ Economy += 2
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog25:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, sizdeki iyi bir zırh takımını Bertrumlu bir tacir istiyormuş. Ne yapmak istersiniz?"
    $ daily_visitors += 1
    menu:
        "Tamam, satıyorum":
            $ Economy += 1
            $ Politics -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Benim küçük tacirlerle işim olmaz":
            $ check_bars()
            $ demirci_relationship -=1
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog26:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, halkın silahları eskidi ve düşman sınırlarda geziyor. Yeni silahlar yapmam için bana daha fazla demir ve kömür tahsis edin."
    $ daily_visitors += 1
    menu:
        "Kabul ediyorum, ordumuzun güçlenmesi önemli":
            $ Military += 2
            $ Economy -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Reddediyorum, şu an kaynaklarımız kısıtlı":
            $ Military -= 1
            $ People += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog27:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, tapınakların kutsal kılıçlarını yenilemek istiyorum. Din adamları bana altın ve gümüş verilmesini talep ediyor."
    $ daily_visitors += 1
    menu:
        "Kutsal işlere kaynak ayırmak elbette önemli":
            $ Religion += 2
            $ Economy -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Şu an devletin hazinesi dini işlere yetecek kadar dolu değil":
            $ Religion -= 1
            $ Politics += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog28:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, köylülerin sabanları kırık. Tarım verimi düşecek. Onlara yeni aletler yapmam için bana destek olun!"
    $ daily_visitors += 1
    menu:
        "Halkın refahı önemli, hemen kaynak ayır":
            $ People += 2
            $ Economy -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Önce askeri ihtiyaçlar bitmeli":
            $ People -= 1
            $ Military += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog29:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, sarayın korumaları için daha sağlam zırhlar yapabilirim, ancak bu iş için fazla çalışmam gerekecek. Bana ek ücret ödenmeli."
    $ daily_visitors += 1
    menu:
        "Sarayın güvenliği önceliğim, kabul":
            $ Politics += 1
            $ Economy -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Şimdilik mevcut zırhlar yeterli":
            $ Politics -= 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog30:
    show Demirci at demirci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Demirci "Kralım, vebadan kırılan kasabalar için tıbbi aletler yapmak istiyorum. Bana yardımcı olacak birkaç çırak verin."
    $ daily_visitors += 1
    menu:
        "Sağlık her şeyden önemli, hemen çırakları gönderin":
            $ Health += 2
            $ Economy -= 1
            $ check_bars()
            $ demirci_relationship += 1
        "Başka bölgelerde daha acil ihtiyaçlar var":
            $ Health -= 2
            $ Military += 1
            $ check_bars()
    hide image Demirci
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog31:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Kralım, sınırda görev yapan askerlerimizin erzakları tükenmek üzere. Yeni ikmal için emir verir misiniz?"
    $ daily_visitors += 1
    menu:
        "Derhal erzak gönderin":
            $ Economy -= 2
            $ Military += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şehirdeki stoklarımızı zorlamayalım":
            $ Military -= 1
            $ Economy += 1
            Muhafız_Başı "Aç bir asker, zayıf bir sınır demektir, majesteleri…"
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog32:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Son zamanlarda askerler arasında hoşnutsuzluk var. Daha iyi şartlar için şikayet ediyorlar."
    $ daily_visitors += 1
    menu:
        "Maaşlarını artırın":
            $ Economy -= 3
            $ Military += 2
            $ People += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Onlara sadakatlerini hatırlatın":
            $ Military -= 1
            $ Politics += 1
            Muhafız_Başı "Umarım bu kararınız, askerlerin sadakatini sarsmaz, majesteleri…"
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog33:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Sarayınızı koruyan muhafızların sayısını artırmayı öneriyorum. Güvenliğiniz her şeyden önemli."
    $ daily_visitors += 1
    menu:
        "Haklısınız, daha fazla muhafız alın":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şu an için yeterli olduklarını düşünüyorum":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog34:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Komşu topraklardan gelen çapulcular, sınır kasabalarımıza saldırıyor. Ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Ek asker gönderin, halkı koruyun!":
            $ Military -= 2
            $ People += 1
            $ Economy -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Önceliğimiz büyük şehirlerdir":
            $ People -= 2
            $ Economy += 1
            Muhafız_Başı "Sınırdaki halkımız kendini yalnız hissedecek, majesteleri…"
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog35:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Ordumuzun silahları eskiyor. Yeni kılıç ve zırhlar için yatırım yapmalıyız."
    $ daily_visitors += 1
    menu:
        "Demircilere emir verin, yeni silahlar yapılsın!":
            $ Economy -= 3
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Mevcut silahları onarıp kullanın":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog36:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Halk arasında huzursuzluk çıkaran bazı kişiler var. Onları gözaltına alalım mı?"
    $ daily_visitors += 1
    menu:
        "Evet, huzuru bozacak kimseye izin vermeyin!":
            $ People -= 2
            $ Politics += 1
            $ Military += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Önce onları dinleyelim":
            $ People += 2
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog37:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Askerlerimizi formda tutmak için büyük bir tatbikat düzenlemeyi öneriyorum."
    $ daily_visitors += 1
    menu:
        "Harika fikir, derhal düzenleyin!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şimdilik gereksiz bir masraf":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog38:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Bazı soylular, ordunun desteğini almaya çalışıyor. Bu bir darbe hazırlığı olabilir."
    $ daily_visitors += 1
    menu:
        "Şüpheli soyluları gözaltına alın!":
            $ Politics -= 1
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Onlarla bir toplantı yapalım":
            $ Politics += 1
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog39:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Bazı muhafızlar rüşvet almakla suçlanıyor. Araştırmamı emreder misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, suçlu olanları cezalandırın":
            $ People += 1
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Göz ardı edin, bunlar küçük meselelerdir":
            $ People -= 2
            Muhafız_Başı "Adaletin zayıflaması, krallığın çöküşüne sebep olabilir…"
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog40:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Yeni savaş stratejileri geliştirmek için daha fazla vakit ve kaynak ayırmalıyız."
    $ daily_visitors += 1
    menu:
        "Bu işe zaman ve para ayırın":
            $ Economy -= 3
            $ Military += 3
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şimdilik mevcut taktiklere güvenelim":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog41:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Şehirde suç oranı artıyor. Daha fazla devriye görevlendirelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın güvenliği her şeyden önemli!":
            $ Economy -= 2
            $ People += 1
            $ Military += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Halk kendi güvenliğini sağlamalı":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog42:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Sarayda bir suikast girişimi oldu. Soruşturma başlatılsın mı?"
    $ daily_visitors += 1
    menu:
        "Derhal başlatın, hainler bulunmalı!":
            $ Politics += 1
            $ Military += 1
            $ Economy -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Bu bir söylenti olabilir, önemsemeyin":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog43:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Kale duvarlarımızın bazı bölümleri eskiyor. Onları güçlendirelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, krallığımızı koruyalım":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şimdilik bir tehdit yok, erteleyin":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog44:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Düşman casuslarının sarayımıza sızdığına dair bilgiler var."
    $ daily_visitors += 1
    menu:
        "Derhal casusları tespit edin ve tutuklayın!":
            $ Military += 2
            $ Politics -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Önce onların amaçlarını öğrenelim":
            $ Politics += 1
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog45:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim Narga Krallığı sınırlarımızı ihlal ediyor bu bir son vermemiz gerek."
    $ daily_visitors += 1
    menu:
        "Savaş açalım hadlerini aşmasınlar":
            $ Economy -= 1
            $ People -= 2
            $ Military -= 2
            $ Politics += 2
            Muhafız_Başı "Efendim, savaş ilan edildi."
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Barış imzalayalım, şartlarını kabul edelim":
            $ Economy -= 3
            $ Politics -= 2
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog46:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim askerler arasında bir husumet çıktı bu sorunu çözmeliyiz."
    $ daily_visitors += 1
    menu:
        "Bölükleri ayıralım, husumet dağılsın":
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Komutan sen değil misin, bastır onları":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog47:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim Kuzey bölgesinden bir grup haydut bir köyü basıp insanları rehin almış."
    $ daily_visitors += 1
    menu:
        "Ben haydutlarla pazarlık yapmam, orduyu üzerlerine sür":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Ne istiyorlarsa verip köylüleri kurtarın":
            $ Economy -= 2
            $ People += 1
            Muhafız_Başı "Efendim, köylüler kurtarıldı."
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog48:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim ordu için ekipman yetersiz, sağlıkçıların aletlerini eritip silah yapalım mı?"
    $ daily_visitors += 1
    menu:
        "Olur, demircilere talimat verin":
            $ Military += 1
            $ Health -= 2
            Muhafız_Başı "Efendim, silahlar hazır."
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şu anki durum yeterli":
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog49:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim ordudaki askerlerin sayısı az, buna bir çözüm bulalım."
    $ daily_visitors += 1
    menu:
        "Köylerden asker toplamaya çıkın":
            $ Military += 1
            $ People -= 2
            Muhafız_Başı "Efendim, köylerden askerler toplandı."
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Paralı asker alalım":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()
            $ muhafızbaşı_relationship += 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog50:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim asker sayımız çok fazla, bazılarını size koruma olarak verebilirim."
    $ daily_visitors += 1
    menu:
        "Yeterli muhafızım var":
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
        "Olur, ver bakalım":
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog51:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Bir grup haydut yolumuzu kesmişti, hepsini öldürüp silahlarını aldık. Bunları ne yapalım?"
    $ daily_visitors += 1
    menu:
        "Eritip tarım aletleri yapalım":
            $ Economy += 1
            $ People += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Askerlerimiz kullansınlar":
            $ Military += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog52:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Askerlerimiz savaş ganimetleri arasında bir takım sıhhiye aletleri buldu. Kime verelim?"
    $ daily_visitors += 1
    menu:
        "Otacılara verelim":
            $ Health += 1
            $ Religion -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
        "Şifacılara verelim":
            $ Health += 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog53:
    show Muhafız_Başı at muhafiz_basi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Muhafız_Başı "Efendim, askerler aileleri için ayrıcalık talep ediyorlar."
    $ daily_visitors += 1
    menu:
        "Herkes eşit haklara sahip olmalı":
            $ Military -= 1
            $ check_bars()
            $ muhafızbaşı_relationship -= 1
        "Ayrıcalıkları verelim":
            $ Military += 1
            $ People -= 1
            $ Politics -= 1
            $ check_bars()
            $ muhafızbaşı_relationship += 1
    hide image Muhafız_Başı
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog54:
    show Kadı at kadi_poz   
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor. Adaletin tecelli etmesi için kararınızı bekliyorum."
    $ daily_visitors += 1
    menu:
        "Bu topraklar Tacir'e ait. ":
            $ Economy += 1
            $ check_bars()
            $ kadı_relationship += 1
        "Bu topraklar Soylu'ya ait.":
            $ Politics += 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return

label dialog55:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Efendim, şehirdeki zengin bir tüccar, ödediği vergilerin haksız olduğunu iddia ediyor. Eğer bu konu çözülemezse, diğer tacirler de aynı yola başvurabilir."
    $ daily_visitors += 1
    menu:
        "O da herkes gibi vergisini ödemeli.":
            $ People += 1
            $ check_bars()
            $ kadı_relationship += 1
        "Ona ayrıcalık tanıyabiliriz.":
            $ Economy -= 1
            $ People -= 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog56:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Majesteleri, köylüler genç bir kadını büyücülükle suçluyor. Kadının suçlu olup olmadığına karar vermek için sizden bir hüküm beklenmektedir."
    $ daily_visitors += 1
    menu:
        "Büyü saçmalıklarına inanmam.": 
            $ People -= 1
            $ check_bars()
            $ kadı_relationship += 1
        "Büyü mü? O zaman idam edilsin.":
            $ People += 1
            $ religion += 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog57:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Kralım, muhafızlardan biri düşman krallıkla gizlice haberleşmekle suçlanıyor. Kanıtlar yetersiz ama halk idam edilmesini istiyor. Adaletin sağlanması için kesin bir emir vermelisiniz."
    $ daily_visitors += 1
    menu:
        "İdam edelim, şüphe kalmasın.":
            $ military -= 1
            $ People += 1
            $ check_bars()
            $ kadı_relationship -= 1
        "Hapis cezası verelim.":
            $ check_bars()
            $ kadı_relationship += 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog58:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Kralım, adaletin doğru ve hızlı bir şekilde yerine getirilebilmesi için yeni bir mahkeme binasına ihtiyacımız var. Eski bina küçük ve yetersiz kaldı."
    $ daily_visitors += 1
    menu:
        "Yeni bir mahkeme binası yapalım.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
            $ kadı_relationship += 1
        "Gerek yok, eski bina yeterli.":
            $ Politics -= 1
            $ People -= 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog59:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Efendim, yargıçlar ve mahkeme personelinin maaşları çok düşüktür. Onların maaşlarında bir artış yapılmasını talep ediyorum."
    $ daily_visitors += 1
    menu:
        "Maaşlara zam yapalım.":
            $ Economy -= 1
            $ People -= 1
            $ Politics += 1
            $ check_bars()
            $ kadı_relationship += 1
        "Maaşlarınız yeterli.":
            $ Economy += 1
            $ People += 1
            $ Politics -= 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog60:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Bazı suçlar, halk arasında büyük tartışmalara yol açıyor. Bu durumu önlemek için belirli suçların cezalarında değişiklik yapmamız gerekiyor."
    $ daily_visitors += 1
    menu:
        "Sorunlu cezalar hafiflesin.":
            $ People += 1
            $ Politics += 1
            $ check_bars()
            $ kadı_relationship += 1
        "Cezalar caydırıcı olmalıdır.":
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog61:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Kadı "Ülkemizin büyüklüğü ve adalet talepleri göz önüne alındığında, daha fazla kadı ve yargıç atanmasına ihtiyaç var."
    $ daily_visitors += 1
    menu:
        "Hemen işlemleri başlatıyorum.":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()
            $ kadı_relationship += 1
        "Daha fazla alım yapamayız.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()
            $ kadı_relationship -= 1
    hide image Kadı
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog62:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
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
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog63:
    show Kadı at kadi_poz
    $ visitors_today = renpy.random.randint(2, 4)
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
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog65:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Majesteleri, bu yılın hasadı çok iyi olacak gibi görünüyor. Vergileri biraz hafifletebilir misiniz?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın yükünü azaltın!":
            $People += 2
            $Economy -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Hayır, güçlü bir ekonomi için vergiler aynı kalmalı!":
            $People -= 2
            $Economy += 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog


label dialog66:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Topraklarımız kuruyor, sulama kanalları yapamaz mıyız?"
    $ daily_visitors += 1
    menu:
        "Evet, su yolları inşa edin!":
            $Economy -= 3
            $People += 2
            Çiftçi "Sağ olun, majesteleri. Topraklarımız size minnettar olacak!"
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu yıl idare edin, şimdilik bütçe yok.":
            $People -= 1
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog


label dialog67:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Köyümüzde veba var! Doktorlar gönderir misiniz?"
    $ daily_visitors += 1
    menu:
        "Derhal şifacıları yollayın!":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Köyü karantinaya alın, ama daha fazla uğraşmayın.":
            $People -= 1
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1  
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog68:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Yabancı tüccarlar mallarımızı ucuza alıyor, onlara karşı bir şey yapacak mısınız?"
    $ daily_visitors += 1
    menu:
        "Tüccarlarla görüşüp fiyatları adil hale getirin!":
            $Politics -= 1
            $Economy += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Serbest ticaret böyle işler, alışmalısınız.":
            $People -= 2
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog69:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
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
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog70:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Sürüdeki domuzlarımız kayboldu, hırsızlar mı aldı bilemiyoruz…"
    $ daily_visitors += 1
    menu:
        "Birkaç asker gönderin, hırsızları bulun!":
            $Military -= 1
            $People += 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Çiftlik işlerine karışamayız, kendi başınızın çaresine bakın.":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog71:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Yeni araziler açarsak daha fazla mahsul yetiştirebiliriz."
    $ daily_visitors += 1
    menu:
        "Toprak genişletme projelerine başlayın!":
            $Economy -= 3
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şimdilik elimizdekilerle idare edin.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog72:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Baş İmam, kutsal dualarla hasadın bereketli olacağını söylüyor. Bir ayin düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, ayini düzenleyin!":
            $Religion += 2
            $Economy -= 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Dualarla mahsul artmaz, çalışmaya devam edin!":
            $Religion -= 2
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog73:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Ürünlerimizin çoğu şehre gidiyor, köydekiler aç kalıyor!"
    $ daily_visitors += 1
    menu:
        "Şehirden köylere daha fazla yiyecek gönderin.":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şehir halkı önceliklidir, köylüler sabretsin.":
            $People -= 2
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog74:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Askerlerimiz eğitim yaparken ekinlerimizi eziyor, buna bir çözüm bulunabilir mi?"
    $ daily_visitors += 1
    menu:
        "Eğitim alanlarını başka bir yere taşıyın!":
            $Military -= 1
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Tarla her yıl büyür, askerlerimiz daha önemli!":
            $People -= 2
            $Military += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog75:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Gençlerimiz köyleri terk edip şehre gidiyor, tarım zayıflıyor…"
    $ daily_visitors += 1
    menu:
        "Köylere teşvik verin, daha fazla kişi tarımla uğraşsın!":
            $Economy -= 3
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Şehirde daha çok insana ihtiyaç var, bu doğal bir süreç.":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog76:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Tohum bulmak zorlaştı, ekim yapamazsak kıtlık başlar!"
    $ daily_visitors += 1
    menu:
        "Tohum desteği sağlayın!":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Çiftçiler kendi yollarını bulmalı.":
            $People -= 1
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog77:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Geleneksel hasat festivalimizi düzenleyelim mi?"
    $ daily_visitors += 1
    menu:
        "Evet, halkın morale ihtiyacı var!":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Festival gereksiz harcamadır, iptal edin.":
            $People -= 2
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog78:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Şiddetli bir fırtına yüzünden tarlalarımız mahvoldu!"
    $ daily_visitors += 1
    menu:
        "Çiftçilere yardım edin!":
            $Economy -= 3
            $People += 2
            Çiftçi "Bizi unutmadığınız için minnettarız, majesteleri!"
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu yıl kaybı kabullenmek zorundayız.":
            $People -= 1
            $Economy += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog79:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Kendimizi haydutlara karşı koruyabilmek için silah taşıyabilir miyiz?"
    $ daily_visitors += 1
    menu:
        "Evet, köylülere basit silahlar verin!":
            $People += 2
            $Military -= 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Hayır, ordu varken köylülerin silaha ihtiyacı yok.":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog80:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralım bana güneydeki arsalarınızı verirseniz onları sizin için ekebilirim."
    $ daily_visitors += 1
    menu:
        "Tamam, kârın bir kısmını alabilirsin.":
            $Economy += 1
            $Politics -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Benim arsam senin gibi bir çiftçinin insafına bırakılamaz.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
            Çiftçi "Haklısınız efendim."
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog81:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralımız, biz vergilerimizi ödeyen kısım askerlerden yeteri korumayı sağlamıyorlar."
    $ daily_visitors += 1
    menu:
        "Bir bölük askeri köyünüze yollayacağım.":
            $People += 2
            $Military -= 2
            $Politics -= 1
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
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog82:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralımız, köylüler olarak taleplerimizi bildirmek için sizinle bir görüşme yapmak istiyoruz."
    $ daily_visitors += 1
    menu:
        "Gerekli önlemleri alıp görüşmeyi yapacağım.":
            $People += 3
            $Economy -= 1
            $Politics -= 1
            $Military -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Halka bizzat benim görüşmem tehlikeli olacaktır.":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog83:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralımız, köyümüze hiç yağmur yağmadı. Çok zarar ettik, lütfen bu sene vergi almayın."
    $ daily_visitors += 1
    menu:
        "Vergilerinizi azaltıyorum.":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Herkes vergisini ödeyecek.":
            $People -= 2
            $Politics += 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog84:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Saygı değer Kralımız, köyümüzde yeterli insan gücü kalmadı. Tarım yaparken zorlanıyoruz. Bize hayvan desteği verir misiniz?"
    $ daily_visitors += 1
    menu:
        "10 baş hayvanı size hibe ediyorum.":
            $Economy -= 2
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu benim sorunum değil.":
            $People -= 2
            Çiftçi "Haklısınız efendim."
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

    label dialog85:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Majesteleri, bu yıl kuraklık hasatlarımızı mahvetti. Vergileri azaltmazsanız ailelerimiz aç kalacak. Lütfen bizden alınan vergiyi bu yıl için düşürün."
    $ daily_visitors += 1
    menu:
        "Vergiler aynı kalacak.":
            $People -= 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
        "Vergilerinizi ben ödeyeceğim.":
            $Economy -= 3
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog86:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Kralım, yıllardır lordumun topraklarında çalışıyorum ama kendi ailem için hiçbir şeyim yok. Bana ve aileme işleyebileceğimiz küçük bir arazi bağışlamanızı dilerim."
    $ daily_visitors += 1
    menu:
        "Sana ve ailene arazi veriyorum.":
            $Politics -= 3
            $Economy -= 1
            $People += 1
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Bu kabul edilemez.":
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog87:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Efendimiz, köyümüzden çok fazla genç erkek askere alındı. Tarlalarımızı ekecek kimse kalmadı. Daha fazla adam almamanız için yalvarıyorum."
    $ daily_visitors += 1
    menu:
        "Asker alımlarını azaltıyorum.":
            $People += 2
            $Military -= 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Sanmıyorum.":
            $People -= 1
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog

label dialog88:
    show Çiftçi at ciftci_poz
    $ visitors_today = renpy.random.randint(2, 4)
    Çiftçi "Efendim, haydutlar ve paralı askerler köylerimizi talan ediyor. Kadınlarımız ve çocuklarımız korku içinde yaşıyor. Bizi koruyacak bir grup asker gönderir misiniz?"
    $ daily_visitors += 1
    menu:
        "Köyünüze bir bölük asker gönderiyorum.":
            $Military -= 1
            $People += 2
            $ check_bars()
            $ chr_chng("çiftçi","+",1)
        "Köyünüzü korumak için bir de asker mi göndereceğim, git başımdan!":
            $People -= 2
            $ check_bars()
            $ chr_chng("çiftçi","-",1)
    hide image Çiftçi
    if daily_visitors >= visitors_today:
        $ managed_day += 1
        $ daily_visitors = 0
        $ advance_date(1)
    $ last_dialog = None
    $ main_story_count += 1
    jump random_dialog
