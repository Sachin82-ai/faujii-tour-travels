"""All site content. Text is (English, Hindi) tuples. Edit here, not in templates."""

BUSINESS = {
    "name": ("Faujii Tour & Travels", "फौजी टूर एंड ट्रैवल्स"),
    "owner": ("Ex/Havaldar Upender Singh", "पूर्व हवलदार उपेंद्र सिंह"),
    "phone": "8278618368",
    "phone_display": "82786 18368",
    "whatsapp": "918278618368",
    "address": ("Girdharpur, Govardhan Chauraha, Mathura", "गिरधरपुर, गोवर्धन चौराहा, मथुरा"),
    "map_query": "Girdharpur Govardhan Chauraha Mathura",
    "timings": ("Timings: please call to confirm", "समय: कृपया कॉल करके पूछें"),
    "domain": "https://www.faujiitourtravels.com",  # change after domain purchase
    "facebook": "", "instagram": "", "youtube": "",  # fill in to show social icons
}

NAV = [
    ("home", "/", ("Home", "होम")),
    ("about", "/about", ("About", "हमारे बारे में")),
    ("services", "/services", ("Services", "सेवाएँ")),
    ("braj", "/braj-darshan", ("Braj Darshan", "ब्रज दर्शन")),
    ("packages", "/packages", ("Packages", "पैकेज")),
    ("vehicles", "/vehicles", ("Vehicles", "वाहन")),
    ("destinations", "/destinations", ("Destinations", "स्थान")),
    ("gallery", "/gallery", ("Gallery", "गैलरी")),
    ("guide", "/travel-guide", ("Travel Guide", "यात्रा गाइड")),
    ("contact", "/contact", ("Contact Us", "संपर्क करें")),
]

# Only services the business actually offers should stay here.
SERVICES = [
    ("fa-taxi", ("Local Taxi Services", "लोकल टैक्सी सेवा"),
     ("Local transportation in Mathura and surrounding areas.", "मथुरा और आसपास के क्षेत्रों में स्थानीय यात्रा।")),
    ("fa-om", ("Braj Darshan", "ब्रज दर्शन"),
     ("Religious and cultural sightseeing tours.", "धार्मिक और सांस्कृतिक दर्शन यात्राएँ।")),
    ("fa-route", ("Outstation Travel", "आउटस्टेशन यात्रा"),
     ("Long-distance trips and intercity journeys.", "लंबी दूरी और शहरों के बीच की यात्राएँ।")),
    ("fa-plane-departure", ("Airport Transfers", "एयरपोर्ट ट्रांसफर"),
     ("Airport pickup and drop services.", "एयरपोर्ट पिकअप और ड्रॉप सेवा।")),
    ("fa-ring", ("Wedding Car Services", "शादी के लिए कार सेवा"),
     ("Travel arrangements for special occasions.", "विशेष अवसरों के लिए यात्रा व्यवस्था।")),
    ("fa-briefcase", ("Corporate Travel", "कॉर्पोरेट यात्रा"),
     ("Transportation for business travel.", "व्यावसायिक यात्रा के लिए वाहन।")),
]

DESTINATIONS = [
    dict(id="mathura", icon="fa-landmark", color="#101B50", name=("Mathura", "मथुरा"),
         tag=("The birthplace of Lord Krishna", "भगवान श्रीकृष्ण की जन्मभूमि"),
         about=("One of India's seven holiest cities, Mathura is the centre of Braj culture and home to the Krishna Janmasthan complex.",
                "भारत की सात पवित्र नगरियों में से एक, मथुरा ब्रज संस्कृति का केंद्र है और यहाँ श्रीकृष्ण जन्मस्थान परिसर है।"),
         sig=("Traditionally regarded as the birthplace of Lord Krishna.", "परंपरा के अनुसार भगवान श्रीकृष्ण का जन्मस्थान।"),
         location=("Mathura, Uttar Pradesh", "मथुरा, उत्तर प्रदेश"), duration=("3–4 hours", "3–4 घंटे"),
         nearby=("Vishram Ghat, Dwarkadhish Temple, Janmasthan", "विश्राम घाट, द्वारकाधीश मंदिर, जन्मस्थान")),
    dict(id="vrindavan", icon="fa-place-of-worship", color="#E96C19", name=("Vrindavan", "वृंदावन"),
         tag=("Land of temples and devotion", "मंदिरों और भक्ति की भूमि"),
         about=("A town of thousands of temples where Krishna is said to have spent his youth. Famous for Banke Bihari, Prem Mandir and ISKCON.",
                "हज़ारों मंदिरों का नगर, जहाँ माना जाता है कि श्रीकृष्ण ने अपनी युवावस्था बिताई। बाँके बिहारी, प्रेम मंदिर और इस्कॉन के लिए प्रसिद्ध।"),
         sig=("Centre of Krishna devotion and the Radha-Krishna tradition.", "राधा-कृष्ण भक्ति परंपरा का प्रमुख केंद्र।"),
         location=("Vrindavan, ~12 km from Mathura", "वृंदावन, मथुरा से लगभग 12 किमी"), duration=("4–5 hours", "4–5 घंटे"),
         nearby=("Banke Bihari Temple, Prem Mandir, ISKCON Temple", "बाँके बिहारी मंदिर, प्रेम मंदिर, इस्कॉन मंदिर")),
    dict(id="govardhan", icon="fa-mountain", color="#8a5a12", name=("Govardhan", "गोवर्धन"),
         tag=("The sacred hill of Giriraj", "पवित्र गिरिराज पर्वत"),
         about=("Devotees perform the Govardhan Parikrama around the sacred Giriraj hill, associated with Krishna lifting the hill.",
                "श्रद्धालु पवित्र गिरिराज पर्वत की परिक्रमा करते हैं, जो श्रीकृष्ण द्वारा पर्वत उठाने की कथा से जुड़ा है।"),
         sig=("Giriraj is worshipped as a form of Krishna.", "गिरिराज जी को श्रीकृष्ण का स्वरूप मानकर पूजा जाता है।"),
         location=("Govardhan, ~22 km from Mathura", "गोवर्धन, मथुरा से लगभग 22 किमी"), duration=("2–3 hours (darshan)", "2–3 घंटे (दर्शन)"),
         nearby=("Mansi Ganga, Daan Ghati, Radha Kund", "मानसी गंगा, दान घाटी, राधा कुंड")),
    dict(id="barsana", icon="fa-dharmachakra", color="#b3265c", name=("Barsana", "बरसाना"),
         tag=("Hometown of Shri Radha Rani", "श्री राधा रानी की नगरी"),
         about=("Barsana is crowned by the Shriji (Radha Rani) Temple on the hill and is world-famous for its Lathmar Holi.",
                "बरसाना की पहाड़ी पर श्रीजी (राधा रानी) मंदिर स्थित है और यह लट्ठमार होली के लिए विश्वप्रसिद्ध है।"),
         sig=("Regarded as the birthplace of Radha.", "राधा जी की जन्मस्थली माना जाता है।"),
         location=("Barsana, ~50 km from Mathura", "बरसाना, मथुरा से लगभग 50 किमी"), duration=("2–3 hours", "2–3 घंटे"),
         nearby=("Shriji Temple, Prem Sarovar, Nandgaon", "श्रीजी मंदिर, प्रेम सरोवर, नंदगाँव")),
    dict(id="nandgaon", icon="fa-torii-gate", color="#1b6b5a", name=("Nandgaon", "नंदगाँव"),
         tag=("Home of Nand Baba", "नंद बाबा का गाँव"),
         about=("Nandgaon is associated with Krishna's childhood home with Nand Baba and Yashoda, with a temple on the hilltop.",
                "नंदगाँव श्रीकृष्ण के नंद बाबा और यशोदा जी के साथ बचपन के घर से जुड़ा है; पहाड़ी पर मंदिर स्थित है।"),
         sig=("Krishna's childhood home in Braj tradition.", "ब्रज परंपरा में श्रीकृष्ण का बाल्यकाल का निवास।"),
         location=("Nandgaon, ~8 km from Barsana", "नंदगाँव, बरसाना से लगभग 8 किमी"), duration=("1–2 hours", "1–2 घंटे"),
         nearby=("Nand Bhavan, Pavan Sarovar, Barsana", "नंद भवन, पावन सरोवर, बरसाना")),
    dict(id="gokul", icon="fa-baby", color="#2b6cb0", name=("Gokul", "गोकुल"),
         tag=("Where Krishna grew up", "जहाँ कृष्ण ने बचपन बिताया"),
         about=("Gokul on the Yamuna is linked to Krishna's infancy. Nearby are Raman Reti, Brahmand Ghat and Chaurasi Khamba.",
                "यमुना किनारे गोकुल श्रीकृष्ण के शैशव से जुड़ा है। पास में रमण रेती, ब्रह्मांड घाट और चौरासी खंभा हैं।"),
         sig=("Associated with Krishna's childhood leelas.", "श्रीकृष्ण की बाल लीलाओं से जुड़ा स्थल।"),
         location=("Gokul, ~15 km from Mathura", "गोकुल, मथुरा से लगभग 15 किमी"), duration=("2–3 hours", "2–3 घंटे"),
         nearby=("Raman Reti, Brahmand Ghat, Chaurasi Khamba", "रमण रेती, ब्रह्मांड घाट, चौरासी खंभा")),
    dict(id="agra", icon="fa-mosque", color="#6b4e9b", name=("Agra", "आगरा"),
         tag=("Home of the Taj Mahal", "ताजमहल का शहर"),
         about=("Agra is about 55 km from Mathura and is home to the Taj Mahal, Agra Fort and other Mughal monuments.",
                "आगरा मथुरा से लगभग 55 किमी दूर है और यहाँ ताजमहल, आगरा किला व अन्य मुगलकालीन स्मारक हैं।"),
         sig=("UNESCO World Heritage city of Mughal architecture.", "मुगल स्थापत्य का यूनेस्को विश्व धरोहर शहर।"),
         location=("Agra, ~55 km from Mathura", "आगरा, मथुरा से लगभग 55 किमी"), duration=("Full day", "पूरा दिन"),
         nearby=("Taj Mahal, Agra Fort, Mehtab Bagh", "ताजमहल, आगरा किला, मेहताब बाग")),
    dict(id="fatehpur-sikri", icon="fa-chess-rook", color="#a0522d", name=("Fatehpur Sikri", "फतेहपुर सीकरी"),
         tag=("Akbar's red sandstone capital", "अकबर की लाल बलुआ पत्थर की राजधानी"),
         about=("A well-preserved Mughal city built by Emperor Akbar, with the Buland Darwaza and Jama Masjid.",
                "सम्राट अकबर द्वारा बसाया गया सुरक्षित मुगल नगर, जहाँ बुलंद दरवाज़ा और जामा मस्जिद हैं।"),
         sig=("UNESCO World Heritage Site.", "यूनेस्को विश्व धरोहर स्थल।"),
         location=("Near Agra, ~40 km", "आगरा के पास, लगभग 40 किमी"), duration=("2–3 hours", "2–3 घंटे"),
         nearby=("Buland Darwaza, Jama Masjid, Agra", "बुलंद दरवाज़ा, जामा मस्जिद, आगरा")),
]

# Braj Darshan groups from the poster
BRAJ_GROUPS = [
    (("Group 1", "समूह 1"), ["nandgaon", "barsana", "govardhan"], None),
    (("Group 2", "समूह 2"), ["gokul"],
     [("Raman Reti", "रमण रेती"), ("Brahmand Ghat", "ब्रह्मांड घाट"),
      ("Chaurasi Khamba", "चौरासी खंभा"), ("Janmasthan", "जन्मस्थान")]),
]
BRAJ_EXTRA = [("Banke Bihari Temple", "बाँके बिहारी मंदिर"), ("Prem Mandir", "प्रेम मंदिर"),
              ("ISKCON Temple", "इस्कॉन मंदिर"), ("Dwarkadhish Temple", "द्वारकाधीश मंदिर")]

# Prices intentionally NOT published. Set price=("₹...", "₹...") after the rate chart is final.
PACKAGES = [
    dict(id="mathura-local", icon="fa-landmark", color="#101B50", name=("Mathura Local Tour", "मथुरा लोकल टूर"),
         places=("Janmasthan, Vishram Ghat, Dwarkadhish Temple", "जन्मस्थान, विश्राम घाट, द्वारकाधीश मंदिर"),
         duration=("Half day", "आधा दिन"), price=None),
    dict(id="vrindavan", icon="fa-place-of-worship", color="#E96C19", name=("Vrindavan Darshan", "वृंदावन दर्शन"),
         places=("Banke Bihari, Prem Mandir, ISKCON", "बाँके बिहारी, प्रेम मंदिर, इस्कॉन"),
         duration=("Half day", "आधा दिन"), price=None),
    dict(id="complete-braj", icon="fa-om", color="#8a5a12", name=("Complete Braj Darshan", "संपूर्ण ब्रज दर्शन"),
         places=("Nandgaon, Barsana, Govardhan, Gokul, Raman Reti, Brahmand Ghat, Chaurasi Khamba, Janmasthan",
                 "नंदगाँव, बरसाना, गोवर्धन, गोकुल, रमण रेती, ब्रह्मांड घाट, चौरासी खंभा, जन्मस्थान"),
         duration=("Full day", "पूरा दिन"), price=None),
    dict(id="govardhan-barsana", icon="fa-mountain", color="#b3265c", name=("Govardhan and Barsana Tour", "गोवर्धन और बरसाना टूर"),
         places=("Govardhan, Barsana, Nandgaon", "गोवर्धन, बरसाना, नंदगाँव"),
         duration=("Full day", "पूरा दिन"), price=None),
    dict(id="mathura-agra", icon="fa-mosque", color="#6b4e9b", name=("Mathura–Agra Tour", "मथुरा–आगरा टूर"),
         places=("Agra and nearby sights", "आगरा और आसपास के स्थल"),
         duration=("Full day", "पूरा दिन"), price=None),
    dict(id="taj-fatehpur", icon="fa-chess-rook", color="#a0522d", name=("Taj Mahal & Fatehpur Sikri Tour", "ताजमहल और फतेहपुर सीकरी टूर"),
         places=("Taj Mahal, Agra Fort, Fatehpur Sikri", "ताजमहल, आगरा किला, फतेहपुर सीकरी"),
         duration=("Full day", "पूरा दिन"), price=None),
    dict(id="custom", icon="fa-route", color="#1b6b5a", name=("Custom Outstation Trips", "कस्टम आउटस्टेशन यात्रा"),
         places=("Your choice of destination", "आपकी पसंद का गंतव्य"),
         duration=("As required", "आवश्यकतानुसार"), price=None),
]
PACKAGE_INCLUDES = [("Vehicle with driver", "ड्राइवर सहित वाहन"), ("Pick-up and drop", "पिकअप और ड्रॉप")]
PACKAGE_EXCLUDES = [("Entry tickets & meals", "प्रवेश टिकट और भोजन"), ("Tolls / parking (confirm)", "टोल / पार्किंग (पुष्टि करें)")]
PACKAGE_VEHICLES = ("AC / Non-AC car", "एसी / नॉन-एसी कार")

# Replace with the real fleet (model, capacity) once photos and details are confirmed.
VEHICLES = [
    dict(id="ac-car", color="#101B50", icon="fa-car-side", name=("AC Car", "एसी कार"), ac=("AC", "एसी"),
         seats=("Contact for details", "विवरण के लिए संपर्क करें"),
         use=("Local sightseeing, Braj Darshan, outstation", "लोकल दर्शन, ब्रज दर्शन, आउटस्टेशन")),
    dict(id="non-ac-car", color="#8a5a12", icon="fa-car", name=("Non-AC Car", "नॉन-एसी कार"), ac=("Non-AC", "नॉन-एसी"),
         seats=("Contact for details", "विवरण के लिए संपर्क करें"),
         use=("Local trips and budget-friendly travel", "लोकल यात्राएँ और किफ़ायती सफ़र")),
]

GALLERY_CATEGORIES = [
    ("vehicles", ("Vehicles", "वाहन")), ("braj", ("Braj Darshan", "ब्रज दर्शन")),
    ("temples", ("Temples", "मंदिर")), ("destinations", ("Destinations", "पर्यटन स्थल")),
    ("company", ("Our Service", "हमारी सेवा")),
]
# Add real photos: ("file name inside static/images/gallery/", category, caption)
GALLERY = [
    ("g01.jpg", "temples", "Prem Mandir, Vrindavan"),
    ("g02.jpg", "temples", "Prem Mandir lit up at night"),
    ("g03.jpg", "temples", "Shrine at Vishram Ghat, Mathura"),
    ("g04.jpg", "destinations", "Taj Mahal reflection"),
    ("g05.jpg", "destinations", "Agra Fort gardens"),
    ("g06.jpg", "destinations", "Agra Fort walls"),
    ("g07.jpg", "destinations", "Agra Fort entrance"),
    ("g08.jpg", "destinations", "Diwan-i-Am, Agra Fort"),
    ("g09.jpg", "braj", "Radha Kund, Govardhan"),
    ("g10.jpg", "braj", "Radha Kund and Shyam Kund"),
    ("g11.jpg", "braj", "Kusum Sarovar, Govardhan"),
    ("g12.jpg", "braj", "View over Barsana"),
    ("g13.jpg", "temples", "Radha Krishna deities, Vrindavan"),
    ("g15.jpg", "destinations", "Taj Mahal, Agra"),
    ("g16.jpg", "temples", "Temple at Gokul"),
]

GUIDES = [
    dict(id="mathura-places", title=("Best Places to Visit in Mathura", "मथुरा में घूमने की सबसे अच्छी जगहें"),
         body=("Start at the Krishna Janmasthan complex, walk to Vishram Ghat on the Yamuna and visit the Dwarkadhish Temple. Keep 3–4 hours for a relaxed visit.",
               "कृष्ण जन्मस्थान से शुरुआत करें, यमुना किनारे विश्राम घाट जाएँ और द्वारकाधीश मंदिर के दर्शन करें। आराम से घूमने के लिए 3–4 घंटे रखें।")),
    dict(id="braj-guide", title=("Complete Braj Darshan Travel Guide", "संपूर्ण ब्रज दर्शन यात्रा गाइड"),
         body=("A full Braj Darshan covers Nandgaon, Barsana, Govardhan, Gokul, Raman Reti, Brahmand Ghat, Chaurasi Khamba and Janmasthan. Start early and wear comfortable footwear.",
               "संपूर्ण ब्रज दर्शन में नंदगाँव, बरसाना, गोवर्धन, गोकुल, रमण रेती, ब्रह्मांड घाट, चौरासी खंभा और जन्मस्थान शामिल हैं। सुबह जल्दी निकलें और आरामदायक जूते पहनें।")),
    dict(id="mathura-vrindavan", title=("Mathura to Vrindavan Travel Guide", "मथुरा से वृंदावन यात्रा गाइड"),
         body=("Vrindavan is about 12 km from Mathura. Temples close for a break in the afternoon, so plan darshan for morning or evening and confirm timings.",
               "वृंदावन मथुरा से लगभग 12 किमी है। दोपहर में मंदिर बंद रहते हैं, इसलिए सुबह या शाम का दर्शन चुनें और समय की पुष्टि करें।")),
    dict(id="govardhan-parikrama", title=("Govardhan Parikrama Guide", "गोवर्धन परिक्रमा गाइड"),
         body=("The traditional parikrama is roughly 21 km and is commonly walked. Many visitors do darshan at key points by car instead; ask us about options.",
               "पारंपरिक परिक्रमा लगभग 21 किमी की है और अक्सर पैदल की जाती है। कई यात्री कार से प्रमुख स्थलों का दर्शन करते हैं; विकल्पों के लिए हमसे पूछें।")),
    dict(id="barsana-time", title=("Best Time to Visit Barsana", "बरसाना जाने का सबसे अच्छा समय"),
         body=("Winter (October–March) is the most comfortable. Lathmar Holi in February–March is famous but very crowded, so book transport well in advance.",
               "सर्दियाँ (अक्टूबर–मार्च) सबसे सुविधाजनक हैं। फरवरी–मार्च की लट्ठमार होली प्रसिद्ध है लेकिन बहुत भीड़ होती है, इसलिए वाहन पहले से तय करें।")),
    dict(id="mathura-agra", title=("Mathura to Agra Travel Guide", "मथुरा से आगरा यात्रा गाइड"),
         body=("Agra is roughly 55 km from Mathura. Note that the Taj Mahal is closed on Fridays; start early to combine it with Fatehpur Sikri.",
               "आगरा मथुरा से लगभग 55 किमी है। ताजमहल शुक्रवार को बंद रहता है; फतेहपुर सीकरी के साथ घूमने के लिए जल्दी निकलें।")),
]

WHY = [
    ("fa-user-shield", ("Safe & Disciplined", "सुरक्षित और अनुशासित"),
     ("Run by an ex-serviceman who values punctuality and your safety.", "एक पूर्व सैनिक द्वारा संचालित, समय और आपकी सुरक्षा को प्राथमिकता।")),
    ("fa-map-location-dot", ("Local Braj Knowledge", "ब्रज की स्थानीय जानकारी"),
     ("Based in Mathura, we know the temples, routes and best timings.", "मथुरा में स्थित, हमें मंदिरों, मार्गों और सही समय की जानकारी है।")),
    ("fa-snowflake", ("AC & Non-AC Cars", "एसी और नॉन-एसी कारें"),
     ("Choose the comfort level that fits your budget.", "अपने बजट के अनुसार आरामदायक विकल्प चुनें।")),
    ("fa-handshake", ("Transparent Service", "पारदर्शी सेवा"),
     ("Talk to us directly and confirm everything before you travel.", "सीधे बात करें और यात्रा से पहले सब कुछ तय करें।")),
]

ROUTES = [("Mathura → Vrindavan", "मथुरा → वृंदावन"), ("Mathura → Govardhan", "मथुरा → गोवर्धन"),
          ("Mathura → Barsana", "मथुरा → बरसाना"), ("Mathura → Agra", "मथुरा → आगरा"),
          ("Mathura → Fatehpur Sikri", "मथुरा → फतेहपुर सीकरी")]

FAQS = [
    (("Do I need to fill any form to book?", "क्या बुकिंग के लिए कोई फ़ॉर्म भरना होगा?"),
     ("No. Just call or message us on WhatsApp and we will confirm your trip directly.", "नहीं। बस कॉल करें या WhatsApp पर संदेश भेजें, हम सीधे आपकी यात्रा तय कर देंगे।")),
    (("How much does a tour cost?", "टूर का खर्च कितना है?"),
     ("Prices depend on the package, vehicle and distance. Please contact us for the current rate.", "कीमत पैकेज, वाहन और दूरी पर निर्भर करती है। कृपया वर्तमान दर के लिए संपर्क करें।")),
    (("Are AC cars available?", "क्या एसी कारें उपलब्ध हैं?"),
     ("Yes, we offer both AC and Non-AC cars. Contact us to check availability.", "हाँ, हमारे पास एसी और नॉन-एसी दोनों कारें हैं। उपलब्धता के लिए संपर्क करें।")),
    (("Can you plan a custom trip?", "क्या आप कस्टम यात्रा बना सकते हैं?"),
     ("Yes, tell us where you want to go and we will arrange it.", "हाँ, बताइए आप कहाँ जाना चाहते हैं, हम व्यवस्था कर देंगे।")),
]
