define Kütüphaneci = Character("Kütüphaneci")
define Demirci = Character("Demirci")
define Baş_İmam = Character("Baş İmam")
define Ozan = Character("Ozan")
define Muhafız_Başı = Character("Muhafız Başı")  # define ile karakterleri tanımlıyoruz
define Kadı = Character("Kadı")
define Asker = Character("Asker")
define Çiftçi = Character("Çiftçi")
define Zengin_Tüccar = Character("Zengin Tüccar")
define Yerel_Bakan = Character("Yerel Bakan")
define Soylu = Character("Soylu")
define Gizemli_Adam = Character("Gizemli Adam")
define Büyücü = Character("Büyücü")
define Otacı = Character("Otacı")
define Şifacı = Character("Şifacı")
define Hizmetçi_Başı = Character("Hizmetçi Başı")

init:
    image Asker:
        "asker.png"
        zoom 0.65
    image Kütüphaneci:
        "kütüphaneci.png"
        zoom 0.7
    image Demirci:
        "demirci.png"
        zoom 0.7
    image Baş_İmam:
        "bas_imam.png"
        zoom 0.7
    image Ozan:
        "ozan.png"
        zoom 0.7
    image Muhafız_Başı:
        "muhafız_basi.png"
        zoom 0.7                               
init:
    image Kadı:
        "Kadı.png"
        zoom 0.7
    image Soylu:
        "soylu.png"
        zoom 0.8
    image Yerel_Bakan:
        "yerel_bakan.png"
        zoom 0.7
    image Çiftçi:
        "çiftçi.png"
        zoom 1.2
    image Büyücü:
        "büyücü.png"
        zoom 0.8
    image Gizemli_Adam:
        "gizemli_adam.png"
        zoom 0.7
    image Şifacı:
        "şifacı.png"
        zoom 0.7
    image Zengin_Tüccar:
        "zengin_tüccar.png"
        zoom 0.7
init:
    image Otacı:
        "Otacı.png"
        zoom 0.7
    image Hizmetçi_Başı:
        "hizmetci_basi.png"
        zoom 0.7
    image startbcg :
        "game_start_bgd.png"
        size(config.screen_width, config.screen_height)
    

init:
    $ Health = 5
    $ Religion = 5
    $ Politics = 5
    $ Military = 5
    $ Economy = 5
    $ People = 5
# Diyalog sayısının başlatılması
default dialog_count = 0

# Diyalog sayısını gösterecek ekran
screen dialog_counter():
    text "Diyalog Sayısı: [dialog_count]" xpos 20 ypos 50 color "#FFFFFF"


transform bar_animation:
    ease 0.5 xsize 400  # Barların geçişlerini akışkan hale getirmek

screen bars():
    vbox:
        xalign 1.0  # Sağ tarafa hizalar
        yalign 0.4  # Ortalar
        spacing 5  # Çubuklar arası boşluk

        text "Sağlık" xalign 0.5  
        frame:  #herşeyin oturtulcağı yeri ayarlar.
            background None
            xsize 400  
            ysize 30
            bar:
                value Health
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000") #Dolan barı kırmızı gösterir.
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5) #Kenarlık gösterir.

        text "Din" xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Religion
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Siyaset" xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Politics
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Askeri" xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Military
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Ekonomi" xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Economy
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Halk" xalign 0.5
        frame:
            background None
            xsize 400
            ysize 30
            bar:
                value People
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

init:#Tanımlamalar
    $ game_over_triggered = False
    $ character_alive = True
    $ knight_of_swan_clan_minicard = 0
    $ health_potion_minicard = 0
    $ black_magic_minicard = 0
    $ granary_warehouse_minicard = 0
    $ assassin_leagu_minicard = 0
    $ holy_relics_minicard = 0
    $ superior_political_science_book_minicard = 0
    $ spoils_of_ar_minicard = 0
    $ royal_guard_minicard = 0
    $ silk_trade_income_minicard = 0
    $ blue_cap_mushroom_minicard = 0
    $ loyalty_potion_minicard = 0

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.9  # Seçenekleri ekranın altına taşır.
        spacing 10

        for item in items:
            textbutton item.caption action item.action

label zero_point:
    $ dialog_count = 0
    $ Economy = 5
    $ Politics = 5
    $ Military = 5
    $ Religion = 5
    $ Health = 5
    $ People = 5
    jump start

label game_over:
    scene startbcg
    if not game_over_triggered:
        $ game_over_triggered = True
        $ character_alive=False
    if Health <= 0: 
        show Otacı at Position(xalign=0.5, yalign=0.9) 
        Otacı "Kralım bulaşıcı bir hastalık çıktı ve engel olamıyoruz."
        menu:
            "Ne?":
                hide image Otacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 
            "Olamaz":
                hide image Otacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 

    elif Health >= 10:
        show Şifacı at Position(xalign=0.5, yalign=0.9) 
        Şifacı "Kralım araştırma bölgelerimizin birinde bir hata yaptık." 
        menu:
            "Ne hatası?":
                hide image Şifacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 
            "Neler oluyor?":
                hide image Şifacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 
    elif Religion <= 0:
        
        show Baş_İmam at Position(xalign=0.5, yalign=0.9) 
        Baş_İmam "Kralım siz doğru yoldan ayrıldınız."
        menu:
            "Neler oluyor?":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 
            "Ne?":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        return 
                    
    elif Religion >= 10:
        
        show Baş_İmam at Position(xalign=0.5, yalign=0.9) 
        Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
        menu:
            "Ne diyosun be":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
            "Ne oluyor":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  

    elif Politics <= 0:
        
        show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
        Yerel_Bakan "Kralım meclis üyeleri sizi sattı."
        menu:
            "Nasıl olur?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
            "Hayır!":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
    elif Politics >= 10:
        
        show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
        Yerel_Bakan "Kralım artık zamanın doldu."
        menu:
            "Ne oluyor?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
            "Ne?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin." 
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
    elif Military <= 0:
        
        show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
        Muhafız_Başı "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
        menu:
            "Olamaz!":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
            "Hayır!":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 
    elif Military >= 10:
        
        show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
        Muhafız_Başı "Kralım artık sizin bir yetkiniz kalmadı."
        menu:
            "Ne?":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 
            "Ne saçmalıyorsun?":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return
    elif Economy <= 0:
        
        show Soylu at Position(xalign=0.5, yalign=0.5)
        Soylu "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
        menu:
            "Olamaz!":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        $ game_over_triggered = False  # Bitiş ekranı sıfırlansın
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()
                        return 
            "Ne?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 
    elif Economy >= 10:
        
        show Soylu at Position(xalign=0.5, yalign=0.5)
        Soylu "Kralım artık sizi başımızda istemiyoruz."
        menu:
            "Ne saçmalıyorsun sen?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return
            "Aklınımı kaçırdın?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return  
    elif People <= 0:
        
        show Kadı at Position(xalign=0.5, yalign=0.9)
        Kadı "Kralım halktan çalarak yönettiğiniz bu düzen bozuldu."
        menu:
            "Ne?":
                hide image Kadı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 
            "Ne oluyor?":
                hide image Kadı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 
    elif People >= 10:
        
        show Çiftçi at Position(xalign=0.5, yalign=0.9)
        Çiftçi "Kralım o tahtı hak etmiyorsunuz."
        menu:
            "Ne saçmalıyorsun sen?":
                hide image Çiftçi
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz."
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return
            "Aklınımı kaçırdın?":
                hide image Çiftçi
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz." 
                menu:
                    "Yeniden başla":
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
                        return 

label minicard:
    if Health <= 0:
        if blue_cap_mushroom_minicard > 0:
            $ Health += 3
            $ blue_cap_mushroom_minicard -= 1
            $ check_bars()
            return
        elif health_potion_minicard > 0:
            $ Health += 3
            $ health_potion_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Health >= 10:
        if health_potion_minicard > 0:
            $ Health -= 3
            $ health_potion_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Religion <= 0:
        if holy_relics_minicard > 0:
            $ Religion += 3
            $ holy_relics_minicard -= 1
            $ check_bars()
            return
        elif knight_of_swan_clan_minicard > 0:
            $ Religion += 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Religion >= 10:
        if loyalty_potion_minicard > 0:
            $ Religion -= 3
            $ loyalty_potion_minicard -= 1
            $ check_bars()
            return
        elif holy_relics_minicard > 0:
            $ Religion -= 3
            $ holy_relics_minicard -= 1
            $ check_bars()
            return
        elif assassin_leagu_minicard > 0:
            $ Religion -= 3
            $ assassin_leagu_minicard -= 1
            $ check_bars()
            return
        elif knight_of_swan_clan_minicard > 0:
            $ Religion -= 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Politics <= 0:
        if superior_political_science_book_minicard > 0:
            $ Politics += 3
            $ superior_political_science_book_minicard -= 1
            $ check_bars()
            return
        elif knight_of_swan_clan_minicard > 0:
            $ Politics += 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Politics >= 10:
        if assassin_leagu_minicard > 0:
            $ Politics -= 3
            $ assassin_leagu_minicard -= 1
            $ check_bars()
            return
        elif black_magic_minicard > 0:
            $ Politics -= 3
            $ black_magic_minicard -= 1
            $ check_bars()
            return
        elif royal_guard_minicard > 0:
            $ Politics -= 3
            $ royal_guard_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Military <= 0:
        if royal_guard_minicard > 0:
            $ Military += 3
            $ royal_guard_minicard -= 1
            $ check_bars()
            return
        elif black_magic_minicard > 0:
            $ Military += 3
            $ black_magic_minicard -= 1
            $ check_bars()
            return
        elif knight_of_swan_clan_minicard > 0:
            $ Military += 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Military >= 10:
        if knight_of_swan_clan_minicard > 0:
            $ Military -= 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        elif black_magic_minicard > 0:
            $ Military -= 3
            $ black_magic_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Economy <= 0:
        if spoils_of_ar_minicard > 0:
            $ Economy += 3
            $ spoils_of_ar_minicard -= 1
            $ check_bars()
            return
        elif silk_trade_income_minicard > 0:
            $ Economy += 3
            $ silk_trade_income_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif Economy >= 10:
        if granary_warehouse_minicard > 0:
            $ People += 3
            $ granary_warehouse_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif People <= 0:
        if spoils_of_ar_minicard > 0:
            $ People += 3
            $ spoils_of_ar_minicard -= 1
            $ check_bars()
            return
        elif granary_warehouse_minicard > 0:
            $ People += 3
            $ granary_warehouse_minicard -= 1
            $ check_bars()
            return
        else:
            jump game_over

    elif People >= 10:
        if knight_of_swan_clan_minicard > 0:
            $ People -= 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        elif holy_relics_minicard > 0:
            $ People -= 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        elif royal_guard_minicard > 0:
            $ People -= 3
            $ knight_of_swan_clan_minicard -= 1
            $ check_bars()
            return
        elif :
            jump game_over

init python:# Barların kontrol edilmesi
    def check_bars():
        if Health <= 0 or Health >= 10:
            renpy.jump("minicard")
        elif Religion <= 0 or Religion >= 10:
            renpy.jump("minicard")
        elif Politics <= 0 or Politics >= 10:
            renpy.jump("minicard")
        elif Military <= 0 or Military >= 10:
            renpy.jump("minicard")
        elif Economy <= 0 or Economy >= 10:
            renpy.jump("minicard")
        elif People <= 0 or People >= 10:
            renpy.jump("minicard")

init python:# Diyologlar
    import random

    # Tüm diyalogları bir liste içine koyuyoruz
    dialogs = [
        "dialog1", "dialog2", "dialog3", "dialog4", "dialog5",
        "dialog6", "dialog7", "dialog8", "dialog9", "dialog10",
        "dialog11", "dialog12", "dialog13", "dialog14", "dialog15",
        "dialog16", "dialog17", "dialog18", "dialog19", "dialog20",
        "dialog21", "dialog22", "dialog23", "dialog24", "dialog25",
        "dialog26", "dialog27", "dialog28", "dialog29", "dialog30",
        "dialog31", "dialog32", "dialog33", "dialog34", "dialog35",
        "dialog36", "dialog37", "dialog38", "dialog39", "dialog40",
        "dialog41", "dialog42", "dialog43", "dialog44", "dialog45",
        "dialog46", "dialog47", "dialog48", "dialog49", "dialog50",
        "dialog51", "dialog52", "dialog53", "dialog54", "dialog55",
        "dialog56", "dialog57", "dialog58", "dialog59", "dialog60",
        "dialog61", "dialog62", "dialog63", "dialog64", "dialog65",
        "dialog66", "dialog67", "dialog68", "dialog69", "dialog70",
        "dialog71", "dialog72", "dialog73", "dialog74", "dialog75",
        "dialog76", "dialog77", "dialog78", "dialog79", "dialog80",
        "dialog81", "dialog82", "dialog83", "dialog84", "dialog85",
        "dialog86", "dialog87", "dialog88", "dialog89", "dialog90",
        "dialog91", "dialog92", "dialog93", "dialog94", "dialog95",
        "dialog96", "dialog97", "dialog98", "dialog99", "dialog100",
        "dialog101", "dialog102", "dialog103", "dialog104", "dialog105",
        "dialog106", "dialog107", "dialog108", "dialog109", "dialog110",
        "dialog111", "dialog112", "dialog113", "dialog114", "dialog115",
        "dialog116"
    ]

    def get_random_dialog():
        return random.choice(dialogs)  # Rastgele bir diyalog seçiyoruz


label start:
    stop music
    queue music[
        "audio/Bleak_Falls.mp3",
        "audio/Lake_of_Light.mp3",
        "audio/Rite_of_the_Fading_Light.mp3"] loop
    show screen bars
    scene startbcg
    show screen dialog_counter
    $ character_alive=True
    while True:
        $ chosen_dialog = get_random_dialog()  # Yeni bir rastgele diyalog al
        jump expression chosen_dialog

label dialog1:
    show Demirci at Position(xalign=0.5, yalign=0.9) 
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
    jump random_dialog
label dialog2:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog3:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog4:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog5:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog6:
    show Baş_İmam at Position(xalign=0.4, yalign=0.5)
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
    jump random_dialog
label dialog7:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog8:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog9:
    show Soylu at Position(xalign=0.5, yalign=0.6)
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
    jump random_dialog
label dialog10:
    show Kadı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog11:
    show Şifacı at Position(xalign=0.5, yalign=1)
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
    jump random_dialog
label dialog12:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog14:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog15:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog16:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog17:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.8)
    Muhafız_Başı "Efendim asker sayımız çok fazla bazılarını size koruma olarak verebilirim"
        
    menu: 
        "Yeterli muhafızım var":
            $ check_bars()
        "Olur ver bakalım":
            $ Military -= 1
            $ check_bars()
    hide image Muhafız_Başı
    jump random_dialog
label dialog18:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog19:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog20:
    show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog21:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog22:
    show Kadı at Position(xalign=0.5, yalign=0.8)
    Kadı "Efendim, şehirdeki zengin bir tüccar, ödediği vergilerin haksız olduğunu iddia ediyor .Eğer bu konu çözülemezse, diğer tacirler de aynı yola başvurabilir."
    $ dialog_count += 1
    menu:
        "Oda herkes gibi vergisini ödemeli.":
            $ check_bars()
        "Oda herkes gibi vergisini ödemeli.":
            $ Economy -= 1
            $ check_bars()
    hide image Kadı
    jump random_dialog
label dialog23:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog24:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog25:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog26:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog27:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog28:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog29:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog30:
    show Kadı at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog31:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog32:
      show Muhafız_Başı at Position(xalign=0.5, yalign=0.9)
    Muhafız_Başı "Efendim bir grup iyi asker sizin hizmetinize girmek istiyorlar. Belli bir ücret karşılığında tabii."
    $ dialog_count += 1
    menu:
        "Evet çağır onları.":
            $ Economy -= 3
            $ assassin_leagu_minicard = 1
            $ check_bars()

        "Hayır ,muhafızlarım gayet yeterli.":
            $ check_bars()
    hide image Muhafız_Başı
    jump random_dialog
  
label dialog33:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog34:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog35:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog36:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog37:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog38:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog39:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog40:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog41:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog42:
    show Çiftçi at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog43:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
    Baş_İmam "Topladığımız paralardan artanları getirdim hazineye koyalım"
    $ dialog_count += 1
    menu:
        "Olur koyalım":
            $ Economy += 2
            $ check_bars()

        "Halka dağıtalım":
            $ Religion += 1
            $ People += 1
            $ check_bars()
    hide image Baş_İmam
    jump random_dialog
label dialog44:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog45:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog46:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog47:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog48:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog49:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog50:
    show Baş_İmam at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog51:
    show Soylu at Position(xalign=0.5, yalign=0.5)
    Soylu "Aquila Kralı elinizdeki mevcut hazine ile zor zamanlar için bir tahıl ambarı açmalısınız."
    $ dialog_count += 1
    menu:
        "Mantıklı açıyorum tahıl ambarını.":
            $ Economy -= 3
            $ check_bars()
        "Hazineyi kullanmak istemiyorum.":
            $ check_bars()
    hide image Soylu
    jump random_dialog
label dialog52:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog53:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog54:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog55:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog56:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog57:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog58:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog59:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog60:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog61:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog62:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog63:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog64:
    show Soylu at Position(xalign=0.5, yalign=0.5)
    Soylu "Efendim, danışmanlarınız arasında daha fazla söz hakkına sahip olmalıyım. Kraliyet konseyinizde bana bir yer verirseniz, tecrübemle kararlarınıza rehberlik edebilirim."
    $ dialog_count += 1
    menu:
        "Kraliyet konseyine alıyorum.":
            $ Politics -= 2
            $ check_bars()

        "Kraliyet konseyine almam söz konusu bile olamaz.":
            $ check_bars()
    hide image Soylu
    jump random_dialog
label dialog65:
    show Soylu at Position(xalign=0.5, yalign=0.5)
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
    jump random_dialog
label dialog66:
    show Asker at Position(xalign=0.5, yalign=0.8)
    Asker "Saygı değer Kralım talimler çok fazla sayısını azaltmalısınız. Bu durumda ne yapacaksınız?"
    $ dialog_count += 1
    menu:
        "Muhafız başı ile konuşacağım.":
            $ Military -= 1
            $ check_bars()

        "Gerek görmüyorum.":
            $ check_bars()
    hide image Asker
    jump random_dialog
label dialog67:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog68:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog69:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog70:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog71:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog72:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog73:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog74:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog75:
    show Asker at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog76:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
    Zengin_Tüccar "Elimde çok değerli bir tarihi eser var bunu almak isteyebilirsiniz."
    $ dialog_count += 1
    menu:
        "Tamam alıyorum.":
            $ Economy -= 2
            $ check_bars()

        "Ben böyle şeylere para harcamam.":
            $ check_bars()
    hide image Zengin_Tüccar
    jump random_dialog
label dialog77:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog78:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
    Zengin_Tüccar "Yargea dan geldim elimde güzel deriler var bakmak istemisin."
    $ dialog_count += 1
    menu:
        "Tamam alıyorum.":
            $ Economy -= 1
            $ check_bars()

        "saçma şeylere para harcamam.":
            $ check_bars()
    hide image Zengin_Tüccar
    jump random_dialog
label dialog79:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog80:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog81:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog82:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog83:
    show Zengin_Tüccar at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog84:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog85:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog86:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog87:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog88:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog89:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog90:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog91:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog92:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog93:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog94:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
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
    jump random_dialog
label dialog95:
    show Yerel_Bakan at Position(xalign=0.5, yalign=0.3)
    Yerel_Bakan "Krallığınızda farklı bölgelerde kanunlar farklı işliyor, bazı lordlar kendi hukukunu uyguluyor. Merkezi bir yasa çıkararak otoritenizi pekiştirebiliriz. Ancak soylular bu değişime karşı çıkabilir."
    $ dialog_count += 1
    menu:
        "Yeni yasalar çıkaralım.":
            $ Politics += 1
            $ check_bars()

        "Aynı düzen devam etsin.":
            $ check_bars()
    hide image Yerel_Bakan
    jump random_dialog
label dialog96:
    show Büyücü at Position(xalign=0.5, yalign=0.4)
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
    jump random_dialog
label dialog97:
    show Büyücü at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog98:
    show Büyücü at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog99:
    show Büyücü at Position(xalign=0.5, yalign=0.8)
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
    jump random_dialog
label dialog100:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog101:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog102:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog103:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog104:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog105:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog106:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog107:
    show Ozan at Position(xalign=0.5, yalign=0.9)
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
    jump random_dialog
label dialog108:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
    Hizmetçi_Başı "Elbiselerimiz eskidi yeni bir şeyler istiyoruz Kralım."
    $ dialog_count += 1
    menu:
        "Tamam yeni elbiseler alacağım.":
            $ Economy -= 1
            $ check_bars()

        "Şimdilik idare edin.":
            $ check_bars()
    hide image Hizmetçi_Başı
    jump random_dialog
label dialog109:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
    Hizmetçi_Başı "Bugün saçım nasıl olmuş Kralım?"
    $ dialog_count += 1
    menu:
        "Çok güzel olmuş.":
            $ check_bars()

        "Her zamanki gibi.":
            $ check_bars()
    hide image Hizmetçi_Başı
    jump random_dialog
label dialog110:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
    Hizmetçi_Başı "Efendim yeni bir saç stili mi istersiniz yoksa yeni bir elbisemi?"
    $ dialog_count += 1
    menu:
        "Yeni bir saç stili istiyorum.":
            $ check_bars()

        "Yeni bir elbise istiyorum.":
            $ Economy -= 1
            $ check_bars()
    hide image Hizmetçi_Başı
    jump random_dialog
label dialog111:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
    Hizmetçi_Başı "Kralımız bugün nasıllar?"
    $ dialog_count += 1
    menu:
        "Gayet iyi.":
            $ check_bars()

        "Yorgun":
            $ check_bars()
            Hizmetçi_Başı "Bir masaj yapıyım kralım düzelirsiniz."
            
    hide image Hizmetçi_Başı
    jump random_dialog
label dialog112:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
    Hizmetçi_Başı "Efendim biraz hamama girip rahatlamak istermisiniz?"
    $ dialog_count += 1
    menu:
        "Güzel olur.":
            $ Politics -= 1
            $ check_bars()

        "Bir hizmetçiyle hamama girmem":
            $ check_bars()
    hide image Hizmetçi_Başı
    jump random_dialog
label dialog113:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
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
    jump random_dialog
label dialog114:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
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
    jump random_dialog
label dialog115:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
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
    jump random_dialog
label dialog116:
    show Hizmetçi_Başı at Position(xalign=0.5, yalign=0.4)
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
    jump random_dialog

label random_dialog: # bu label daima dialog label larından sonra olacak şekilde yerleştirilmedilir
    $ chosen_dialog = renpy.random.choice(dialogs)  # Yeni rastgele diyalog seç
    jump expression chosen_dialog  # Yeni seçilen diyaloga git
