################################################################################
## Başlatma
################################################################################

## Başlatma uzaklık ifadesi bu dosyadaki başlatma ifadelerinin başka bir
## dosyadaki başlatma ifadelerinden önce çalışmasını sağlar.
init offset = -2

## gui.init çağrısı duyarlı varsayılan stilleri sıfırlar, oyunun en ve boyunu
## ayarlar.
init python:
    gui.init(1280, 720)

## Ekranlarda veya dönüşümlerde geçersiz veya kararsız özellikler için
## kontrolleri etkinleştirin
define config.check_conflicting_properties = True


################################################################################
## GUI Yapılandırma Değişkenleri
################################################################################


## Renkler #####################################################################
##
## Arayüzdeki metin renkleri

## Arayüzde başlık ve vurgulu metinlerde kullanılan bir renk
define gui.accent_color = '#cccc00'

## Bir metin düğmesi seçili ya da fare üstünde değilken kullanılan renk.
define gui.idle_color = '#888888'

## Küçük renk, aynı etkiyi yaratmak için daha parlak/koyu olması gereken küçük
## metin için kullanılır.
define gui.idle_small_color = '#aaaaaa'

## Üstüne fare imleci tutulan düğme ve çubuklar için kullanılan renk.
define gui.hover_color = '#e0e066'

## Odaklanmamış ancak seçilmiş bir metin düğmesi için kullanılan renk. Bir buton
## ancak ekranda ise ya da tercih değeri ise seçilir.
define gui.selected_color = '#ffffff'

## Seçilemeyen bir metin düğmesinde kullanılan renk.
define gui.insensitive_color = '#8888887f'

## Çubukların dolmamış parçaları için kullanılan renk. Direkt olarak
## kullanılmazlar, ancak resimleri yeniden yaratırken kullanılırlar.
define gui.muted_color = '#515100'
define gui.hover_muted_color = '#7a7a00'

## Diyalog ve menü seçimleri için kullanılan renkler.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fontlar ve Font Boyutları ###################################################

## Oyun-içi metin için kullanılan font.
define gui.text_font = "DejaVuSans.ttf"

## Karakter adları için kullanılan font.
define gui.name_text_font = "DejaVuSans.ttf"

## Oyun-dışı metin için kullanılan font.
define gui.interface_text_font = "DejaVuSans.ttf"

## Normal diyalog metni için kullanılan boyut.
define gui.text_size = 22

## Karakter adı boyutu.
define gui.name_text_size = 30

## Oyun arayüzü için kullanılan metin boyutu.
define gui.interface_text_size = 22

## Oyun arayüzünde kullanılan başlık boyutu.
define gui.label_text_size = 24

## Bildirim ekranındaki metin boyutu.
define gui.notify_text_size = 16

## Oyun başlığı boyutu.
define gui.title_text_size = 50


## Ana ve Oyun Menüleri ########################################################

## Ana menü ve oyun menüsü için kullanılan resimler.
define gui.main_menu_background = "gui/main_menu.jpeg"
define gui.game_menu_background = "gui/main_menu.jpeg"


## Diyalog #####################################################################
##
## Bu değişkenler diyaloğun ekranda satır satır nasıl görüneceğini belirler.

## Diyalog metni kutusunun boyu.
define gui.textbox_height = 185

## Metin kutusunun dikey olarak ekrandaki yeri. 0.0 en üst, 0.5 merkez, 1.0 ise
## en alt.
define gui.textbox_yalign = 1.0


## Konuşan karakterin adının metin kutusuna göre yerleştirilmesi. Soldan ya da
## üstten herhangi sayıda piksel olabilir, ya da 0.5 ile ortalanabilir.
define gui.name_xpos = 240
define gui.name_ypos = 0

## Karakter adının yatay hizalanması. 0.0 ile sola yapıştırılabilir, 0.5 ile
## ortalanabilir ve 1.0 ile sağa yapıştırılabilir.
define gui.name_xalign = 0.0

## Karakter adını taşıyan kutunun eni, boyu ve sınırları. Otomatik boyutlandırma
## için seçim yapmayın.
define gui.namebox_width = None
define gui.namebox_height = None

## Karakter adını taşıyan kutunun sınırları, sırasıyla sol, üst, sağ ve alt.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Etkin ise isim kutusunun arkaplanı eğilecek, etkin değil ise arkaplan
## boyutlandırılacak.
define gui.namebox_tile = False


## Metin kutusuna göre diyaloğun yerleştirilmesi. Soldan ya da üstten herhangi
## sayıda piksel olabilir, ya da 0.5 ile ortalanabilir.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## Diyalog metninin piksel olarak maksimum genişliği.
define gui.dialogue_width = 744

## Diyalog metninin yatay hizalandırılması. 0.0 ile sola yapıştırılabilir, 0.5
## ile ortalanabilir ve 1.0 ile sağa yapıştırılabilir.
define gui.dialogue_text_xalign = 0.0


## Düğmeler ####################################################################
##
## Bu değişkenler, gui/button'daki resim dosyaları ile birlikte hangi düğmelerin
## gösterileceğini kontrol eder.

## Bir düğmenin piksel olarak eni ve boyu. Eğer seçilmezse, Ren'Py bir boyut
## hesaplar.
define gui.button_width = None
define gui.button_height = None

## Bir düğmenin sınırları, sırasıyla sol, üst, sağ ve alt.
define gui.button_borders = Borders(4, 4, 4, 4)

## Etkin ise arkaplan resmi eğilecek. Etkin değil ise arkaplan resmi doğrusal
## boyutlandırılacak.
define gui.button_tile = False

## Düğme tarafından kullanılan font.
define gui.button_text_font = gui.interface_text_font

## Düğme tarafından kullanılan metin boyutu.
define gui.button_text_size = gui.interface_text_size

## Düğme metninin değişik durumlardaki rengi.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Düğme metninin yatay hizalandırılması. (0.0 sol, 0.5 merkez, 1.0 sağ).
define gui.button_text_xalign = 0.0


## Bu değişkenler değişik butonlarda kullanılan ayarların üstüne yazılır. Lütfen
## hangi düğmelerin mevcut olduğu ve ne için kullanıldıklarını öğrenmek için gui
## blgelerine bakınız.
##
## Bu yapılandırmalar varsayılan arayüz tarafından kullanılır:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Düzgün isimlendirilmiş değişkenler ekleyerek kendi düzenlemelerinizi de
## yapabilirsiniz. Örneğin bir sonraki yorum satırını aktifleştirerek bit
## navigasyon düğmesinin genişliğini ayarlayabilirsiniz.

# define gui.navigation_button_width = 250


## Seçim Düğmeleri #############################################################
##
## Seçim düğmeleri oyun içi menülerde kullanılır.

define gui.choice_button_width = 900
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Dosya Solut Düğmeleri #######################################################
##
## Bir dosya slotu düğmesi özel bir tür düğmedir. Bir önizleme resmi ve kayıdın
## içeriğine dair bir metin içerir. Diğer düğmeler gibi bir kayıt slotu düğmesi
## de gui/button'daki resimleri kullanır.

## Kayıt slotu düğmesi.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Kayıt slotlarında kullanılan önizleme resminin boy ve eni.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## Kayıt slotlarının gösterildiği satır ve sütun sayısı.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Konumlandırma ve Boşluklar ##################################################
##
## Bu değişkenler değişik kullanıcı arayüzü elemanlarının yerlerini ve
## aralarındaki boşlukları kontrol eder.

## Navigasyon düğmelerinin sol taraflarının ekranın sağına göre konumları.
define gui.navigation_xpos = 100

## Atlama göstergesinin dikey konumu.
define gui.skip_ypos = 10

## Bildirim ekranının dikey konumu.
define gui.notify_ypos = 45

## Menü seçimleri arası boşluk.
define gui.choice_spacing = 22

## Ana menü ve oyun menülerindeki navigasyon bölümündeki düğmeler.
define gui.navigation_spacing = 4

## Tercihler arası boşluk miktarını kontrol eder.
define gui.pref_spacing = 10

## Terchi düğmeleri arası boşluk miktarını kontrol eder.
define gui.pref_button_spacing = 0

## Dosya sayfası düğmeleri arası boşluk.
define gui.page_spacing = 0

## Dosya slotları arası boşluk.
define gui.slot_spacing = 10

## Ana menü metni konumu.
define gui.main_menu_text_xalign = 1.0


## Çerçeveler ##################################################################
##
## Bu değişkenler bir pencere veya üst sayfa olmadığı zaman kullanıcı arayüzü
## elemanlarının görünümünü kontrol eder.

## Genel çerçeveler.
define gui.frame_borders = Borders(4, 4, 4, 4)

## Onay ekranının bir parçası olarak kullanılan çerçeve.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## Atlama ekranının bir parçası olarak kullanılan çerçeve.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## Bildirim ekranının bir parçası olarak kullanılan çerçeve.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Çerçeve arkaplanları eğimli olmalı mı ?
define gui.frame_tile = False


## Çubuklar, Kaydırma Çububkları ve Kaydırıcılar ###############################
##
## Bunlar çubuklar, kaydırma çububkları ve kaydırıcıların boyutunu kontrol eder.
##
## Varsayılan GUI yalnızca kaydırıcıları ve dikey kaydırma çubuklarını kullanır.
## Diğer bütün çubuklar sadece yaratıcı tarafından yazılmış ekranlarda
## kullanılır.

## Yatay çubuklar, kaydırma çububkları ve kaydırıcıların boyu. Dikey çubuklar,
## kaydırma çububkları ve kaydırıcıların eni.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## Eğer çubuk resimleri eğilmeliyse etkin. Eğer doğrusal boyutlandırılmalılar
## ise etkin değil.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Yatay sınırlar.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Dikey sınırlar.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Geçmiş ######################################################################
##
## Geçmiş ekranı oyuncunun halihazırda gördüğü diyaloğu gösterir.

## Ren'Py tarafından tutulacak diyalog bloklarının sayısı.
define config.history_length = 250

## Geçmiş ekranı girişinin boyu. Performans bedeliyle boyu değişken yapmak için
## seçim yapmayın.
define gui.history_height = 140

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Konuşan karakterin isminin konumu, genişliği ve hizalanması.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## Diyalog metninin konumu, genişliği ve hizalanması.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## NVL-Modu ####################################################################
##
## NVL-mod ekran, NVL-mod karakterler tarafından konuşulan diyalogu gösterir.

## NVL-mod arkaplan penceresinin sınırları.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## Ren'Py tarafındad gösterilecek maksimum NVL-modu girişi sayısı. Bundan daha
## çok giriş gösterilmesi gerektiğinde, en eski giriş kaldırılacak.
define gui.nvl_list_length = 6

## NVL-modu girişinin boyu. Boyun dinamik olarak değiştirilmesi için seçim
## yapmayın.
define gui.nvl_height = 115

## gui.nvl_height seçili değilken NVL-modu girişleri arası, aynı zamanda NVL-
## modu menüsü ve NVL-modu girişleri arası boşluk.
define gui.nvl_spacing = 10

## Konuşan karakterin isminin konumu, genişliği ve hizalanması.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## Diyalog metninin konumu, genişliği ve hizalanması.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## nvl_thought metninin konumu, genişliği ve hizalanması (nvl_narrator karakteri
## tarafından konuşulan metin.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## nvl menu_button'ları konumu.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


## Yerelleştirme ###############################################################

## Satırları kırma iznini kontrol eder. Varsayılan ayar pek çok dile
## uygundur. Mevctu bütün değerler https://www.renpy.org/doc/html/
## style_properties.html#style-property-language adresinde bulunabilir.

define gui.language = "unicode"


################################################################################
## Mobil cihazlar
################################################################################

init python:

    ## Hızlı düğmelerin boyutlarını değiştirerek tablet ve telefonlarda
    ## dokunmayı kolaylaştırır.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## Telefonlarda kolayca görünebildiklerinden emin olmak için çeşitli GUI
    ## elemanlarının boy ve aralığını değiştirir.
    @gui.variant
    def small():

        ## Font boyutları.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Metin kutusunun konumunu ayarla.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## Çeiştli şeylerin boy ve aralığını ayarla.
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## Dosya düğmesi düzeni.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-modu.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
