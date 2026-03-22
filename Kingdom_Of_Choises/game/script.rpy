
label splashscreen:
    play movie "movies/trailer.webm"
    show movie
    $ renpy.pause(10, hard=True)
    stop movie
    return

define Kütüphaneci = Character(_("Kütüphaneci"), what_cps=70)
define Demirci = Character(_("Demirci"), what_cps=70)
define Baş_İmam = Character(_("Baş İmam"), what_cps=70)
define Ozan = Character(_("Ozan"), what_cps=70)
define Muhafız_Başı = Character(_("Muhafız Başı"), what_cps=70)  
define Kadı = Character(_("Kadı"), what_cps=70)
define Asker = Character(_("Asker"), what_cps=70)
define Çiftçi = Character(_("Çiftçi"), what_cps=70)
define Zengin_Tüccar = Character(_("Zengin Tüccar"), what_cps=70)
define Yerel_Bakan = Character(_("Yerel Bakan"), what_cps=70)
define Soylu = Character(_("Soylu"), what_cps=70)
define Gizemli_Adam = Character(_("Gizemli Adam"), what_cps=70)
define Büyücü = Character(_("Büyücü"), what_cps=70)
define Otacı = Character(_("Otacı"), what_cps=70)
define Şifacı = Character(_("Şifacı"), what_cps=70)
define Hizmetçi_Başı = Character(_("Hizmetçi Başı"), what_cps=70)
define Kraliçe = Character(_("Kraliçe"), what_cps=70)
define Lider_Yardımcısı = Character(_("Lider Yardımcısı"), what_cps=70)
define Komutan = Character(_("Komutan"), what_cps=70)
define Haznedar = Character(_("Haznedar"), what_cps=70)
define Tacir = Character(_("Tacir"), what_cps=70)
define Baş_Danışman = Character(_("Baş Danışman"), what_cps=70)
define Elçi = Character(_("Elçi"), what_cps=70)
define Kögan_Lideri = Character(_("Kögan Lideri"), what_cps=70)
define tukan = Character(_("tukan"), what_cps=70)
#image ile karakterlere bir resim atıyoruz

define audio.deadeffect = "audio/deadeffect.mp3"

default level_1_t = 0
default level_2_t = 0
default level_3_t = 0
default level_4_t = 0
default level_5_t = 0
default level_6_t = 0
default level_7_t = 0
default level_8_t = 0
default level_9_t = 0
default level_10_t = 0
default level_11_t = 0
default level_12_t = 0
default level_13_t = 0
default level_14_t = 0
default level_15_t = 0
default level_16_t = 0
default level_17_t = 0
default level_18_t = 0
default level_19_t = 0
default level_20_t = 0
default level_21_t = 0
default level_22_t = 0
default level_23_t = 0
default level_24_t = 0
default level_25_t = 0
default level_26_t = 0

define mnc_info = {
    0: {
        "ad": _("Knight Of Swan Klanı"),
        "etki": _("Askeri, Siyaset, Halk veya Din değeri bittiğinde veya yükseldiğinde sizi ölümden korur."),
        "img":"gui/minicard_resim/kosc_mnc.png",
        "val":0
    },
    1: {
        "ad": _("Sağlık İksiri"),
        "etki": _("Sağlık değeri bittiğinde veya dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/hp_mnc.png",
        "val":0
    },
    2: {
        "ad": _("Kara Büyü Kitabı"),
        "etki": _("Askeri değeri bittiğinde veya dolduğunda yada siyaset değeri dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/bm_mnc.png",
        "val":0
    },
    3: {
        "ad": _("Tahıl Ambarı Deposu"),
        "etki": _("Ekonomi değeri bittiğinde veya dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/gw_mnc.png",
        "val":0
    },
    4: {
        "ad": _("Suikastçi Birliği"),
        "etki": _("Askeri, siyaset veya din değerleri dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/al_mnc.png",
        "val":0
    },
    5: {
        "ad": _("Kustal Emanetler"),
        "etki": _("Din değeri bittiğinde veya dolduğunda yada halk değeri dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/hr_mnc.png",
        "val":0
    },
    6: {
        "ad": _("Üstün Siyaset Bilimi Kitabı"),
        "etki": _("Siyaset değeri bittiğinde yada dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/spcb_mnc.png",
        "val":0
    },
    7: {
        "ad": _("Savaş Ganimetleri"),
        "etki": _("Ekonomi veya halk değerleri bittiğinde sizi ölümden korur."),
        "img":"gui/minicard_resim/sow_mnc.png",
        "val":0
    },
    8: {
        "ad": _("Kraliyet Muhafızları"),
        "etki": _("Askeri değeri bittiğinde veya dolduğunda yada siyaset veya halk dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/rg_mnc.png",
        "val":0
    },
    9: {
        "ad": _("İpek Ticareti Gelirleri"),
        "etki": _("Ekonomi değeri bittiğinde veya dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/sti_mnc.png",
        "val":0
    },
    10: {
        "ad": _("Mavi Şapkalı Mantarlar"),
        "etki": _("Ekonomi veya Sağlık değeri bittiğinde sizi ölümden korur."),
        "img":"gui/minicard_resim/bcm_mnc.png",
        "val":0
    },
    11: {
        "ad": _("Sadakat iksiri"),
        "etki": _("Siyaset veya din değeri dolduğunda sizi ölümden korur."),
        "img":"gui/minicard_resim/lp_mnc.png",
        "val":0
    }
}

init:
    # Mini Kart Adı Stili
    style minicard_name_style is default:
        size 20 
        color "#FFFFFF"
        outlines [(2, "#000000", 0, 0)]

    # Mini Kart Açıklama/Etki Stili
    style minicard_desc_style is default:
        size 15
        color "#CCCCCC"
        text_align 0.5
        outlines [(1, "#000000", 0, 0)]

image aa = "day/aa.png"
image bb = "day/bb.png"
image cc = "day/cc.png"
image dd = "day/dd.png"
image ee = "day/ee.png" # gün geçiş animasyon şeysi
# Karakterler
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
    
    image tukan:
        "2kan.png"
        zoom 0.85
        
init:
    image Otacı:
        "Otacı.png"
        zoom 0.85
        
    image Hizmetçi_Başı:
        "Hizmetçi_Başı.png"
        zoom 0.85
    image Kraliçe:
        "kraliçe.png"
        zoom 0.85
    image Lider_Yardımcısı:
        "lider_yardımcısı.png"
        zoom 0.85
    image Komutan:
        "Komutan.png"
        zoom 0.85
    image Elçi:
        "elçi.png"
        zoom 0.85
    image Haznedar:
        "Haznedar.png"
        zoom 0.85
    image Baş_Danışman:
        "baş_danışman.png"
        zoom 0.85
    image Tacir:
        "tacir.png"
        zoom 0.85
    image Kögan_Lideri:
        "Kögan_Lideri.png"
        zoom 0.85

init:
    image al_mnc :
        "gui/minicard_resim/al_mnc.png"

    image bcm_mnc :
        "gui/minicard_resim/bcm_mnc.png"   

    image bm_mnc :
        "gui/minicard_resim/bm_mnc.png"

    image gw_mnc :
        "gui/minicard_resim/gw_mnc.png"

    image hp_mnc :
        "gui/minicard_resim/hp_mnc.png"
    
    image hr_mnc :
        "gui/minicard_resim/hr_mnc.png"

    image kosc_mnc :
        "gui/minicard_resim/kosc_mnc.png"

    image lp_mnc :
        "gui/minicard_resim/lp_mnc.png"

    image rg_mnc :
        "gui/minicard_resim/rg_mnc.png"

    image sow_mnc :
        "gui/minicard_resim/sow_mnc.png"

    image spcb_mnc :
        "gui/minicard_resim/spcb_mnc.png"

    image sti_mnc :
        "gui/minicard_resim/sti_mnc.png"
    
init:
    image rune1 :
        "gui/rune/rune1.png"
    
    image rune2 :
        "gui/rune/rune2.png"
    
    image rune3 :
        "gui/rune/rune3.png"

    image rune4 :
        "gui/rune/rune4.png"
    
    image rune5 :
        "gui/rune/rune5.png"
    
    image rune6 :
        "gui/rune/rune6.png"

    image rune7 :
        "gui/rune/rune7.png"

    image rune8 :
        "gui/rune/rune8.png"

    image rune9 :
        "gui/rune/rune9.png"

    image rune10 :
        "gui/rune/rune10.png"

    image rune11 :
        "gui/rune/rune11.png"

    image rune12 :
        "gui/rune/rune12.png"

        
init: # ekranlar cart curt
    image startbcg :
        "mekan/arka_plan.jpg"
        size(config.screen_width, config.screen_height)
        # taht odası resmin
    image eski_oda :
        "mekan/eski_oda.jpg"
        size(config.screen_width, config.screen_height)
        # eski kütüphane anahtarlı
    image dev_salon :
        "mekan/dev_salon.png"
        size(config.screen_width, config.screen_height)
        # toplantı odası meclis
    image orman :
        "mekan/orman.png"
        size(config.screen_width, config.screen_height)
        # orman işte 
    image gizemli_oda :
        "mekan/gizemli_oda.jpg"
        size(config.screen_width, config.screen_height)
        # panzehir yapılan tarifin bulunduğu yer
    image day_sabah :
        "mekan/main_menü_gündüz.png"
        size(config.screen_width, config.screen_height)
    image day_gece :
        "mekan/main_menü_gece.png"
        size(config.screen_width, config.screen_height)
    image kasaba :
        "mekan/balik_kasaba.png"
        size(config.screen_width, config.screen_height)
        # lider yardımcısı nın oralar
    image tunel_ucgan :
        "mekan/tunel.ucgan.png"
        size(config.screen_width, config.screen_height)
        # üçgen sembollü tünel odası
    image tunel_x :
        "mekan/tunel.x.png"
        size(config.screen_width, config.screen_height)
        # x sembollü tünel odası
    image tunel_o :
        "mekan/tunel.o.png"
        size(config.screen_width, config.screen_height)
        # o sembollü tünel odası
    image tunel_k :
        "mekan/tunel.k.png"
        size(config.screen_width, config.screen_height)
        # k sembollü tünel odası
    image tuneldead :
        "mekan/tunel_dead.png"
        size(config.screen_width, config.screen_height)
        # ölünen tünel odası
    image parola :
        "mekan/parola.png"
        size(config.screen_width, config.screen_height)
        # parola odası
    image parola_tuzak :
        "mekan/parola_tuzak.png"
        size(config.screen_width, config.screen_height)
        # hatalı şifrede ki oda
    image lahit :
        "mekan/lahit.png"
        size(config.screen_width, config.screen_height)
        # kütüphanedeki gizli oda lahit 
    image kuzeykale :
        "mekan/kuzey.kalesi.png"
        size(config.screen_width, config.screen_height)
        # terk edilmiş kuzey şehri
    image tunelgiris :
        "mekan/tunelgiris.png"
        size(config.screen_width, config.screen_height)
        # gizli tünellere inen merdiven
    image orman2 :
        "mekan/orman2.png"
        size(config.screen_width, config.screen_height)
        # orman 2 işte 
    image kalekapi :
        "mekan/kalekapi.png"
        size(config.screen_width, config.screen_height)
        # kale kapısı görseli
    image a11son :
        "mekan/a11son.png"
        size(config.screen_width, config.screen_height)
        # tahta oturan soylu 
    image harita :
        "mekan/map.png"
        size(config.screen_width, config.screen_height)
        # map
    image orman3 :
        "mekan/orman3.png"
        size(config.screen_width, config.screen_height)
        # orman 3 işte 
    image koganson :
        "mekan/koganson.png"
        size(config.screen_width, config.screen_height)
        #koganların öldürmeleri falan filan
    image gecekamp :
        "mekan/gecekamp.png"
        size(config.screen_width, config.screen_height)
        # koganlardan kaçarken kamp
    image kuzeykaleon :
        "mekan/kuzeykaleon.png"
        size(config.screen_width, config.screen_height)
        # kuzey kalenin kapısı
    image a122son :
        "mekan/a122son.png"
        size(config.screen_width, config.screen_height)
        # boş taht
    image terkkale :
        "mekan/terkkale.png"
        size(config.screen_width, config.screen_height)
        # terk edilmiş başkent resmi 
    image sefer :
        "mekan/sefer.png"
        size(config.screen_width, config.screen_height)
        # aquila gece resmi
    image ormankus :
        "mekan/ormankus.png"
        size(config.screen_width, config.screen_height)
        # orman 2 işte 
    image ormank :
        "mekan/ormank.png"
        size(config.screen_width, config.screen_height)
        # orman 2 işte 
    image b11son :
        "mekan/b11son.png"
        size(config.screen_width, config.screen_height)
        # b11end
    image Kralheykel :
        "mekan/Kralheykel.png"
        size(config.screen_width, config.screen_height)
        # kral heykeli sonu
    image zehirson :
        "mekan/zehirson.png"
        size(config.screen_width, config.screen_height)
        # zehir son
    image mutison :
        "mekan/mutison.png"
        size(config.screen_width, config.screen_height)
        # mutasyon son
    image dinson :
        "mekan/dinson.png"
        size(config.screen_width, config.screen_height)
        # din son
    image darson :
        "mekan/darson.png"
        size(config.screen_width, config.screen_height)
        # darbe son
    image sison :
        "mekan/sison.png"
        size(config.screen_width, config.screen_height)
        # siyaset son
    image sokak :
        "mekan/sokak.png"
        size(config.screen_width, config.screen_height)
        # sşehir sokağı
    image sokakson :
        "mekan/sokakson.png"
        size(config.screen_width, config.screen_height)
        # sşehir sokağı isyan sonu
    image askeridarbe :
        "mekan/askeridarbe.png"
        size(config.screen_width, config.screen_height)
        # komutan muhafızbaşı asker
    image zengin :
        "mekan/zengin.png"
        size(config.screen_width, config.screen_height)
        # zengin tüccar soylu tacir
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

default current_date = {
    "day": 24,
    "month": 2,
    "year": 1224
}

init python:
    # Ay isimlerini dışarıda bir fonksiyon veya değişken olarak tutuyoruz
    def get_month_name(month_index):
        months = {
            1: _("01"), 2: _("02"), 3: _("03"), 4: _("04"),
            5: _("05"), 6: _("06"), 7: _("07"), 8: _("08"),
            9: _("09"), 10: _("10"), 11: _("11"), 12: _("12")
        }
        return months.get(month_index, "")

    def advance_date(days_to_add):
        month_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        current_date["day"] += days_to_add
        
        while current_date["day"] > month_days[current_date["month"]]:
            current_date["day"] -= month_days[current_date["month"]]
            current_date["month"] += 1
            
            if current_date["month"] > 12:
                current_date["month"] = 1
                current_date["year"] += 1

screen date_display():
    # Burada get_month_name fonksiyonunu çağırarak ismi anlık çekiyoruz
    $ current_month_text = get_month_name(current_date['month'])
    
    text "{color=#FFFFFF}[current_date['day']] [current_month_text]\n      {color=#FFFFFF}[current_date['year']]{/color}":
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 124
        ypos 78
        size 20
        line_spacing 5

init: # Başlangıç değerleri
    $ Health = 6
    $ Religion = 6
    $ Politics = 6
    $ Military = 6
    $ Economy = 6
    $ People = 6

init python:
    for i in range(1, 27):
        achievement.register(f"level_{i}_t")


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
default tunel = 0
# Diyalog sayısını gösterecek ekran

init python:
    # GLOBAL DEĞİŞKENLER
    player_cards = ["kart1.png", "kart2.png", "kart3.png", "kart4.png"]
    player_mana = 5
    BOARD_ROWS = 3
    BOARD_COLS = 4
    CARD_COST = 3 

    board_slots = [[None for c in range(BOARD_COLS)] for r in range(BOARD_ROWS)]

    def can_place_card(slot_row, slot_col):
        # Sadece 0. sütuna (en soldaki 3'lü kare) yerleştirmeye izin ver
        return slot_col == 0 and board_slots[slot_row][slot_col] is None

    def is_card_placed(card_name):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                slot_data = board_slots[row][col]
                if slot_data and slot_data[0] == card_name and slot_data[1]:
                    return True
        return False
        
    def get_card_name_from_drag_name(drag_name):
        if drag_name.startswith("card_"):
            return drag_name.split("card_")[1]
        return None

    def can_place_card(slot_row, slot_col):
        return slot_row == 0 and slot_col == 0 and board_slots[slot_row][slot_col] is None

    def place_card(card_file_name, slot_row, slot_col):
        global player_mana
        
        if player_mana >= CARD_COST and can_place_card(slot_row, slot_col):
            board_slots[slot_row][slot_col] = (card_file_name, True) 
            
            player_mana -= CARD_COST
            renpy.notify(f"{card_file_name} yerleştirildi! (Mana: {player_mana})")
            return True
        else:
            if player_mana < CARD_COST:
                renpy.notify(_("Yeterli mana yok!"))
            else:
                renpy.notify(_("Geçersiz alan! Kartlar sadece ilk satıra ve ilk sütuna yerleştirilebilir.")) 
            return False

# DRAG DROP FONKSİYONU
init python:
    def drop_card(drags, drop):
        drag = drags[0]
        drop_name = drop.drag_name
        
        if drop_name.startswith("slot_"):
            _, row_str, col_str = drop_name.split("_")
            row, col = int(row_str), int(col_str)
            
            card_file_name = get_card_name_from_drag_name(drag.drag_name)
            
            if card_file_name and place_card(card_file_name, row, col):
                renpy.restart_interaction()
                return 

        return None

init python:
    def check_all_levels_completed():
        # 1'den 25'e kadar tüm seviyeleri kontrol et
        for i in range(1, 26):
            # getattr kullanarak değişkenin varlığını ve değerini güvenli kontrol et
            if not getattr(store, f"level_{i}_t", 0):
                return
        
        # Hepsi tamamlanmışsa 26'yı aç
        unlock_level(26)

    def unlock_level(level_number):
        name = f"level_{level_number}_t"
        
        # Değişkeni güvenli bir şekilde al, yoksa 0 (False) kabul et
        current_status = getattr(store, name, 0)
        
        if not current_status:
            # Seviyeyi aç (Global değişkeni güncelle)
            setattr(store, name, 1)
            
            # --- STEAM VE BAŞARIM SİSTEMİ ---
            # Modern Ren'Py'da Steam kontrolü böyle yapılır:
            # Eğer Steam API Name ile 'name' değişkenin aynıysa direkt çalışır.
            achievement.grant(name)
            
            # Değişiklikleri hemen işle/kaydet (Eski storeStats yerine geçer)
            achievement.sync()
            # --------------------------------

            # Eğer 1-25 arası bir şey açıldıysa kontrol et
            if level_number < 26:
                check_all_levels_completed()

screen managed_day(): # tabela sol üst
    text _("Yönetilen Gün: [managed_day]"):
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 89
        ypos 160
        color "#FFFFFF"
        size 13

screen menu_buttons(): 
    text _("Karakter"):
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 465
        ypos 20
        color "#FFFFFF"
        outlines [(2.5, "#000000")]
        size 22
    text _("Rün"):
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 720
        ypos 20
        color "#FFFFFF"
        outlines [(2.5, "#000000")]
        size 22
    text _("Minikart"):
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 913
        ypos 20
        color "#FFFFFF"
        outlines [(2.5, "#000000")]
        size 22
    text _("Harita"):
        font "gui/font/CinzelDecorative-Regular.otf"
        xpos 1150
        ypos 20
        color "#FFFFFF"
        outlines [(2.5, "#000000")]
        size 22

transform bar_animation: # asla çalışmayan dola animasyonu
    ease 0.5 xsize 400  

screen bars():
    vbox:
        xalign 1.0  
        yalign 0.4  
        spacing 5  
        text _("Sağlık") xalign 0.5  
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Health # değişken
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text _("Din") xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Religion
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text _("Siyaset") xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Politics
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text _("Askeri") xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Military
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text _("Ekonomi") xalign 0.5
        frame:
            background None
            xsize 400  
            ysize 30
            bar:
                value Economy
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)

        text _("Halk") xalign 0.5
        frame:
            background None
            xsize 400
            ysize 30
            bar:
                value People
                range 12
                xsize 400
                ysize 30
                left_bar Frame("#cc0000")
                right_bar Frame("#00000000")
                align (0, 0.5)
                at bar_animation
            add "gui/bar/bars_borders.png" xsize 550 ysize 50 align (0.5, 0.5)


init python:#Mouse imleci
    config.mouse = {
        'default': [ ('images/arma.png', 0, 0) ],
        'pointer': [ ('images/arma2.png', 0, 0) ]
    }

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
    $ main_story_count2 = 0
    $ which_story = 0
    $ Economy = 6
    $ Politics = 6
    $ Military = 6
    $ Religion = 6
    $ Health = 6
    $ People = 6
    $ zero_chr_scr()
    $ zero_chr()
    $ zero_mnc()
    jump start

init python:# Bağımsız fonksiyonlar //Check_bars & zero_chr_scr & chr ile alakalı & mnc ile alakalı
    def check_bars():
        for value in [Health,Religion,Politics,Military,Economy,People]:
            if value <= 0 or value >= 12:
                renpy.jump("game_over")    # oyun bitiş 

    def zero_chr_scr():
        renpy.hide("Asker")
        renpy.hide("Baş_İmam")
        renpy.hide("Büyücü")
        renpy.hide("Demirci")
        renpy.hide("Hizmetçi_Başı")
        renpy.hide("Kadı")
        renpy.hide("Kütüphaneci")
        renpy.hide("Muhafız_Başı")
        renpy.hide("Ozan")
        renpy.hide("Soylu")
        renpy.hide("Yerel_Bakan")
        renpy.hide("Zengin_Tüccar")
        renpy.hide("Çiftçi")
        renpy.hide("Şifacı")
        renpy.hide("Gizemli_Adam")
        renpy.hide("Komutan")
        renpy.hide("Tacir")
        renpy.hide("Baş_Danışman")
        renpy.hide("Elçi")
        renpy.hide("Haznedar")


    def zero_chr():
        for i in range(0,20):
            chr_data[i]["info"]=6
    
    def chr_chng(name, sign, value): # karakter ilişkileri
        names = {
            "ozan": 0, "demirci": 1, "büyücü": 2, "kadı": 3, "mhf_baş": 4, "hzmt_baş": 5,
            "asker": 6, "baş_imam": 7, "çiftçi": 8, "ktpnc": 9, "otacı": 10, "soylu": 11,
            "şifacı": 12, "yrl_bkn": 13, "zng_tcr": 14, "kmtn": 15, "tcr": 16, "baş_dnş": 17,
            "elçi": 18, "hznc": 19
        }
        i = names[name]
        if sign == "+":
            chr_data[i]["info"] = min(chr_data[i]["info"] + value, 12)
        elif sign == "-":
            chr_data[i]["info"] = max(chr_data[i]["info"] - value, 0)

    def zero_mnc():
        for i in range(0,12):
            mnc_info[i]["val"] = 0 # minicard

    def mnc_chng(name,value):
        names={
            "kosc_mnc":0,"hp_mnc":1,"bm_mnc":2,"gw_mnc":3,"al_mnc":4,"hr_mnc":5,"spcb_mnc":6,"sow_mnc":7,
            "rg_mnc":8,"sti_mnc":9,"bcm_mnc":10,"lp_mnc":11
        }
        mnc_info[names[name]]["val"] = value
        mnc_info[names[name]]["val"] = max(0,mnc_info[names[name]]["val"],1)

label rune:
    scene startbcg
    if chr_data[7]["info"] <= 0:
        show Kraliçe at kraliçe_poz
        show rune1 at rune1_poz
        Kraliçe "Baş İmam ile ilişkinizin kötü olması bazı sonuçlar doğurdu."
        $ Religion -= 1
        $ check_bars()
        Kraliçe "Lanet rünü etkisiyle 1 Din kaybediyorsunuz."
        $ chr_chng("baş_imam","+",6)
        hide image rune1
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[17]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune2 at rune2_poz
        Kraliçe "Baş Danışman ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ Politics += 1
        $ check_bars()
        Kraliçe "Yardımcı rünü etkisiyle 1 Siyaset kazanıyorsunuz."
        $ chr_chng("baş_dnş","-",6)
        hide image rune2
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[19]["info"] <= 0:
        show Kraliçe at kraliçe_poz
        show rune3 at rune3_poz
        Kraliçe "Haznedar ile ilişkinizin kötü olması bazı sonuçlar doğurdu."
        $ Economy -= 1
        $ check_bars()
        $ chr_chng("hzmt_baş","+",6)
        Kraliçe "Hırsız rünü etkisiyle 1 Ekonomi Kaybediyorsunuz."
        hide image rune3
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[3]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune4 at rune4_poz
        Kraliçe "Kadı ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ Religion += 1
        $ check_bars()
        Kraliçe "Adalet rünü etkisiyle 1 Din kazanıyorsunuz."
        $ chr_chng("kadı","-",6)
        hide image rune4
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[15]["info"] <= 0:
        show Kraliçe at kraliçe_poz
        show rune5 at rune5_poz
        Kraliçe "Komutan ile ilişkinizin kötü olması bazı sonuçlar doğurdu."
        $ Military -= 1
        $ check_bars()
        Kraliçe "Balta rünü etkisiyle 1 Askeri kaybediyorsunuz."
        $ chr_chng("mhf_baş","+",6)
        hide image rune5
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[9]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune6 at rune6_poz
        Kraliçe "Kütüphaneci ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ People += 1
        $ check_bars()
        Kraliçe "Kitap rünü etkisiyle 1 Siyaset kazanıyorsunuz."
        $ chr_chng("ktpnc","-",6)
        hide image rune6
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[10]["info"] <= 0:
        show Kraliçe at kraliçe_poz
        show rune7 at rune7_poz
        Kraliçe "Otacı ile ilişkinizin kötü olması bazı sonuçlar doğurdu."
        $ Health -= 1
        $ check_bars()
        $ chr_chng("otacı","+",6)
        Kraliçe "Zehir rünü etkisiyle 1 Sağlık kaybediyorsunuz."
        hide image rune7
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[4]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune8 at rune8_poz
        Kraliçe "Muhafız Başı ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ Military += 1
        $ check_bars()
        Kraliçe "Koruma rünü etkisiyle 1 Askeri kazanıyorsunuz."
        $ chr_chng("mhf_baş","-",6)
        hide image rune8
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[11]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune9 at rune9_poz
        Kraliçe "Soylu ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ People -= 1
        $ check_bars()
        Kraliçe "Burjuva rünü etkisiyle 1 Halk kaybediyorsunuz."
        $ chr_chng("mhf_baş","-",6)
        hide image rune9
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[14]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune10 at rune10_poz
        Kraliçe "Zengin Tüccar ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ Economy += 1
        $ check_bars()
        Kraliçe "Altın rünü etkisiyle 1 Ekonomi kazanıyorsunuz."
        hide image rune10
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        $ chr_chng("kadı","-",1)
        hide image Kraliçe
    elif chr_data[13]["info"] <= 0:
        show Kraliçe at kraliçe_poz
        show rune11 at rune11_poz
        Kraliçe "Yerel Bakan ile ilişkinizin kötü olması bazı sonuçlar doğurdu."
        $ Politics -= 1
        $ check_bars()
        $ chr_chng("yrl_bkn","+",6)
        Kraliçe "Meclis rünü etkisiyle 1 Siyaset kaybediyorsunuz."
        hide image rune11
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    elif chr_data[12]["info"] >= 12:
        show Kraliçe at kraliçe_poz
        show rune12 at rune12_poz
        Kraliçe "Şifacı ile ilişkinizin iyi olması bazı sonuçlar doğurdu."
        $ Health += 1
        $ check_bars()
        $ chr_chng("şifacı","-",1)
        Kraliçe "Bitki rünü etkisiyle 1 Sağlık kazanıyorsunuz."
        hide image rune12
        Kraliçe "Yukardaki menüden rünler hakkında bilgiye ulaşabilirsin."
        $ unlock_level(24)
        hide image Kraliçe
    
# 0 knight of swan klanı
# 1 sağlık iksiri
# 2 kara büyü kitabı
# 3 Tahıl ambarı
# 4 suikastçi birliği
# 5 Kutsal emanetler sandığı
# 6 üstün siyaset bilimi kitabı
# 7 savaş ganimetleri
# 8 Kraliyet muhafızları
# 9 ipek ticareti gelirleri 
#10 mavi şapkalı mantarlar
#11 sadakat iksiri

label game_over:
    scene startbcg
    $ zero_chr()
    if not game_over_triggered:
        $ game_over_triggered = True
        $ character_alive=False
    if Health <= 0: 
        if mnc_info[10]["val"] == 1:
            show Otacı at otaci_poz
            Otacı "Kralım bulaşıcı bir hastalık çıktı ve engel olamıyoruz."
            hide image otacı 
            show Kraliçe at kraliçe_poz
            show bcm_mnc at bcm_mnc_poz
            Kraliçe "Efendim bu mavi şapkalı mantarlar bu bulaşıcı hastalığa bir deva olabilir."
            $ Health += 3
            hide image bcm_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[10]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[1]["val"] == 1:
            show Otacı at otaci_poz
            Otacı "Kralım bulaşıcı bir hastalık çıktı ve engel olamıyoruz."
            hide image otacı 
            show Kraliçe at kraliçe_poz
            show hp_mnc at hp_mnc_poz
            Kraliçe "Kralım, daha önce aldığınız bu sağlık iksiri bu bulaşıcı hastalığı önleyebilir."
            $ Health += 3
            hide image hp_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[1]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Otacı at otaci_poz
            $ unlock_level(9)
            Otacı "Kralım bulaşıcı bir hastalık çıktı ve engel olamıyoruz."
            
            menu:
                "Ne?":
                    hide image Otacı
                    scene zehirson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")   
                        "Çık":
                            $ renpy.full_restart()
                "Olamaz":
                    hide image Otacı
                    scene zehirson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Vakalar arttı ve hastalık en sonunda sarayınızıda kırıp geçirdi."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")   
                        "Çık":
                            $ renpy.full_restart()

    elif Health >= 12:
        if mnc_info[1]["val"] == 1:
            show Şifacı at sifaci_poz
            Şifacı "Kralım araştırma bölgelerimizin birinde bir hata yaptık."
            hide image Şifacı
            show Kraliçe at kraliçe_poz
            show hp_mnc at hp_mnc_poz
            Kraliçe "Kralım, daha önce aldığınız bu sağlık iksiri bu mutasyonu önleyebilir."
            $ Health -= 3
            hide image hp_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[1]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Şifacı at sifaci_poz
            $ unlock_level(10)
            Şifacı "Kralım araştırma bölgelerimizin birinde hata yaptık." 
        
            menu:
                "Ne hatası?":
                    hide image Şifacı
                    scene mutison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point") 
                        "Çık":
                            $ renpy.full_restart() 
                "Neler oluyor?":
                    hide image Şifacı
                    scene mutison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkeni mutantlar bastı, sürekli üreyen bu yaratıklar Aquiladaki herkesi öldürdü."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()
    elif Religion <= 0:
        if mnc_info[5]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Kralım siz doğru yoldan ayrıldınız."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show hr_mnc at hr_mnc_poz
            Kraliçe "Kralım daha önceden kurtardığımız Kutsal emanetler sandığı bizi kurtarabilir."
            $ Religion += 3
            hide image hr_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[5]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[0]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Kralım siz doğru yoldan ayrıldınız."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Kralım, daha önceden katıldığınız Knight Of Swan Klanı sizi bu darbeden kurtarabilir."
            $ Religion += 3
            hide image kosc_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[0]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Kralım siz doğru yoldan ayrıldınız."
            $ unlock_level(11)
    
            menu:
                "Neler oluyor?":
                    hide image Baş_İmam
                    scene orman2
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()
                "Ne?":
                    hide image Baş_İmam
                    scene orman2
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    " Dinsizlikle yargılanarak ülkeden sürgün edildiğiniz yolda suikast e uğradınız."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
                    
    elif Religion >= 12:
        if mnc_info[11]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show lp_mnc at lp_mnc_poz
            Kraliçe "Kralım daha önceden aldığınız sadakat iksiri işe yarayabilir."
            $ Religion -= 3
            hide image lp_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[11]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[5]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show hr_mnc at hr_mnc_poz
            Kraliçe "Kralım daha önceden kurtardığınız kutsal emanetler sandığı bu durumu çözebilir."
            $ Religion -= 3
            hide image hr_mnc
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ mnc_info[5]["val"] = 0
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[4]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show al_mnc at al_mnc_poz
            Kraliçe "Kralım daha önceden kurduğunuz suikastçi birliği sizi bu durumdan kurtarabilir."
            $ Religion -= 3
            hide image al_mnc
            $ mnc_info[4]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[0]["val"] == 1:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
            hide image Baş_İmam
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Efendim daha önceden katıldığınız Knight Of Swan Klanı sizi koruyacaktır."
            $ Religion -= 3
            hide image kosc_mnc
            $ mnc_info[0]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Baş_İmam at bas_imam_poz
            Baş_İmam "Siz bu ülkeyi yönetçek doğru kişi değilsiniz."
            $ unlock_level(12)
            menu:
                "Ne diyosun be":
                    hide image Baş_İmam
                    scene dinson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")  
                        "Çık":
                            $ renpy.full_restart()  
                "Ne oluyor":
                    hide image Baş_İmam
                    scene dinson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Çok güçlenen Baş İmam seni tahttan indirerek idam etti ve yerine kendi geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()  

    elif Politics <= 0:
        if mnc_info[6]["val"] == 1:
            show Baş_Danışman at bas_danisman_poz
            Baş_Danışman "Kralım meclis üyeleri sizi sattı."
            hide image Baş_Danışman
            show Kraliçe at kraliçe_poz
            show spcb_mnc at spcb_mnc_poz
            Kraliçe "Kralım daha önceden satın aldığınız üstün siyaset bilimi kitabı işe yarayabilir."
            $ Politics += 3
            hide image spcb_mnc
            $ mnc_info[6]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[0]["val"] == 1:
            show Baş_Danışman at bas_danisman_poz
            Baş_Danışman "Kralım meclis üyeleri sizi sattı."
            hide image Baş_Danışman
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Efendim daha önceden katıldığınız Knight Of Swan Klanı sizi koruyacaktır."
            $ Politics += 3
            hide image kosc_mnc
            $ mnc_info[0]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Baş_Danışman at bas_danisman_poz
            $ unlock_level(5)
            Baş_Danışman "Kralım meclis üyeleri sizi sattı."
            
            menu:
                "Nasıl olur?":
                    hide image Baş_Danışman
                    scene sison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı işgal etti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()  
                "Hayır!":
                    hide image Baş_Danışman
                    scene sison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkenin tüm istihbaratları sızdırılmış düşman ülkeler Aquila yı işgal etti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point") 
                        "Çık":
                            $ renpy.full_restart()  
    elif Politics >= 12:
        if mnc_info[4]["val"] == 1:
            show Yerel_Bakan at yerel_bakan_poz
            Yerel_Bakan "Kralım artık zamanın doldu."
            hide image Yerel_Bakan
            show Kraliçe at kraliçe_poz
            show al_mnc at al_mnc_poz
            Kraliçe "Kralım daha önceden kurduğunuz Suikastçiler birliği sizi kurtarabilir."
            $ Politics -= 3
            hide image al_mnc
            $ mnc_info[4]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[2]["val"] == 1:
            show Yerel_Bakan at yerel_bakan_poz
            Yerel_Bakan "Kralım artık zamanın doldu."
            hide image Yerel_Bakan
            show Kraliçe at kraliçe_poz
            show bm_mnc at bm_mnc_poz
            Kraliçe "Kralım daha önceden aldığınız kara büyü kitabı ile bu darbeden kurtulabilirsiniz."
            $ Politics -= 3
            hide image bm_mnc
            $ mnc_info[2]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[8]["val"] == 1:
            show Yerel_Bakan at yerel_bakan_poz
            Yerel_Bakan "Kralım artık zamanın doldu."
            hide image Yerel_Bakan
            show rg_mnc at rg_mnc_poz
            show Kraliçe at kraliçe_poz
            Kraliçe "Kralım daha önceden kurduğunuz Kraliyet Muhafızları sizi koruyabilir."
            $ Politics -= 3
            hide image rg_mnc
            $ mnc_info[8]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Yerel_Bakan at yerel_bakan_poz
            Yerel_Bakan "Kralım artık zamanın doldu."
            $ unlock_level(6)
            scene darson
            menu:
                "Ne oluyor?":
                    hide image Yerel_Bakan
                    scene darson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Kraliyet meclisi sana baş kaldırıp isyan etti, seni öldürüp yerine Yerel Bakan tahta geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point") 
                        "Çık":
                            $ renpy.full_restart()  
                "Ne?":
                    hide image Yerel_Bakan
                    scene darson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Kraliyet meclisi sana baş kaldırıp isyan etti, seni öldürüp yerine Yerel Bakan tahta geçti." 
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()  
    elif Military <= 0:
        if mnc_info[8]["val"] == 1:
            show Komutan at komutan_poz
            Komutan "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
            hide image Komutan
            show rg_mnc at rg_mnc_poz
            show Kraliçe at kraliçe_poz
            Kraliçe "Kralım daha önceden kurduğunuz Kraliyet Muhafızları sizi koruyabilir."
            $ Military += 3
            hide image rg_mnc
            $ mnc_info[8]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[2]["val"] == 1:
            show Komutan at komutan_poz
            Komutan "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
            hide image Komutan
            show Kraliçe at kraliçe_poz
            show bm_mnc at bm_mnc_poz
            Kraliçe "Kralım daha önceden aldığınız kara büyü kitabı ile bu darbeden kurtulabilirsiniz."
            $ Military += 3
            hide image bm_mnc
            $ mnc_info[2]["val"] = 0
            Kraliçe "işe yaradı!"
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[0]["val"] == 1:
            show Komutan at komutan_poz
            Komutan "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
            hide image Komutan
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Efendim daha önceden katıldığınız Knight Of Swan Klanı sizi koruyacaktır."
            $ Military += 3
            hide image kosc_mnc
            $ mnc_info[0]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Komutan at komutan_poz
            $ unlock_level(7)
            Komutan "Diğer ülkeler bize savaş açtı yeterli sayıda askerimiz yok."
            
            menu:
                "Olamaz!":
                    hide image Komutan 
                    scene sison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")   
                        "Çık":
                            $ renpy.full_restart()  
                "Hayır!":
                    hide image Komutan
                    scene sison
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Düşman orduları sarayınızı basıyor ve sizi yakalıp öldürüyorlar Aquila Krallığı sizin hükümdarlığınızda yok oluyor."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
    elif Military >= 12:
        if mnc_info[0]["val"] == 1:
            show Muhafız_Başı at muhafiz_basi_poz
            Muhafız_Başı "Kralım artık sizin bir yetkiniz kalmadı."
            hide image Muhafız_Başı
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Efendim daha önceden katıldığınız Knight Of Swan Klanı sizi koruyacaktır."
            $ Military -= 3
            hide image kosc_mnc
            $ mnc_info[0]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[2]["val"] == 1:
            show Muhafız_Başı at muhafiz_basi_poz
            Muhafız_Başı "Kralım artık sizin bir yetkiniz kalmadı."
            hide image Muhafız_Başı
            show Kraliçe at kraliçe_poz
            show bm_mnc at bm_mnc_poz
            Kraliçe "Kralım daha önceden aldığınız kara büyü kitabı ile bu darbeden kurtulabilirsiniz."
            $ Military -= 3
            hide image bm_mnc
            $ mnc_info[2]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Muhafız_Başı at muhafiz_basi_poz
            Muhafız_Başı "Kralım artık sizin bir yetkiniz kalmadı."
            $ unlock_level(8)
            
            menu:
                "Ne?":
                    hide image Muhafız_Başı
                    scene askeridarbe
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
                "Ne saçmalıyorsun?":
                    hide image Muhafız_Başı
                    scene askeridarbe
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Askerler sarayınızı basıyor ve sizi yakalayıp asarak idam ediyorlar Ülkeniz darbe girişimi ile Ordunun eline geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()
    elif Economy <= 0:
        if mnc_info[7]["val"] == 1:
            show Haznedar at Haznedar_poz
            Haznedar "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
            hide image Haznedar
            show Kraliçe at kraliçe_poz
            show sow_mnc at sow_mnc_poz
            Kraliçe "Kralım daha önceden sakladığınız savaş ganimetlerini satarak kullanabiliriz."
            $ Economy += 3
            hide image sow_mnc
            $ mnc_info[7]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[9]["val"] == 1:
            show Haznedar at Haznedar_poz
            Haznedar "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
            hide image Haznedar
            show Kraliçe at kraliçe_poz
            show sti_mnc at sti_mnc_poz
            Kraliçe "Kralım daha önceden yapmış olduğunuz ipek ticareti gelirleni kullanabiliriz."
            $ Economy += 3
            hide image sti_mnc
            $ mnc_info[9]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[3]["val"] == 1:
            show Haznedar at Haznedar_poz
            Haznedar "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
            hide image Haznedar
            show Kraliçe at kraliçe_poz
            show gw_mnc at gw_mnc_poz
            Kraliçe "Kralım daha önceden açtığınız tahıl ambarındaki tahılları satarak kullanabiliriz."
            $ Economy += 3
            hide image gw_mnc
            $ mnc_info[3]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Haznedar at Haznedar_poz
            $ unlock_level(1)
            Haznedar "Efendim hazinemiz tükendi borcumuz olan dış ülkeler yağmaya başladı."
             
            menu:
                "Olamaz!":
                    hide image Haznedar
                    scene terkkale
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
                "Ne?":
                    hide image Haznedar
                    scene terkkale
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Dış ülkeler dört bir yandan saldıraya geçti ve yavaş yavaş ülkeni ele geçirdiler."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")  
                        "Çık":
                            $ renpy.full_restart() 
    elif Economy >= 12:
        if mnc_info[3]["val"] == 1:
            show Soylu at soylu_poz
            Soylu "Kralım artık sizi başımızda istemiyoruz."
            hide image Soylu
            show Kraliçe at kraliçe_poz
            show gw_mnc at gw_mnc_poz
            Kraliçe "Kralım daha önceden açtığınız tahıl ambarındaki tahılları halka dağatarak kurtulabiliriz."
            $ Economy -= 3
            hide image gw_mnc
            $ mnc_info[3]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[9]["val"] == 1:
            show Soylu at soylu_poz
            Soylu "Kralım artık sizi başımızda istemiyoruz."
            hide image Soylu
            show Kraliçe at kraliçe_poz
            show sti_mnc at sti_mnc_poz
            Kraliçe "Kralım daha önceden yapmış olduğunuz ipek ticareti gelirleni kullanabiliriz."
            $ Economy -= 3
            hide image sti_mnc
            $ mnc_info[9]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Soylu at soylu_poz
            $ unlock_level(2)
            Soylu "Kralım artık sizi başımızda istemiyoruz."
            
            menu:
                "Ne saçmalıyorsun sen?":
                    hide image Soylu 
                    scene zengin
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar. Ülkeniz artık zengin kesimin eline geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point") 
                        "Çık":
                            $ renpy.full_restart()
                "Aklınımı kaçırdın?":
                    hide image Soylu
                    scene zengin
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Ülkende monarşi ortadan kalıyor ve sizi yakalayıp idam ediyorlar. Ülkeniz artık zengin kesimin eline geçti."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart()  
    elif People <= 0:
        if mnc_info[7]["val"] == 1:
            show Kadı at kadi_poz
            Kadı "Kralım halktan çalarak yönettiğiniz bu düzen bozuldu."
            hide image Kadı
            show Kraliçe at kraliçe_poz
            show sow_mnc at sow_mnc_poz
            Kraliçe "Kralım daha önceden sakladığınız savaş ganimetlerini satarak halka dağıtabiliriz."
            $ People += 3
            hide image sow_mnc
            $ mnc_info[7]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[3]["val"] == 1:
            show Kadı at kadi_poz
            Kadı "Kralım halktan çalarak yönettiğiniz bu düzen bozuldu."
            hide image Kadı
            show Kraliçe at kraliçe_poz
            show gw_mnc at gw_mnc_poz
            Kraliçe "Kralım daha önceden açtığınız tahıl ambarındaki tahılları halka dağatarak kurtulabiliriz."
            $ People += 3
            hide image gw_mnc
            $ mnc_info[3]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else:
            show Kadı at kadi_poz
            $ unlock_level(3)
            Kadı "Kralım halktan çalarak yönettiğiniz bu düzen bozuldu."
            
            menu:
                "Ne?":
                    hide image Kadı
                    scene sefer
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
                "Ne oluyor?":
                    hide image Kadı
                    scene sefer
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Halk size daha fazla dayanamadı ve sarayınızı basıp sizi kargılarla öldürdüler."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")
                        "Çık":
                            $ renpy.full_restart() 
    elif People >= 12:
        if mnc_info[0]["val"] == 1:
            show Çiftçi at ciftci_poz
            Çiftçi "Kralım o tahtı hak etmiyorsunuz."
            hide image Çiftçi
            show Kraliçe at kraliçe_poz
            show kosc_mnc at kosc_mnc_poz
            Kraliçe "Efendim daha önceden katıldığınız Knight Of Swan Klanı sizi koruyacaktır."
            $ People -= 3
            hide image kosc_mnc
            $ mnc_info[0]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[5]["val"] == 1:
            show Çiftçi at ciftci_poz
            Çiftçi "Kralım o tahtı hak etmiyorsunuz."
            hide image Çiftçi
            show Kraliçe at kraliçe_poz
            show hr_mnc at hr_mnc_poz
            Kraliçe "Kralım daha önceden kurtardığınız kutsal emanetler sandığı bu durumu çözebilir."
            $ People -= 3
            hide image hr_mnc
            $ mnc_info[5]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        elif mnc_info[8]["val"] == 1:
            show Çiftçi at ciftci_poz
            Çiftçi "Kralım o tahtı hak etmiyorsunuz."
            hide image Çiftçi
            show Kraliçe at kraliçe_poz
            show rg_mnc at rg_mnc_poz
            Kraliçe "Kralım daha önceden kurduğunuz Kraliyet Muhafızları sizi koruyabilir."
            $ People -= 3
            hide image rg_mnc
            $ mnc_info[8]["val"] = 0
            Kraliçe "İşe yaradı!"
            $ unlock_level(23)
            $ check_bars()
            hide image Kraliçe
            scene startbcg
            jump random_dialog
            return
        else :
            show Çiftçi at ciftci_poz
            $ unlock_level(4)
            Çiftçi "Kralım o tahtı hak etmiyorsunuz."
            
            menu:
                "Ne saçmalıyorsun sen?":
                    hide image Çiftçi
                    scene sokakson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz."
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")  
                        "Çık":
                            $ renpy.full_restart()
                "Aklınımı kaçırdın?":
                    hide image Çiftçi
                    scene sokakson
                    play voice "audio/deadeffect.mp3" volume 0.5 
                    "Doyumsuz halk daha fazlasını istiyor sarayınızı basan isyancılardan kaçarken öldünüz." 
                    menu:
                        "Yeniden başla":
                            $ renpy.jump("zero_point")  
                        "Çık":
                            $ renpy.full_restart() 

                        
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
        "dialog85", "dialog86", "dialog87", "dialog88", "dialog89",
        "dialog90", "dialog91", "dialog92", "dialog93", "dialog94",
        "dialog95", "dialog96", "dialog97", "dialog98", "dialog99",
        "dialog100", "dialog101", "dialog102", "dialog103", "dialog104",
        "dialog105", "dialog106", "dialog107", "dialog108", "dialog109",
        "dialog110", "dialog111", "dialog112", "dialog113", "dialog114",
        "dialog115", "dialog116", "dialog117", "dialog118", "dialog119",
        "dialog120", "dialog121", "dialog122", "dialog123", "dialog124",
        "dialog125", "dialog126", "dialog127", "dialog128", "dialog129",
        "dialog130", "dialog131", "dialog132", "dialog133", "dialog134",
        "dialog135", "dialog136", "dialog137", "dialog138", "dialog139",
        "dialog140", "dialog141", "dialog142", "dialog143", "dialog144",
        "dialog145", "dialog146", "dialog147", "dialog148", "dialog149",
        "dialog150", "dialog151", "dialog152", "dialog153", "dialog154",
        "dialog155", "dialog156", "dialog157", "dialog158", "dialog159",
        "dialog160", "dialog161", "dialog162", "dialog163", "dialog164",
        "dialog165", "dialog166", "dialog167", "dialog168", "dialog169",
        "dialog170", "dialog171", "dialog172", "dialog173", "dialog174",
        "dialog175", "dialog176", "dialog177", "dialog178", "dialog179",
        "dialog180", "dialog181", "dialog182", "dialog183", "dialog184",
        "dialog185", "dialog186", "dialog187", "dialog188", "dialog189",
        "dialog190", "dialog191", "dialog192", "dialog193", "dialog194",
        "dialog195", "dialog196", "dialog197", "dialog198", "dialog199",
        "dialog200", "dialog201", "dialog202", "dialog203", "dialog204",
        "dialog205", "dialog206", "dialog207", "dialog208", "dialog209",
        "dialog210", "dialog211", "dialog212", "dialog213", "dialog214",
        "dialog215", "dialog216", "dialog217", "dialog218", "dialog219",
        "dialog220", "dialog221", "dialog222", "dialog223", "dialog224",
        "dialog225", "dialog226", "dialog227", "dialog228", "dialog229",
        "dialog230", "dialog231", "dialog232", "dialog233", "dialog234",
        "dialog235", "dialog236", "dialog237", "dialog238", "dialog239",
        "dialog240", "dialog241", "dialog242", "dialog243", "dialog245",
        "dialog246", "dialog247", "dialog248", "dialog249", "dialog250",
        "dialog251", "dialog252", "dialog253", "dialog254", "dialog255",
        "dialog256", "dialog257", "dialog258", "dialog259", "dialog260",
        "dialog261", "dialog262", "dialog263", "dialog264", "dialog265",
        "dialog266", "dialog267", "dialog268", "dialog269", "dialog270",
        "dialog271", "dialog272", "dialog273", "dialog274", "dialog275",
        "dialog276", "dialog277", "dialog278", "dialog279", "dialog280",
        "dialog281", "dialog282", "dialog283", "dialog284", "dialog285",
        "dialog286", "dialog287", "dialog288", "dialog289", "dialog290",
        "dialog291", "dialog292", "dialog293", "dialog294", "dialog295",
        "dialog296", "dialog297", "dialog298", "dialog299", "dialog300",
        "dialog301", "dialog302", "dialog303", "dialog304", "dialog305",
        "dialog306", "dialog307", "dialog308", "dialog309", "dialog310",
        "dialog311", "dialog312"

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
init python:
    import random

    rune = [
        "rune1", "rune2", "rune3", "rune4", "rune5", "rune6",
        "rune7", "rune8", "rune9", "rune10", "rune11", "rune12",
        "runeabc", "rune"
    ]

init python:# Hikaye metinleri
    import random

    stories = [
        "story1", "story2", "story3", "story4",
        "story5", "boardgame", "story6", "story7",
        "story8", "story9", "story10", "story11",
        "story12"
    ]

label start:
    stop movie
    stop music 
    queue music[
        "audio/Battle_OF_The_Creek.mp3",
        "audio/The_Medieval_Banquet.mp3",
        "audio/Lake_of_Light.mp3"] loop
    show screen bars
    show screen style_start
    show screen sign_hist
    show screen map_button
    show screen run_button
    show screen character_button
    show screen minicard_button
    show screen menu_buttons
    scene startbcg
    show screen managed_day
    show screen date_display
    while True:
        $ zero_chr_scr()
        show Kraliçe at kraliçe_poz
        "Ses testi başlıyor..."
        play voice "audio/deadeffect.mp3" volume 0.5 
        $ renpy.pause(3.0, hard=True) # 3 saniye boyunca oyuncu ekranı geçemez, sesi bekler.
        "Ses çalmış olmalı. Eğer duymadıysan hoparlör veya dosya bitrate ayarlarını kontrol etmelisin."
        Kraliçe "Merhaba Majesteleri… Önünüzde uzun ve zorlu bir hükümdarlık yolu var. Her gün halktan ya da saraydan biri huzurunuza çıkacak ve sizden bir karar vermenizi bekleyecek. Vereceğiniz her karar, ülkemizin din, siyaset, ekonomi, askeri, sağlık ve halkın refahı gibi hayati dengelerini doğrudan etkileyecek."
        Kraliçe "Fakat yalnızca bu değil… İnsanların gönülleri de kararlarınızla şekillenecek. Birine sürekli hayır derseniz, kalbinde size karşı bir kin birikebilir. Ama her isteğini kabul ederseniz, size olan bağlılığı artar. Her kişi farklıdır, her kararın bedeli olur…"
        Kraliçe "Lütfen unutmayın majesteleri; din, sağlık, siyaset, halk, ekonomi ve askerî güç… Bu unsurların biri bile biter yada dolarsa , krallığımız tehlikeye girer. Denge... İşte asıl ihtiyacımız olan budur."
        Kraliçe "Şimdi… Tahtınız sizi bekliyor."
        hide Kraliçe
    
        $ chosen_dialog = get_random_dialog()
        jump expression chosen_dialog
    
label random_dialog:
    if main_story_count ==20:
        jump story1
    elif main_story_count ==35:
        jump story2
    elif main_story_count ==45:
        jump story3
    elif main_story_count ==55 and which_story ==1:
        jump story4
    elif main_story_count ==55 and which_story ==2:
        jump story5
    elif main_story_count ==65 and which_story ==3:
        jump story6
    elif main_story_count ==65 and which_story ==4:
        jump story7
    elif main_story_count ==59 and which_story ==5:
        jump story8
    elif main_story_count ==69 and which_story ==6:
        jump story9
    elif main_story_count ==57 and which_story ==7:
        jump story10
    elif main_story_count ==55 and which_story ==8:
        jump story11
    elif main_story_count == 3 and not minicard_used:
        $ minicard_used = True
        $ chosen_card = renpy.random.choice(minicard_dialogs)
        $ minicard_used = False 
        jump expression chosen_card
    elif main_story_count == 28 and not minicard_used:
        $ minicard_used = True
        $ chosen_card = renpy.random.choice(minicard_dialogs)
        $ minicard_used = False 
        jump expression chosen_card
    else:
        $ chosen_dialog = renpy.random.choice(dialogs)
        jump expression chosen_dialog  # Yeni seçilen diyaloga git

