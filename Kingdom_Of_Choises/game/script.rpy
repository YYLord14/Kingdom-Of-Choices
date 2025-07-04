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

#image ile karakterlere bir resim atıyoruz

init:     
    image Asker:
        "asker.png"
        zoom 0.35
        xalign 0.5
        yalign 0.3
    image Kütüphaneci:
        "kütüphaneci.png"
        zoom 0.35
        xalign 0.5
        yalign 0.4
    image Demirci:
        "demirci.png"
        zoom 0.35
        xalign 0.5
        yalign 0.5
    image Baş_İmam:
        "bas_imam.png"
        zoom 0.3
        xalign 0.5
        yalign 0.3
    image Ozan:
        "ozan.png"
        zoom 0.55
        xalign 0.5
        yalign 0.1
    image Muhafız_Başı:
        "muhafız_basi.png"
        zoom 0.35
        xalign 0.5
        yalign 0.5
init:
    image Kadı:
        "Kadı.png"
        zoom 0.3
        xalign 0.5
        yalign 0.4
    image Soylu:
        "soylu.png"
        zoom 0.45
        xalign 0.5
        yalign 0.2
    image Yerel_Bakan:
        "yerel_bakan.png"
        zoom 0.55
        xalign 0.5
        yalign 0.35   
    image Çiftçi:
        "çiftçi.png"
        zoom 0.4
        xalign 0.5
        yalign 0.05
    image Büyücü:
        "büyücü.png"
        zoom 0.35
        xalign 0.5
        yalign 0.4
    image Gizemli_Adam:
        "gizemli_adam.png"
        zoom 0.25
        xalign 0.5
        yalign 0.2
    image Şifacı:
        "şifacı.png"
        zoom 0.35
        xalign 0.5
        yalign 0.3
    image Zengin_Tüccar:
        "zengin_tüccar.png"
        zoom 0.35
        xalign 0.5
        yalign 0.4
init:
    image Otacı:
        "Otacı.png"
        zoom 0.35
        xalign 0.5
        yalign 0.6
    image Hizmetçi_Başı:
        "hizmetci_basi.png"
        zoom 0.25
        xalign 0.5
        yalign 0.2
    image startbcg :
        "game_start_bgd.jpg"
        size(config.screen_width, config.screen_height)
    image style_start :
        "gui/overlay/style_start.png"
        size(config.screen_width,100)
        yalign 0.0

label open_preferences:#Esc on clik to open preferences
    call screen preferences
    return
screen esc_listener():#Esc control
    key "escape" action Call("open_preferences")

transform Demirci:
    xalign 0.5
    yalign 0.5
transform Ozan:
    xalign 0.5
    yalign 0.1
transform Muhafız_Başı:
    xalign 0.5
    yalign 0.5
transform Asker:
    xalign 0.5
    yalign 0.3
transform Çiftçi:
    xalign 0.5
    yalign 0.05
transform Baş_İmam:
    xalign 0.5
    yalign 0.3
transform Zengin_Tüccar:
    xalign 0.5
    yalign 0.4
transform Yerel_Bakan:
    xalign 0.5
    yalign 0.35
transform Soylu:
    xalign 0.5
    yalign 0.2
transform Kadı:
    xalign 0.5
    yalign 0.4
transform Şifacı:
    xalign 0.5
    yalign 0.3
transform Hizmetçi_Başı:
    xalign 0.5
    yalign 0.2
transform Büyücü:
    xalign 0.5
    yalign 0.4
transform Kütüphaneci:
    xalign 0.5
    yalign 0.4
transform Otacı:
    xalign 0.5
    yalign 0.6
transform Gizemli_Adam:
    xalign 0.5
    yalign 0.2

## Tarih kodları ################################################################
default current_date = {
    "day": 24,
    "month": 2,
    "year": 1224,
    "month_names": {
        1: "Ocak",
        2: "Şubat",
        3: "Mart",
        4: "Nisan",
        5: "Mayıs",
        6: "Haziran",
        7: "Temmuz",
        8: "Ağustos",
        9: "Eylül",
        10: "Ekim",
        11: "Kasım",
        12: "Aralık"
    }
}

init python:
    

    def format_date():
        return f"{current_date['day']} {current_date['month_names'][current_date['month']]} {current_date['year']}"

    def managed_day(days_to_add):
        # Ay günlerini belirle (Artık yılları hesaba katmıyoruz)
        month_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        # Günleri ekle
        current_date["day"] += days_to_add
        
        # Ay ve yıl ilerlemesi
        while current_date["day"] > month_days[current_date["month"]]:
            current_date["day"] -= month_days[current_date["month"]]
            current_date["month"] += 1
            
            if current_date["month"] > 12:
                current_date["month"] = 1
                current_date["year"] += 1
 
screen date_display():
    text "{color=#FFFFFF}[current_date['day']]  [current_date['month_names'][current_date['month']]]\n   {color=#FFFFFF}[current_date['year']]{/color}":
        xpos 105
        ypos 60
        size 18
        line_spacing 5

init: # Başlangıç değerleri
    $ Health = 5
    $ Religion = 5
    $ Politics = 5
    $ Military = 5
    $ Economy = 5
    $ People = 5


####### sayaçlar ############################
default dialog_count = 0
default day_managed = managed_day
default minicard_count = 0
default main_story_count = 0

# Diyalog sayısını gösterecek ekran
screen managed_day():
    text "Yönetilen Gün: [dialog_count]":
        xpos 90
        ypos 115
        color "#FFFFFF"
        size 15



transform bar_animation:
    ease 0.5 xsize 400  # Barların geçişlerini akışkan hale getirmek

screen bars():
    vbox:
        xalign 1.0  # Sağ tarafa hizalar
        yalign 0.4  # Ortalar
        spacing 5  # Çubuklar arası boşluk

        text "Sağlık" xalign 0.5  
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Health
                range 10
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

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
    $ last_dialog = None
    $ in_game = False
    $ game_over_triggered = False
    $ character_alive = True
    $ chosen_dialog = 0
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

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.9  # Seçenekleri ekranın altına taşır.
        spacing 10

        for item in items:
            textbutton item.caption action item.action

label zero_point:#0 noktası
    $ dialog_count = 0
    $ day_managed = 1
    $ minicard_count = 0
    $ main_story_count = 0
    $ Economy = 5
    $ Politics = 5
    $ Military = 5
    $ Religion = 5
    $ Health = 5
    $ People = 5
    jump in_start

init python:# Bağımsız fonksiyonlar //Check_bars and zero_chr_button
    def check_bars():
        for value in [Health,Religion,Politics,Military,Economy,People]:
            if value <= 0 or value >= 10:
                renpy.jump("minicard")
        
    
    def zero_chr_button():
        renpy.hide_screen("chr_button_asker")
        renpy.hide("Asker")
        renpy.hide_screen("chr_button_baş_imam")
        renpy.hide("Baş İmam")
        renpy.hide_screen("chr_button_büyücü")
        renpy.hide("Büyücü")
        renpy.hide_screen("chr_button_demirci")
        renpy.hide("Demirci")
        renpy.hide_screen("chr_button_hizmetci")
        renpy.hide("Hizmetçi Başı")
        renpy.hide_screen("chr_button_kadı")
        renpy.hide("Kadı")
        renpy.hide_screen("chr_button_kütüphaneci")
        renpy.hide("Kütüphaneci")
        renpy.hide_screen("chr_button_muhafız_başı")
        renpy.hide("Muhafız Başı")
        renpy.hide_screen("chr_button_ozan")
        renpy.hide("Ozan")
        renpy.hide_screen("chr_button_soylu")
        renpy.hide("Soylu")
        renpy.hide_screen("chr_button_yerel_bakan")
        renpy.hide("Yerel Bakan")
        renpy.hide_screen("chr_button_zengin_tüccar")
        renpy.hide("Zengin Tüccar")
        renpy.hide_screen("chr_button_çiftçi")
        renpy.hide("Çiftçi")
        renpy.hide_screen("chr_button_şifacı")
        renpy.hide("Şifacı")

label game_over:
    scene startbcg
    $ zero_chr_button()
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
        "dialog11", "dialog12", "dialog13", "dialog14", "dialog15"
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
    show screen style_start
    show screen sign_hist
    show screen map_button
    show screen run_button
    show screen setting_button
    show screen character_button
    show screen minicard_button
    scene startbcg
    show screen managed_day
    show screen date_display
    
    $ character_alive=True
    label in_start:
        while True:
            $ in_game = True
            show screen esc_listener
            if last_dialog == None:
                $ zero_chr_button()
                $ chosen_dialog = get_random_dialog()  # Yeni bir rastgele diyalog al
                $ last_dialog = chosen_dialog
            else :
                $ zero_chr_button()
                $ chosen_dialog = last_dialog
            jump expression chosen_dialog

   

label check_minicard: #bunun yeri ile oynamayın rastgele minicard dialogu atıyor
    if dialog_count == 15 and not minicard_used:
        $ chosen_card = renpy.random.choice(minicard_dialogs)
        $ minicard_used = True 
        jump expression chosen_card
    else:
        jump random_dialog


label random_dialog:
    $ chosen_dialog = renpy.random.choice(dialogs)  # Yeni rastgele diyalog seç
    jump expression chosen_dialog  # Yeni seçilen diyaloga git
