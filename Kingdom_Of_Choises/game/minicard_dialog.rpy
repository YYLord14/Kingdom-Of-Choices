label card1: 
    show Gizemli_Adam
    Gizemli_Adam "Eğer bana istediğim ödemeyi yaparsan sana bağlı bir şövalye teşkilatı oluştururum."
    menu:
        "sende kimsin":
            $ check_bars()
        "Ödemeyi kabul ediyorum":
            $ Economy -= 4
            $ knight_of_swan_clan_minicard = 1
            $ check_bars() #knight of the swan minikart
    hide image Gizemli_Adam
label card2:
    show Büyücü
    Büyücü "Biraz paraya ihtiyacım var elimdeki sağlık iksirini seninle paylaşabilirim ne dersin."
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2 # Sağlık iksiri mini kartı
            $ health_potion_minicard = 1
            $ check_bars()
        "İksirlere inanmıyorum":
            $ check-bars()
    hide image Büyücü
label card3:
    show Büyücü
    Büyücü "Biraz paraya ihtiyacım var sana zor zamanlarda yardım edecek bir şeyler öğretebilirim"
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2
            $ black_magic_minicard = 1
            $ check_bars() #Kara büyü kartı
        "Benim büyü ile işim olmaz":
            $ check_bars()
    hide image Büyücü
label card4:
    show Soylu
    Soylu "Aquila Kralı elinizdeki mevcut hazine ile zor zamanlar için bir tahıl ambarı açmalısınız."
    menu:
        "Mantıklı açıyorum":
            $ Economy -= 3
            $ granary_warehouse_minicard = 1
            $ check_bars()
        "Hazineyi kullanmak istemiyorum":
            $ check_bars()
    hide image Soylu
label card5:
    show Muhafız_Başı
    Muhafız_Başı "Efendim bir grup iyi asker sizin hizmetinize girmek istiyorlar. Belli bir ücret karşılığında tabii."
    menu:
        "Evet çağır onları":
            $ Economy -= 3
            $ assassin_leagu_minicard = 1
            $ check_bars()
        "Hayır ihtiyacım yok":
            $ check_bars()
    hide image Muhafız_Başı
label card6:
    show Baş_İmam
    Baş_İmam "Ne vakittir aradığımız kutsal emanetlerin yerini buldum bir ordu ile onları kurtaralım."
    menu:
        "Ordumla yola çıkıyorum hemen":
            $ Military -= 2
            $ holy_relics_minicard = 1
            $ check_bars()
        "Yeterli gücüm yok maalesef":
            $ check_bars()
    hide image Baş_İmam
label card7:
    show Kütüphaneci
    Kütüphaneci "Kralım babanızın kütüphanesinde eski bir kitap buldum belki işinize yarayabilir."
    menu:
        "Ver bakalım":
            $ superior_political_science_book_minicard = 1
            $ check_bars()
        "Sende kalsın":
            $ check_bars()
    hide image Kütüphaneci
label card8:
    show Muhafız_Başı
    Muhafız_Başı "Efendim Krallığınız Yargea ile olan savaşı kazandı gelen ganimeti ne yapalım"
    menu:
        "Zor günler için ayıralım":
            $ spoils_of_war_minicard = 1
            $ check_bars()
        "Bir kısmını orduya bir kısmını hazineye dağıt":
            $ Military += 1
            $ Economy += 1
            $ Politics += 1
            $ check_bars()
    hide image Muhafız_Başı
label card9:
    show Muhafız_Başı
    Muhafız_Başı "Efendim bana bağlı bir grup askeri sizin emrinize vermek istiyorum can güvenliğinizi arttırmak için."
    menu:
        "Tamam ücretlerini ben karşılayacağım":
            $ Economy -= 3
            $ royal_guard_minicard = 1
            $ check_bars()
        "Şuan böyle bir tehdit yok":
            $ check_bars()
    hide image Muhafız_Başı
label card10:
    show Zengin_Tüccar
    Zengin_Tüccar "Sizinle bir anlaşma yapmak istiyorum eğer bana koruma ve maddi destek sağlarsanız Donovia ile ipek ticareti yapalım, karın bir kısmınıda size vereceğim."
    menu:
        "Kabul ediyorum destek vereceğim.":
            $ Economy -= 2
            $ Military -= 2
            $ silk_trade_income_minicard = 1
            $ check_bars()
        "Ben bir Kralım sana ihtiyacım yok":
            $ check_bars()
    hide image Zengin_Tüccar
label card11:
    show Çiftçi
    Çiftçi "Saygı değer Kralım bir mağranın içinde mavi şapkalı mantar bulduk bize ekonomik destek sağlarsanız onları sizin için toplayabiliriz."
    menu:
        "Böyle saçma işlerle huzuruma bir daha çıkma":
            $ People -= 1
            $ check_bars()
        "Tamam destek veriyorum":
            $ Economy -= 1
            $ People += 1
            $ blue_cap_mushroom_minicard = 1
            $ check_bars()
    hide image Çiftçi
label card12:
    show Büyücü
    Büyücü "Biraz paraya ihtiyacım var elimdeki sadakat iksirini seninle paylaşabilirim ne dersin. "
    menu:
        "Kabul ediyorum":
            $ Economy -= 2
            $ Religion -= 2
            $ loyalty_potion_minicard = 1
            $ check_bars()
        "İksirlere inanmıyorum renkli su":
            $ Religion += 1
            $ check_bars()
    hide image Büyücü