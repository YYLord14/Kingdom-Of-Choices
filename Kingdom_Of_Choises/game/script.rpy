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
define Kraliçe = Character("Kraliçe")
#image ile karakterlere bir resim atıyoruz
init:     
    image Asker:
        "asker.png"
        zoom 0.85
        
    image Kütüphaneci:
        "kütüphaneci.png"
        zoom 0.85
        
    image Demirci:
        "demirci.png"
        zoom 0.8
       
    image Baş_İmam:
        "bas_imam.png"
        zoom 0.8
        
    image Ozan:
        "ozan.png"
        zoom 0.85
        
    image Muhafız_Başı:
        "muhafız_basi.png"
        zoom 0.85
        
init:
    image Kadı:
        "Kadı.png"
        zoom 0.8
        
    image Soylu:
        "soylu.png"
        zoom 0.85
        
    image Yerel_Bakan:
        "yerel_bakan.png"
        zoom 0.85
          
    image Çiftçi:
        "çiftçi.png"
        zoom 0.8
        
    image Büyücü:
        "büyücü.png"
        zoom 0.85
        
    image Gizemli_Adam:
        "gizemli_adam.png"
        zoom 0.75
        
    image Şifacı:
        "şifacı.png"
        zoom 0.85
        
    image Zengin_Tüccar:
        "zengin_tüccar.png"
        zoom 0.85
        
init:
    image Otacı:
        "Otacı.png"
        zoom 0.85
        
    image Hizmetçi_Başı:
        "hizmetci_basi.png"
        zoom 0.85
    image Kraliçe:
        "kraliçe.png"
        zoom 0.85
        
init:
    image startbcg :
        "game_start_bgd.jpg"
        size(config.screen_width, config.screen_height)
init:
    image style_start :
        "style_start.png"
        size(config.screen_width,100)
        yalign 0.0

label open_preferences:#Esc on clik to open preferences
    call screen preferences
    return

screen esc_listener():#Esc control
    key "escape" action Call("open_preferences")


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

    def advance_date(days_to_add):
        # hangi ayda kaç gün olduğu 
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
 
screen date_display(): # burdaki boşlukları cart curt ellemeyelim lütfen tarih ekranı şeysi
    text "{color=#FFFFFF}[current_date['day']]  [current_date['month_names'][current_date['month']]]\n      {color=#FFFFFF}[current_date['year']]{/color}":
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 107
        ypos 78
        size 20
        line_spacing 5



init: # Başlangıç değerleri
    $ Health = 5
    $ Religion = 5
    $ Politics = 5
    $ Military = 5
    $ Economy = 5
    $ People = 5

####### sayaçlar ############################
default managed_day = 0
default minicard_count = 0
default main_story_count = 0
default daily_visitors = 0
default demirci_relationship = 0
default ozan_relationship = 0
default kütüphaneci_relationship = 0
default büyücü_relationship = 0
default hizmetci_basi_relationship = 0
default kadı_relationship = 0
default başimam_relationship = 0
default muhafızbaşı_relationship = 0
default yerelbakan_relationship = 0
default soylu_relationship = 0
default zengintüccar_relationship = 0
default asker_relationship = 0
default şifacı_relationship = 0
default otacı_relationship = 0
default çiftçi_relationship = 0
# Diyalog sayısını gösterecek ekran

screen managed_day():
    text "Yönetilen Gün: [managed_day]":
        xpos 90
        ypos 160
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
    $ in_main_menu = True
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
    $ visitors_today = 0
    
screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.9  # Seçenekleri ekranın altına taşır.
        spacing 9

        for item in items:
            textbutton item.caption action item.action

label zero_point:#0 noktası
    $ managed_day = 0
    $ daily_visitors = 0
    $ visitors_today = 0
    $ minicard_count = 0
    $ main_story_count = 0
    $ Economy = 5
    $ Politics = 5
    $ Military = 5
    $ Religion = 5
    $ Health = 5
    $ People = 5
    $ zero_chr_scr()
    $ zero_chr()
    $ zero_mnc()
    jump in_start

init python:# Bağımsız fonksiyonlar //Check_bars & zero_chr_scr & chr ile alakalı & mnc ile alakalı
    def check_bars():
        for value in [Health,Religion,Politics,Military,Economy,People]:
            if value <= 0 or value >= 10:
                renpy.jump("minicard")
            
    def zero_chr_scr():
        renpy.hide("Asker")
        renpy.hide("Baş İmam")
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

    def zero_chr():
        for i in range(0,15):
            chr_data[i]["info"]=5
    
    def chr_chng(name, sign, value):
        names = {
            "ozan": 0, "demirci": 1, "büyücü": 2, "kadı": 3, "mhf_baş": 4, "hzm_baş": 5,
            "asker": 6, "baş_imam": 7, "çiftçi": 8, "ktpnc": 9, "otacı": 10, "soylu": 11,
            "şifacı": 12, "yrl_bkn": 13, "zng_tcr": 14
        }
        i = names[name]
        if sign == "+":
            chr_data[i]["info"] = min(chr_data[i]["info"] + value, 10)
        elif sign == "-":
            chr_data[i]["info"] = max(chr_data[i]["info"] - value, 0)


    def zero_mnc():
        for i in range(0,12):
            mnc_data[i]["val"] = 0

    def mnc_chng(name,value):
        names={
            kosc_mnc:0,hp_mnc:1,bm_mnc:2,gw_mnc:3,al_mnc:4,hr_mnc:5,spsb_mnc:6,sow_mnc:7,
            rg_mnc:8,sti_mnc:9,bcm_mnc:10,lp_mnc:11
        }
        mnc_data[names[name]]["val"] = value
        mnc_data[names[name]]["val"] = max(0,mnc_data[names[name]]["val"],1)

label game_over:
    scene startbcg
    $ zero_chr_scr()
    if not game_over_triggered:
        $ game_over_triggered = True
        $ character_alive=False
    if Health <= 0: 
        show Otacı at otaci_poz
        Otacı "Kralım bulaşıcı bir hastalık çıktı ve engel olamıyoruz."
        menu:
            "Ne?":
                hide image Otacı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Olamaz":
                hide image Otacı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 

    elif Health >= 10:
        show Şifacı at sifaci_poz
        Şifacı "Kralım araştırma bölgelerimizin birinde bir hata yaptık." 
        menu:
            "Ne hatası?":
                hide image Şifacı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Neler oluyor?":
                hide image Şifacı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
    elif Religion <= 0:
        
        show Baş_İmam at bas_imam_poz
        Baş_İmam "Kralım siz doğru yoldan ayrıldınız."
        menu:
            "Neler oluyor?":
                hide image Baş_İmam
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Ne?":
                hide image Baş_İmam
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
                    
    elif Religion >= 10:
        
        show Baş_İmam at bas_imam_poz
        Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
        menu:
            "Ne diyosun be":
                hide image Baş_İmam
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
            "Ne oluyor":
                hide image Baş_İmam
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  

    elif Politics <= 0:
        
        show Yerel_Bakan at yerel_bakan_poz
        Yerel_Bakan "Kralım meclis üyeleri sizi sattı."
        menu:
            "Nasıl olur?":
                hide image Yerel_Bakan
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
            "Hayır!":
                hide image Yerel_Bakan
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı alt etti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
    elif Politics >= 10:
        
        show Yerel_Bakan at yerel_bakan_poz
        Yerel_Bakan "Kralım artık zamanın doldu."
        menu:
            "Ne oluyor?":
                hide image Yerel_Bakan
                show Gizemli_Adam at gizemli_adam_poz 
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
            "Ne?":
                hide image Yerel_Bakan
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Kraliyet meclisi sana baş kaldırıp isyan etti halkının önünde idam edildin." 
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
    elif Military <= 0:
        
        show Muhafız_Başı at muhafiz_basi_poz
        Muhafız_Başı "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
        menu:
            "Olamaz!":
                hide image Muhafız_Başı
                show Gizemli_Adam at gizemli_adam_poz 
                Gizemli_Adam "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
            "Hayır!":
                hide image Muhafız_Başı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
    elif Military >= 10:
        
        show Muhafız_Başı at muhafiz_basi_poz
        Muhafız_Başı "Kralım artık sizin bir yetkiniz kalmadı."
        menu:
            "Ne?":
                hide image Muhafız_Başı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Ne saçmalıyorsun?":
                hide image Muhafız_Başı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()
    elif Economy <= 0:
        
        show Soylu at soylu_poz
        Soylu "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
        menu:
            "Olamaz!":
                hide image Soylu
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Ne?":
                hide image Soylu
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
    elif Economy >= 10:
        
        show Soylu at soylu_poz
        Soylu "Kralım artık sizi başımızda istemiyoruz."
        menu:
            "Ne saçmalıyorsun sen?":
                hide image Soylu
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()
            "Aklınımı kaçırdın?":
                hide image Soylu
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar Ülkeniz artık zengin kesimin eline geçti."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()  
    elif People <= 0:
        
        show Kadı at kadi_poz
        Kadı "Kralım halktan çalarak yönettiğiniz bu düzen bozuldu."
        menu:
            "Ne?":
                hide image Kadı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
            "Ne oluyor?":
                hide image Kadı
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 
    elif People >= 10:
        
        show Çiftçi at ciftci_poz
        Çiftçi "Kralım o tahtı hak etmiyorsunuz."
        menu:
            "Ne saçmalıyorsun sen?":
                hide image Çiftçi
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz."
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit()
            "Aklınımı kaçırdın?":
                hide image Çiftçi
                show Gizemli_Adam at gizemli_adam_poz
                Gizemli_Adam "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz." 
                menu:
                    "Yeniden başla":
                        hide image Gizemli_Adam
                        jump zero_point   
                    "Çık":
                        $ renpy.quit() 

label minicard:
    if Health <= 0:
        if bmnc_data[10]["val"] == 1:
            $ Health += 3
            $ bmnc_data[10]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[1]["val"] == 1:
            $ Health += 3
            $ mnc_data[1]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Health >= 10:
        if mnc_data[1]["val"] == 1:
            $ Health -= 3
            $ mnc_data[1]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Religion <= 0:
        if mnc_data[5]["val"] == 1:
            $ Religion += 3
            $ mnc_data[5]["val"] = 0
            $ check_bars()
            return
        elif chr_data[0]["val"] == 1:
            $ Religion += 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Religion >= 10:
        if mnc_data[11]["val"] == 1:
            $ Religion -= 3
            $ mnc_data[11]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[5]["val"] == 1:
            $ Religion -= 3
            $ mnc_data[5]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[4]["val"] == 1:
            $ Religion -= 3
            $ mnc_data[4]["val"] = 0
            $ check_bars()
            return
        elif chr_data[0]["val"] == 1:
            $ Religion -= 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Politics <= 0:
        if mnc_data[6]["val"] == 1:
            $ Politics += 3
            $ mnc_data[6]["val"] = 0
            $ check_bars()
            return
        elif chr_data[0]["val"] == 1:
            $ Politics += 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Politics >= 10:
        if mnc_data[4]["val"] == 1:
            $ Politics -= 3
            $ mnc_data[4]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[2]["val"] == 1:
            $ Politics -= 3
            $ mnc_data[2]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[8]["val"] == 1:
            $ Politics -= 3
            $ mnc_data[8]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Military <= 0:
        if mnc_data[8]["val"] == 1:
            $ Military += 3
            $ mnc_data[8]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[2]["val"] == 1:
            $ Military += 3
            $ mnc_data[2]["val"] = 0
            $ check_bars()
            return
        elif chr_data[0]["val"] == 1:
            $ Military += 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Military >= 10:
        if chr_data[0]["val"] == 1:
            $ Military -= 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[2]["val"] == 1:
            $ Military -= 3
            $ mnc_data[2]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Economy <= 0:
        if mnc_data[7]["val"] == 1:
            $ Economy += 3
            $ mnc_data[7]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[9]["val"] == 1:
            $ Economy += 3
            $ mnc_data[9]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif Economy >= 10:
        if mnc_data[3]["val"] == 1:
            $ People += 3
            $ mnc_data[3]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif People <= 0:
        if mnc_data[7]["val"] == 1:
            $ People += 3
            $ mnc_data[7]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[3]["val"] == 1:
            $ People += 3
            $ mnc_data[3]["val"] = 0
            $ check_bars()
            return
        else:
            jump game_over

    elif People >= 10:
        if chr_data[0]["val"] == 1:
            $ People -= 3
            $ chr_data[0]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[5]["val"] == 1:
            $ People -= 3
            $ mnc_data[5]["val"] = 0
            $ check_bars()
            return
        elif mnc_data[8]["val"] == 1:
            $ People -= 3
            $ mnc_data[8]["val"] = 0
            $ check_bars()
            return
        else :
            jump game_over



init python:# Diyologlar
    import random

    # Tüm diyalogları bir liste içine koyuyoruz sonuncusunda virgül olmayacak
    dialogs = [
        "dialog1", "dialog2", "dialog3", "dialog4", "dialog5",
        "dialog6", "dialog7", "dialog8", "dialog9", "dialog10",
        "dialog11", "dialog12", "dialog13", "dialog14", "dialog15",
        "dialog16", "dialog17", "dialog18", "dialog19", "dialog20",
        "dialog21", "dialog22", "dialog23", "dialog24", "dialog25",
        "dialog26", "dialog27", "dialog28", "dialog29", "dialog30",
        "dialog30", "dialog31", "dialog32", "dialog33", "dialog34",
        "dialog35", "dialog36", "dialog37", "dialog38", "dialog39",
        "dialog40", "dialog41", "dialog42", "dialog43", "dialog44",
        "dialog45", "dialog46", "dialog47", "dialog48", "dialog49",
        "dialog50", "dialog51", "dialog52", "dialog53", "dialog54",
        "dialog55", "dialog56", "dialog57", "dialog58", "dialog59",
        "dialog60", "dialog61", "dialog62", "dialog63", "dialog64",
        "dialog65", "dialog66", "dialog67", "dialog68", "dialog69",
        "dialog70", "dialog71", "dialog72", "dialog73", "dialog74",
        "dialog75", "dialog76", "dialog77", "dialog78", "dialog79",
        "dialog80", "dialog81", "dialog82", "dialog83", "dialog84",
        "dialog85", "dialog86", "dialog87", "dialog88"
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

init python:# Hikaye metinleri
    import random

    stories = [
        "story1", "story2", "story3", "story4"
    ]


label start:
    stop music 
    queue music[
        "audio/Rite_of_the_Fading_Light.mp3",
        "audio/Lake_of_Light.mp3",
        "audio/Bleak_Falls.mp3"] loop
    show screen bars
    show screen style_start
    show screen sign_hist
    show screen map_button
    show screen run_button
    show screen character_button
    show screen minicard_button
    scene startbcg
    show screen managed_day
    show screen date_display
    
    $ character_alive=True
    label in_start:
        while True:
            $ zero_chr_scr()
            $ in_main_menu = 0
            $ in_game = True
            show screen esc_listener
            show Kraliçe at kraliçe_poz
            Kraliçe "Merhaba Majesteleri… Önünüzde uzun ve zorlu bir hükümdarlık yolu var. Her gün halktan ya da saraydan biri huzurunuza çıkacak ve sizden bir karar vermenizi bekleyecek. Vereceğiniz her karar, ülkemizin din, siyaset, ekonomi, askeriye, sağlık ve halkın refahı gibi hayati dengelerini doğrudan etkileyecek."
            Kraliçe "Fakat yalnızca bu değil… İnsanların gönülleri de kararlarınızla şekillenecek. Birine sürekli hayır derseniz, kalbinde size karşı bir kin birikebilir. Ama her isteğini kabul ederseniz, size olan bağlılığı artar. Her kişi farklıdır, her kararın bedeli olur…"
            Kraliçe "Lütfen unutmayın majesteleri; din, sağlık, siyaset, halk, ekonomi ve askerî güç… Bu unsurların biri bile uç noktalara savrulursa, krallığımız tehlikeye girer. Denge... İşte asıl ihtiyacımız olan budur."
            Kraliçe "Şimdi… Tahtınız sizi bekliyor."
            hide Kraliçe
            if last_dialog == None:
                $ chosen_dialog = get_random_dialog()  # Yeni bir rastgele diyalog al
                $ last_dialog = chosen_dialog
            else :
                $ chosen_dialog = last_dialog
            jump expression chosen_dialog
   
label check_minicard: #bunun yeri ile oynamayın rastgele minicard dialogu atıyor
    if managed_day == 2 and not minicard_used:
        $ chosen_card = renpy.random.choice(minicard_dialogs)
        $ minicard_used = True 
        $ last_dialog = chosen_card
        jump expression chosen_card
    else:
        jump random_dialog
    jump random_dialog

label random_dialog:
    if main_story_count == 5:
        jump story1
    else:
        $ chosen_dialog = renpy.random.choice(dialogs)
        $ last_dialog = chosen_dialog
        jump expression chosen_dialog  # Yeni seçilen diyaloga git

