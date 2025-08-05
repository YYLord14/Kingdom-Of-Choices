#Oyun hikayesi

label story1:
    show Kadı at kadi_poz 
    Kadı "Sayım Kralım bu anahtar size babanızdan mirastır. Eski Kral babanız size bunu vermem için bana vermişti."
    menu:
        "Bu kadar önemliyse neden şimdi veriyorsun?":
            Kadı "Çünkü baban olgunlaşıp iyi bir kral olduğunda bu anahtara ulaşmanı istedi."     
            menu:
                "Peki bu anahtar nereyi açıyor.":
                    Kadı "Bu anahtar taht odasındaki 3. sütunun olduğu yerdeki duvarın orda saklanmış kapıyı açıyor."
                    hide image Kadı
                    "Kadı kapıyı gösterip oradan uzaklaşır  artık gerçek ile baş başasın. Büyük bir kararlılıkla babanın odasındaki gizli kapıyı keşfettin."
                    "Eski ahşap kapı sessizce açtın ve tozlu bir parşömen odasında buldun kendini. Odada dolaşırken, duvarlarda asılı olan eski haritaları ve yazılı belgeleri inceledin. Bir köşede, tozun altında saklı kalmış bir parşomen buldun ve sayfalarını açtın."
                    "Sayfaların arasında Babanın el yazısıyla yazılmış notlar vardı. Kalbin hızla çarpmaya başladı, çünkü bu notlar, babanın ülkeyi kurarken gizemli yaratıklardan yardım aldığını, askerlerinin ateşi yönetebildiğini ve insanlara büyük zulmettiğini anlatıyordu."
                    "Gözyaşları içinde bu karanlık gerçekleri sindirmeye çalışırken, notlardan bir şey daha öğrendin. Baban bu zulmün sonucunda gizemli yaratıkları ülkenin kuzeyindeki bir açıklıkta bırakmıştı."
                    "Babanın yapmış olduğu kötülükleri öğrenmen seni derinden etkiledi. Ancak, artık bu gerçekle yüzleşmek zorundaydın ve bununla birlikte babanın hatalarını düzeltme sorumluluğunu hissettin"
                    "Parşomen elinde..."
                    menu:
                        "Tek başına çözmeye çalış":
                            "Parşomeni çözmek için saatlerini harcarsın ama birine gösterim yardım almaktan başka çaren kalmaz." #yardım kısmı dahil en sona kadar buraya kopyalanacak
                        "Birine gösterip yardım al":
                            menu:
                                "Muhafız başına gösterip ateş kullanan askerleri araştırmaya başlamalıyım.":
                                    show Muhafız_Başı at muhafiz_basi_poz
                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                    menu:
                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                            menu:
                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                    hide image Muhafız_Başı
                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                    Muhafız_Başı "Emredersiniz efendim."
                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                        "Peki dediğin gibi olsun, Kadı ya soracağım.":
                                            show Kadı at kadi_poz
                                            Kadı "Efendim bu dedikleriniz imkansız ama babanızın neden böyle şeyler yazdığını bilmiyorum gizli odaya bende girebilirmiyim."
                                            menu:
                                                "Tamam gel beraber girelim.": # alttakinin aynısı buray kopyala
                                                    Kadı "Efendim okuduğum bir kaç parşomene göre babanız kadim yaratıklarla iş birliği yapmış. Bu yaratıkların ismi Kögan. Köganlar son derece tehlikeli insan yiyen dev yaratıkalrdır."
                                                    Kadı "Babanız onlara bir zehir vermiş ve panzehir karşılığında onları zorla savaştırmış. Burda panzehirin bir ilaç olmadığıda yazıyor yani sürekli birinin onlara panzehir tedarik ettiğini düşünebiliriz."
                                                    hide image Kadı
                                                    menu:
                                                        "Köganların yerini bulup onları yok edelim": 
                                                            "Ordunun toplanması için bir toplantı düzenledin. Mahiyetini Köganlara saldırmaya ikna ettin."
                                                            show Yerel_Bakan at yerel_bakan_poz
                                                            Yerel_Bakan "Efendim büyülü yaratıklarla savaşmak mantıklı değil zehirin nasıl yapıldığını ve panzehiri kimin tedarik ettiğini öğrenirsek panzehiri kesmemiz yeterli olucaktır."
                                                            menu:
                                                                "Haklısın değerli bakanım":
                                                                    "Yerel bakanın neden bu görevde olduğunu düşünüp ona hak verdin ve araştırma yapmaya karar verdin."
                                                                    hide image Yerel_Bakan
                                                                    menu:
                                                                        "Panzehiri araştırmak için Otacı ile konuşmalıyım": 
                                                                            show Otacı at otaci_poz
                                                                            Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                            menu:
                                                                                "Sende benimle gel beraber gidelim.":
                                                                                    Otacı "Üzgünüm efendim ama parşomendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                                    "Tamam sen burda kal."
                                                                                    hide image Otacı
                                                                                "Ben yalnız gideceğim.":
                                                                                    hide image Otacı
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                        "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                            show Şifacı at sifaci_poz
                                                                            Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                            hide image Şifacı
                                                                "Ben kararımı verdim, SAVAŞA HAZIRLANIN!": # Köganlara saldırmak için savaş kararı aldırmak
                                                                    "Yerel Bakanın dediklerini önemsemedin."
                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                    Muhafız_Başı "Emredin Kralım."
                                                                    menu:
                                                                        "Halkı savaştan haberdar et ve seferberlik ilan et.":
                                                                            Muhafız_Başı "Orduları hazırladım efendim"
                                                                            menu:
                                                                                "Kuzeye ilerliyoruz!":
                                                                                    hide image Muhafız_Başı
                                                                                    "Kuzeye paroşmende yazıldığı yere doğru ilerledin ve önünde ladin ağaçlarından yapılmış bir sur gördün üstünde Aquila Krallığının simgeleri var. Ama kimse yaşamıyor."
                                                                                    menu:
                                                                                        "Bir bölük asker surlara tırmansın!":
                                                                                            "Askerlerinin bazılarını surlara tırmandırdın ve sana içerisinin ağaçlık bir alan olduğunu ve güvenli olduğunu söylediler. Ordunla birlikte içeriye girdin."
                                                                                            "Bir süre sonra köganlar üstünüze hücum etti 3 metre boyunda olan bu yaratıklar eline geçen askerleri parçalayıp yiyorlardı."
                                                                                            "Hemen dağılan ordunu düzene soktun ve surun üstüne yerleştirdiğin okçulardan destek alarak savaştın ."
                                                                                            "Atının üstünden savaşarak bir çok köganı indirdin askerlerin karşı koyamıyor ve hepsi teker teker ölüyordu okçularının desteğiyle ufak bir boşluk yakalayıp küçük bir birlik ile kaçmayı başardın."
                                                                                            "Ordunun nerdeyse hepsi katledildi ancak köganların az bir kısmını öldürebildiniz."
                                                                                            menu:
                                                                                                "Aquila Krallığına dönmeye çalışmalıyız.":
                                                                                                    "Kaçmaya çalışırken Köganlar yetiştiler ve ordunu yok ettiler ölüm senin için bir kurtuluş oldu." #SON###########
                                                                                                "En yakın yerde kamp kur ordunu düzene sok ve yaralıları dinlendirmeliyiz.":
                                                                                                    "Kamp kurdun ve ordunu düzene soktun. Köganların uzaktan hızla orduna yaklaştığını gördün."
                                                                                                    menu:
                                                                                                        "Okçular saldırın Savaş düzenine geçiyoruz!":
                                                                                                            "Okçular köganlar yaklaşmadan bir kaç tanesini indirdi Köganlar saldırıya geçip ordunu yok etti sadece 3-5 tane Kögan kaldı ve tek başına kaldın"
                                                                                                            menu:
                                                                                                                "KAÇ":
                                                                                                                    "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                "SAVAŞ": #alt satır SON #############
                                                                                                                    "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                        "Askerler! atlara binin vur kaç yapacağız!":
                                                                                                            "Büyük bir kısmını indirdiniz uzun bir mesafe kaçarak köganların sayısını azalttın tüm ordun yok edildi sadece 3-5 tane kögan kaldı ve tek kaldın."
                                                                                                            menu:
                                                                                                                "KAÇ":
                                                                                                                    "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                "SAVAŞ": #alt satır SON #############
                                                                                                                    "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                "Sur kapısını kırın içeri giriyoruz.":
                                                                                    "Bir süre ilerledikten sonra aniden 3 metrelik devasa yaratıklar ordunun üstüne doğru koşmaya başladı savunma düzeni almaya çalıştın ama ordunun düzeni bozuldu bazıları kaçmaya çalıştı ama Köganlar eline geçen askelerin kafalarını ısırıyor elleriyle ekiye bölüyor paraçlaıyolarlardı ."
                                                                                    menu:
                                                                                        "KAÇ":
                                                                                            "Ordun katledilerken kaçtın. uzun bir süre at koşturduktan sonra köganlar senin peşinden geldi ve seni yakalayıp parçalara ayırdılar."#SON##################
                                                                                        "Askerler! Savaş düzeni ÇEMBEER!": #SON################
                                                                                            "Askerlerinin bir kısmı hala sana sadık ve kendi birliğinle bir düzen oturtmayı başardın Atlarınızdan inmeyerek bir şekilde aradaki boy  farkını kapattınız bir kaç tane köganı indirdin eline onların mor kanları bulaştı kaçmaya çalışan ordun katledildi. etraf kan götürüyor ordun daki askerler yavaş yavaş düşüyor geriye muhafız başı ile sen kaldın bir kaç tanesini de öldürdükten sonra ikinizde öldünüz"
                                                        "Köganlara kimin panzehir verdiğini araştıralım.":
                                                            menu:                                                               
                                                                "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                    show Şifacı at sifaci_poz
                                                                    Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                    hide image Şifacı
                                                                "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                    show Otacı at otaci_poz
                                                                    Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                    menu:
                                                                        "Sende benimle gel beraber gidelim.":
                                                                            Otacı "Üzgünüm efendim ama parşomendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                            "Tamam sen burda kal."
                                                                            hide image Otacı
                                                                        "Ben yalnız gideceğim.":
                                                                            hide image Otacı
                                                                            "Büyücün yanına gidip olanları anlatırız"
                                                                            show Büyücü at buyucu_poz
                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                            hide image Büyücü
                                                                            menu:
                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                    menu:
                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                            menu:
                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                    hide image Muhafız_Başı
                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                "Kadıya gösterip kütüphaneye geri dönmeliyim.":
                                    show Kadı at kadi_poz
                                    Kadı "Efendim bu dedikleriniz imkansız ama babanızın neden böyle şeyler yazdığını bilmiyorum gizli odaya bende girebilirmiyim."
                                    menu:
                                                "Tamam gel beraber girelim.":
                                                    Kadı "Efendim okuduğum bir kaç parşomene göre babanız kadim yaratıklarla iş birliği yapmış. Bu yaratıkların ismi Kögan. Köganlar son derece tehlikeli insan yiyen dev yaratıkalrdır."
                                                    Kadı "Babanız onlara bir zehir vermiş ve panzehir karşılığında onları zorla savaştırmış. Burda panzehirin bir ilaç olmadığıda yazıyor yani sürekli birinin onlara panzehir tedarik ettiğini düşünebiliriz."
                                                    hide image Kadı
                                                    menu:
                                                        "Köganların yerini bulup onları yok edelim":
                                                            "Ordunun toplanması için bir toplantı düzenledin. Mahiyetini Köganlara saldırmaya ikna ettin."
                                                            show Yerel_Bakan at yerel_bakan_poz
                                                            Yerel_Bakan "Efendim büyülü yaratıklarla savaşmak mantıklı değil zehirin nasıl yapıldığını ve panzehiri kimin tedarik ettiğini öğrenirsek panzehiri kesmemiz yeterli olucaktır."
                                                            menu:
                                                                "Ben kararımı verdim, SAVAŞA HAZIRLANIN!": # Köganlara saldırmak için savaş kararı aldırmak
                                                                    "Yerel Bakanın dediklerini önemsemedin."
                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                    Muhafız_Başı "Emredin Kralım."
                                                                    menu:
                                                                        "Halkı savaştan haberdar et ve seferberlik ilan et.":
                                                                            Muhafız_Başı "Orduları hazırladım efendim"
                                                                            menu:
                                                                                "Kuzeye ilerliyoruz!":
                                                                                    hide image Muhafız_Başı
                                                                                    "Kuzeye paroşmende yazıldığı yere doğru ilerledin ve önünde ladin ağaçlarından yapılmış bir sur gördün üstünde Aquila Krallığının simgeleri var. Ama kimse yaşamıyor."
                                                                                    menu:
                                                                                        "Bir bölük asker surlara tırmansın!":
                                                                                            "Askerlerinin bazılarını surlara tırmandırdın ve sana içerisinin ağaçlık bir alan olduğunu ve güvenli olduğunu söylediler. Ordunla birlikte içeriye girdin."
                                                                                            "Bir süre sonra köganlar üstünüze hücum etti 3 metre boyunda olan bu yaratıklar eline geçen askerleri parçalayıp yiyorlardı."
                                                                                            "Hemen dağılan ordunu düzene soktun ve surun üstüne yerleştirdiğin okçulardan destek alarak savaştın ."
                                                                                            "Atının üstünden savaşarak bir çok köganı indirdin askerlerin karşı koyamıyor ve hepsi teker teker ölüyordu okçularının desteğiyle ufak bir boşluk yakalayıp küçük bir birlik ile kaçmayı başardın."
                                                                                            "Ordunun nerdeyse hepsi katledildi ancak köganların az bir kısmını öldürebildiniz."
                                                                                            menu:
                                                                                                "Aquila Krallığına dönmeye çalışmalıyız.":
                                                                                                    "Kaçmaya çalışırken Köganlar yetiştiler ve ordunu yok ettiler ölüm senin için bir kurtuluş oldu." #SON###########
                                                                                                "En yakın yerde kamp kur ordunu düzene sok ve yaralıları dinlendirmeliyiz.":
                                                                                                    "Kamp kurdun ve ordunu düzene soktun. Köganların uzaktan hızla orduna yaklaştığını gördün."
                                                                                                    menu:
                                                                                                        "Okçular saldırın Savaş düzenine geçiyoruz!":
                                                                                                            "Okçular köganlar yaklaşmadan bir kaç tanesini indirdi Köganlar saldırıya geçip ordunu yok etti sadece 3-5 tane Kögan kaldı ve tek başına kaldın"
                                                                                                            menu:
                                                                                                                "KAÇ":
                                                                                                                    "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                "SAVAŞ": #alt satır SON #############
                                                                                                                    "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                                        "Askerler! atlara binin vur kaç yapacağız!":
                                                                                                            "Büyük bir kısmını indirdiniz uzun bir mesafe kaçarak köganların sayısını azalttın tüm ordun yok edildi sadece 3-5 tane kögan kaldı ve tek kaldın."
                                                                                                            menu:
                                                                                                                "KAÇ":
                                                                                                                    "Kaçmaya çalışırken seni yakaladılar ve biri kolllarından biri bacaklarından çekti ve seni öldürdü."#SON###########
                                                                                                                "SAVAŞ": #alt satır SON #############
                                                                                                                    "Üzerine doğru gelen köganın kolunu kesip onu öldürdün diğeri atını ayağını çekip seni yere düşürdü Kılıcını alıp diğerinin ayağanı kestin ancak biri arkandan gelip seni yakaldı ve hepsi birden seni yemeye başladı."
                                                                                        "Sur kapısını kırın içeri giriyoruz.":
                                                                                            "Bir süre ilerledikten sonra aniden 3 metrelik devasa yaratıklar ordunun üstüne doğru koşmaya başladı savunma düzeni almaya çalıştın ama ordunun düzeni bozuldu bazıları kaçmaya çalıştı ama Köganlar eline geçen askelerin kafalarını ısırıyor elleriyle ekiye bölüyor paraçlaıyolarlardı ."
                                                                                            menu:
                                                                                                "KAÇ":
                                                                                                    "Ordun katledilerken kaçtın. uzun bir süre at koşturduktan sonra köganlar senin peşinden geldi ve seni yakalayıp parçalara ayırdılar."#SON##################
                                                                                                "Askerler! Savaş düzeni ÇEMBEER!": #SON################
                                                                                                    "Askerlerinin bir kısmı hala sana sadık ve kendi birliğinle bir düzen oturtmayı başardın Atlarınızdan inmeyerek bir şekilde aradaki boy  farkını kapattınız bir kaç tane köganı indirdin eline onların mor kanları bulaştı kaçmaya çalışan ordun katledildi. etraf kan götürüyor ordun daki askerler yavaş yavaş düşüyor geriye muhafız başı ile sen kaldın bir kaç tanesini de öldürdükten sonra ikinizde öldünüz"
                                                                "Haklısın değerli bakanım":
                                                                    "Yerel bakanın neden bu görevde olduğunu düşünüp ona hak verdin ve araştırma yapmaya karar verdin."
                                                                    hide image Yerel_Bakan
                                                                    menu:
                                                                        "Panzehiri araştırmak için Otacı ile konuşmalıyım": 
                                                                            show Otacı at otaci_poz
                                                                            Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                            menu:
                                                                                "Sende benimle gel beraber gidelim.":
                                                                                    Otacı "Üzgünüm efendim ama parşomendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                                    "Tamam sen burda kal."
                                                                                    hide image Otacı
                                                                                "Ben yalnız gideceğim.":
                                                                                    hide image Otacı
                                                                                    "Büyücün yanına gidip olanları anlatırız"
                                                                                    show Büyücü at buyucu_poz
                                                                                    Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                                    hide image Büyücü
                                                                                    menu:
                                                                                        "Muhafız Başı ile görüşmeliyim":
                                                                                            show Muhafız_Başı at muhafiz_basi_poz
                                                                                            Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                            menu:
                                                                                                "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                                    Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                                    menu:
                                                                                                        "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                            Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                            hide image Muhafız_Başı
                                                                                                        "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                            Muhafız_Başı "Emredersiniz efendim."
                                                                                                            hide image Muhafız_Başı # burda bitiyor story 1 #####################
                                                                        "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                            show Şifacı at sifaci_poz
                                                                            Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                            hide image Şifacı
                                                        "Köganlara kimin panzehir verdiğini araştıralım.":
                                                            menu:                                                               
                                                                "Zehiri araştırmak için Şifacı ile konuşmalıyım":
                                                                    show Şifacı at sifaci_poz
                                                                    Şifacı "Efendim böyle bir zehiri hazırlmak imkansız bu beni aşıyor."
                                                                    hide image Şifacı
                                                                "Panzehiri araştırmak için Otacı ile konuşmalıyım":
                                                                    show Otacı at otaci_poz
                                                                    Otacı "Kralım böyle bir durumun benzeri tarihte yaşanmıştır ama bu bir destan gerçek değil. Büyücünün bu tür zehirlerden anlayacağını düşünüyorum gidip onunla konuşmalısın."
                                                                    menu:
                                                                        "Sende benimle gel beraber gidelim.":
                                                                            Otacı "Üzgünüm efendim ama parşomendeki panzehir hakkında daha çok bilgi toplamak istiyorum."
                                                                            "Tamam sen burda kal."
                                                                            hide image Otacı
                                                                        "Ben yalnız gideceğim.":
                                                                            hide image Otacı
                                                                            "Büyücün yanına gidip olanları anlatırız"
                                                                            show Büyücü at buyucu_poz
                                                                            Büyücü "Daha önce böyle bir zehri baban için hazırladım ama bahsettiğin Köganlardan haberim yok. Muhafız Başı ile görüşmelisin."
                                                                            hide image Büyücü
                                                                            menu:
                                                                                "Muhafız Başı ile görüşmeliyim":
                                                                                    show Muhafız_Başı at muhafiz_basi_poz
                                                                                    Muhafız_Başı "Efendim hafızam gayet yerinde dediklerinize inanmıyorum hiç bir askerin bu tür büyüler kullandığını görmedim."
                                                                                    menu:
                                                                                        "Gel bakalım Muhafız Başı seninle eski kütüphaneye gidelim.":
                                                                                            Muhafız_Başı "Efendim dediğim gibi benim bu olanlardan haberim yok eski Muhafız Başının yardımcısı hala hayatta isterseniz birde ona sorun belki dilediğiniz cevapları ondan alırsınız."
                                                                                            menu:
                                                                                                "Nerden bulacağım Eski Muhafız Başının yardımcısını?":
                                                                                                    Muhafız_Başı "Efendim onu ben ararım bulduğumda ise size haber veririm."# ölen muhafız başının ailesi ile konuş a gelinmedi.
                                                                                                    hide image Muhafız_Başı
                                                                                                "Onu bulmak senin görevin ben ülkemin başında olmalıyım.":
                                                                                                    Muhafız_Başı "Emredersiniz efendim."
                                                                                                    hide image Muhafız_Başı # burda bitiyor story 1 #####################


                
    $ last_dialog= None
    $ main_story_count += 1
    jump random_dialog
    return