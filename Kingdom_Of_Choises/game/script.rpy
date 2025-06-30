# Define ile karakterleri tanımlıyoruz

define Kütüphaneci = Character("Kütüphaneci")
define Demirci = Character("Demirci")
define Baş_İmam = Character("Baş İmam")
define Ozan = Character("Ozan")
define Muhafız_Başı = Character("Muhafız Başı")  
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

default last_dialog = None
#image ile karakterlere bir resim atıyoruz

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
        zoom 0.6
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
        yalign 0.5
    image Yerel_Bakan:
        "yerel_bakan.png"
        zoom 0.55
        yalign 0.2
    image Çiftçi:
        "çiftçi.png"
        zoom 0.8
    image Büyücü:
        "büyücü.png"
        zoom 0.7
    image Gizemli_Adam:
        "gizemli_adam.png"
        zoom 0.7
    image Şifacı:
        "şifacı.png"
        zoom 1.3
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
    
label open_preferences:#Esc on clik to open preferences
    call screen preferences
    return
screen esc_listener():#Esc control
    key "escape" action Call("open_preferences")
    
init: # Başlangıç değerleri
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
    ease 0.5 xsize 395  # Barların geçişlerini akışkan hale getirmek

screen bars():
    vbox:
        xalign 1.0  # Sağ tarafa hizalar
        yalign 0.4  # Ortalar
        spacing 5  # Çubuklar arası boşluk

        text "Sağlık" xalign 0.5  
        frame:
            background None
            xsize 395  
            ysize 30
            bar:
                value Health
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Din" xalign 0.5
        frame:
            background None
            xsize 395  
            ysize 30
            bar:
                value Religion
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Siyaset" xalign 0.5
        frame:
            background None
            xsize 395  
            ysize 30
            bar:
                value Politics
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Askeri" xalign 0.5
        frame:
            background None
            xsize 395  
            ysize 30
            bar:
                value Military
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Ekonomi" xalign 0.5
        frame:
            background None
            xsize 395  
            ysize 30
            bar:
                value Economy
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text "Halk" xalign 0.5
        frame:
            background None
            xsize 395
            ysize 30
            bar:
                value People
                range 10
                xsize 395
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

init:#Tanımlamalar
    $ last_dialog = None
    $ in_game = False
    $ game_over_triggered = False
    $ character_alive = True
    $ chosen_dialog = 0
    $ chr_zero_point = 0
    $ knight_of_swan_clan_minicard = 0
    $ health_potion_minicard = 0
    $ black_magic_minicard = 0
    $ granary_warehouse_minicard = 0
    $ assassin_leagu_minicard = 0
    $ holy_relics_minicard = 0
    $ superior_political_science_book_minicard = 0
    $ spoils_of_war_minicard = 0
    $ royal_guard_minicard = 0
    $ silk_trade_income_minicard = 0
    $ blue_cap_mushroom_minicard = 0
    $ loyalty_potion_minicard = 0

init python:# Gerekli Fonksiyonlar
    def check_bars():
        renpy.pause(0.1)
        for value in [Health,Religion,Politics,Military,Economy,People]:
            if value <= 0 or value >= 10:
                renpy.jump("minicard")

    def zero_chr():
        renpy.hide("Asker")
        renpy.hide("Baş_İmam")
        renpy.hide("Büyücü")
        renpy.hide("Demirci")
        renpy.hide("Hizmetçi Başı")
        renpy.hide("Kadı")
        renpy.hide("Kütüphaneci")
        renpy.hide("Muhafız Başı")
        renpy.hide("Ozan")
        renpy.hide("Soylu")
        renpy.hide("Yerel Bakan")
        renpy.hide("Zengin Tüccar")
        renpy.hide("Çiftçi")
        renpy.hide("Şifacı")

label zero_point:#0 noktası
    $ dialog_count = 0
    $ Economy = 5
    $ Politics = 5
    $ Military = 5
    $ Religion = 5
    $ Health = 5
    $ People = 5
    $ last_dialog = None
    jump in_start

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.9  # Seçenekleri ekranın altına taşır.
        spacing 10

        for item in items:
            textbutton item.caption action item.action

label game_over:
    $ zero_chr()
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
            "Olamaz":
                hide image Otacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 

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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
            "Neler oluyor?":
                hide image Şifacı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
            "Ne?":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
                    
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
            "Ne oluyor":
                hide image Baş_İmam
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  

    elif Politics <= 0:
        
        show Yerel_Bakan at Position(xalign=0.5, yalign=0.1)
        Yerel_Bakan "Kralım meclis üyeleri sizi sattı."
        menu:
            "Nasıl olur?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
            "Hayır!":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
    elif Politics >= 10:
        
        show Yerel_Bakan at Position(xalign=0.5, yalign=0.1)
        Yerel_Bakan "Kralım artık zamanın doldu."
        menu:
            "Ne oluyor?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
            "Ne?":
                hide image Yerel_Bakan
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.4)
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin." 
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
            "Hayır!":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
            "Ne saçmalıyorsun?":
                hide image Muhafız_Başı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
    elif Economy <= 0:
        
        show Soylu at Position(xalign=0.5, yalign=0.3)
        Soylu "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
        menu:
            "Olamaz!":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Ne?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
    elif Economy >= 10:
        
        show Soylu at Position(xalign=0.5, yalign=0.3)
        Soylu "Kralım artık sizi başımızda istemiyoruz."
        menu:
            "Ne saçmalıyorsun sen?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
            "Aklınımı kaçırdın?":
                hide image Soylu
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()  
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
            "Ne oluyor?":
                hide image Kadı
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 
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
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit()
            "Aklınımı kaçırdın?":
                hide image Çiftçi
                show Gizemli_Adam at Position(xalign=0.5, yalign=0.7)
                Gizemli_Adam "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz." 
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point  
                    "Çık":
                        $ renpy.quit() 

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
        if spoils_of_war_minicard > 0:
            $ Economy += 3
            $ spoils_of_war_minicard -= 1
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
        if spoils_of_war_minicard > 0:
            $ People += 3
            $ spoils_of_war_minicard -= 1
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
            $ holy_relics_minicard -= 1
            $ check_bars()
            return
        elif royal_guard_minicard > 0:
            $ People -= 3
            $ royal_guard_minicard -= 1
            $ check_bars()
            return
        else :
            jump game_over

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

init python:# Minicard diyolglar
    import random

    minicard_dialogs = [
        "card1", "card2", "card3", "card4", 
        "card5", "card6", "card7", "card8",
        "card9", "card10", "card11", "card12"
    ]
    
    minicard_used = False

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
    jump zero_point
    label in_start:
        $ in_game = True
        show screen esc_listener
        while True:
            if last_dialog == None:
                $ chosen_dialog = get_random_dialog()  # Yeni bir rastgele diyalog al
                $ last_dialog = chosen_dialog
            else :
                $ chosen_dialog = last_dialog
            jump expression chosen_dialog
    
label check_minicard: #bunun yeri ile oynamayın rasgele minicard dialogu atıyor
    if dialog_count == 20 and not minicard_used:
        $ chosen_card = renpy.random.choice(minicard_dialogs)
        $ minicard_used = True 
        jump expression chosen_card
    else:
        jump random_dialog


label random_dialog:
    $ chosen_dialog = renpy.random.choice(dialogs)  # Yeni rastgele diyalog seç
    $ last_dialog = chosen_dialog
    jump expression chosen_dialog  # Yeni seçilen diyaloga git
