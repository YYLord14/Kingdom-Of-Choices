label dialog1:
    show Demirci
    
    Demirci "Kralım elimde kaliteli bir maden geçti bununla ne yapmalıyım?"
    $ dialog_count += 1

    menu:
        "Tarım aletleri yapabiliriz.":
            $ People += 1
            $ Economy += 1
            Demirci "Halk memnun olacaktır."
            $ check_bars()
        "Madeni satabiliriz.":
            $ Economy += 2
            Demirci "Güzel kar ettik."
            $ check_bars()
    
    hide image Demirci
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog2:
    show Ozan
    
    Ozan "Kralım saray ahalisi çok mutsuz bir eğlence düzenleyelim"
    $ dialog_count += 1

    menu:
        "Çok güzel olur, hadi yapalım.":
            $ People += 1
            $ Economy -= 2
            Ozan "Harika!"
            $ check_bars()
        "Ülkenin parasını çarçur edemeyiz.":
            Ozan "Ufff..."
            $ check_bars()
    
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog3:
    show Muhafız_Başı
    
    Muhafız_Başı "Ordumuzun gücünü artırmak için yeni askerler toplamalıyız"
    $ dialog_count += 1
    menu:
        "Evet, ordumuzu güçlendirelim.":
            $ Military += 2
            $ Economy -=1
            $ People -=1
            Muhafız_Başı "Halk hoşnut olmayacak ama ordumuz güçlenecek." 
            $ check_bars()

        "Hayır, halkın tepkisini çekebiliriz.":
            $ People += 1
            Muhafız_Başı "Peki."
            $ check_bars()
           
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog4:
    show Asker
    
    Asker "Saygı değer Kralım talimler çok fazla sayısını azaltmalısınız."
    $ dialog_count += 1

    menu: 
        "Muhafız Başı ile konuşacağım":
            $ Military -=1
            Asker "Çok yaşayın efendimiz"
            $ check_bars()

        "Gerek yok":
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog5:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralım Köyümüzü fareler bastı lütfen yardım edin"
    $ dialog_count += 1

    menu:
        "Ordudan bir bölük gönderiyorum":
            $ Military -= 2
            $ People +=2
            Çiftçi "Teşekkür ederim efendimiz"
            $ check_bars()

        "Başınızın çaresine bakın":
            $ People -= 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog6:
    show Baş_İmam
    
    Baş_İmam "Ülkedeki camiler yetersiz halkımız dışarda kalıyor destek talep ediyorum"
    $ dialog_count += 1

    menu:
        "Tamam vereceğim":
            $ Economy -= 2 
            $ Religion += 2
            $ check_bars()

        "Lüzumu yok":
            $ Religion -= 1
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog7:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Eğer vergilerde indirim yaparsanız kendi halkımdan gelen tacirleri  ülkenize yönlendiririm kazan kazan ne dersiniz"
    $ dialog_count += 1
    menu:
        "Kabul ediyorum":
            $ Economy += 1
            $ Politics += 2
            Zengin_Tüccar "Doğru karar verdiniz efendim"
            $ check_bars()
        "Herkese nasıl davranılıyorsa sanada öyle davranılacak":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog8:
    show Yerel_Bakan
    
    Yerel_Bakan "Kralım ülkenin bütçesinin büyük bir kısmı askeriye ye harcanıyor inşaatları arttıralım."
    $ dialog_count += 1
    menu:
        "Ordunun bütçesine dokunamayız":
            $ check_bars()
        "Olur ülkeyi kalkındıralım":
            $ Military -= 2
            $ Economy += 1
            $ People += 1
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog9:
    show Soylu
    
    Soylu "Yeterli sayıda kölem yok yenilerini nerden bulabilirim"
    $ dialog_count += 1
    menu:
        "Benim kölelerimin birazını satın alabilirsin":
            $ Economy += 2
            $ Politics -= 1
            Soylu "Teşekkürler"
            $ check_bars()
        "Bu benim sorunum değil":
            $ check_bars
            Soylu "Doğru, değil."
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog10:
    show Kadı
    
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor."
    $ dialog_count += 1
    menu:
        "Arazi Soylunun hakkı":
            $ Politics += 1 
            $ Economy -= 1
            $ check_bars()
        "Arazi Tacirin hakkı":
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog11:
    show Şifacı
    
    Şifacı "Tıp için bir araştırma yapmam gerekiyo bütçeyi nasıl oluşturayım"
    $ dialog_count += 1
    menu: 
        "Ben vereceğim":
            $ Economy -= 2
            $ Health += 1
            Şifacı "Teşekkür ederim efendim"
            $check_bars()
        "Bu araştırma gereksiz":
            $check_bars()
    hide image Şifacı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog12:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim Narga Krallığı sınırlarımızı ihlal ediyor bu bir son vermemiz gerek."
    $ dialog_count += 1
    menu:
        "Savaş açalım hadlerini aşmasınlar.":
            $ Economy -= 1
            $ People -= 2
            $ Military -= 2
            $ Politics += 2
            Muhafız_Başı "Efendim, savaş ilan edildi."
            $ check_bars()

        "Barış imzalayalım şartlarını kabul edelim.":
            $ Economy -= 2
            $ Politics -= 2
            $ check_bars()
    hide image Muhafız_Başı
    
label dialog13:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim askerler arasında bir husumet çıktı bu sorunu çözmeliyiz."
    $ dialog_count += 1
    menu:
        "Bölükleri ayıralım husumet dağılsın.":
            $ Military -= 1
            Muhafız_Başı "Efendim, bölükler ayrıldı, husumet sona erdi."
            $ check_bars()

        "Komutan sen değil misin bastır onları.":
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog14:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim Kuzey bölgesinden bir grup haydut bir köyü basıp insanları rehin almış."
    $ dialog_count += 1
    menu:
        "Ben haydutlarla pazarlık yapmam orduyu üzerlerine sür.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()

        "Ne istiyorlarsa verip köylüleri kurtarın":
            $ Economy -= 2
            $ People += 1
            $ check_bars()
            Muhafız_Başı "Efendim, köylüler kurtarıldı."
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog15:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim ordu için ekipman yetersiz sağlıkçıların aletlerini eritip silah yapalım mı?"
    $ dialog_count += 1
    menu:
        "Olur demircilere talimat verin.":
            $ Military += 1
            $ Health -= 2
            Muhafız_Başı "Efendim, silahlar hazır."
            $ check_bars()

        "şuan ki durum yeterli.":
            $ Military -= 1
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog16:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim ordudaki askerlerin sayısı az buna bir çözüm bulalım."
    $ dialog_count += 1
    menu:
        "köylerden asker toplamaya çıkın.":
            $ Military += 1
            $ People -= 2
            Muhafız_Başı "Efendim, köylerden askerler toplandı."
            $ check_bars()

        "Paralı asker alalım.":
            $ Economy -= 2
            $ Military += 2
            Muhafız_Başı "Paralı askerler geldi."
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog17:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim asker sayımız çok fazla bazılarını size koruma olarak verebilirim"
        
    menu: 
        "Yeterli muhafızım var":
            $ check_bars()
        "Olur ver bakalım":
            $ Military -= 1
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog18:
    show Muhafız_Başı
    
    Muhafız_Başı "Bir grup haydut yolumuzu kesmişti hepsini öldürüp silahlarını aldık bunları ne yapalım?"
    $ dialog_count += 1
    menu:
        "Eritip tarım aletleri yapalım.":
            $ Economy += 1
            $ People += 1
            Muhafız_Başı "Efendim, tarım aletleri hazır."
            $ check_bars()
        "Askerlerimiz kullansınlar.":
            $ Military += 1
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog19:
    show Muhafız_Başı
    
    Muhafız_Başı "Askerlerimiz savaş ganimetleri arasında bir takım sıhhıyye aletleri buldu kime verelim."
    $ dialog_count += 1
    menu:
        "Otacılara verelim.":
            $ Health += 1
            $ Religion += 1
            $ check_bars()

        "Şifacılara verelim.":
            $ Health += 1
            $ Politics += 1
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog20:
    show Muhafız_Başı
    
    Muhafız_Başı "Efendim askerler aileleri için yarıcalık talep ediyorlar."
    $ dialog_count += 1
    menu:
        "Herkes eşit haklara sahip olmalı.":
            $ Military -= 1
            $ check_bars()

        "Ayrıcalıkları verelim.":
            $ Military += 1
            $ People -= 1
            $ Politics -= 1
            $ check_bars()
    hide image Muhafız_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog21:
    show Kadı
    
    Kadı "Majesteleri, bir Soylu ve bir  Tacir , sınırları belirlenmemiş bir arazi yüzünden yıllardır anlaşmazlık içinde. Her ikisi de bu toprakların kendilerine ait olduğunu iddia ediyor. Adaletin tecelli etmesi için kararınızı bekliyorum."
    $ dialog_count += 1
    menu:
        "Bu topraklar Tacir'e ait.":
            $ Economy += 1
            $ check_bars()

        "Bu topraklar Soylu'ya ait.":
            $ Politics += 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog22:
    show Kadı
    
    Kadı "Efendim, şehirdeki zengin bir tüccar, ödediği vergilerin haksız olduğunu iddia ediyor .Eğer bu konu çözülemezse, diğer tacirler de aynı yola başvurabilir."
    $ dialog_count += 1
    menu:
        "Oda herkes gibi vergisini ödemeli.":
            $ check_bars()
        "Oda herkes gibi vergisini ödemeli.":
            $ Economy -= 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog23:
    show Kadı
    
    Kadı"Majesteleri, köylüler genç bir kadını büyücülükle suçluyor. Kadının suçlu olup olmadığına karar vermek için sizden bir hüküm beklenmektedir."
    $ dialog_count += 1
    menu:
        "Büyü saçmalıklarına inanmam.":
            $ People -= 1
            $ check_bars()

        "Büyümü? O zaman idam edilsin.":
            $ People += 1
            $ check_bars()
        
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog24:
    show Kadı
    
    Kadı "Kralım muhafızlardan biri, düşman krallıkla gizlice haberleşmekle suçlanıyor. Kanıtlar yetersiz ama halk idam edilmesini istiyor. Adaletin sağlanması için kesin bir emir vermelisiniz."
    $ dialog_count += 1
    menu:
        "İdam edelim şüphe kalmasın.":
            $ Military -= 1
            $ People += 1
            Kadı "En iyisini kralımız bilir."
            $ check_bars()
        "Hapis cezası verelim.":
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog25:
    show Kadı
    
    Kadı "Kralım, adaletin doğru ve hızlı bir şekilde yerine getirilebilmesi için yeni bir mahkeme binasına ihtiyacımız var. Eski bina küçük ve yetersiz kaldı."
    $ dialog_count += 1
    menu:
        "Yeni bir mahkeme binası yapalım.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()

        "Gerek yok, eski bina yeterli.":
            $ Politics -= 1
            $ People -= 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog26:
    show Kadı
    
    Kadı "Efendim , Yargıçlar ve mahkeme personelinin maaşları çok düşüktür, Onların maaşlarında bir artış yapılmasını talep ediyorum."
    $ dialog_count += 1
    menu:
        "Maaşlara zam yapalım.":
            $ Economy -= 1
            $ People -= 1
            $ Politics += 1
            $ check_bars()

        "Lan gevşekler, zaten çok kazanıyolar.":
            $ Economy += 1
            $ People += 1
            $ Politics -= 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog27:
    show Kadı
    
    Kadı "Bazı suçlar, halk arasında büyük tartışmalara yol açıyor. Bu durumu önlemek için belirli suçların cezalarında değişiklik yapmamız gerekiyor."
    $ dialog_count += 1
    menu:
        "Sorunlu Cezalar Hafiflesin.":
            $ People += 1
            $ Politics += 1
            $ check_bars()

        "Cezalar caydırıcı olmalıdır.":
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog28:
    show Kadı
    
    Kadı "Ülkemizin büyüklüğü ve adalet talepleri göz önüne alındığında, daha fazla kadı ve yargıç atanmasına ihtiyaç var."
    $ dialog_count += 1
    menu:
        "Hemen işlemleri başlatıyorum.":
            $ Economy -= 2
            $ Politics += 2
            $ check_bars()

        "Yoldan geçeni kadı mı yapalım? alla alla ya git işine,sen çalışsan hekes çalışır.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog29:
    show Kadı
    
    Kadı "Kralım , Halk arasında eşitlik ve adaletin sağlanması adına, köylerde ve kasabalarda da düzenli olarak adaletli bir şekilde duruşmalar yapılmalıdır."
    $ dialog_count += 1
    menu:
        "Köylülerin de hakkını koruyalım.":
            $ Economy -= 1
            $ People += 2
            $ check_bars()

        "La köylünün ne işi var siyasette , gitsin kahvelerde yapsın siyasetini.":
            $ People -= 1
            $ Politics -= 1

            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog30:
    show Kadı
    
    Kadı "Büyük Kralım, kadınların ve çocukların korunması hususunda daha fazla önlem alınmasını rica ediyorum. Bu, toplumda adalete olan güveni pekiştirecek ve halkın huzurunu sağlayacaktır."
    $ dialog_count += 1
    menu:
        "Kadın ve çocukların korunması için yeni yasalar çıkaralım.":
            $ People += 2
            $ Politics += 1
            $ check_bars()

        "Kadınlar ve çocuk cinayetinin artması toplumun içine işlemiş bunu ancak toplum düzeltebilir.":
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
    hide image Kadı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog31:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralım Köyümüzü fareler bastı lütfen yardım edin."
    $ dialog_count += 1
    menu:
        "Orduyu gönderiyorum":
            $ Military -= 2
            $ People += 2
            $ check_bars()

        "Benim askerlerim fare toplamak için yok.":
            $ People -= 1
            $ Military +=1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog32:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralım bir mağranın içinde Mavi şapkalı mantar bulduk bize ekonomik destek sağlarsanız onları sizin için toplayabiliriz."
    $ dialog_count += 1
    menu:
        "Böyle saçma işlerle huzuruma bir daha çıkma!":
            $ People -= 1
            $ check_bars()

        "Tamam destediği sağlıyorum.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog33:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralım bana güneydeki arsalarınızı verirseniz onları sizin için ekebilirim."
    $ dialog_count += 1
    menu:
        "Tamam kârın bir kısmını alabilirsin.":
            $ Economy += 1
            $ Politics -= 2
            $ check_bars()

        "Benim arsam senin gibi bir çiftçinin insafına bırakılamaz.":
            Çiftçi "Haklısınız Efendim."
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog34:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralımız biz vergilerimizi ödeyen kısım askerlerden yeteri korumayı sağlamıyorlar."
    $ dialog_count += 1
    menu:
        "Bir bölük askeri köyünüze yollayacağım.":
            $ People += 2
            $ Military -= 2
            $ Politics -= 1
            Çiftçi "Minnettarım efendim."
            $ check_bars()

        "Size savaşmayı öğretmesi için bir komutanımı göndereceğim.":
            $ Military -= 1
            $ People += 1
            $ Politics += 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog35:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralımız köylüler olarak taleplerimizi bildirmek için sizinle bir görüşme yapmak istiyoruz."
    $ dialog_count += 1
    menu:
        "Gerekleri önlemleri alıp görüşmeyi yapacağım.":
            $ People += 3
            $ Economy -= 1
            $ Politics -= 1
            $ Military -= 2
            Çiftçi "Çok teşekkür ederiz efendim."
            $ check_bars()

        "Halka bizzat benim görüşmem tehlikli olacaktır.":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog36:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralımız köyümüze hiç yağmur yağmadı çok zarar ettik lütfen bu sene vergi almayın."
    $ dialog_count += 1
    menu:
        "Vergilerinizi azaltıyorum.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()

        "Herkes vergisini ödeyecek":
            $ People -= 2
            $ Politics += 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog37:
    show Çiftçi
    
    Çiftçi "Saygı değer Kralımız köyümüzde yeterli insan gücü kalmadı tarım yaparken zorlanıyoruz bize hayvan desteği verirmisiniz."
    $ dialog_count += 1
    menu:
        "10 baş hayvanı veriyorum.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()

        "bu benim sorunum değil":
            $ People -= 2
            Çiftçi "Haklısınız efendim."
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog38:
    show Çiftçi
    
    Çiftçi "Majesteleri, bu yıl kuraklık hasatlarımızı mahvetti. Vergileri azaltmazsanız ailelerimiz aç kalacak. Lütfen bizden alınan vergiyi bu yıl için düşürün."
    $ dialog_count += 1
    menu:
        "Vergiler aynı kalacak.":
            $ People -= 2
            $ check_bars()

        "Vergileri düşürdüm.":
            $ Economy -= 3
            $ People += 2
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog39:
    show Çiftçi
    
    Çiftçi "Kralım, yıllardır lordumun topraklarında çalışıyorum ama kendi ailem için hiçbir şeyim yok. Bana ve aileme işleyebileceğimiz küçük bir arazi bağışlamanızı dilerim."
    $ dialog_count += 1
    menu:
        "Sana ve ailene arazi veriyorum.":
            $ Politics -= 3
            $ Economy -= 1
            $ People += 1
            $ check_bars()

        "Bu kabul edilemez.":
            $ People -= 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog40:
    show Çiftçi
    
    Çiftçi "Efendimiz, köyümüzden çok fazla genç erkek askere alındı. Tarlalarımızı ekecek kimse kalmadı. daha fazla adam almamanız için yalvarıyorum."
    $ dialog_count += 1
    menu:
        "Asker alımlarını azaltıyorum.":
            $ People += 2
            $ Military -= 2
            Çiftçi "Siz adaletli bir kralmışsınız efendim."
            $ check_bars()
        "Sanmıyorum.":
            $ People -= 1
            $ check_bars()

    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog41:
    show Çiftçi
    
    Çiftçi "Efendim, haydutlar ve paralı askerler köylerimizi talan ediyor. Kadınlarımız ve çocuklarımız korku içinde yaşıyor. Bizi koruyacak bir grup asker gönderir misiniz?"
    $ dialog_count += 1
    menu:
        "Köyünüze bir bölük asker gönderiyorum.":
            $ Military -= 1
            $ People += 2
            Çiftçi "Heybetinizle köyümüzü koruyacaklarınıza inanıyoruz efendim."
            $ check_bars()

        "Köyünüzü korumak için bide asker mi göndercem,zaten işim başımdan aşkın git başımdan!":
            $ People -= 2
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog42:
    show Çiftçi
    
    Çiftçi "Kralım, tarlalarımız kuruyor ve mahsul alamıyoruz. Köyümüze bir kuyu açtırmanız veya bir sulama kanalı yaptırmanız için yalvarıyoruz."
    $ dialog_count += 1
    menu:
        "Köyünüze bir kuyu açtırıyorum.":
            $ Economy -= 2
            $ People += 1
            $ Health += 1
            $ check_bars()

        "Köyünüz gözümde bir belde değil, kuyu açtırmak size düşer.":
            $ People -= 1
            $ check_bars()
    hide image Çiftçi
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog43:
    show Baş_İmam
    
    Baş_İmam "Topladığımız paralardan artanları getirdim hazineye koyalım"
    $ dialog_count += 1
    menu:
        "Olur koyalım":
            $ Economy += 2
            $ check_bars()

        "Halka dağıtalım":
            $ Religion += 1
            $ People += 1
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog44:
    show Baş_İmam
    
    Baş_İmam "Ülkedeki camiler yetersiz destek talep ediyorum."
    $ dialog_count += 1
    menu:
        "Tamam câmi yapımı için destek vericem.":
            $ Economy -= 2
            $ Religion += 2
            Baş_İmam "Desteğiniz için teşekkür ederiz efendim"
            $ check_bars()

        "Câmi'lerin yeterli olduğunu düşünüyorum,talebinizi reddediyorum.":
            $ Religion -= 1
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog45:
    show Baş_İmam
    
    Baş_İmam "Camilerde topladığımız yardımlar arttı bu kadarına ihtiyacımız yok ne yapalım."
    $ dialog_count += 1
    menu:
        "Halka yemek dağıtalım.":
            $ People += 1
            $ check_bars()

        "Orduya yemek dağıtalım.":
            $ Military += 1
            $ check_bars()

    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog46:
    show Baş_İmam
    
    Baş_İmam "Gençlerimizin gereken eğitimi alması için medreseler açalım."
    $ dialog_count += 1
    menu:
        "Gençlerin gelişimi için gerekli buluyorum,talebiniz onaylanmıştır çocuklarımızı geliştirin.":
            $ Economy -= 2
            $ Politics += 2
            $ People += 1
            $ Religion += 1
            Baş_İmam "Sağolun efendim, elimden gelenin daha iyisini yapıcam."
            $ check_bars()

        "Gençlerimizin zaten bilinçli olduğunu düşünüyorum.":
            $ Religion -= 1
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog47:
    show Baş_İmam
    
    Baş_İmam"Vergilerin bir kısmı ile başı boş kişilere eğitim verelim."
    $ dialog_count += 1
    menu:
        "Çok iyi fikir.":
            $ Economy -= 2
            $ Religion += 1
            $ Politics += 1
            $ check_bars()

        "Zaten işlerim var bide bunlara para veremem.":
            $ Religion -= 1
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog48:
    show Baş_İmam
    
    Baş_İmam"Efendimiz, şehirlerimizde kumar, içki ve sefahat artıyor. Bu günahları önlemek için daha sert yasalar getirmenizi rica ediyorum."
    $ dialog_count += 1
    menu:
        "Yeni yasalar getirilsin.":
            $ People -= 2
            $ Religion += 3
            $ check_bars()

        "Burası laik bir krallık,isteyen istediğini yapar.":
            $ Religion -= 1
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog49:
    show Baş_İmam
    
    Baş_İmam"Kralım, halkın inancını güçlendirmek için kutsal bir günü kraliyet kararıyla resmî bayram ilan edelim."
    $ dialog_count += 1
    menu:
        "Tamam Hangi günler olsun?":
            $ Economy -= 1
            $ Religion += 2
            $ check_bars()

        "Kafamıza göre bir bayram ilan etmicem çok saçma!":
            $ Religion -= 2
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog50:
    show Baş_İmam
    
    Baş_İmam"Majesteleri, kararlarınıza rehberlik etmesi için yanınıza bir din bilgini almanızı öneririm."
    $ dialog_count += 1
    menu:
        "Mantıklı, bende arıyordum sen olmak istermisin?":
            $ Politics -= 1
            $ Religion += 2
            Baş_İmam "Efendim ! ne yaptınız ? Elimden gelenin en iyisini yapıcağım."
            $ check_bars()
        "Siyaset bilmezsin,hala diyosun yanıma din adamı alıyım.":
            $ check_bars()
    hide image Baş_İmam
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog51:
    show Soylu
    
    Soylu "Aquila Kralı elinizdeki mevcut hazine ile zor zamanlar için bir tahıl ambarı açmalısınız."
    $ dialog_count += 1
    menu:
        "Mantıklı açıyorum tahıl ambarını.":
            $ Economy -= 3
            $ check_bars()
        "Hazineyi kullanmak istemiyorum.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog52:
    show Soylu
    
    Soylu "Yeterli sayıda kölem yok yenilerini nerden bulabilirim."
    $ dialog_count += 1
    menu:
        "Benim kölelerimi satın alabilirsin.":
            $ Politics -= 1
            $ Economy += 2
            $ check_bars()
        "Benim sorunum değil.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog53:
    show Soylu
    
    Soylu "Evimin yanındaki inşaat yıkıldı ve evimin duvarı zarar gördü karşılanmasını talep ediyorum."
    $ dialog_count += 1
    menu:
        "Tüm zararın benim tarafımdan ödecenek.":
            $ Economy -= 2
            $ People += 2
            Soylu "Desteğiniz için teşekkür ederim efendim."
            $ check_bars()

        "Git inşaat sahibinden al zararını.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog54:
    show Soylu
    
    Soylu "Pazarlarda büyük tüccarlar çok kar ederken küçük tüccarlar zarara uğruyor bunun önüne geçmemizz gerek."
    $ dialog_count += 1
    menu:
        "Vergileri adaletli yapalım.":
            $ Politics += 2
            $ check_bars()

        "Vergileri eşit yapalım.":
            $ Politics -= 1
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog55:
    show Soylu
    
    Soylu "Komutanlar çok kazanıyor maaşlarını azaltıp başka alanlara yöneltelim."
    $ dialog_count += 1
    menu:
        "İnşaatları arttıralım.":
            $ Economy += 1
            $ Military -= 2
            $ check_bars()

        "Komutanlarımın sadakatini sorgulama.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog56:
    show Soylu
    
    Soylu "Ülke zor durumda , bazı Soylular elindeki değerli eşyaları size vermek istiyor."
    $ dialog_count += 1
    menu:
        "Hazineye koyalım.":
            $ Economy += 2
            $ check_bars()

        "Askeri harcamalar yapalım.":
            $ Military += 2
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog57:
    show Soylu
    
    Soylu "Efendim bazı köyler eksik vergi ödemişler ne yapalım?"
    $ dialog_count += 1
    menu:
        "Kalan borçlarını ödesinler.":
            $ Economy += 1
            $ check_bars()

        "Cezalandırılacaklar.":
            $ Economy += 3
            $ People -= 2
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog58:
    show Soylu
    
    Soylu "Tavernada bir eğlence düzenlemek istiroum bu sayede tacirler ülkemize daha çok uğrar."
    $ dialog_count += 1
    menu:
        "Mantıklı ücretini karşılıyorum.":
            $ Economy -= 1
            $ People += 1
            Soylu "Desteğiniz gözüm de saygınızı artırdı efendim."
            $ check_bars()

        "Böyle şeylere para harcamak mantıklı değil.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog59:
    show Soylu
    
    Soylu "Kralım kölelerim çok fazla size satmak istiyorum."
    $ dialog_count += 1
    menu:
        "Tamam hepsini satın alıyorum. Askeriyede getir götür için çalışacaklar.":
            $ Economy -= 2
            $ Military += 1
            $ Politics += 1
            Soylu "Kazan kazan."
            $ check_bars()

        "Kölelerin çoksa onlara el koyuyorum tarlalarda çalışacaklar.":
            $ Economy += 2
            $ People += 1
            $ Politics -= 3
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog60:
    show Soylu
    
    Soylu "Daha fazla para için köleleri su kenarlarına götürelim balık yakalasınlar."
    $ dialog_count += 1
    menu:
        "Kölelerinizi balıkçılık yapmaları için götürelim.":
            $ People -= 1
            $ Economy += 1
            $ check_bars()

        "Kölelerinizi balıkçılık yapmaları için götürmeyin,kölelerde insan.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog61:
    show Soylu
    
    Soylu "Köylerden gelen vergileri arttıralım."
    $ dialog_count += 1
    menu:
        "Vergileri arttıralım.":
            $ Economy += 2
            $ People -= 2
            $ Politics -= 1
            $ check_bars()

        "Vergiler ideal.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog62:
    show Soylu
    
    Soylu "Daha fazla para için köleleri inşaatlarda çalıştıralım."
    $ dialog_count += 1
    menu:
        "Köleleri inşaatlarda çalıştıralım.":
            $ Economy += 2
            $ People -= 2
            $ Politics -= 1
            $ check_bars()
        "Kölelerde insan,zaten çok çalışıyolar":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog63:
    show Soylu
    
    Soylu "Majesteleri, Bana bir toprak bağışlamanızı talep ediyorum. Böylece hem krallığınıza daha fazla vergi ödeyebilir hem de sınırları koruyabilirim."
    $ dialog_count += 1
    menu:
        "Toprak bağışlıyorum.":
            $ Politics -= 3
            $ Economy += 1
            $ Military += 1
            Soylu "Bana güvenebilirsiniz majesteleri."
            $ check_bars()

        "Kendi alabiliyorsa alsın,benden toprak yok.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog64:
    show Soylu
    
    Soylu "Efendim, danışmanlarınız arasında daha fazla söz hakkına sahip olmalıyım. Kraliyet konseyinizde bana bir yer verirseniz, tecrübemle kararlarınıza rehberlik edebilirim."
    $ dialog_count += 1
    menu:
        "Kraliyet konseyine alıyorum.":
            $ Politics -= 2
            $ check_bars()

        "Kraliyet konseyine almam söz konusu bile olamaz.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog65:
    show Soylu
    
    Soylu "Majesteleri, güçlü bir ittifak ve sizin otoritenizi güçlendirmek için beni bir başka asile evlendirmenizi rica ediyorum."
    $ dialog_count += 1
    menu:
        "İttifak için evlendiriyorum.":
            $ Politics += 2
            $ Economy -= 2
            Soylu "Yüzünüzü kara çıkartmicam efendim."
            $ check_bars()

        "Gerek yok,ittifaklarım zaten güçlü.":
            $ check_bars()
    hide image Soylu
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog66:
    show Asker
    
    Asker "Saygı değer Kralım talimler çok fazla sayısını azaltmalısınız. Bu durumda ne yapacaksınız?"
    $ dialog_count += 1
    menu:
        "Muhafız başı ile konuşacağım.":
            $ Military -= 1
            $ check_bars()

        "Gerek görmüyorum.":
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog67:
    show Asker
    
    Asker "Saygı değer Kralım savaş ganimetlerinin çoğu komutanlarımıza gidiyor adalet istiyoruz."
    $ dialog_count += 1
    menu:
        "Düzenleme yapacağım.":
            $ Military += 1
            $ Politics -= 1
            Asker "Minnattarım yüce kralım."
            $ check_bars()

        "Mevcut düzen iyi.":
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog68:
    show Asker
    
    Asker "Saygı değer Kralım silahlarımız eskidi yenilerine ihtiyaç var."
    $ dialog_count += 1
    menu:
        "Demircilere talimat vericem.":
            $ Military += 1
            $ Economy -= 1
            $ check_bars()

        "Elinizdekilerle yetinin.":
            $ Military -= 1
            Asker "Emriniz olur efendim."
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog69:
    show Asker
    
    Asker "Kralım yemekler yeterince iyi değil değişmesini talep ediyoruz."
    $ dialog_count += 1
    menu:
        "Yemeklerin kalitesini arttıracağım.":
            $ Economy -= 2
            $ Military += 2
            Asker "Minnettarım efendim."
            $ check_bars()

        "Yemeklerin kalitesi yeterli.":
            $ Military -= 1
            Asker "Emredersiniz!"
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog70:
    show Asker
    
    Asker "Kralım yatakhaneler çok berbat daha iyilerini hak ediyoruz."
    $ dialog_count += 1
    menu:
        "Haklısın düzenlemeleri yapacağım.":
            $ Economy -= 2
            $ Military += 2
            Asker "Sağolun kralım."
            $ check_bars()

        "İdare etmeye çalışın.":
            $ Military -= 1
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog71:
    show Asker
    
    Asker "Kralım askerler size minnetlerini sunmak için sizi kışlaya davet ediyorlar."
    $ dialog_count += 1
    menu:
        "Kışlaya gideceğim.":
            $ Politics += 1
            $ check_bars()

        "Askerleri saraya davet ediyorum.":
            $ Military += 1
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog72:
    show Asker
    
    Asker "Majesteleri, savaş meydanında gösterdiğim kahramanlıklar nedeniyle bana ve aileme küçük bir arazi bağışlamanızı rica ederim."
    $ dialog_count += 1
    menu:
        "Yaptığın kahramanlaıklar için minnettarız arazi bağışlıyoruz.":
            $ Politics -= 1
            $ Economy -= 1
            $ Military += 1
            Asker "Minnettarım yüce kralım."
            $ check_bars()

        "Hayır sende herkes gibi eşit pay alacaksın.":
            $ Military -= 1
            $ Politics += 1
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog73:
    show Asker
    
    Asker "Efendim, uzun yıllardır ordunuza sadakatle hizmet ettim. Bana şövalyelik unvanı ve komuta edebileceğim küçük bir birlik bahşetmenizi dilerim."
    $ dialog_count += 1
    menu:
        "Artık yeni bir komutanımız var.":
            $ Politics -= 2
            $ Military += 1
            Asker "Minnettarım efendim"
            $ check_bars()

        "Bunun için çok erken.":
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog74:
    show Asker
    
    Asker "Majesteleri, askerlerimiz zor şartlar altında görev yapmaktadır. Orduya daha fazla destek sağlamanızı arz ederim."
    $ dialog_count += 1
    menu:
        "Haklısın!":
            $ Economy -= 2
            $ Military += 2
            $ check_bars()

        "Şimdilik bu kadarı yeter.":
            $ Military -= 1
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog75:
    show Asker
    
    Asker "Kralım, yıllardır seferden sefere koşuyorum. Eşim ve çocuklarım beni görmeyi özledi. Kısa bir süreliğine köyüme dönmem için izin vermenizi istiyorum."
    $ dialog_count += 1
    menu:
        "Aileni görmek seninde hakkın tabiki gidebilirsin,izin veriyorumm.":
            $ Military -= 2
            $ People += 1
            Asker "Çocuğuma sizin isminizi vericem efendim."
            $ check_bars()

        "Hayır bölüğünden ayrılamassın.":
            $ People -= 1
            $ check_bars()
    hide image Asker
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog76:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Elimde çok değerli bir tarihi eser var bunu almak isteyebilirsiniz."
    $ dialog_count += 1
    menu:
        "Tamam alıyorum.":
            $ Economy -= 2
            $ check_bars()

        "Ben böyle şeylere para harcamam.":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog77:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Kiralık asker arıyorum ordunuzdan bir bölük alabilirmiyim."
    $ dialog_count += 1
    menu:
        "Tamam senin için bir bölük hazırlayacağım.":
            $ Politics -= 1
            $ Economy += 3
            $ Military -= 2
            $ check_bars()

        "Ben Kraliyet ordusunu para için savaştırtmam seninle işim yok.":
            $ Politics += 1
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog78:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Yargea dan geldim elimde güzel deriler var bakmak istemisin."
    $ dialog_count += 1
    menu:
        "Tamam alıyorum.":
            $ Economy -= 1
            $ check_bars()

        "saçma şeylere para harcamam.":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog79:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Majesteleri, tüccarlarınızın yolları haydutlarla dolu! Eğer askerleriniz bu yolları korursa, ticaretimiz büyür ve hazineniz altınla dolar."
    $ dialog_count += 1
    menu:
        "Tamam senin için bir bölük hazırlayacağım.GELSİN PARALAR":
            $ Military -= 2
            $ Economy += 3
            $ check_bars()

        "Ben Kraliyet ordusunu para için savaştırtmam seninle işim yok.":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog80:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Kralım, eğer bana ve loncalarıma özel bir vergi indirimi sağlarsanız, size her yıl bol miktarda altın ve mal göndermeye söz veririm."
    $ dialog_count += 1
    menu:
        "Kabul ediyorum kadı ya söyleyin.":
            $ Politics -= 3
            $ Economy += 2
            $ check_bars()

        "Bu kabul edilemez.":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog81:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Majesteleri, tuz ve baharat ticaretinin tek yetkilisi ben olayım. Karşılığında size her yıl belirli bir miktar gelir aktarırım."
    $ dialog_count += 1
    menu:
        "Ben rüşvet kabul etmem.":
            $ check_bars()

        "Kulağa harika geliyor.":
            $ Politics -= 3
            $ Economy += 2
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog82:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Kralım, ticaretin gelişmesi için yeni bir pazar yeri ya da liman açılmasını öneriyorum. Böylece, yabancı tüccarlar gelip daha fazla vergi ödeyebilirler."
    $ dialog_count += 1
    menu:
        "İnşaat için köleleri kullanalım ve yeni bir liman açalım.":
            $ Economy += 2
            $ People -= 2
            $ Politics += 1
            $ check_bars()

        "Pazar yerleri yeterli.":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog83:
    show Zengin_Tüccar
    
    Zengin_Tüccar "Efendim, soylular ve Baş imam çok fazla güce sahip. Bana daha fazla yetki verirseniz, ticareti ve dolayısıyla krallığın ekonomisini sizin için büyütürüm."
    $ dialog_count += 1
    menu:
        "Tamamdır! istediğin olsun.":
            $ Politics -= 2
            $ Religion -= 2
            $ Economy += 3
            $ check_bars()

        "Olmaz!":
            $ check_bars()
    hide image Zengin_Tüccar
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog84:
    show Yerel_Bakan
    
    Yerel_Bakan "Kralım soyluların elinde çok fazla değerli eşya var bunları eritip ordunun harcamaları için kullanalım."
    $ dialog_count += 1
    menu:
        "Kabul ediyorum gerekenleri yap!":
            $ Politics -= 1
            $ People -= 1
            $ Military += 1
            $ check_bars()

        "Soyluların şahsi mallarına dokunamayız.":
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog85:
    show Yerel_Bakan
    
    Yerel_Bakan "Efendim batı daki köyler sınırlarımıza çok yakın onlar için tehlike arz ediyor."
    $ dialog_count += 1
    menu:
        "Köylüleri daha güvenli yerlere taşıyalım.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()

        "Sınır bölgelerini boşaltırsak o toprakları sahipsiz bırakırız.":
            $ Politics += 1
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog86:
    show Yerel_Bakan
    
    Yerel_Bakan "Kralım hazinemiz tükeniyor bir çare bulmamız gerek."
    $ dialog_count += 1
    menu:
        "Askerleri yağmaya gönderelim.":
            $ Military -= 3
            $ Economy += 2
            $ check_bars()

        "Kölelerimizi geceleride çalıştıralım.":
            $ People -= 2
            $ Economy += 2
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog87:
    show Yerel_Bakan
    
    Yerel_Bakan "Efendim hazineden bir miktar altın arttırdım bunu ne için kullanalım."
    $ dialog_count += 1
    menu:
        "Sağlıkçıların eşyalarını yeniliyelim.":
            $ Health += 2
            $ check_bars()

        "Ordunun ihtiyaçlarını karşılayalım":
            $ Military += 2
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog88:
    show Yerel_Bakan
    
    Yerel_Bakan "Kralım Zemorvia Krallığı ile barış antlaşmamız ın süresi bitiyor yenisini imzalıyıp sulh e devam edelim mi?"
    $ dialog_count += 1
    menu:
        "Olur ticaretteki becerileri ekonomimizi iyileştirecektir.":
            $ Economy += 1
            $ Politics += 1
            $ check_bars()

        "Savaşalım orduları bizden zayıf yağma yaparak daha çok gamimet elde edebiliriz.":
            $ Economy += 3
            $ Military -= 3
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog89:
    show Yerel_Bakan
    
    Yerel_Bakan "Soyluların çok fazla değerli  eşyaları var onlara el koyup hazineye ekleyebiliriz."
    $ dialog_count += 1
    menu:
        "Bu zalimlik olur.":
            $ check_bars()

        "Ülkenin paraya ihtiyacı var,yapalım.":
            $ People -= 2
            $ Politics -= 2
            $ Economy += 3
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog90:
    show Yerel_Bakan
    
    Yerel_Bakan "Yonkur Krallığı bize savaş açtığını iletti ne yapacağız."
    $ dialog_count += 1
    menu:
        "Muhafız başına haber ver savaşalım.":
            $ Military -= 3
            $ Politics -= 1
            $ Economy += 1
            $ check_bars()

        "Bu işi masade çözebiliriz.":
            $ Politics += 2
            $ Economy -= 2
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog91:
    show Yerel_Bakan
    
    Yerel_Bakan "Donovia yadan elçi geldi bizden borç istiyorlar karşılığında bize paralı askerler vericekler ."
    $ dialog_count += 1
    menu:
        "Bu kadar yüklü bir borcu veremeyiz.":
            $ Politics -= 1
            $ check_bars()

        "Tamam hazineden verelim":
            $ Economy -= 4
            $ Politics += 2
            $ Military += 3
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog92:
    show Yerel_Bakan
    
    Yerel_Bakan "Majesteleri, hazinemiz zayıflıyor. Soyluların ve büyük tüccarların daha fazla vergi ödemesi için yeni bir düzenleme yapmalıyız. Eğer onlara fazla yük bindirmek istemezseniz, köylülerden ek vergiler toplayabiliriz."
    $ dialog_count += 1
    menu:
        "Soylular ve Büyük Tüccarlardan alalım vergiyi.":
            $ Economy += 3
            $ Politics -= 2
            $ check_bars()

        "Köylülerden alalım vergiyi.":
            $ People -= 2
            $ Economy += 1
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog93:
    show Yerel_Bakan
    
    Yerel_Bakan "Efendim, sarayda ve taşrada bazı memurlar rüşvet alıyor, halk arasında huzursuzluk artıyor. Yetkilerini kötüye kullanan bürokratları cezalandırmalı ve yeni, güvenilir kişiler atamalıyız."
    $ dialog_count += 1
    menu:
        "Haklısın hemen işe koyul.":
            $ Politics += 1
            $ check_bars()

        "Yiyin birbirinizi.":
            $ Politics -= 1
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog94:
    show Yerel_Bakan
    
    Yerel_Bakan "Kralım, halkımız giderek daha fazla açlık ve kıtlık içinde. Yeni tahıl ambarları kurup yiyecekleri adil dağıtırsak, isyanları önleyebiliriz. Ancak bu, hazineye ek yük getirecektir."
    $ dialog_count += 1
    menu:
        "Halka erzak dağıtalım.":
            $ Economy -= 3
            $ Politics -= 1
            $ People += 3
            $ check_bars()

        "Bu işe girmeyelim.":
            $ People -= 2
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog95:
    show Yerel_Bakan
    
    Yerel_Bakan "Krallığınızda farklı bölgelerde kanunlar farklı işliyor, bazı lordlar kendi hukukunu uyguluyor. Merkezi bir yasa çıkararak otoritenizi pekiştirebiliriz. Ancak soylular bu değişime karşı çıkabilir."
    $ dialog_count += 1
    menu:
        "Yeni yasalar çıkaralım.":
            $ Politics += 1
            $ check_bars()

        "Aynı düzen devam etsin.":
            $ check_bars()
    hide image Yerel_Bakan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog96:
    show Büyücü
    
    Büyücü "Canım biraz para istiyor istersen meclisindekilere kısa süreli bir büyü yapıp Siyaset i 3 arttırabilirim."
    $ dialog_count += 1
    menu:
        "Tamam sana paranı vereceğim.":
            $ Economy -= 2
            $ Politics += 3
            $ Religion -= 2
            $ check_bars()

        "Büyü zırvalıklarına inanmıyorum.":
            $ check_bars()
    hide image Büyücü
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog97:
    show Büyücü
    
    Büyücü "Eğer bana biraz ödeme yaparsan sana büyü yaparım veherşeyi önceden fark edersin."
    $ dialog_count += 1
    menu:
        "Tamam hemen para veriyorum büyü yap.":
            $ Economy -= 2
            $ Religion -= 2
            Büyücü "(Hiçbir şey olmadı)"
            $ check_bars()

        "Böyle bir şeyin olması mümkün değil sana inanmıyorum.":
            $ Religion += 1
            $ check_bars()
    hide image Büyücü
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog98:
    show Büyücü
    
    Büyücü "Majesteleri, Diyanet in bazı mensupları benim karanlık sanatlarla uğraştığımı iddia ediyor ve cezalandırmak istiyor."
    $ dialog_count += 1
    menu:
        "Para cezası verdim.":
            $ Economy += 1
            $ Religion -= 1
            $ check_bars()

        "Onlar haksız bunu konuşacağım.":
            $ Religion -= 2
            $ check_bars()
    hide image Büyücü
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog99:
    show Büyücü
    
    Büyücü "Efendim, son zamanlarda kıtlık arttı. Bunun doğal sebeplerle mi, yoksa bir lanet yüzünden mi olduğunu belirlemem için sizden destek istiyorum."
    $ dialog_count += 1
    menu:
        "Tamam destek olucağım.":
            $ Economy -= 3
            $ check_bars()

        "Sana inanmıyorum.":
            $ Religion += 1
            $ check_bars()
    hide image Büyücü
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog100:
    show Ozan
    
    Ozan "Majesteleri, halkımızı eğlendirmek ve moralini yükseltmek adına büyük bir şenlik düzenlemek istiyoruz. Şenliklerde müzik, hikâyeler ve gösteriler olacak. Halkın sevgisini kazanmak için harika bir fırsat!"
    $ dialog_count += 1
    menu:
        "Halkın bize ihtiyacı var,şenlik düzenlensin.":
            $ Economy -= 2
            $ People += 3
            $ check_bars()

        "Mantıksız, halkın sevgisiyle krallık yönetilmez.":
            $ People -= 2
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog101:
    show Ozan
    
    Ozan "Efendim Taverna ve hanlarda yeteri kadar çalışan yok destek talep ediyorum."
    $ dialog_count += 1
    menu:
        "Tamam destek olacağım.":
            $ Economy -= 1
            $ People += 1
            $ check_bars()

        "İdare edin.":
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog102:
    show Ozan
    
    Ozan "Taciler için Taverna ve Hanlara daha fazla oda lazım."
    $ dialog_count += 1
    menu:
        "Tamam,gerekli yatırımı yapıyorum.":
            $ Economy -= 1
            $ People += 1
            $ Politics += 1
            $ check_bars()

        "İdare edin, şimdilik yeterli.":
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog103:
    show Ozan
    
    Ozan "Ulu Kralım, halkınızın ruhunu ve ahengini güçlendirmek için sarayda bir şiir ve şarkı gecesi düzenleyelim. Böylece hem soylular hem de halk, müzik ve hikâyelerle huzur bulur."
    $ dialog_count += 1
    menu:
        "Düzenleyelim.":
            $ Economy -= 1
            $ People += 1
            $ Politics += 1
            $ check_bars()

        "İdare edin.":
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog104:
    show Ozan
    
    Ozan "Büyük Kralım, sizin ve krallığınızın şanını tüm ülkeye duyurmak için sarayınızın resmî ozanı olmak istiyorum. Destanlar yazıp şanınızı nesilden nesile aktarayım."
    $ dialog_count += 1
    menu:
        "Adımı duymayan kalmasın, sen ozanım ol.":
            $ Economy -= 1
            $ Politics += 2
            $ check_bars()

        "Gereksiz, işine bak.":
            $ Politics -= 1
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog105:
    show Ozan
    
    Ozan "Majesteleri, ordumuzun cesur savaşçıları için destanlar yazıp bunları tüm ülkeye yaymak istiyorum. Böylece askerlerimiz daha büyük bir gurur ve inançla savaşabilir!"
    $ dialog_count += 1
    menu:
        "Ordumuzun cesaretini tüm ülkeye duyur.":
            $ Military += 1
            $ Politics += 1
            $ check_bars()

        "Yazdıkların yeterli.":
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog106:
    show Ozan
    
    Ozan "Büyük Kralım, din adamlarıyla birlikte çalışarak ilahiler ve kutsal şarkılar bestelemek istiyoruz. Böylece halkımızın manevi huzuru artacaktır."
    $ dialog_count += 1
    menu:
        "İlahiler bestelenmeli.":
            $ Religion += 1
            $ People += 1
            $ check_bars()

        "Yeterli, işine bak.":
            $ People -= 1
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog107:
    show Ozan
    
    Ozan "Majesteleri, krallığınızın başarılarını yücelten şarkılar yazıp her köye ve kasabaya yaymak istiyorum. Böylece halkınız sizi daha çok sevecektir."
    $ dialog_count += 1
    menu:
        "Başarılarımızı tüm halka duyur.":
            $ Politics += 1
            $ Economy -= 1
            $ check_bars()

        "Yeterince seviliyorum.Senin popülerliğini kullanmam.":
            $ check_bars()
    hide image Ozan
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog108:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Elbiselerimiz eskidi yeni bir şeyler istiyoruz Kralım."
    $ dialog_count += 1
    menu:
        "Tamam yeni elbiseler alacağım.":
            $ Economy -= 1
            $ check_bars()

        "Şimdilik idare edin.":
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog109:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Bugün saçım nasıl olmuş Kralım?"
    $ dialog_count += 1
    menu:
        "Çok güzel olmuş.":
            $ check_bars()

        "Her zamanki gibi.":
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog110:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Efendim yeni bir saç stili mi istersiniz yoksa yeni bir elbisemi?"
    $ dialog_count += 1
    menu:
        "Yeni bir saç stili istiyorum.":
            $ check_bars()

        "Yeni bir elbise istiyorum.":
            $ Economy -= 1
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog111:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Kralımız bugün nasıllar?"
    $ dialog_count += 1
    menu:
        "Gayet iyi.":
            $ check_bars()

        "Yorgun":
            $ check_bars()
            Hizmetçi_Başı "Bir masaj yapıyım kralım düzelirsiniz."
            
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog112:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Efendim biraz hamama girip rahatlamak istermisiniz?"
    $ dialog_count += 1
    menu:
        "Güzel olur.":
            $ Politics -= 1
            $ check_bars()

        "Bir hizmetçiyle hamama girmem":
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog113:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Efendim soylular bizi zorla dans ettiriyor böyle bir hakları olmamalı."
    $ dialog_count += 1
    menu:
        "Haklısın bunu değiştiriyorum.":
            $ Politics -= 1
            $ People += 1
            $ check_bars()

        "Soylularımla böyle bir konuyu konuşmayacağım.":
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog114:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Kralım, hizmetkârlarınızınaldıkları ücret yetmiyor. Eğer maaşlarını artırırsanız, daha verimli ve sadık çalışırlar."
    $ dialog_count += 1
    menu:
        "Maaşları arttıracağım.":
            $ Economy -= 2
            $ People += 2
            $ check_bars()

        "Ücretlerini artırmam mümkün değil.":
            $ People -= 1
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog115:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Majesteleri, sarayınızın temizlik işleri yetersiz kalıyor. Duvarlar küflenmeye, halılar kokmaya başladı. Daha fazla hizmetkâr ve malzeme almamıza izin verin."
    $ dialog_count += 1
    menu:
        "Tamam, hizmetkârların sayısını arttırabilirsiniz.":
            $ Economy -= 1
            $ Health += 2
            Hizmetçi_Başı "Yuppi, yeni arkadaşlar."
            $ check_bars()

        "Şimdilik idare edin.":
            $ Health -= 2
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return
label dialog116:
    show Hizmetçi_Başı
    
    Hizmetçi_Başı "Kralım, mutfağınızda kullanılan malzemeler bayat ve kalitesiz. Daha iyi ve taze malzemeler almak için bütçemizi artırmalıyız, yoksa hastalıklar baş gösterebilir."
    $ dialog_count += 1
    menu:
        "Tamam, bütçeyi arttıracağım.Temizlik önemli.":
            $ Economy -= 1
            $ Health += 1
            $ check_bars()

        "Yemeklerimiz yeterince iyi.Gereksiz şeyler sorma!!":
            $ Health -= 1
            $ check_bars()
    hide image Hizmetçi_Başı
    
    $ last_dialog= None
    jump random_dialog
    return