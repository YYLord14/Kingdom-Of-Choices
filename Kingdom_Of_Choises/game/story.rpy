#Oyun hikayesi

label story1:
    show Kadı at kadi_poz 
    hide screen bars
    Kadı "Efendim, sizinle konuşmam gereken bir durum var."
    Kadı "Sayın Kralım bu anahtar size babanızdan mirastır. Eski Kral babanız size bunu vermem için bana vermişti."
    menu:
        "Bu kadar önemliyse neden şimdi veriyorsun?":
            Kadı "Çünkü baban olgunlaşıp iyi bir kral olduğunda bu anahtara ulaşmanı istedi." 
            menu:
                "Peki bu anahtar nereyi açıyor.":
                    Kadı "Bu anahtar taht odasındaki 3. sütunun olduğu yerdeki duvarın orda saklanmış kapıyı açıyor."
                    hide image Kadı
                    "Kadı kapıyı gösterip oradan uzaklaşır  artık gerçek ile baş başasın. Büyük bir kararlılıkla babanın odasındaki gizli kapıyı keşfettin."
                    scene eski_oda
                    "Eski ahşap kapıyı sessizce açtın ve tozlu bir parşömen odasında buldun kendini. Odada dolaşırken, duvarlarda asılı olan eski haritaları ve yazılı belgeleri inceledin. Bir köşede, tozun altında saklı kalmış bir parşömen buldun ve sayfalarını açtın."
                    "Sayfaların arasında Babanın el yazısıyla yazılmış notlar vardı. Kalbin hızla çarpmaya başladı, çünkü bu notlar, babanın ülkeyi kurarken gizemli yaratıklardan yardım aldığını, askerlerinin ateşi yönetebildiğini ve insanlara büyük zulmettiğini anlatıyordu."
                    "Gözyaşları içinde bu karanlık gerçekleri sindirmeye çalışırken, notlardan bir şey daha öğrendin. Baban bu zulmün sonucunda gizemli yaratıkları ülkenin kuzeyindeki bir açıklıkta bırakmıştı."
                    "Babanın yapmış olduğu kötülükleri öğrenmen seni derinden etkiledi. Ancak, artık bu gerçekle yüzleşmek zorundaydın ve bununla birlikte babanın hatalarını düzeltme sorumluluğunu hissettin"
                    "parşömen elinde..."
                    menu:
                        "Tek başına çözmeye çalış":
                            "parşömeni çözmek için saatlerini harcarsın ama birine gösterip yardım almaktan başka çaren kalmaz." #yardım kısmı dahil en sona kadar buraya kopyalanacak
                            menu:
                                "Muhafız başına gösterip ateş kullanan askerleri araştırmaya başlamalıyım.":
                                    scene startbcg
                                    show Muhafız_Başı at muhafiz_basi_poz
                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                    menu:
                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                            scene eski_oda
                                            show Muhafız_Başı at muhafiz_basi_poz
                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                            menu:
                                                "Peki dediğin gibi olsun, Kadı ya soracağım.":
                                                    scene startbcg
                                                    show Kadı at kadi_poz
                                                    Kadı "Efendim bu dedikleriniz imkansız ama babanızın neden böyle şeyler yazdığını bilmiyorum gizli odaya bende girebilirmiyim."
                                                    menu:
                                                        "Tamam gel beraber girelim.": # alttakinin aynısı buray kopyala
                                                            scene eski_oda
                                                            Kadı "Efendim okuduğum bir kaç parşömene göre babanız kadim yaratıklarla iş birliği yapmış. Bu yaratıkların ismi Kögan. Köganlar son derece tehlikeli insan yiyen dev yaratıklardır."
                                                            Kadı "Babanız onlara bir zehir vermiş ve panzehir karşılığında onları zorla savaştırmış. Burda panzehirin bir ilaç olmadığıda yazıyor yani sürekli birinin onlara panzehir tedarik ettiğini düşünebiliriz."
                                                            hide image Kadı
                                                            menu:
                                                                "Köganların yerini bulup onları yok edelim": 
                                                                    scene dev_salon
                                                                    "Ordunun toplanması için bir toplantı düzenledin. Mahiyetini Köganlara saldırmaya ikna ettin."
                                                                    show Yerel_Bakan at yerel_bakan_poz
                                                                    Yerel_Bakan "Efendim büyülü yaratıklarla savaşmak mantıklı değil zehirin nasıl yapıldığını ve panzehiri kimin tedarik ettiğini öğrenirsek panzehiri kesmemiz yeterli olucaktır."
                                                                    menu:
                                                                        "Haklısın değerli bakanım":
                                                                            "Yerel bakanın neden bu görevde olduğunu düşünüp ona hak verdin ve araştırma yapmaya karar verdin."
                                                                            hide image Yerel_Bakan
                                                                            menu:
                                                                                "Panzehri araştırmak için Otacı ile konuşmalıyım": 
                                                                                    scene startbcg
                                                                                    show Otacı at otaci_poz
                                                                                    Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                                    menu:
                                                                                        "Sende benimle gel beraber gidelim.":
                                                                                            Otacı "Üzgünüm efendim ama parşömendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                                            "Tamam sen burda kal."
                                                                                            hide image Otacı
                                                                                            scene gizemli_oda
                                                                                            "Büyücünün yanına gidip olanları anlatırız"
                                                                                            show Büyücü at buyucu_poz
                                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                            hide image Büyücü
                                                                                            menu:
                                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                                    scene startbcg
                                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                                    menu:
                                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                            scene eski_oda
                                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                            menu:
                                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                                    hide image Muhafız_Başı
                                                                                                                    scene startbcg
                                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                                    scene startbcg
                                                                                        "Ben yalnız gideceğim.":
                                                                                            hide image Otacı
                                                                                            "Büyücün yanına gidip olanları anlatırız"
                                                                                            scene gizemli_oda
                                                                                            show Büyücü at buyucu_poz
                                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                            hide image Büyücü
                                                                                            menu:
                                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                                    scene startbcg
                                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                                    menu:
                                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                            scene eski_oda
                                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                            menu:
                                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                                    hide image Muhafız_Başı
                                                                                                                    scene startbcg
                                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                                    scene startbcg
                                                                
                                                                        "Ben kararımı verdim, SAVAŞA HAZIRLANIN!": # Köganlara saldırmak için savaş kararı aldırmak ###############################
                                                                            hide image Yerel_Bakan
                                                                            "Yerel Bakanın dediklerini önemsemedin."
                                                                            scene dev_salon
                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                            Muhafız_Başı "Emredin Kralım."
                                                                            menu:
                                                                                "Halkı savaştan haberdar et ve seferberlik ilan et.":
                                                                                    Muhafız_Başı "Orduları hazırladım efendim"
                                                                                    menu:
                                                                                        "Kuzeye ilerliyoruz!":
                                                                                            hide image Muhafız_Başı
                                                                                            scene orman
                                                                                            "Kuzeye parşömende yazılan yere doğru ilerledin ve önünde ladin ağaçlarından yapılmış bir sur gördün üstünde Aquila Krallığının simgeleri var. Ama kimse yaşamıyor."
                                                                                            scene kuzeykale
                                                                                            menu:
                                                                                                "Bir bölük asker surlara tırmansın!":
                                                                                                    "Askerlerinin bazılarını surlara tırmandırdın ve sana içerisinin ağaçlık bir alan olduğunu ve güvenli olduğunu söylediler. Ordunla birlikte içeriye girdin."
                                                                                                    "Bir süre sonra köganlar üstünüze hücum etti 3 metre boyunda olan bu yaratıklar eline geçen askerleri parçalayıp yiyorlardı."
                                                                                                    "Hemen dağılan ordunu düzene soktun ve surun üstüne yerleştirdiğin okçulardan destek alarak savaştın ."
                                                                                                    "Atının üstünden savaşarak bir çok köganı indirdin askerlerin karşı koyamıyor ve hepsi teker teker ölüyordu okçularının desteğiyle ufak bir boşluk yakalayıp küçük bir birlik ile kaçmayı başardın."
                                                                                                    "Ordunun nerdeyse hepsi katledildi ancak köganların az bir kısmını öldürebildiniz."
                                                                                                    menu:
                                                                                                        "Aquila Krallığına dönmeye çalışmalıyız.":
                                                                                                            play sound deadeffect
                                                                                                            "Kaçmaya çalışırken Köganlar yetiştiler ve ordunu yok ettiler ölüm senin için bir kurtuluş oldu." #SON###########
                                                                                                            scene koganson
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                                                                        "En yakın yerde kamp kurup ordumuzu düzene sokup, yaralıları dinlendirmeliyiz.":
                                                                                                            scene gecekamp
                                                                                                            "Kamp kurdun ve ordunu düzene soktun. Köganların uzaktan hızla orduna yaklaştığını gördün."
                                                                                                            menu:
                                                                                                                "Okçular saldırın Savaş düzenine geçiyoruz!":
                                                                                                                    "Okçular köganlar yaklaşmadan bir kaç tanesini indirdi Köganlar saldırıya geçip ordunu yok etti sadece 3-5 tane Kögan kaldı ve tek başına kaldın"
                                                                                                                    menu:
                                                                                                                        "Kaç":
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                        "Savaş": #alt satır SON #############
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                "Askerler! atlara binin vur kaç yapacağız!":
                                                                                                                    "Büyük bir kısmını indirdiniz uzun bir mesafe kaçarak köganların sayısını azalttın tüm ordun yok edildi sadece 3-5 tane kögan kaldı ve tek kaldın."
                                                                                                                    menu:
                                                                                                                        "Kaç":
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                        "Savaş": #alt satır SON #############
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()
                                                                                                "Sur kapısını kırın içeri giriyoruz.":
                                                                                                    "Bir süre ilerledikten sonra aniden 3 metrelik devasa yaratıklar ordunun üstüne doğru koşmaya başladı savunma düzeni almaya çalıştın ama ordunun düzeni bozuldu bazıları kaçmaya çalıştı ama Köganlar eline geçen askelerin kafalarını ısırıyor elleriyle ikiye bölüyor parçalıyorlardı."
                                                                                                    menu:
                                                                                                        "Kaç":
                                                                                                            scene koganson
                                                                                                            play sound deadeffect
                                                                                                            "Ordun katledilerken kaçtın. uzun bir süre at koşturduktan sonra köganlar senin peşinden geldi ve seni yakalayıp parçalara ayırdılar."#SON##################
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                                                                        "Askerler! Savaş düzeni ÇEMBEER!": 
                                                                                                            scene koganson
                                                                                                            play sound deadeffect
                                                                                                            "Askerlerinin bir kısmı hala sana sadık ve kendi birliğinle bir düzen oturtmayı başardın Atlarınızdan inmeyerek bir şekilde aradaki boy  farkını kapattınız bir kaç tane köganı indirdin eline onların mor kanları bulaştı kaçmaya çalışan ordun katledildi."
                                                                                                            "Etraf kan götürüyor ordun daki askerler yavaş yavaş düşüyor geriye muhafız başı ile sen kaldın bir kaç tanesini de öldürdükten sonra ikinizde öldünüz."
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                                "Köganlara kimin panzehir verdiğini araştıralım.":
                                                                    menu:                                                               
                                                                        "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                            scene startbcg
                                                                            show Şifacı at sifaci_poz
                                                                            Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                            hide image Şifacı
                                                                            menu:
                                                                                "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                                    show Otacı at otaci_poz
                                                                                    Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                                    menu:
                                                                                        "Ben yalnız gideceğim.":
                                                                                            hide image Otacı
                                                                                            "Büyücün yanına gidip olanları anlatırız"
                                                                                            scene gizemli_oda
                                                                                            show Büyücü at buyucu_poz
                                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                            hide image Büyücü
                                                                                            menu:
                                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                                    scene startbcg
                                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                                    menu:
                                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                            menu:
                                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                                    hide image Muhafız_Başı
                                                                                                                    scene startbcg
                                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                                    scene startbcg
                                                                        "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                            scene startbcg
                                                                            show Otacı at otaci_poz
                                                                            Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                            menu:
                                                                                "Ben yalnız gideceğim.":
                                                                                    hide image Otacı
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    scene gizemli_oda
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            scene startbcg
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                            scene startbcg
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                            scene startbcg                                           
                                        "Peki dediğin gibi olsun, Kadı ya soracağım.":
                                            scene startbcg
                                            show Kadı at kadi_poz
                                            Kadı "Efendim bu dedikleriniz imkansız ama babanızın neden böyle şeyler yazdığını bilmiyorum gizli odaya bende girebilirmiyim."
                                            menu:
                                                "Tamam gel beraber girelim.": # alttakinin aynısı buray kopyala
                                                    scene eski_oda
                                                    Kadı "Efendim okuduğum bir kaç parşömene göre babanız kadim yaratıklarla iş birliği yapmış. Bu yaratıkların ismi Kögan. Köganlar son derece tehlikeli insan yiyen dev yaratıklardır."
                                                    Kadı "Babanız onlara bir zehir vermiş ve panzehir karşılığında onları zorla savaştırmış. Burda panzehirin bir ilaç olmadığıda yazıyor yani sürekli birinin onlara panzehir tedarik ettiğini düşünebiliriz."
                                                    hide image Kadı
                                                    menu:
                                                        "Köganların yerini bulup onları yok edelim": 
                                                            scene dev_salon
                                                            "Ordunun toplanması için bir toplantı düzenledin. Mahiyetini Köganlara saldırmaya ikna ettin."
                                                            show Yerel_Bakan at yerel_bakan_poz
                                                            Yerel_Bakan "Efendim büyülü yaratıklarla savaşmak mantıklı değil zehirin nasıl yapıldığını ve panzehiri kimin tedarik ettiğini öğrenirsek panzehiri kesmemiz yeterli olucaktır."
                                                            menu:
                                                                "Haklısın değerli bakanım":
                                                                    "Yerel bakanın neden bu görevde olduğunu düşünüp ona hak verdin ve araştırma yapmaya karar verdin."
                                                                    hide image Yerel_Bakan
                                                                    menu:
                                                                        "Panzehiri araştırmak için Otacı ile konuşmalıyım": 
                                                                            scene startbcg
                                                                            show Otacı at otaci_poz
                                                                            Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                            menu:
                                                                                "Sende benimle gel beraber gidelim.":
                                                                                    Otacı "Üzgünüm efendim ama parşömendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                                    "Tamam sen burda kal."
                                                                                    hide image Otacı
                                                                                    scene gizemli_oda
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            scene startbcg
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    scene eski_oda
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                            scene startbcg
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                            scene startbcg
                                                                                "Ben yalnız gideceğim.":
                                                                                    hide image Otacı
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    scene gizemli_oda
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            scene startbcg
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    scene eski_oda
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                            scene startbcg
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                            scene startbcg
                                                                    
                                                                "Ben kararımı verdim, SAVAŞA HAZIRLANIN!": # Köganlara saldırmak için savaş kararı aldırmak ###############################
                                                                            hide image Yerel_Bakan
                                                                            "Yerel Bakanın dediklerini önemsemedin."
                                                                            scene dev_salon
                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                            Muhafız_Başı "Emredin Kralım."
                                                                            menu:
                                                                                "Halkı savaştan haberdar et ve seferberlik ilan et.":
                                                                                    Muhafız_Başı "Orduları hazırladım efendim"
                                                                                    menu:
                                                                                        "Kuzeye ilerliyoruz!":
                                                                                            hide image Muhafız_Başı
                                                                                            scene orman
                                                                                            "Kuzeye parşömende yazılan yere doğru ilerledin ve önünde ladin ağaçlarından yapılmış bir sur gördün üstünde Aquila Krallığının simgeleri var. Ama kimse yaşamıyor."
                                                                                            scene kuzeykale
                                                                                            menu:
                                                                                                "Bir bölük asker surlara tırmansın!":
                                                                                                    "Askerlerinin bazılarını surlara tırmandırdın ve sana içerisinin ağaçlık bir alan olduğunu ve güvenli olduğunu söylediler. Ordunla birlikte içeriye girdin."
                                                                                                    "Bir süre sonra köganlar üstünüze hücum etti 3 metre boyunda olan bu yaratıklar eline geçen askerleri parçalayıp yiyorlardı."
                                                                                                    "Hemen dağılan ordunu düzene soktun ve surun üstüne yerleştirdiğin okçulardan destek alarak savaştın ."
                                                                                                    "Atının üstünden savaşarak bir çok köganı indirdin askerlerin karşı koyamıyor ve hepsi teker teker ölüyordu okçularının desteğiyle ufak bir boşluk yakalayıp küçük bir birlik ile kaçmayı başardın."
                                                                                                    "Ordunun nerdeyse hepsi katledildi ancak köganların az bir kısmını öldürebildiniz."
                                                                                                    menu:
                                                                                                        "Aquila Krallığına dönmeye çalışmalıyız.":
                                                                                                            scene koganson
                                                                                                            play sound deadeffect
                                                                                                            "Kaçmaya çalışırken Köganlar yetiştiler ve ordunu yok ettiler ölüm senin için bir kurtuluş oldu." #SON###########
                                                                    
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                                                                        "En yakın yerde kamp kurup ordumuzu düzene sokup, yaralıları dinlendirmeliyiz.":
                                                                                                            scene gecekamp
                                                                                                            "Kamp kurdun ve ordunu düzene soktun. Köganların uzaktan hızla orduna yaklaştığını gördün."
                                                                                                            menu:
                                                                                                                "Okçular saldırın Savaş düzenine geçiyoruz!":
                                                                                                                    "Okçular köganlar yaklaşmadan bir kaç tanesini indirdi Köganlar saldırıya geçip ordunu yok etti sadece 3-5 tane Kögan kaldı ve tek başına kaldın"
                                                                                                                    menu:
                                                                                                                        "Kaç":
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                        "Savaş": #alt satır SON #############
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                "Askerler! atlara binin vur kaç yapacağız!":
                                                                                                                    "Büyük bir kısmını indirdiniz uzun bir mesafe kaçarak köganların sayısını azalttın tüm ordun yok edildi sadece 3-5 tane kögan kaldı ve tek kaldın."
                                                                                                                    menu:
                                                                                                                        "Kaç":
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()

                                                                                                                        "Savaş": #alt satır SON #############
                                                                                                                            scene koganson
                                                                                                                            play sound deadeffect
                                                                                                                            "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                                            menu:
                                                                                                                                "Çıkış":
                                                                                                                                    $ renpy.full_restart()
                                                                                                "Sur kapısını kırın içeri giriyoruz.":
                                                                                                    "Bir süre ilerledikten sonra aniden 3 metrelik devasa yaratıklar ordunun üstüne doğru koşmaya başladı savunma düzeni almaya çalıştın ama ordunun düzeni bozuldu bazıları kaçmaya çalıştı ama Köganlar eline geçen askelerin kafalarını ısırıyor elleriyle ekiye bölüyor paraçlaıyolarlardı ."
                                                                                                    menu:
                                                                                                        "Kaç":
                                                                                                            scene koganson
                                                                                                            play sound deadeffect
                                                                                                            "Ordun katledilerken kaçtın. uzun bir süre at koşturduktan sonra köganlar senin peşinden geldi ve seni yakalayıp parçalara ayırdılar."#SON##################
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                                                                        "Askerler! Savaş düzeni ÇEMBEER!": 
                                                                                                            scene koganson
                                                                                                            play sound deadeffect
                                                                                                            "Askerlerinin bir kısmı hala sana sadık ve kendi birliğinle bir düzen oturtmayı başardın Atlarınızdan inmeyerek bir şekilde aradaki boy  farkını kapattınız bir kaç tane köganı indirdin eline onların mor kanları bulaştı kaçmaya çalışan ordun katledildi. etraf kan götürüyor ordun daki askerler yavaş yavaş düşüyor geriye muhafız başı ile sen kaldın bir kaç tanesini de öldürdükten sonra ikinizde öldünüz"
                                                                                                            menu:
                                                                                                                "Çıkış":
                                                                                                                    $ renpy.full_restart()

                                                        "Köganlara kimin panzehir verdiğini araştıralım.":
                                                            menu:                                                               
                                                                "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                    scene startbcg
                                                                    show Şifacı at sifaci_poz
                                                                    Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                    hide image Şifacı
                                                                    menu:
                                                                        "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                            show Otacı at otaci_poz
                                                                            Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                            menu:
                                                                                "Sende benimle gel beraber gidelim.":
                                                                                    Otacı "Üzgünüm efendim ama parşömendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                                    "Tamam sen burda kal."
                                                                                    hide image Otacı
                                                                                "Ben yalnız gideceğim.":
                                                                                    hide image Otacı
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    scene gizemli_oda
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            scene startbcg
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                            scene startbcg
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                            scene startbcg
                                                                "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                    scene startbcg
                                                                    show Otacı at otaci_poz
                                                                    Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                    menu:
                                                                        "Sende benimle gel beraber gidelim.":
                                                                            Otacı "Üzgünüm efendim ama parşömendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                            "Tamam sen burda kal."
                                                                            hide image Otacı
                                                                        "Ben yalnız gideceğim.":
                                                                            hide image Otacı
                                                                            "Büyücün yanına gidip olanları anlatırız"
                                                                            scene gizemli_oda
                                                                            show Büyücü at buyucu_poz
                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                            hide image Büyücü
                                                                            menu:
                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                    scene startbcg
                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                    menu:
                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                            menu:
                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                    hide image Muhafız_Başı
                                                                                                    scene startbcg
                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                                                    scene startbcg
                                

    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story2:
    scene startbcg
    hide screen bars
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Efendim emrettiğiniz gibi araştırmamı tamamladım Eski Lider Yardımcısının yerini buldum."
    menu:
        "Güzel, birliğimle yola çıkıyorum.":
            Muhafız_Başı "Emredersiniz efendim."
            hide image Muhafız_Başı
            scene orman3
            "Uzun süren yolculuk sonunda son bulur."
            scene kasaba
            "..."
            show Lider_Yardımcısı at Lider_yardimcisi_poz
            Lider_Yardımcısı "Sende kimsin?"
            $ unlock_level(13)
            menu:
                "Ben Aquila'nın yeni Kralı, sana sorularım var.":
                    Lider_Yardımcısı "Bende seni bekliyordum."
                    Lider_Yardımcısı "Gel otur şöyle şerbetim var içermisin?"
                    menu:
                        "Tabi.":
                            Lider_Yardımcısı "Baban ülkenin aynı zamanda Yargea, Eternas ve Narga Krallıkları ile savaşta olduğu dönemde kendi babasını kaybetti ve erken yaşta tahta oturdu. Babanın üç farklı savaşı tek başına yönetmesi gerekiyordu."
                            Lider_Yardımcısı "Aquila Krallığı için karanlık bir dönemdi ama seninde bileceğin gibi topraklarımızın bir kısmını kaybetsekte başarılı savaşlar çıkarıp ülkemizi koruduk ama kimse bunun nasıl yapıldığını bilmiyor."
                            Lider_Yardımcısı "Baban askerleri sadece Narga Krallığı ile olan savaşa götürdü Yargea ve Eternas ile olan savaşlarda Köganlardan yardım aldı"
                            menu:
                                "Köganlar hakkında ne biliyosun, anlat.":
                                    Lider_Yardımcısı "Köganlar boyları 3 metreye varabilen mavi yaratıklardır. İnsan yiyen bu kadim yaratıklar çok tehlikelidir."
                                    Lider_Yardımcısı "Baban Köganlar ile bir anlaşma yaptı. Onları güçlü kılan insan etiyle besledi ve kendisi için savaşmalarına ikna etti"
                                    Lider_Yardımcısı "Köganların lideri ona tamamen bağlı olmayabilirdi sonuçta Aquila Krallığı zor zamanlardan geçiyordu ve baban Köganları insan ile beslerken tüm insanların kanına zehir enjekte etti"
                                    menu:
                                        "Bana bu zehirden bahset":
                                            Lider_Yardımcısı "Bu zehir onları panzehir almazlarsa yavaş yavaş kaslarını durdurup felç ediyor sonrada öldürüyordu."
                                            Lider_Yardımcısı "Bunu öğrenen köganların lideri çok sinirlendi ve babanın ordusuna saldırdı çok kayıp verdiler ama zehirin etkisiyle köganlar yenildi. "
                                            Lider_Yardımcısı "Baban onları kendi için savaşmalarına ikna etmek için zehirden kendiside içti."
                                            menu:
                                                "Babam bilerek kendinimi zehirledi.":
                                                    Lider_Yardımcısı "Yaptığı bu fedakarlık Köganların güvenini kazandı. Bu şekilde 15 günde 1 kez panzehir almak için sürekli ülkenin kuzeyine köganların yanına gidiyordu."
                                                    menu:
                                                        "Babamın sürekli gizlice bir yerlere gittiğini hatırlıyorum.":
                                                            Lider_Yardımcısı "Zehrin panzehrini ülkedeki büyücü yapıyordu zehride o yapmıştı sonra zaten bildiğin gibi baban büyücüden yardım alarak herkesin hafızasını sildi. Buna Eternas ve Yargea halkı da dahil."
                                                            Lider_Yardımcısı "Bu şekilde Aquila krallığının sağlam temelleri atıldı. "
                                                            Lider_Yardımcısı "Baban kara büyü kullanıp herkesin hafızasını silince bazı yan etkileri oldu, askerler ateşi yönetme yeteneğine sahip oldu ama bunu yapabilen çok az asker kaldı."
                                                            Lider_Yardımcısı "Babanda yaptığı büyünün bedelini canıyla ödedi şimdi senin yapman gereken köganlara panzehir götürmeye devam etmek bu işi uzun zamandır ben yapıyorum. "
                                                            menu:
                                                                "Bana Panzehiri nasıl elde edeceğimi anlat.":
                                                                    Lider_Yardımcısı "Peki, bu kağıdı büyücüye ver o sana herşeyi anlatacaktır."
                                                                    hide image Lider_Yardımcısı
                                                                    scene gizemli_oda
                                                                    show Büyücü at buyucu_poz
                                                                    Büyücü "Aynı zehirden sanada içirmiş, artık sende baban gibi bu panzehire muhtaçsın."
                                                                    Büyücü "Panzehiri ben yaptım, parşömeni bulduğun yere geri dön ve aramaya devam et baban onu o odada bir yere saklamış olmalı."
                                                                    hide image Büyücü
                                                                    scene eski_oda ########################################################################### alttaki kod buraya yapıştıralacak paralel.
                                                                    "Eski kütüphaneye tekrar girdin. Bir kaç gün süren araştırmanın ardından. Antik bir dilde yazılmış bir parşömen bulursun."
                                                                    scene tunelgiris
                                                                    "parşömeni yerinden aldığında bir kapı açılır"
                                                                    menu:
                                                                        "parşömeni Kütüphaneciye sor.":
                                                                            scene startbcg
                                                                            show Kütüphaneci at kutuphaneci_poz
                                                                            Kütüphaneci "Efendim ne yazdığını tam olarak anlayamadım ama şöyle bir şifre var 'Δ bir , O sıfır, X bir, K bir' bu nedemek bilmiyorum."
                                                                            menu:
                                                                                "Tamam teşekkür ederim aklımda tutacağım. Şimdi o kapıya gidiyorum":
                                                                                    scene tunelgiris
                                                                                    hide image Kütüphaneci
                                                                                    "Açılan kapıdan aşağı indin ve biraz yürüdükten sonra karşına 2 adet tünel çıktı."
                                                                                    scene tunel_k
                                                                                    menu:
                                                                                        "Soldan git":
                                                                                            "Tünelde aldığın bir koku seni korkuttu ve geri dönüp sağdan gitmeye karar verdin."
                                                                                            scene tunel_ucgan #### Delta kapısı
                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."    
                                                                                            menu:
                                                                                                "Soldan git":
                                                                                                        scene tuneldead
                                                                                                        "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                        play sound deadeffect
                                                                                                        "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                        menu:
                                                                                                            "Çık":
                                                                                                                $ renpy.full_restart()
                                                                                        
                                                                                                "Sağdan git":
                                                                                                    scene tunel_o #### O kapısı
                                                                                                    "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                    menu:
                                                                                                        "Soldan git":
                                                                                                            scene tunel_x #### X Kapısı
                                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                            menu:
                                                                                                                "Soldan git.":
                                                                                                                        scene tuneldead
                                                                                                                        "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                                        play sound deadeffect
                                                                                                                        "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                                        menu:
                                                                                                                            "Çık":
                                                                                                                                $ renpy.full_restart()
                                                                                                                "Sağdan git.":
                                                                                                                    scene parola
                                                                                                                    "Tünellerde ilerleme devam ediyorsun artık bu yürüyüşlerden sıkılmaya başladın ve karşına şifreli bir kapı geliyor."
                                                                                                                    menu:
                                                                                                                        "Δ , O , K , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                            
                                                                                                                        "Δ , K , O , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                        "K , Δ , O , X":
                                                                                                                            "Doğru konbinasyonu yaptın."
                                                                                                                            scene lahit
                                                                                                                            "Tozlanmış  bir odaya geldin bir kitapçıkta panzehiri nasıl yapacağın anlatılıyor."
                                                                                                                            "Panzehiri yapman için Köganların Liderinin saç tellerine ihtiyacın olduğunu öğrendin, yani Köganlarla birbirinize bağlısınız."
                                                                                                                            "Eski odada sana uzun süre yeticek malzeme var."
                                                                                                                            menu:
                                                                                                                                "Taht odasına çık":
                                                                                                                                    $ unlock_level(14)
                                                                                                                                    scene startbcg
                                                                                                                                    show Şifacı at sifaci_poz
                                                                                                                                    "Sana gösterdiğim odaya gitmeni ve bana panzehir üretmeni istiyorum."
                                                                                                                                    Şifacı "Emredersiniz efendim. Elimizdeki malzemeleri en iyi şekilde kullanacağım." ###### burda story2 bitti devam edecek.
                                                                                                                                    hide image Şifacı
                                                                                                                            
                                                                                                                        "K , Δ , X , O":
                                                                                                                            scene parola_tuzak 
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                        "Sağdan git":
                                                                                                            scene tuneldead
                                                                                                            "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                            play sound deadeffect
                                                                                                            "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                            menu:
                                                                                                                "Çık":
                                                                                                                    $ renpy.full_restart()                              
                                                                                                
                                                                                        "Sağdan git":
                                                                                            scene tunel_ucgan #### Delta kapısı
                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."    
                                                                                            menu:
                                                                                                "Soldan git":
                                                                                                    "Tünelde aldığın bir koku seni korkuttu ve geri dönüp sağdan gitmeye karar verdin."
                                                                                                    scene tunel_o #### O kapısı
                                                                                                    "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                    menu:
                                                                                                        "Soldan git":
                                                                                                            scene tunel_x #### X Kapısı
                                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                            menu:
                                                                                                                "Soldan git.":
                                                                                                                        scene tuneldead
                                                                                                                        "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                                        play sound deadeffect
                                                                                                                        "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                                        menu:
                                                                                                                            "Çık":
                                                                                                                                $ renpy.full_restart()
                                                    
                                                                                                                "Sağdan git.":
                                                                                                                    scene parola
                                                                                                                    "Tünellerde ilerleme devam ediyorsun artık bu yürüyüşlerden sıkılmaya başladın ve karşına şifreli bir kapı geliyor."
                                                                                                                    menu:
                                                                                                                        "Δ , O , K , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                            
                                                                                                                        "Δ , K , O , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                        "K , Δ , O , X":
                                                                                                                            "Doğru konbinasyonu yaptın."
                                                                                                                            scene lahit
                                                                                                                            "Tozlanmış  bir odaya geldin bir kitapçıkta panzehiri nasıl yapacağın anlatılıyor."
                                                                                                                            "Panzehiri yapman için Köganların Liderinin saç tellerine ihtiyacın olduğunu öğrendin, yani Köganlarla birbirinize bağlısınız."
                                                                                                                            "Eski odada sana uzun süre yeticek malzeme var."
                                                                                                                            menu:
                                                                                                                                "Taht odasına çık":
                                                                                                                                    $ unlock_level(14)
                                                                                                                                    scene startbcg
                                                                                                                                    show Şifacı at sifaci_poz
                                                                                                                                    "Sana gösterdiğim odaya gitmeni ve bana panzehir üretmeni istiyorum."
                                                                                                                                    Şifacı "Emredersiniz efendim. Elimizdeki malzemeleri en iyi şekilde kullanacağım." ###### burda story2 bitti devam edecek.
                                                                                                                                    hide image Şifacı
                                                                                                                            
                                                                                                                        "K , Δ , X , O":
                                                                                                                            scene parola_tuzak 
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                        "Sağdan git":
                                                                                                                scene tuneldead
                                                                                                                "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                                play sound deadeffect
                                                                                                                "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                                menu:
                                                                                                                    "Çık":
                                                                                                                        $ renpy.full_restart()
                                                                                                        
                                                                                                "Sağdan git":
                                                                                                    scene tunel_o #### O kapısı
                                                                                                    "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                    menu:
                                                                                                        "Soldan git":
                                                                                                            scene tunel_x #### X Kapısı
                                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                            menu:
                                                                                                                "Soldan git.":
                                                                                                                    "Tünelde aldığın bir koku seni korkuttu ve geri dönüp sağdan gitmeye karar verdin."
                                                                                                                    scene parola
                                                                                                                    "Tünellerde ilerleme devam ediyorsun artık bu yürüyüşlerden sıkılmaya başladın ve karşına şifreli bir kapı geliyor."
                                                                                                                    menu:
                                                                                                                        "Δ , O , K , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                            
                                                                                                                        "Δ , K , O , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                        "K , Δ , O , X":
                                                                                                                            "Doğru konbinasyonu yaptın."
                                                                                                                            scene lahit
                                                                                                                            "Tozlanmış  bir odaya geldin bir kitapçıkta panzehiri nasıl yapacağın anlatılıyor."
                                                                                                                            "Panzehiri yapman için Köganların Liderinin saç tellerine ihtiyacın olduğunu öğrendin, yani Köganlarla birbirinize bağlısınız."
                                                                                                                            "Eski odada sana uzun süre yeticek malzeme var."
                                                                                                                            menu:
                                                                                                                                "Taht odasına çık":
                                                                                                                                    $ unlock_level(14)
                                                                                                                                    scene startbcg
                                                                                                                                    show Şifacı at sifaci_poz
                                                                                                                                    "Sana gösterdiğim odaya gitmeni ve bana panzehir üretmeni istiyorum."
                                                                                                                                    Şifacı "Emredersiniz efendim. Elimizdeki malzemeleri en iyi şekilde kullanacağım." ###### burda story2 bitti devam edecek.
                                                                                                                                    hide image Şifacı
                                                                                                                            
                                                                                                                        "K , Δ , X , O":
                                                                                                                            scene parola_tuzak 
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                "Sağdan git.":
                                                                                                                    scene parola
                                                                                                                    "Tünellerde ilerleme devam ediyorsun artık bu yürüyüşlerden sıkılmaya başladın ve karşına şifreli bir kapı geliyor."
                                                                                                                    menu:
                                                                                                                        "Δ , O , K , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                            
                                                                                                                        "Δ , K , O , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                        "K , Δ , O , X":
                                                                                                                            "Doğru konbinasyonu yaptın."
                                                                                                                            scene lahit
                                                                                                                            "Tozlanmış  bir odaya geldin bir kitapçıkta panzehiri nasıl yapacağın anlatılıyor."
                                                                                                                            "Panzehiri yapman için Köganların Liderinin saç tellerine ihtiyacın olduğunu öğrendin, yani Köganlarla birbirinize bağlısınız."
                                                                                                                            "Eski odada sana uzun süre yeticek malzeme var."
                                                                                                                            menu:
                                                                                                                                "Taht odasına çık":
                                                                                                                                    $ unlock_level(14)
                                                                                                                                    scene startbcg
                                                                                                                                    show Şifacı at sifaci_poz
                                                                                                                                    "Sana gösterdiğim odaya gitmeni ve bana panzehir üretmeni istiyorum."
                                                                                                                                    Şifacı "Emredersiniz efendim. Elimizdeki malzemeleri en iyi şekilde kullanacağım." ###### burda story2 bitti devam edecek.
                                                                                                                                    hide image Şifacı
                                                                                                                            
                                                                                                                        "K , Δ , X , O":
                                                                                                                            scene parola_tuzak 
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                        "Sağdan git":
                                                                                                            "Tünelde aldığın bir koku seni korkuttu ve geri dönüp soldan gitmeye karar verdin."
                                                                                                            scene tunel_x #### X Kapısı
                                                                                                            "Tünelde biraz daha ilerdin ve karşına tekrar 2 kapı geldi."
                                                                                                            menu:
                                                                                                                "Soldan git.":
                                                                                                                    scene tuneldead
                                                                                                                    "Tünelde bir süre ilerledikten sonra bir koku dikkatini çekti artık zar zor nefes alıyorsun hemen geri dönmeyi düşünüyorsun ama başaramıyorsun."
                                                                                                                    play sound deadeffect
                                                                                                                    "Tahtının altındaki tünellerin içinde zehirli dumanı soluya soluya can veriyosun ve cesedini kimse bulamıyor."
                                                                                                                    menu:
                                                                                                                        "Çık":
                                                                                                                            $ renpy.full_restart()
                                                                                                                    
                                                                                                                "Sağdan git.":
                                                                                                                    scene parola
                                                                                                                    "Tünellerde ilerleme devam ediyorsun artık bu yürüyüşlerden sıkılmaya başladın ve karşına şifreli bir kapı geliyor."
                                                                                                                    menu:
                                                                                                                        "Δ , O , K , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                            
                                                                                                                        "Δ , K , O , X":
                                                                                                                            scene parola_tuzak
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()
                                                                                                                        "K , Δ , O , X":
                                                                                                                            "Doğru konbinasyonu yaptın."
                                                                                                                            scene lahit
                                                                                                                            "Tozlanmış  bir odaya geldin bir kitapçıkta panzehiri nasıl yapacağın anlatılıyor."
                                                                                                                            "Panzehiri yapman için Köganların Liderinin saç tellerine ihtiyacın olduğunu öğrendin yani Köganlarla birbirinize bağlısınız."
                                                                                                                            "Eski odada sana uzun süre yeticek malzeme var."
                                                                                                                            menu:
                                                                                                                                "Taht odasına çık":
                                                                                                                                    $ unlock_level(14)
                                                                                                                                    scene startbcg
                                                                                                                                    show Şifacı at sifaci_poz
                                                                                                                                    "Sana gösterdiğim odaya gitmeni ve bana panzehir üretmeni istiyorum."
                                                                                                                                    Şifacı "Emredersiniz efendim. Elimizdeki malzemeleri en iyi şekilde kullanacağım." ###### burda story2 bitti devam edecek.
                                                                                                                                    hide image Şifacı
                                                                                                                            
                                                                                                                        "K , Δ , X , O":
                                                                                                                            scene parola_tuzak 
                                                                                                                            play sound deadeffect
                                                                                                                            "Yanlış kombinasyonu oluşturdun ve zemin ayaklarının altından kaydı."
                                                                                                                            menu:
                                                                                                                                "Çık":
                                                                                                                                    $ renpy.full_restart()

                                                                
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return
                                                                  
label story3:
    scene startbcg
    hide screen bars
    show Şifacı at sifaci_poz
    Şifacı "Efendim emrettiğiniz gibi parşömendeki tarifi kullanarak panzehir ürettim."
    $ unlock_level(15)
    menu:
        "Tamamdır. Komutana haber ver huzuruma çıksın hemen.":
            Şifacı "Emredersiniz efendim."
            hide image Şifacı
            show Komutan at komutan_poz
            Komutan "Efendim beni emretmişsiniz."
            menu:
                "Bölüğünü hazırla gidiyoruz.":
                    Komutan "Nereye gidiyoruz efendim?"
                    menu: 
                        "Kuzeye gidiyoruz. Şifacının getirdiği el arabasını götüreceğiz.":
                            Komutan "Başüstüne Kralım. Ama orası yıllardır terk edilmiş neden oraya gidiyoruz?"
                            menu:
                                "Çok fazla soru soruyorsun hadi işinin başına.":
                                    hide image komutan
                                    scene orman 
                                    "Bir süre ormanda ilerledikten sonra Kuzeye ulaşıyorsunuz."
                                    scene kuzeykale 
                                    "Kuzey kalesine yaklaştınız."
                                    scene kuzeykaleon
                                    Komutan "Efendim burda kimse yok demiştim."
                                    menu:
                                        "Sessiz ol.":
                                            "Biraz daha ilerledikten sorna etrafınız 3 metrelik dev mavi yaratıklar tarafından sarılır."
                                            scene orman
                                            menu:
                                                "savaş düzenine geç!":
                                                    "Ordun savaş düzenine geçer."
                                                    "Köganlar tehdit algılar ve size saldırmak üzere hareketlenirler."
                                                    "Daha okunu yayına koymadan bölüğünün yarısı acımasızca katledilir."
                                                    scene koganson
                                                    play sound deadeffect
                                                    "Bir kaç köganı alt etmeyi başarırsın ama sonunda sende uzuvların koparılarak ölürsün."
                                                    menu:
                                                        "Çık":
                                                            $ renpy.full_restart()
                                                "Panzehir arabasından bir şişe al ve kaldır.":
                                                    "Şişeyi kaldırdığında Köganlar durdu."
                                                    "Kögan lideri kalabalığın içinden sıyrıldı."
                                                    show Kögan_Lideri at Kogan_poz
                                                    Kögan_Lideri "Bende seni bekliyordum genç kral."
                                                    Kögan_Lideri "Bize vermek için getirdiğin panzehiri teslim et."
                                                    menu:
                                                        "Karşılığında senden sihirli saçlarını istiyorum":
                                                            Kögan_Lideri "Şimdilik getirdiğin miktar kadar sihirli saçımdan vereceğim."
                                                            Kögan_Lideri "Daha fazlası için tekrar konuşacağız."
                                                            "Takas gerçekleşir"
                                                            hide image Kögan_Lideri
                                                            menu:
                                                                "Komutan! Gidiyoruz.":
                                                                    show Komutan at komutan_poz
                                                                    Komutan "Emredersiniz!"
                                                                    hide image Komutan
                                                                    scene orman2
                                                                    "Birkaç saat süren yolculuğun ardından saraya ulaştınız."
                                                                    scene startbcg
                                                                    "Taht odasıda düşünmeye başlarsınız."
                                                                    menu:
                                                                        "Köganlar tehlikeli yaratıklar onlara güvenemeyiz.":
                                                                            "Köganlardan herkes gibi sende çekiniyorsun panzehir ne kadar onları kontrol altına almış olsada bu büyük bir risk."
                                                                            "Bir plan yapmak için meclisi toplama kararı alırsın."
                                                                            scene dev_salon
                                                                            "Bir kaç saat süren hazırlıklar tamamlanır ve meclis kurulur."
                                                                            show Yerel_Bakan at yerel_bakan_poz
                                                                            Yerel_Bakan "Saygıdeğer Kralım bizi neden çağırdığınızı öğrenebilirmiyim"
                                                                            hide image Yerel_Bakan
                                                                            "Köganlar ile olan durumdan bahsedilir."
                                                                            menu:
                                                                                "Köganların hepsini öldürüp sihirli saçları için Liderlerini sağ bırakmalıyız.":
                                                                                    show Kadı at kadi_poz
                                                                                    Kadı "Efendim, bu dev yaratıklar çok tehlikeli onları öldürmeyi düşünmekte haklısınız."
                                                                                    Kadı "Askerlerimizle Kuzey Kalesini kuşatıp onları yenebiliriz."
                                                                                    hide image Kadı
                                                                                    show Soylu at soylu_poz
                                                                                    Soylu "Kralım, köganlarla savaşmanın faydası yok. Onlara panzehiri zaten biz tedarik ediyoruz."
                                                                                    Soylu "Eğer bir hile ile panzehire zehir karıştırırsak hepsini savaşmadan kolayca yeneriz."
                                                                                    hide image Soylu
                                                                                    show Yerel_Bakan
                                                                                    Yerel_Bakan "Eğer tüm köganları zehirlersek Kögan Lideri de ölür. Bu riski alamayız."
                                                                                    Yerel_Bakan "Muhafız Başı ve Komutan'ın askeri dehasına güvenebiliriz. Köganların üstesinden gelirler."
                                                                                    hide image Yerel_Bakan
                                                                                    show Baş_Danışman at bas_danisman_poz
                                                                                    Baş_Danışman "Kralım bu sorunu büyücü çözebilir. Kögan Liderine özgü sihirli saçları kullanarak sadece Liderlerinin sağ çıkacağı bir zehir yapabilir."
                                                                                    Baş_Danışman "Otacı ve Büyücü kafa kafaya verirse bu sorunu çözebiliriz."
                                                                                    Baş_Danışman "Son sözlerimiz bunlardı efendim. Karar tabiki sizlerin."
                                                                                    hide image Baş_Danışman
                                                                                    menu:
                                                                                        "Komutan ve Muhafız Başı ile birlikte Köganların üstesinden geleceğiz.":
                                                                                            "Köganları savaşarak yok etme kararı aldın."
                                                                                            scene sefer
                                                                                            "Ülkede seferberlik ilan edildi ve orduya asker toplamaya başla başlandı."
                                                                                            "Bu sürede kral olarak görevine devam etmen gerekiyor..."
                                                                                            #################### B1 den devam edecek.

                                                                                        "Büyücü ve Otacı ile birlikte Köganları zehirleyeceğiz.":
                                                                                            "Büyücü ve Otacıyı Panzehir hazırladığınız odaya çağırtırsın."
                                                                                            scene gizemli_oda
                                                                                            show Otacı at otaci_poz
                                                                                            Otacı "Kralım bizi neden çağırdığınızı öğrenebilirmiyiz."
                                                                                            menu:
                                                                                                "Sizden beraber çalışarak bir zehir üretmenizi istiyorum. Bu zehirle tüm köganları öldürüp sadece Kögan Liderini sağ bırakmak istiyorum.":
                                                                                                    hide image Otacı
                                                                                                    show Büyücü at buyucu_poz
                                                                                                    Büyücü "Kralım bu istediğini Kögan Liderinin saçlarından yapacağım bir büyü ile yapabilirim."
                                                                                                    Büyücü "Panzehiri onlara verdiğinizde bu büyülü iksir sayesinde tüm köganlar ölecektir."
                                                                                                    hide image Büyücü
                                                                                                    show Otacı at otaci_poz
                                                                                                    Otacı "Efendim, bildiğiniz gibi büyü işleri çok tehlikelidir her zaman sonucunun ne olacağını bilemeyiz."
                                                                                                    Otacı "Ben Kögan Liderinin saçlarındaki iyileştirici özellikten yararlanarak Kögan Liderinin ölmeyeceğini varsayıyorum."
                                                                                                    Otacı "Saçları olmayan tüm köganlar zehri içtiği gibi ölecektir."
                                                                                                    hide image Otacı
                                                                                                    show Büyücü at buyucu_poz
                                                                                                    Büyücü "Kralım, vericeğiniz bu karar büyüyemi yoksa bilimemi güvendiğinizi gösterecek."
                                                                                                    hide image Büyücü
                                                                                                    menu:
                                                                                                        "Bilim.":
                                                                                                            "Bilime güvenmeyi seçtin. Otacı ve büyücü huzurundan ayrıldı."
                                                                                                            $ which_story = 7
                                                                                                            # B21
                                                                                                        "Büyü.":
                                                                                                            "Büyüye güvenmeyi seçtin. Büyücü ve Otacı huzurundan ayrıldı."
                                                                                                            $ which_story = 8
                                                                                                            # B22

                                                                        "Babamın kurduğu düzeni devam ettirmek zorundayım.":
                                                                            $ unlock_level(21)
                                                                            "Köganlar çok güçlü yaratıklar onları savaşlarda kullanabiliriz." #A
                                                                            "Mahiyetime bunu açıklamam gerekiyor"
                                                                            "Baş Danışman!"
                                                                            show Baş_Danışman at bas_danisman_poz
                                                                            Baş_Danışman "Emredin kralım."
                                                                            menu:
                                                                                "Meclistekilere haber ver toplantı yapacağız.":
                                                                                    Baş_Danışman "Başüstüne."
                                                                                    hide image Baş_Danışman
                                                                                    scene dev_salon
                                                                                    "Aquila Krallığının ileri gelenleri meclis salonunda toplanır."
                                                                                    show Yerel_Bakan at yerel_bakan_poz
                                                                                    Yerel_Bakan "Saygıdeğer Kralım bizi neden çağırdığınızı öğrenebilirmiyim."
                                                                                    hide image Yerel_Bakan
                                                                                    "Köganlar ile olan durumdan bahsedilir."
                                                                                    show Soylu at soylu_poz
                                                                                    Soylu "Kralım, böyle bir gücümüzün olduğunu herkese duyuralım bu sayede bize savaş açamak isteyen Krallıklar korkacaktır."
                                                                                    Soylu "Böyle bir gücümüzün olduğunu söylersek masada çok savaş kazanırız."
                                                                                    hide image Soylu
                                                                                    show Baş_Danışman at bas_danisman_poz
                                                                                    Baş_Danışman "Halk bunu öğrendiğinde korkabilir bu yaratıklar oldukça tehlikeli sadece yetkili kişilerin bilmesi önemli."
                                                                                    Baş_Danışman "Diğer Krallıklar bu gücümüzü öğrenirse bize karşı birleşir. Ambargo altına alınırsak bizim için felaket olur."
                                                                                    hide image Baş_Danışman
                                                                                    show Kadı at kadi_poz
                                                                                    Kadı "Halkınızdan birşeyi gizlemeniz doğru olmaz. Gazeteler aracılığıyla bunu duyuralım."
                                                                                    Kadı "Halkın desteğini arkanıza alırsanız gücünüz katlanır."
                                                                                    hide image Kadı
                                                                                    show Yerel_Bakan at yerel_bakan_poz
                                                                                    Yerel_Bakan "Halktaki muhalefet kesim bunu aleyhinizde kullanabilir. Halkın cahilliği ile uğraşmayalım efendim."
                                                                                    Yerel_Bakan "Gerektiğinde halka uygun birşeyler anlatırız. Bu Gücümüzün saklı olması bize gizli bir silah avantajı sağlar."
                                                                                    Yerel_Bakan "Son sözlerimiz bunlardı efendim karar tabiki sizlerin."
                                                                                    menu:
                                                                                        "Tüm olan biteni halka duyuralım.":
                                                                                            "Halkımızı böyle bir bilgiden mahrum bırakamayız."
                                                                                            hide image Yerel_Bakan
                                                                                            "Halktan gizleyerek doğru bir iş yapmış olmayız. Onları kandırmak kendimizi kandırmak olur."
                                                                                            "Ozanı çağrın."
                                                                                            show Ozan at ozan_poz
                                                                                            "Ozana herşeyi anlatırsın."
                                                                                            menu:
                                                                                                "Git duyduklarını heryerde anlat herkes haberdar olsun.":
                                                                                                    Ozan "Emredersiniz yüce kralım."
                                                                                                    hide image Ozan
                                                                                                    show Kadı at kadi_poz
                                                                                                    Kadı "Halkın ne tepki vereceğini merak ediyorum."
                                                                                                    $ which_story = 2
                                                                                                    hide image Kadı ## devam edecek

                                                                                        "Halktan Köganları saklamalıyız.":
                                                                                            "Bu gücümüzü gizli bir silah olarak tutmalıyız." #A1
                                                                                            hide image Yerel_Bakan
                                                                                            "Daha fazla panzehir için Köganlarla ikinci bir buluşma düzenleyeceğim."
                                                                                            $ which_story = 1
                                                                                            "Bir kaç gün sonra tekrardan yola çıkacağım." #### devam edecek.                                                                                           
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story4:
    scene startbcg
    hide screen bars
    show Komutan at komutan_poz
    Komutan "Efendim emrettiğiniz bölüğü hazırladım."
    menu:
        "O zaman hemen yola çıkalım.":
            hide image komutan
            scene orman2
            "Birkaç saat sonra elçi arkanızdan size yetişir."
            show Elçi at elci_poz
            Elçi "Efendim!"
            Elçi "Bu bir felaket!"
            menu:
                "Uzatmada söyle çabuk.":
                    Elçi "Kralım siz saraydan ayrıldıktan sonra bir gariplik fark ettim. Soylular toplanıyordu ve çok öfkeli görünüyorlardı."
                    Elçi "Köganları büyük bir tehlike olarak görüyorlar ve ayaklanma çıkardılar."
                    Elçi "Meclis üyelerini esir aldılar."
                    hide image Elçi
                    show Komutan at komutan_poz
                    Komutan "Ne yapacağız efendim?"
                    menu:
                        "Hemen geri dönmeliyiz tahtımı korumalıyım!":
                            Komutan "Emredersiniz!"
                            hide image Komutan
                            scene orman3 
                            "Bir kaç saat sonra başkent e ulaşırsınız."
                            scene kalekapi
                            "Kendi bölüğünle sarayının kapılarına dayanırsın."
                            "Soylular çoktan hazırlık yapmışlardır ve ordunu duvarların dibinde yok ederler."
                            "Uzun süren savaşı soylular kazanır ve seni idam ederler."
                            "Köganlar ile yapılan panzehir anlaşması iptal edilir hiç bişeyden haberi olmayan köganlar panzehirleri bittiğinde ölür ve bu kadim millet tekrardan tarihe karışır."
                            scene a11son
                            "Aquila krallığı artık Soylunun eline geçer"
                            $ unlock_level(16)
                            "Soylu Kral olur."
                            play sound deadeffect
                            menu:
                                "Çık":
                                    $ renpy.full_restart()
                        "Kögan Lideriyle konuşmamız gerek bize yardım etmeliler.":
                            "Askerler! gidiyoruz."
                            hide image Komutan
                            scene kuzeykale
                            "Terkedilmiş kaleye gelirsiniz."
                            "Bir süre sonra köganlar ortaya çıkar."
                            scene orman2
                            show Kögan_Lideri at Kogan_poz
                            Kögan_Lideri "Evet seni dinliyorum Genç Kral."
                            menu:
                                "Krallığım sizle olan anlaşmadan dolayı bana karşı ayaklanma çıkardı.":
                                    menu:
                                        "Eğer bizimle gelip tahtımı geri almaya yardım etmezseniz size panzehir vermezler.":
                                            Kögan_Lideri "Bizi kaybetmeyi göze alamazsınız."
                                            menu:
                                                "Ayaklanmayı çıkaranlar tam olarak bunu düşünüyor.":
                                                    Kögan_Lideri "Peki sizi uzaktan takip edeceğiz."
                                                    hide image Kögan_Lideri
                                                    scene orman
                                                    "Bir süre sonra başkente ulaşırsınız."
                                                    scene kalekapi
                                                    "Soylu çoktan tahtı elegeçirmiş ve meclis üyelerini öldürmüştür."
                                                    menu:
                                                        "Çok geç kaldık kendi insanlarımı öldüremem.":
                                                            "Köganları ikna etmek ile uğraşmak bir hataydı tahtını kaybettin."
                                                            scene a11son
                                                            "Soylu Aquila Krallığının yeni hükümdarı olur."
                                                            $ unlock_level(16)
                                                            scene harita
                                                            "Ailenle birlikte Zemorvia ya kaçarsınız ve mütevazi bir hayat sürersiniz"
                                                            scene a121
                                                            play sound deadeffect
                                                            "Saraydan çıkıp bu eski kulubeye yerleşmek sana ve ailene zor gelir ama alışırsınız."
                                                            $ unlock_level(17)
                                                            menu:
                                                                "Çık":
                                                                    $ renpy.full_restart()
                                                        "Köganlar! saldırın!":
                                                            "Şehir eskiden sana ait oluğu için tüm zayıf noktalarını biliyorsun."
                                                            "Bunu kullanarak Köganları ve ordunu akıllıca surların arkasına soktun."
                                                            "Şehirde çıkan savaş yüzünden halkından bir çok masum insan hayatını kaybetti."
                                                            scene a122son
                                                            "Tahtını kanla geri aldın."
                                                            scene tunelgiris
                                                            "Köganların Lideri kargaşadan yararlanıp taht odasının altındaki tünellere ulaştı."
                                                            scene lahit
                                                            "Şifreyi çözüp, panzehirin tarifi öğrendi."
                                                            scene terkkale
                                                            "Köganların artık sana ihtiyacı kalmadı, tarifi öğrendiler."
                                                            "Halkını ve kalan askerlerini acımasızca katlettikten sonra senide öldürdü"
                                                            play sound deadeffect
                                                            "Aquila Krallığı senin hümükdarlığında yok oldu ve tarihe gömüldü."
                                                            menu:
                                                                "Çık":
                                                                    $ renpy.full_restart()

    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story5:
    scene startbcg
    hide screen bars
    show Çiftçi at ciftci_poz
    Çiftçi "Kralım köganlar ile olan bağınızdan dolayı köyümden bir sürü insan korkup Yargea Krallığına kaçtı."
    Çiftçi "Kaçmayıp rahatsız olan bir sürü köylü grubu da var huzurunuza gelmek için şehre geldiğimde burda da bir çok insanın toplandığını gördüm."
    menu:
        "Bu bilgiler çok kıymetli.":
            hide image Çiftçi
            show Baş_Danışman at bas_danisman_poz
            Baş_Danışman "Efendim bir ayaklanma çıkmasından şüphe ediyorum."
            Baş_Danışman "Ne düşünüyorsunuz bu konu hakkında?"
            menu:
                "Bir kaç köylülün toplanması benim tahtıma zarar veremez.":
                    Baş_Danışman "Tedbir alamaktan bir zarar gelmez."
                    menu:
                        "Benim işime karışma!":
                            hide image Baş_Danışman
                            $ which_story = 3
                            ### devam edecek.
                "Muhafız Başı ile konuşup ek önlemler almalıyız.":
                    "Bana Muhafız Başını çağır."
                    hide image Baş_Danışman
                    show Muhafız_Başı at muhafiz_basi_poz
                    Muhafız_Başı "Efendim beni emretmişsiniz."
                    menu:
                        "Olası bir isyandan şüğheleniyorum. Gerekli tedbirler alınsın.":
                            Muhafız_Başı "Emredersiniz efendim."
                            hide image Muhafız_Başı
                            $ which_story = 4
    
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story6:
    scene startbcg
    hide screen bars
    show Hizmetçi_Başı at hizmetci_basi_poz
    Hizmetçi_Başı "Kralım!"
    Hizmetçi_Başı "Halk!"
    menu:
        "Ne oldu? Anlat hemen.":
            Hizmetçi_Başı "Halk, köylüler, başıbozuklar..."
            hide image Hizmetçi_Başı
            show Muhafız_Başı at muhafiz_basi_poz
            Muhafız_Başı "Efendim! isyan var."
            Muhafız_Başı "Ellerinde meşale ve mızraklarla saraya yürüyorlar, çok kalabalıklar."
            menu:
                "Askerler!":
                    hide image Muhafız_Başı
                    "Ordunun başına geçmeye çalışırsın ama nafile."
                    "İsyancılar çoktan her yeri basmış ve taht odana doğru harekete geçmişlerdir."
                    "Komutanlarınla birlikte elinde kılıç ile savaşarak öldürülürsün."
                    scene a2kson
                    "Oğlun büyüyene kadar Aquila Krallığına hizmet etmesi için tahta Kadı geçiriliyor."
                    $ unlock_level(18)
                    "Ülken uzun bir süre Kralsız kaldı."
                    play sound deadeffect
                    menu:
                        "Çık":
                            $ renpy.full_restart()
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story7:
    scene startbcg
    hide screen bars
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Kralım düşündüğünüz gibi bir ayaklanma çıktı."
    Muhafız_Başı "Ama çok büyümeden bastırıp engel olduk."
    Muhafız_Başı "Baş isyancıları ne yapalım."
    menu:
        "İtaatsizlikten idam edilsinler.":
            Muhafız_Başı "Halk idam edilenlerden ibret aldı."
            menu:
                "Tamam gidebilirsin, daha falza sorun çıkacağını zannetmiyorum.":
                    hide image Muhafız_Başı 
                    show Elçi at elci_poz
                    Elçi "Efendim diğer Krallıklardan hiç bir ses soluk yok."
                    Elçi "Bizimle savaşmaktan çekiniyor gibiler. Rahat rahat ülkelerinden geçip vergi vermeden ticaret yapabiliriz."
                    hide image Elçi
                    scene Kralheykel
                    "Diğer ülkelere karşı saldığınız korku sebebiyle Aquila Krallığı gelişti ve halk refaha erdi."
                    "Halkın ülkenin çeşitli yerlerine senin heykellerini yaptırdı."
                    play sound deadeffect
                    $ unlock_level(19)
                    "Aquila Krallığının en görkemli kralı oldun."
                    menu:
                        "Çık.":
                            $ renpy.full_restart()
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story8:
    scene startbcg
    hide screen bars
    show Muhafız_Başı at muhafiz_basi_poz
    Muhafız_Başı "Kralım yeteri kadar asker topladık. Yola Çıkmaya hazırız."
    menu:
        "Herkese haber verin zırhımı getirin kuzeye köganlarla savaşmaya gidiyoruz.":
            scene orman3
            "Bir süre süren yolculuk sonunda Kuzey Kalesine ulaşırsınız."
            scene kuzeykale
            "..."
            scene kuzeykaleon
            show Komutan at komutan_poz
            Komutan "Efendim Köganlara doğrudan saldırmak yerine onlara panzehir getirmiş gibi yapabiliriz."
            Komutan "Böyle bir tuzak kurmak işimize gelir efendim."
            hide image Komutan 
            menu:
                "Sen ne düşünüyorsun Muhafız Başı?":
                    show Muhafız_Başı at muhafiz_basi_poz 
                    Muhafız_Başı "Komutana hak veriyorum efendim bu şekilde onları açık alanda gafil avlayabiliriz."
                    menu:
                        "O halde dediğiniz gibi yapalım.":
                            hide image Muhafız_Başı
                            "Buluşma yerine geri dönersiniz."
                            scene orman2
                            menu:
                                "Askerler, Köganlara niyetimizi belli etmeyeceğiz. ":
                                    show Asker at asker_poz
                                    Asker "Kralım, köganlar geliyor."
                                    hide image Asker 
                                    "..."
                                    show Kögan_Lideri at Kogan_poz
                                    Kögan_Lideri "Neden erken geldiniz?"
                                    Kögan_Lideri "Anlaştığımız zamana daha 3 ay vardı."
                                    menu:
                                        "Yakında bir sefere çıkacağız o yüzden şimdi gelmek durumunda kaldık.":
                                            menu:
                                                "Seninle özel bir konu hakkında konuşmak istiyorum.":
                                                    Kögan_Lideri "Konuş askerlerim dilini bilmiyor."
                                                    Kögan_Lideri "Yoksa kendi askerlerinden mi şüphe ediyorsun Kral."
                                                    menu:
                                                        "Taht oyunları zordur. Sana söyleyeceğim şey çok mühim.":
                                                            Kögan_Lideri "Peki biraz ormana doğru yürüyelim."
                                                            scene ormank
                                                            "Kögan Liderini diğer köganlardan ayırdın. Biraz uzaklaştıktan sonra."
                                                            scene ormankus
                                                            menu: 
                                                                "KUŞA BAK!":
                                                                    $ unlock_level(20)
                                                                    "Kögan_Lideri ne olup bittiğini anlamaz ve bir anlık dikkati dağılır."
                                                                    hide image Kögan_Lideri
                                                                    "Savaşçılık hünerlerile etkisiz hale getirirsin."
                                                                    scene ormank
                                                                    "Kılıcını çekip Köganların üstüne doğru koşarsın."
                                                                    scene orman2
                                                                    show Komutan at komutan_poz
                                                                    Komutan "Saldırın askerlerim!"
                                                                    hide imagae Komutan
                                                                    "Uzun süren ve çok kayıplı bir savaş sonrasında köganları alt etmeyi başarırsınız."
                                                                    "Kögan Liderini uyutup saraya götürürsünüz."
                                                                    scene orman3
                                                                    "Bir süre sonra saraya varırsınız."
                                                                    scene kalekapi
                                                                    $ which_story = 6
                                                                    "Kögan Liderini hapsedip saçlarını almaya başlarsınız." #oyun normal işleyişine devam eder.
        
                                                "Bana sihirli saçlarından ver.":
                                                    Kögan_Lideri "Zaten sende yeteri kadar olmalıydı."
                                                    menu:
                                                        "Sefere gideceğimiz için gerekli vakitte burda olamayacağım.":
                                                            Kögan_Lideri "Tamam vereyim ozaman ama sizde panzehiri hemen getirin."
                                                            menu:
                                                                "Herşey anlaştığımız gibi olacak.":
                                                                    hide image Kögan_Lideri 
                                                                    "Kögan Lideri panzehri verir."
                                                                    menu:
                                                                        "Askerler, saldırın!":
                                                                            "Köganlar hazırlıksız yakalandı ama Liderlerinin tecrübesiyle durumu eşitlediler."
                                                                            "Savaş esnasında Kögan Liderinin komutuyla geride bekelyen köganlar destek çağırdı."
                                                                            "Savaş tamda lehine giderken yardıma yetişen köganlar tüm dengeyi köganlar lehine çevirdi."
                                                                            "Askerlerin ile savaşa savaşa orda öldürüldün."
                                                                            scene koganson
                                                                            "Köganların en iyi savaşçılarını öldürdüğünüz için Aquila ya saldıramadılar."
                                                                            "Canını vererek Köganların soyunu kurutmuş oldun"
                                                                            scene sefer
                                                                            "Aquila Krallığı Köganlardan kurtulmuş oldu."
                                                                            "Senin ani ölümün üstüne ülkende karışıklık yaşanır."
                                                                            scene b11son
                                                                            play sound deadeffect
                                                                            "Oğlun tahta geçerek Aquila Krallığının yeni hükümdarı olur."
                                                                            menu:
                                                                                "Çık":
                                                                                    $ renpy.full_restart()


    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story9:
    scene startbcg
    hide screen bars
    show Asker at asker_poz
    Asker "Kralım!"
    Asker "Felaket!"
    menu:
        "Konuşsana!":
            Asker "Efendim hapse attığınız Kögan Lideri..."
            menu:
                "Ne olmuş ona konuş!":
                    Asker "Kendini öldürmüş."
                    Asker "Yemesi için verdiğimiz etin kemiği ile boynunu kesmiş."
                    menu:
                        "Ya saçları? soldularmı?":
                            Asker "Büyücü gelip tüm kafasını kazıdı ve tüm saçlarını aldı."
                            menu:
                                "Neden dikkat etmediniz sizin yüzünüzden öleceğim.":
                                    Asker "Efendim böyle bir şeyi beklemiyorduk."
                                    menu:
                                        "Zindandaki nöbetçi tüm askerleri idam edeceğim.":
                                            "Zindandaki tüm nöbetçiler idam edilir."
                                            "Büyücünün aldığı saçlarlae ile panzehir yapılır."
                                            "Ancak bu panzehir size 10 yıl kadar yeter."
                                            scene b11son
                                            "Hatanının sonunda oğluna güzel bir gelecek hazırlayıp huzur içinde ölürsün."
                                            play sound deadeffect
                                            "Aquila Krallığı emin ellerde."
                                            "..." # son 
                                            menu:
                                                "Çık":
                                                    $ renpy.full_restart()
                                        "Zindandaki tüm askerlere hapis cezası vereceğim.":
                                            "Zindandaki nöbetçi tüm askerleri zindana attın."
                                            "Büyücünün aldığı saçlarlae ile panzehir yapılır."
                                            "Ancak bu panzehir size 10 yıl kadar yeter."
                                            scene b11son
                                            "Hatanının sonunda oğluna güzel bir gelecek hazırlayıp huzur içinde ölürsün."
                                            play sound deadeffect
                                            "Aquila Krallığı emin ellerde."
                                            "..." # son 
                                            menu:
                                                "Çık":
                                                    $ renpy.full_restart()
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story10:
    hide screen bars
    scene startbcg
    show Otacı at otaci_poz
    Otacı "Kralım, bana güvenerek istediğiniz zehri yaptım."
    Otacı "Bu zehri köganlara götüreceğiniz panzehirin içine döküp iyice karıştırın."
    menu:
        "Güvenimi boşa çıkarmassan iyi edersin. Tüm krallığın umutları senin yapacağın zehre bağlı.":
            hide image Otacı
            scene orman3
            "Askerlerini toplayıp yola çıktın."
            scene kuzeykale
            "Bir kaç saat sonra kuzey kalesine vardın."
            scene kuzeykaleon
            show Asker at asker_poz
            Asker "Kralım, köganlar geliyor."
            hide image Asker 
            "..."
            show Kögan_Lideri at Kogan_poz
            Kögan_Lideri "Neden erken geldiniz?"
            Kögan_Lideri "Anlaştığımız zamana daha 3 ay vardı."
            menu:
                "Yakında bir sefere çıkacağız o yüzden şimdi gelmek durumunda kaldık.":
                    Kögan_Lideri "Ne istiyorsunuz?"
                    menu: 
                        "Tabikide takas.":
                            Kögan_Lideri "Anlaştığımız gibi getirdiğin panzehir miktarı kadar saç vereceğim."
                            menu:
                                "Getirdiklerimiz bunlar saçları ver.":
                                    hide image Kögan_Lideri
                                    "Takas gerçekleşir."
                                    scene orman2
                                    "Askerlerin ile biraz uzaklaşıp köganların bir bir devrilmesini izlediniz."
                                    "Çok beklemeden zehirlenenleri görüp zehri içmeyen köganlara saldırdınız."
                                    "Kögan Lideri zehri içmedi ve kaçmaya çalıştı."
                                    "Askerlerinle peşine düştünüz."
                                    "Çok geçmeden Kögan Lideri yakalanacağını anlayıp kendini öldürdü."
                                    "Hemen cesedinin üstünden saçlarını alıp geri dönmeye karar verdin."
                                    scene orman1
                                    "..."
                                    scene kalekapi
                                    "Hızlı bir şekilde geri dönüp saçları büyücüye verdin."
                                    "Sadece 6 yıl yetecek kadar panzehir üretebildi."
                                    scene b11son
                                    "Hatanının sonunda oğluna güzel bir gelecek hazırlayıp huzur içinde ölürsün."
                                    play sound deadeffect
                                    "Aquila Krallığı emin ellerde."
                                    "..." # son 
                                    menu:
                                        "Çık":
                                            $ renpy.full_restart()
                                
    $ last_dialog= None
    show screen bars
    $ main_story_count += 1
    jump random_dialog
    return

label story11:
    hide screen bars
    scene startbcg
    show Büyücü at buyucu_poz
    Büyücü "Kralım bana güvenerek istediğiniz iksiri yaptım."
    Büyücü "Bu iksiri, köganlara götüreceğiniz panzehrin içine karıştırın."
    menu:
        "Güvenimi boşa çıkarmassan iyi edersin. Tüm krallığın umutları senin yapacağın iksire bağlı.":
            hide image Büyücü
            scene orman3
            "Askerlerini toplayıp yola çıktın."
            scene kuzeykale
            "Bir kaç saat sonra kuzey kalesine vardın."
            scene kuzeykaleon
            show Asker at asker_poz
            Asker "Kralım, köganlar geliyor."
            hide image Asker 
            "..."
            show Kögan_Lideri at Kogan_poz
            Kögan_Lideri "Neden erken geldiniz?"
            Kögan_Lideri "Anlaştığımız zamana daha 3 ay vardı."
            menu:
                "Yakında bir sefere çıkacağız o yüzden şimdi gelmek durumunda kaldık.":
                    Kögan_Lideri "Ne istiyorsunuz?"
                    menu: 
                        "Tabikide takas.":
                            Kögan_Lideri "Anlaştığımız gibi getirdiğin panzehir miktarı kadar saç vereceğim."
                            menu:
                                "Getirdiklerimiz bunlar saçları ver.":
                                    hide image Kögan_Lideri
                                    "Takas gerçekleşir."
                                    scene orman2
                                    "İksiri içen köganların bağzıları içer içmez yere yığıldı."
                                    "Ama iksiri içen bazı köganlar tuhaf bir tepkimeye girdi ve mor bir renk aldılar."
                                    "Mor Köganlar ile mavi köganlar birbiriyle savaşmaya başladı."
                                    menu:
                                        "Askerlerin ile birlikte kaç!":
                                            "Askerlerine geri çekilme emrini verdin ve hemen ordan uzaklaştın."
                                            scene orman3
                                            "Bir kaç saat içinde Aquila Krallığına vardın."
                                            scene kalekapi
                                            "Tüm askerlerini alıp kuzeye ilerliyorsun."
                                            scene orman1
                                            "Hızlı bir şekilde olay yerine ulaştın."
                                            "Tüm köganlar ve mor köganlar ölmüş."
                                            "Cesetlerin arasında gezinirken Kögan Liderinide buldun."
                                            "Üstündeki saçları alıp geri döndün."
                                            scene b11son
                                            "Büyücü bu saçlar ile sana 4 yıl yetecek panzehir hazırladı."
                                            play sound deadeffect
                                            "Öldükten sonra yerine oğlun geçti."
                                            "Aquila Krallığı artık onun emrinde."
                                            menu:
                                                "Çık":
                                                    $ renpy.full_restart()
                                            
                                        "Kalıp Kögan Liderini kurtarmayı dene":
                                            "Askerlerine saldırma talimatı verdin"
                                            "Mavi köganlara yardım ederken Kögan Liderini yaralı olarak kurtardın."
                                            "Onu götürüp Aquila Krallığında tedavi etmek istedin."
                                            scene orman3
                                            "Aquila Krallığına geldin."
                                            scene sefer
                                            "Halkın ilk defa bir köganı canlı görmenin şaşkınlığını yaşıyor."
                                            "Hemen otacını çağırıp onu tedavi ettirdin."
                                            menu:
                                                "Kögan Liderini esir alıp onu zindana at.":
                                                    "B2221"
                                                "Kögan Liderinin uyanmasını bekle.":
                                                    "..."
                                                    scene gizemli_oda
                                                    "Bir süre sonra Kögan Lideri uyandı."
                                                    "Ona olan biteni anlattık ve onu kurtatdığımızı söyledik."
                                                    show Kögan_Lideri at Kogan_poz
                                                    Kögan_Lideri "Beni kurtardığın için sana minnettar değilim ne de olsa kendini kurtarmış oldun."
                                                    Kögan_Lideri "Bu olanları unutup iş birliğimize devam etmeliyiz."
                                                    menu:
                                                        "Haklısın":
                                                            hide image Kögan_Lideri
                                                            "Kögan Lideri kuzeye doğru yola çıktı."
                                                            "Anlaşmanız devam etti. Diğer ülkeler Aquila nın bu gününden korkup çekindi."
                                                            $ unlock_level(19)
                                                            scene Kralheykel
                                                            "Bu sayede ülken refaha erdi ve kentin çeşitli yerlerine heykellerin yapıldı."
                                                            play sound deadeffect
                                                            "Aquila Krallığı senin hükümdarlığında sınırlarını hiç olmadığı kadar genişletti."
                                                            menu:
                                                                "Çık":
                                                                    $ renpy.full_restart()
