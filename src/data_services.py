# -*- coding: utf-8 -*-
"""Prestations d'assainissement. Chaque service génère une page dédiée et une page par commune principale.

Prix : seuls les prix confirmés par l'entreprise sont affichés (`price_min`). `None` = « sur devis ».
"""

SERVICES = [
    # ------------------------------------------------------------------ DÉBOUCHAGE URGENCE
    {
        "slug": "degorgement-canalisation-var",
        "image": "debouchage-wc.jpg",
        "image_alt": "Débouchage d'un WC bouché avec une pompe manuelle",
        "combo": "degorgement",
        "name": "Dégorgement & débouchage 24h/24",
        "short": "Dégorgement 24h/24",
        "icon": "bolt",
        "badge": "Urgence 24/7",
        "price_label": "à partir de 99 €",
        "price_min": 99,
        "title": "Dégorgement et débouchage de canalisations 24h/24",
        "meta": "Dégorgement et débouchage de canalisations, égouts, colonnes et WC, 24h/24 et 7j/7. Furet, hydrocureur haute pression. Prix annoncé avant déplacement. ☎ 06 75 93 19 04",
        "h1": "Dégorgement et débouchage de canalisations 24h/24",
        "lead": "Canalisation principale bouchée, égout qui refoule, colonne d'immeuble obstruée, WC bouché : nous dégorgeons tous les réseaux, du simple évier au collecteur. Un technicien vous répond <b>jour et nuit, week-end et jours fériés compris</b>.",
        "checks": ["Réponse immédiate au téléphone", "Prix annoncé avant de partir", "Matériel professionnel"],
        "card_desc": "Dégorgement de canalisations, égouts, colonnes et WC, jour et nuit, au furet ou à l'hydrocureur.",
        "card_checks": ["Disponible 7j/7", "Du WC au collecteur"],
        "sections": [
            ("Dégorgement : quels réseaux traitons-nous ?",
             "<p>Un bouchon peut se former à n'importe quel endroit du réseau d'évacuation. Nous intervenons sur :</p>"
             "<ul><li><strong>Les WC bouchés</strong>, y compris les WC suspendus et les sanibroyeurs.</li>"
             "<li><strong>Les éviers, lavabos, douches et baignoires</strong> qui s'écoulent mal ou plus du tout.</li>"
             "<li><strong>Les colonnes d'immeuble</strong> et chutes d'eaux usées communes.</li>"
             "<li><strong>Les canalisations enterrées</strong> entre la maison et le tout-à-l'égout ou la fosse.</li>"
             "<li><strong>Les regards et siphons de sol</strong> qui débordent, les eaux pluviales et caniveaux.</li>"
             "<li><strong>Les collecteurs et réseaux privés</strong> de copropriétés, lotissements, campings, hôtels et zones d'activité.</li></ul>"
             "<p>Pour les gros bouchons et les réseaux de grand diamètre, nous intervenons avec un <strong>camion hydrocureur</strong> (haute pression et aspiration).</p>"),
            ("Les bonnes techniques selon le bouchon",
             "<p>Nous choisissons la méthode la moins agressive pour vos canalisations :</p>"
             "<ol><li><strong>Pompe et ventouse professionnelles</strong> pour les bouchons proches de l'appareil.</li>"
             "<li><strong>Furet électrique</strong> pour atteindre un bouchon situé plus loin dans la canalisation.</li>"
             "<li><strong>Hydrocurage haute pression</strong> pour les canalisations encrassées, les racines et les dépôts de graisse ou de calcaire.</li>"
             "<li><strong>Inspection caméra</strong> si le bouchon revient : elle montre s'il s'agit d'une contre-pente, d'un tuyau écrasé ou de racines.</li></ol>"
             "<p>Nous déconseillons les produits déboucheurs corrosifs : ils abîment les joints et les tuyaux en PVC ou en fonte, et sont dangereux pour la personne qui intervient ensuite.</p>"),
            ("Débouchage la nuit, le dimanche et les jours fériés",
             "<p>Un WC bouché quand il n'y en a qu'un dans le logement, ou des eaux usées qui remontent dans la douche, ne peuvent pas attendre lundi. La ligne <strong>06 75 93 19 04</strong> est ouverte 24h/24. Les majorations de nuit, de week-end et de jour férié sont <strong>toujours annoncées avant le déplacement</strong>.</p>"
             "<p>À la fin de l'intervention, vous recevez une facture détaillée et, si le problème risque de revenir, une explication claire de sa cause et des solutions possibles.</p>"),
        ],
        "faq": [
            ("Combien coûte un dégorgement ?", "Un dégorgement simple démarre à 99 € TTC en journée. Le prix dépend de l'emplacement du bouchon, de la méthode (pompe, furet, haute pression) et de l'horaire ; il est annoncé au téléphone avant le départ et confirmé sur place."),
            ("Mon WC est bouché, que faire en attendant ?", "Ne tirez plus la chasse d'eau, coupez l'arrivée d'eau du réservoir et n'utilisez pas de produit corrosif. Une ventouse peut suffire pour un bouchon léger ; sinon, appelez-nous."),
            ("Le bouchon revient régulièrement, pourquoi ?", "Un bouchon récurrent signale souvent un défaut de la canalisation : contre-pente, racines, tuyau affaissé ou encrassement important. Une inspection caméra permet d'en trouver la cause avant de décider d'un curage ou d'une réparation."),
            ("Qui paie le débouchage dans un immeuble ?", "Si le bouchon est dans les canalisations privatives d'un logement, c'est en principe l'occupant. S'il est dans une colonne commune, c'est la copropriété, via le syndic. Nous indiquons sur la facture où se trouvait le bouchon."),
        ],
        "combo_h1": "Dégorgement de canalisations 24h/24",
        "combo_title": "Dégorgement {city} ({cp}) — canalisation, égout, WC 24h/24",
        "combo_meta": "Dégorgement et débouchage {a} 24h/24 et 7j/7 : canalisation, égout, colonne, WC. {delay_txt}. Prix annoncé avant déplacement. ☎ 06 75 93 19 04",
        "combo_intros": [
            "WC bouché, évier qui déborde, canalisation qui refoule : {a}, un technicien vous répond à toute heure au <b>06 75 93 19 04</b> et part avec le matériel adapté. Le délai et le prix vous sont donnés dès l'appel.",
            "Besoin d'un dégorgement tout de suite {a} ? Notre ligne est ouverte jour et nuit, dimanches et jours fériés compris. Pompe, furet ou haute pression : nous choisissons la méthode la moins agressive pour vos canalisations.",
            "Habitants {de}, gardez ce numéro : <b>06 75 93 19 04</b>. Pour un WC bouché ou une canalisation qui refoule, un artisan du secteur vous répond directement, sans plateforme, avec un prix annoncé à l'avance.",
        ],
        "combo_points": [
            "WC bouché ou sanibroyeur en panne",
            "Évier, lavabo ou douche qui ne s'écoule plus",
            "Canalisation qui refoule ou regard qui déborde",
            "Colonne d'immeuble obstruée",
            "Odeurs d'égout et écoulement lent",
            "Bouchon récurrent à diagnostiquer",
        ],
        "combo_tip": "En attendant notre arrivée, n'utilisez plus l'évacuation bouchée, coupez l'arrivée d'eau du WC si besoin et évitez les produits déboucheurs chimiques : ils n'agissent pas sur les vrais bouchons et abîment les tuyaux.",
    },
    # ------------------------------------------------------------------ CURAGE
    {
        "slug": "curage-canalisation-var",
        "image": "curage-hydrocurage.jpg",
        "image_alt": "Hydrocurage haute pression d'une canalisation depuis un regard",
        "combo": "curage-canalisation",
        "name": "Hydrocurage & curage de réseaux",
        "short": "Curage haute pression",
        "icon": "pipe",
        "badge": "Entretien",
        "price_label": "à partir de 190 €",
        "price_min": 190,
        "title": "Curage et hydrocurage de canalisations — haute pression",
        "meta": "Curage et hydrocurage haute pression des canalisations : graisses, calcaire, racines, sable. Particuliers, copropriétés, restaurants. Devis gratuit. ☎ 06 75 93 19 04",
        "h1": "Curage et hydrocurage de canalisations",
        "lead": "Graisses, calcaire, racines, sable, boues : notre <b>hydrocureur haute pression</b> nettoie l'intérieur des canalisations sur toute leur longueur et redonne un écoulement normal, durablement.",
        "checks": ["Haute pression adaptée au tuyau", "Particuliers et professionnels", "Devis gratuit"],
        "card_desc": "Nettoyage complet des canalisations à l'eau sous haute pression : graisses, calcaire, racines, sable.",
        "card_checks": ["Prévient les bouchons", "Contrôle caméra possible"],
        "sections": [
            ("Débouchage ou curage : quelle différence ?",
             "<p>Le débouchage supprime un bouchon pour rétablir l'écoulement. Le <strong>curage</strong> va plus loin : il nettoie toute la paroi intérieure de la canalisation, enlève les dépôts accumulés et rend au tuyau son diamètre d'origine. C'est la solution quand les bouchons se répètent ou quand l'écoulement ralentit petit à petit.</p>"),
            ("Comment se déroule un hydrocurage ?",
             "<ol><li><strong>Repérage</strong> du réseau : regards, tés de visite, sens d'écoulement.</li>"
             "<li><strong>Passage de la buse haute pression</strong>, choisie selon le diamètre et la matière du tuyau (PVC, fonte, grès, béton).</li>"
             "<li><strong>Évacuation des dépôts</strong> vers le réseau ou par aspiration.</li>"
             "<li><strong>Contrôle</strong> de l'écoulement et, si besoin, inspection caméra pour vérifier l'état de la canalisation.</li></ol>"),
            ("Pour qui ?",
             "<p>Maisons individuelles, <strong>copropriétés</strong> (colonnes et réseaux enterrés), <strong>restaurants et commerces</strong> (canalisations chargées en graisses), campings, résidences de tourisme et locaux professionnels. Pour les sites qui en ont besoin, nous proposons un curage préventif à intervalles réguliers.</p>"),
        ],
        "faq": [
            ("À quelle fréquence faut-il curer ses canalisations ?", "Pour une maison, un curage est utile en cas de ralentissements répétés ou tous les 5 à 10 ans selon l'usage. Pour un restaurant ou une copropriété, un curage préventif annuel ou semestriel évite les bouchons."),
            ("Le curage haute pression peut-il abîmer mes tuyaux ?", "Non si la pression et la buse sont adaptées au tuyau. Sur une canalisation très ancienne ou fragile, nous contrôlons d'abord son état à la caméra."),
            ("Combien coûte un curage ?", "Le prix dépend de la longueur du réseau, de son accessibilité et du niveau d'encrassement. Il est établi sur devis gratuit, après un échange au téléphone ou une visite."),
            ("Le curage élimine-t-il les racines ?", "Une buse spéciale coupe et évacue les racines fines. Si les racines ont cassé ou déboîté le tuyau, une réparation est nécessaire : l'inspection caméra permet de le vérifier."),
        ],
        "combo_h1": "Curage de canalisations",
        "combo_title": "Curage canalisation {city} ({cp}) — hydrocurage haute pression",
        "combo_meta": "Curage et hydrocurage de canalisations {a} : graisses, calcaire, racines. {delay_txt}. Devis gratuit. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Des bouchons qui reviennent, un écoulement qui ralentit, des odeurs : {a}, le curage haute pression nettoie vos canalisations sur toute leur longueur et règle le problème à la source.",
            "Nous réalisons le curage et l'hydrocurage des canalisations {a}, pour les maisons, les copropriétés et les professionnels. Devis gratuit, intervention planifiée ou en urgence.",
            "Canalisations encrassées par les graisses, le calcaire ou les racines ? Nous intervenons {a} avec du matériel haute pression adapté à chaque diamètre de tuyau.",
        ],
        "combo_points": [
            "Hydrocurage haute pression des canalisations",
            "Curage des colonnes d'immeuble",
            "Élimination des graisses et du calcaire",
            "Coupe des racines dans les réseaux enterrés",
            "Curage préventif pour restaurants et commerces",
            "Contrôle caméra après curage",
        ],
        "combo_tip": "Pour éviter l'encrassement, ne versez jamais d'huile de friture ni de graisses dans l'évier : laissez-les refroidir et jetez-les à la poubelle ou en déchèterie.",
    },
    # ------------------------------------------------------------------ FOSSE SEPTIQUE
    {
        "slug": "vidange-fosse-septique-var",
        "image": "fosse-septique.jpg",
        "image_alt": "Vidange d'une fosse septique par camion",
        "combo": "vidange-fosse-septique",
        "name": "Vidange de fosse septique & micro-station",
        "short": "Vidange fosse septique",
        "icon": "tank",
        "badge": "Assainissement individuel",
        "price_label": "à partir de 230 €",
        "price_min": 230,
        "title": "Vidange de fosse septique et fosse toutes eaux",
        "meta": "Vidange de fosse septique, fosse toutes eaux et micro-station. Bac dégraisseur, préfiltre, contrôle SPANC, vente immobilière. Devis gratuit. ☎ 06 75 93 19 04",
        "h1": "Vidange de fosse septique, fosse toutes eaux et micro-station",
        "lead": "Dans les communes de la région non raccordées au tout-à-l'égout, la fosse doit être vidangée régulièrement. Nous intervenons pour la <b>vidange, le nettoyage et l'entretien</b> de votre installation d'assainissement individuel.",
        "checks": ["Fosse septique et toutes eaux", "Micro-station et bac dégraisseur", "Justificatif de vidange"],
        "card_desc": "Vidange et entretien des fosses septiques, fosses toutes eaux, micro-stations et bacs dégraisseurs.",
        "card_checks": ["Entretien et urgence", "Utile pour le SPANC"],
        "sections": [
            ("Quand faut-il vidanger sa fosse ?",
             "<p>La réglementation impose de vidanger une fosse lorsque la hauteur des boues atteint <strong>50 % du volume utile</strong>. En pratique, cela représente souvent une vidange tous les <strong>4 ans environ</strong> pour une fosse toutes eaux, selon sa taille et le nombre d'occupants. Les micro-stations demandent un entretien plus fréquent, selon la notice du fabricant.</p>"
             "<p>Certains signes doivent alerter : <strong>odeurs</strong> autour de la fosse ou dans la maison, <strong>écoulement lent</strong> dans toute la maison, regards qui débordent, herbe anormalement verte au-dessus de l'épandage.</p>"),
            ("Ce que comprend notre intervention",
             "<ul><li><strong>Vidange de la fosse</strong> (septique ou toutes eaux) et du <strong>bac dégraisseur</strong> s'il existe.</li>"
             "<li><strong>Nettoyage du préfiltre</strong> (pouzzolane ou cassette) et contrôle des regards.</li>"
             "<li><strong>Remise en eau</strong> de la fosse pour la remettre en fonctionnement.</li>"
             "<li><strong>Contrôle visuel</strong> de l'état de la fosse, des tés et de la ventilation.</li></ul>"
             "<p>La vidange doit être réalisée par une personne agréée par la préfecture, qui remet un <strong>bordereau de suivi des matières de vidange</strong>. Conservez ce document : le SPANC peut vous le demander lors de son contrôle.</p>"),
            ("Vente immobilière et contrôle SPANC",
             "<p>Lors de la vente d'une maison non raccordée au tout-à-l'égout, un diagnostic de l'assainissement non collectif de moins de 3 ans, réalisé par le SPANC, doit être joint au dossier. Une fosse vidangée, propre et accessible facilite ce contrôle. Si des travaux de mise en conformité sont demandés, nous pouvons vous accompagner (voir nos <a href=\"/travaux-assainissement-var/\">travaux d'assainissement</a>).</p>"),
        ],
        "faq": [
            ("Tous les combien faut-il vidanger une fosse septique ?", "Dès que les boues atteignent 50 % du volume utile, soit souvent tous les 4 ans environ pour une fosse toutes eaux. Une résidence secondaire peu occupée peut attendre plus longtemps ; une famille nombreuse moins."),
            ("Combien coûte une vidange de fosse ?", "Le prix dépend du volume de la fosse, de la présence d'un bac dégraisseur, de la distance entre le camion et la fosse et de l'accessibilité. Il est établi sur devis gratuit."),
            ("Faut-il remplir la fosse après la vidange ?", "Oui, une fosse doit être remise en eau après la vidange pour garder sa stabilité et redémarrer son fonctionnement. Nous le faisons à la fin de l'intervention."),
            ("Faut-il utiliser des activateurs biologiques ?", "Ils ne sont pas indispensables pour une fosse bien dimensionnée et bien utilisée. Le plus important est d'éviter les produits chimiques agressifs, les lingettes et les graisses."),
        ],
        "combo_h1": "Vidange de fosse septique",
        "combo_title": "Vidange fosse septique {city} ({cp}) — fosse toutes eaux, micro-station",
        "combo_meta": "Vidange de fosse septique {a} : fosse toutes eaux, micro-station, bac dégraisseur, préfiltre. {delay_txt}. Devis gratuit. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Votre maison {a} n'est pas raccordée au tout-à-l'égout ? Nous intervenons pour la vidange et l'entretien de votre fosse septique, fosse toutes eaux ou micro-station.",
            "Odeurs, écoulement lent, contrôle SPANC ou vente de la maison : {a}, nous vidangeons et nettoyons votre installation d'assainissement individuel, avec un prix annoncé à l'avance.",
            "Vidange de fosse, nettoyage du bac dégraisseur et du préfiltre : un artisan de la région intervient {a} sur rendez-vous ou en urgence si la fosse déborde.",
        ],
        "combo_points": [
            "Vidange de fosse septique et toutes eaux",
            "Entretien de micro-station",
            "Vidange du bac dégraisseur",
            "Nettoyage du préfiltre et des regards",
            "Remise en eau après vidange",
            "Intervention avant contrôle SPANC ou vente",
        ],
        "combo_tip": "Avant notre venue, dégagez l'accès aux tampons de la fosse et du bac dégraisseur et indiquez-nous la distance entre la route et la fosse : elle conditionne le matériel à prévoir.",
    },
    # ------------------------------------------------------------------ INSPECTION CAMÉRA
    {
        "slug": "inspection-camera-canalisation-var",
        "image": "inspection-camera.jpg",
        "image_alt": "Robot caméra d'inspection dans une canalisation",
        "combo": "inspection-camera",
        "name": "Inspection caméra & diagnostic de canalisations",
        "short": "Inspection caméra",
        "icon": "camera",
        "badge": "Diagnostic",
        "price_label": "à partir de 150 €",
        "price_min": 150,
        "title": "Inspection caméra des canalisations — diagnostic sans casse",
        "meta": "Inspection caméra des canalisations : bouchons récurrents, racines, tuyau cassé, contre-pente, achat immobilier. Diagnostic sans casse. ☎ 06 75 93 19 04",
        "h1": "Inspection caméra des canalisations",
        "lead": "Une caméra introduite dans la canalisation montre son état réel, <b>sans rien casser</b> : bouchon, racines, tuyau écrasé, déboîté ou en contre-pente. Le bon diagnostic avant de décider des travaux.",
        "checks": ["Diagnostic sans casse", "Localisation précise du défaut", "Compte rendu avec images"],
        "card_desc": "Caméra dans la canalisation pour trouver la cause d'un bouchon, d'une odeur ou d'une fuite d'eaux usées.",
        "card_checks": ["Sans casse", "Avant achat ou travaux"],
        "sections": [
            ("Quand faire une inspection caméra ?",
             "<ul><li><strong>Bouchons à répétition</strong> malgré les débouchages.</li>"
             "<li><strong>Odeurs d'égout</strong> persistantes, dans la maison ou le jardin.</li>"
             "<li><strong>Affaissement du sol</strong> ou humidité au-dessus d'une canalisation enterrée.</li>"
             "<li><strong>Avant l'achat d'une maison</strong>, pour vérifier l'état du réseau d'évacuation.</li>"
             "<li><strong>Après un curage</strong>, pour contrôler le résultat, ou avant des travaux de réparation.</li></ul>"),
            ("Ce que montre la caméra",
             "<p>La caméra parcourt la canalisation et filme sa paroi. Elle révèle les <strong>racines</strong>, les <strong>fissures et casses</strong>, les <strong>déboîtements</strong> de joints, les <strong>contre-pentes</strong> où l'eau stagne, les <strong>dépôts</strong> de graisse ou de calcaire et les objets coincés. Un localisateur permet de repérer depuis la surface l'endroit exact du défaut : si une réparation est nécessaire, on ne creuse qu'au bon endroit.</p>"),
            ("Un diagnostic utile pour la suite",
             "<p>Après l'inspection, nous vous expliquons ce que nous avons vu et les solutions possibles : simple curage, réparation localisée ou remplacement d'un tronçon. Les images et le compte rendu vous servent aussi pour votre assurance, votre syndic ou une négociation lors d'un achat.</p>"),
        ],
        "faq": [
            ("L'inspection caméra nécessite-t-elle de casser ?", "Non. La caméra passe par un regard, un té de visite ou parfois par le WC démonté. Aucune ouverture n'est nécessaire pour le diagnostic."),
            ("Faut-il déboucher avant l'inspection ?", "Si la canalisation est complètement bouchée ou très encrassée, un débouchage ou un curage est fait d'abord : la caméra a besoin d'un tuyau dégagé pour voir la paroi."),
            ("Combien coûte une inspection caméra ?", "Le prix dépend de la longueur à inspecter, de l'accès et du besoin de compte rendu détaillé. Il est établi sur devis gratuit."),
            ("Recevrai-je les images ?", "Oui, nous vous remettons un compte rendu avec les observations et des images des points importants."),
        ],
        "combo_h1": "Inspection caméra des canalisations",
        "combo_title": "Inspection caméra canalisation {city} ({cp}) — diagnostic sans casse",
        "combo_meta": "Inspection caméra des canalisations {a} : bouchons récurrents, racines, casse, contre-pente, achat immobilier. {delay_txt}. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Bouchons qui reviennent, odeurs, sol qui s'affaisse : {a}, l'inspection caméra montre l'état réel de vos canalisations sans rien casser, et localise précisément le défaut.",
            "Avant d'acheter une maison {a} ou de lancer des travaux, faites contrôler les canalisations à la caméra : vous savez exactement ce qu'il faut réparer, et où.",
            "Nous réalisons l'inspection caméra des canalisations {a} pour les particuliers, les copropriétés et les professionnels, avec un compte rendu clair.",
        ],
        "combo_points": [
            "Recherche de la cause d'un bouchon récurrent",
            "Détection de racines et de casses",
            "Repérage des contre-pentes et déboîtements",
            "Localisation du défaut depuis la surface",
            "Contrôle avant achat immobilier",
            "Compte rendu avec images",
        ],
        "combo_tip": "Notez quand le problème apparaît (après une douche, une forte pluie, l'utilisation du lave-linge) : ces indices nous aident à cibler la zone à inspecter.",
    },
    # ------------------------------------------------------------------ BAC À GRAISSE
    {
        "slug": "bac-a-graisse-var",
        "image": "bac-a-graisse.jpg",
        "image_alt": "Illustration : entretien d'un bac à graisse de restaurant",
        "combo": "bac-a-graisse",
        "name": "Bac à graisse & séparateur",
        "short": "Bac à graisse",
        "icon": "grease",
        "badge": "Professionnels",
        "price_label": "à partir de 150 €",
        "price_min": 150,
        "title": "Vidange et entretien de bac à graisse — restaurants, commerces",
        "meta": "Vidange, nettoyage et entretien de bacs à graisse et séparateurs : restaurants, snacks, boulangeries, cantines, campings. Contrat d'entretien possible. ☎ 06 75 93 19 04",
        "h1": "Vidange et entretien de bacs à graisse",
        "lead": "Restaurants, snacks, boulangeries, cuisines collectives : un bac à graisse bien entretenu évite les <b>bouchons, les odeurs et les problèmes avec le service des eaux</b>. Nous intervenons ponctuellement ou dans le cadre d'un entretien régulier.",
        "checks": ["Restaurants et collectivités", "Intervention hors service possible", "Entretien régulier"],
        "card_desc": "Vidange, nettoyage et entretien des bacs à graisse des restaurants, commerces et collectivités.",
        "card_checks": ["Hors heures de service", "Entretien planifié"],
        "sections": [
            ("Pourquoi entretenir un bac à graisse ?",
             "<p>Le bac à graisse retient les graisses et les huiles des eaux de cuisine avant qu'elles n'atteignent le réseau. Quand il est plein, les graisses passent dans les canalisations, figent et provoquent <strong>bouchons, refoulements et odeurs</strong>, parfois en plein service. Le règlement d'assainissement de la commune peut aussi exiger un entretien régulier et des justificatifs.</p>"),
            ("Notre intervention",
             "<ul><li><strong>Pompage</strong> des graisses et des boues.</li>"
             "<li><strong>Nettoyage</strong> des parois et des cloisons du bac.</li>"
             "<li><strong>Curage</strong> des canalisations d'arrivée et de sortie si besoin.</li>"
             "<li><strong>Remise en eau</strong> et contrôle du bon fonctionnement.</li></ul>"
             "<p>Nous pouvons intervenir <strong>avant ou après le service</strong>, le matin tôt ou en fin de soirée, pour ne pas gêner votre activité.</p>"),
            ("Quelle fréquence ?",
             "<p>Elle dépend de la taille du bac et du nombre de couverts : souvent tous les 1 à 3 mois pour un restaurant, davantage en pleine saison touristique sur le littoral provençal. Nous vous proposons un rythme adapté et un rappel avant chaque passage.</p>"),
        ],
        "faq": [
            ("À quelle fréquence vidanger un bac à graisse ?", "En général tous les 1 à 3 mois pour un restaurant, selon la taille du bac et l'activité. Un contrôle régulier du niveau de graisse permet d'ajuster."),
            ("Pouvez-vous intervenir en dehors des heures d'ouverture ?", "Oui, nous planifions l'intervention avant ou après le service pour ne pas perturber votre activité."),
            ("Combien coûte l'entretien d'un bac à graisse ?", "Le prix dépend du volume du bac, de son accessibilité et de la fréquence d'entretien. Il est établi sur devis gratuit."),
            ("Mon bac à graisse déborde, intervenez-vous en urgence ?", "Oui, nous intervenons en urgence 24h/24 et 7j/7, y compris le week-end."),
        ],
        "combo_h1": "Entretien de bac à graisse",
        "combo_title": "Bac à graisse {city} ({cp}) — vidange et entretien",
        "combo_meta": "Vidange et entretien de bac à graisse {a} : restaurants, snacks, boulangeries, cantines. {delay_txt}. Devis gratuit. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Restaurant, snack ou boulangerie {a} : nous vidangeons et nettoyons votre bac à graisse, avant ou après le service, pour éviter bouchons et odeurs.",
            "Un bac à graisse plein, c'est le risque d'un refoulement en plein service. {a}, nous assurons la vidange, le nettoyage et l'entretien régulier de vos installations.",
            "Nous entretenons les bacs à graisse et séparateurs des professionnels {de} et des environs, ponctuellement ou selon un calendrier fixé avec vous.",
        ],
        "combo_points": [
            "Vidange et pompage des graisses",
            "Nettoyage complet du bac",
            "Curage des canalisations de cuisine",
            "Intervention avant ou après le service",
            "Entretien régulier planifié",
            "Urgence en cas de débordement",
        ],
        "combo_tip": "Équipez les éviers de cuisine de paniers-filtres et récupérez les huiles de friture dans des bidons : votre bac à graisse se remplira beaucoup moins vite.",
    },
    # ------------------------------------------------------------------ POMPE DE RELEVAGE
    {
        "slug": "pompe-de-relevage-var",
        "image": "pompe-relevage.jpg",
        "image_alt": "Pompe de relevage dans une cuve d'eaux usées",
        "combo": "pompe-de-relevage",
        "name": "Pompe & poste de relevage",
        "short": "Pompe de relevage",
        "icon": "pump",
        "badge": "Dépannage",
        "price_label": "à partir de 120 €",
        "price_min": 120,
        "title": "Pompe de relevage et poste de relevage — dépannage, entretien",
        "meta": "Dépannage, entretien et remplacement de pompes et postes de relevage des eaux usées. Alarme, débordement, pompe bloquée. 24h/24. ☎ 06 75 93 19 04",
        "h1": "Dépannage et entretien de pompes de relevage",
        "lead": "Quand la maison ou le sous-sol est plus bas que l'égout, une <b>pompe de relevage</b> remonte les eaux usées. Si elle s'arrête, tout déborde : nous intervenons en urgence, et pour l'entretien qui évite les pannes.",
        "checks": ["Dépannage 24h/24", "Nettoyage du poste", "Remplacement de pompe"],
        "card_desc": "Dépannage, nettoyage, entretien et remplacement des pompes et postes de relevage des eaux usées.",
        "card_checks": ["Alarme ou débordement", "Entretien annuel"],
        "sections": [
            ("Les pannes les plus fréquentes",
             "<ul><li><strong>Pompe bloquée</strong> par des lingettes, des cheveux ou des dépôts.</li>"
             "<li><strong>Flotteur coincé</strong> : la pompe ne démarre plus ou tourne en continu.</li>"
             "<li><strong>Clapet anti-retour</strong> défaillant : l'eau redescend dans la cuve.</li>"
             "<li><strong>Moteur hors service</strong> après des années de fonctionnement ou un orage.</li>"
             "<li><strong>Alarme de niveau haut</strong> qui sonne : la cuve est sur le point de déborder.</li></ul>"),
            ("Notre intervention",
             "<p>Nous <strong>vidangeons la cuve</strong>, nettoyons la pompe et le flotteur, contrôlons le clapet et l'alimentation électrique. Si la pompe est à remplacer, nous vous proposons un modèle adapté au débit et à la hauteur de relevage, avec un devis avant la pose.</p>"),
            ("Prévenir les pannes",
             "<p>Un <strong>entretien annuel</strong> (nettoyage de la cuve, test du flotteur et de l'alarme) prolonge nettement la vie de la pompe. Et surtout : pas de lingettes dans les WC, même si l'emballage les dit « biodégradables ».</p>"),
        ],
        "faq": [
            ("Mon alarme de poste de relevage sonne, que faire ?", "Limitez immédiatement l'utilisation de l'eau (WC, douche, lave-linge) pour éviter le débordement, vérifiez que le disjoncteur de la pompe n'a pas sauté, puis appelez-nous."),
            ("Pourquoi ma pompe de relevage tourne en continu ?", "Le plus souvent, le flotteur est coincé ou le clapet anti-retour ne ferme plus. Un nettoyage ou le remplacement du clapet suffit souvent."),
            ("Combien coûte le remplacement d'une pompe de relevage ?", "Il dépend du modèle, du débit et de la hauteur de relevage nécessaires, et de l'accès au poste. Nous établissons un devis avant toute pose."),
            ("Intervenez-vous pour les postes de relevage de copropriété ?", "Oui, pour les maisons comme pour les postes collectifs des copropriétés et des locaux professionnels."),
        ],
        "combo_h1": "Pompe de relevage",
        "combo_title": "Pompe de relevage {city} ({cp}) — dépannage et entretien",
        "combo_meta": "Dépannage et entretien de pompe et poste de relevage {a} : alarme, débordement, pompe bloquée. {delay_txt}. 24h/24. ☎ 06 75 93 19 04",
        "combo_intros": [
            "L'alarme de votre poste de relevage sonne ou la cuve déborde ? {a}, un technicien intervient 24h/24 pour dépanner, nettoyer ou remplacer la pompe.",
            "Nous dépannons et entretenons les pompes de relevage des eaux usées {a}, pour les maisons en contrebas, les sous-sols et les copropriétés.",
            "Pompe bloquée, flotteur coincé, clapet défaillant : un artisan de la région intervient {a} avec un prix annoncé avant de commencer.",
        ],
        "combo_points": [
            "Dépannage de pompe bloquée",
            "Nettoyage de la cuve et du flotteur",
            "Remplacement du clapet anti-retour",
            "Remplacement de pompe de relevage",
            "Contrôle de l'alarme de niveau",
            "Entretien annuel du poste",
        ],
        "combo_tip": "Si l'alarme sonne, réduisez au maximum l'utilisation de l'eau et vérifiez le disjoncteur de la pompe : souvent, cela suffit à éviter le débordement en attendant notre arrivée.",
    },
    # ------------------------------------------------------------------ TRAVAUX
    {
        "slug": "travaux-assainissement-var",
        "image": "travaux-assainissement.jpg",
        "image_alt": "Pelleteuse et tranchée pour la pose de canalisations d'assainissement",
        "combo": "travaux-assainissement",
        "name": "Travaux d'assainissement & raccordement",
        "short": "Travaux d'assainissement",
        "icon": "wrench",
        "badge": "Sur devis",
        "price_label": "à partir de 390 €",
        "price_min": 390, "rate_card": False,
        "title": "Travaux d'assainissement — réparation, raccordement au tout-à-l'égout",
        "meta": "Travaux d'assainissement : réparation de canalisation enterrée, raccordement au tout-à-l'égout, réhabilitation de fosse, mise en conformité SPANC. Devis gratuit. ☎ 06 75 93 19 04",
        "h1": "Travaux d'assainissement et raccordement au tout-à-l'égout",
        "lead": "Canalisation cassée ou envahie par les racines, raccordement au réseau public, fosse non conforme : nous réalisons les <b>travaux d'assainissement</b> après un diagnostic précis, avec un devis détaillé.",
        "checks": ["Diagnostic avant travaux", "Devis détaillé gratuit", "Travaux soignés"],
        "card_desc": "Réparation de canalisations enterrées, raccordement au tout-à-l'égout, réhabilitation et mise en conformité.",
        "card_checks": ["Devis détaillé", "Après inspection caméra"],
        "sections": [
            ("Nos travaux d'assainissement",
             "<ul><li><strong>Réparation ou remplacement</strong> d'un tronçon de canalisation enterrée cassée, écrasée ou déboîtée.</li>"
             "<li><strong>Raccordement au tout-à-l'égout</strong> lorsque le réseau public arrive dans votre rue, et mise hors service de l'ancienne fosse.</li>"
             "<li><strong>Création ou remplacement de regards</strong> de visite.</li>"
             "<li><strong>Mise en conformité</strong> d'une installation d'assainissement individuel après un contrôle SPANC.</li>"
             "<li><strong>Séparation eaux usées / eaux pluviales</strong> quand le règlement de la commune l'impose.</li></ul>"),
            ("Un diagnostic avant de creuser",
             "<p>Nous commençons toujours par comprendre le problème : <a href=\"/inspection-camera-canalisation-var/\">inspection caméra</a>, repérage du réseau et localisation précise du défaut. Vous savez exactement ce qui est à refaire et pourquoi, et nous n'ouvrons qu'à l'endroit nécessaire.</p>"),
            ("Raccordement au tout-à-l'égout",
             "<p>Lorsque le réseau public d'assainissement est créé dans votre rue, le raccordement est en principe obligatoire dans un délai de deux ans. La partie publique (sous la voirie) est réalisée ou encadrée par le service d'assainissement de la commune ; la partie privée, de la maison jusqu'à la boîte de branchement, est à la charge du propriétaire. Nous réalisons cette partie privée, après accord du service compétent, et la mise hors service de l'ancienne fosse.</p>"
             "<p>Pour la création ou la réhabilitation d'une installation d'assainissement individuel, le projet doit d'abord être validé par le SPANC, souvent sur la base d'une étude de sol. Nous vous expliquons les étapes et travaillons à partir du projet validé.</p>"),
        ],
        "faq": [
            ("Combien coûte un raccordement au tout-à-l'égout ?", "Il dépend de la distance entre la maison et la boîte de branchement, de la profondeur, de la nature du terrain et des revêtements à refaire. Nous établissons un devis détaillé après visite."),
            ("Faut-il une autorisation pour refaire une installation d'assainissement individuel ?", "Oui, le projet doit être validé par le SPANC avant les travaux, puis contrôlé à la fin du chantier. Nous travaillons à partir du projet validé."),
            ("Pouvez-vous réparer une canalisation sans tout casser ?", "Après une inspection caméra qui localise précisément le défaut, nous n'ouvrons qu'à l'endroit nécessaire pour remplacer le tronçon abîmé."),
            ("Que faire de l'ancienne fosse après le raccordement ?", "Elle doit être vidangée, nettoyée, puis comblée ou retirée. Nous pouvons nous en charger lors du raccordement."),
        ],
        "combo_h1": "Travaux d'assainissement",
        "combo_title": "Travaux d'assainissement {city} ({cp}) — raccordement, réparation",
        "combo_meta": "Travaux d'assainissement {a} : réparation de canalisation enterrée, raccordement au tout-à-l'égout, mise en conformité. {delay_txt}. Devis gratuit. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Canalisation cassée, raccordement au tout-à-l'égout, mise en conformité après un contrôle SPANC : nous réalisons vos travaux d'assainissement {a}, après un diagnostic précis.",
            "{a}, nous réparons les canalisations enterrées et réalisons les raccordements au réseau public, avec un devis détaillé et des travaux soignés.",
            "Avant de creuser, nous localisons le problème à la caméra : vos travaux d'assainissement {a} se limitent à ce qui est vraiment nécessaire.",
        ],
        "combo_points": [
            "Réparation de canalisation enterrée",
            "Raccordement au tout-à-l'égout",
            "Mise hors service d'une ancienne fosse",
            "Création et remplacement de regards",
            "Mise en conformité après contrôle SPANC",
            "Séparation eaux usées et eaux pluviales",
        ],
        "combo_tip": "Rassemblez les documents dont vous disposez (plan de la maison, rapport SPANC, courrier de la mairie pour le raccordement) : ils nous permettent d'établir un devis plus précis dès la première visite.",
    },
    # ------------------------------------------------------------------ POMPAGE
    {
        "slug": "pompage-nettoyage-cuves-var",
        "image": "pompage.jpg",
        "image_alt": "Camion aspirateur en train de pomper un regard",
        "combo": "pompage",
        "name": "Pompage & nettoyage de cuves, regards, puisards",
        "short": "Pompage & aspiration",
        "icon": "truck",
        "badge": "Grosses interventions",
        "price_label": "à partir de 220 €",
        "price_min": 220,
        "title": "Pompage et aspiration — cuves, regards, puisards, inondations",
        "meta": "Pompage et aspiration par camion : cuves, regards, puisards, vide sanitaire et sous-sol inondés, séparateurs, eaux usées. 24h/24. ☎ 06 75 93 19 04",
        "h1": "Pompage, aspiration et nettoyage de cuves",
        "lead": "Sous-sol inondé, regard plein, puisard saturé, cuve à vider : nos <b>grosses interventions de pompage</b> sont réalisées avec un camion aspirateur, pour les particuliers, les copropriétés, les entreprises et les collectivités.",
        "checks": ["Camion aspirateur", "Urgence 24h/24", "Particuliers et professionnels"],
        "card_desc": "Pompage par camion des regards, puisards, cuves, vides sanitaires et sous-sols inondés.",
        "card_checks": ["Gros volumes", "Urgence après orage"],
        "sections": [
            ("Nos interventions de pompage",
             "<ul><li><strong>Sous-sols, garages et vides sanitaires inondés</strong> après un orage ou un refoulement.</li>"
             "<li><strong>Regards, puisards et fosses</strong> saturés.</li>"
             "<li><strong>Cuves</strong> d'eaux usées, de récupération d'eau de pluie ou de rétention.</li>"
             "<li><strong>Séparateurs à hydrocarbures</strong> et débourbeurs des parkings, garages et stations de lavage.</li>"
             "<li><strong>Réseaux et postes de relevage</strong> de copropriétés, campings et zones d'activité.</li></ul>"),
            ("Après un épisode cévenol ou un orage",
             "<p>Dans notre secteur, les fortes pluies d'automne saturent vite les réseaux. Nous pompons l'eau, nettoyons les regards et contrôlons les canalisations pour remettre l'installation en service, et nous vous remettons une facture détaillée pour votre assurance.</p>"),
            ("Professionnels et collectivités",
             "<p>Syndics, gestionnaires de résidences, campings, hôtels, restaurants, entreprises et communes : nous intervenons sur devis ou en urgence, avec un compte rendu d'intervention. Les déchets pompés sont évacués vers une filière de traitement adaptée.</p>"),
        ],
        "faq": [
            ("Intervenez-vous après une inondation ?", "Oui, nous pompons les sous-sols, garages, vides sanitaires et regards inondés, 24h/24 et 7j/7, puis contrôlons les canalisations."),
            ("Pompez-vous les séparateurs à hydrocarbures ?", "Oui, pour les parkings, garages, stations de lavage et zones d'activité. Les déchets sont évacués vers une filière agréée."),
            ("Combien coûte un pompage ?", "Il dépend du volume, de la nature des effluents, de l'accès pour le camion et de la distance de tuyau nécessaire. Il est établi sur devis, ou annoncé au téléphone en urgence."),
            ("Travaillez-vous pour les copropriétés et les communes ?", "Oui, nous intervenons pour les syndics, les gestionnaires de résidences, les entreprises et les collectivités, ponctuellement ou dans le cadre d'un entretien régulier."),
        ],
        "combo_h1": "Pompage et aspiration",
        "combo_title": "Pompage {city} ({cp}) — cuves, regards, sous-sols inondés",
        "combo_meta": "Pompage et aspiration par camion {a} : regards, puisards, cuves, sous-sols inondés, séparateurs. {delay_txt}. 24h/24. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Sous-sol inondé, regard qui déborde, cuve à vider : {a}, nous intervenons avec un camion aspirateur, jour et nuit, pour les particuliers comme pour les professionnels.",
            "Après un orage, les réseaux saturent vite. {a}, nous pompons l'eau, nettoyons les regards et remettons votre installation en service.",
            "Grosses interventions de pompage {a} : puisards, séparateurs, cuves et postes de relevage, pour les copropriétés, les entreprises et les collectivités.",
        ],
        "combo_points": [
            "Pompage de sous-sol ou vide sanitaire inondé",
            "Vidange de regards et puisards",
            "Pompage de cuves et bassins",
            "Séparateurs à hydrocarbures et débourbeurs",
            "Intervention après orage",
            "Évacuation vers une filière agréée",
        ],
        "combo_tip": "Avant notre arrivée, coupez l'électricité des pièces inondées et dégagez l'accès pour le camion : nous pouvons tirer des tuyaux sur une bonne distance, mais un accès proche fait gagner du temps.",
    },
]

ASSURANCE_PAGE = {
    "slug": "refoulement-egout-assurance-var",
    "name": "Refoulement d'égout & assurance",
    "image": "degat-des-eaux.jpg",
    "image_alt": "Sol inondé après un refoulement d'eaux usées",
}

SERVICE_ICONS = {
    "bolt": '<path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "drop": '<path d="M12 3s-6 6.6-6 11a6 6 0 0 0 12 0c0-4.4-6-11-6-11Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "pipe": '<path d="M4 8h8a4 4 0 0 1 4 4v8M4 8V5M4 8v3M16 20h-3M16 20h3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "tank": '<rect x="3" y="8" width="18" height="11" rx="3" stroke="currentColor" stroke-width="1.7"/><path d="M8 8V5h3v3M3 14h18" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "camera": '<rect x="3" y="7" width="12" height="10" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="m15 11 6-3v8l-6-3" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="9" cy="12" r="2" stroke="currentColor" stroke-width="1.5"/>',
    "grease": '<path d="M4 10h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4v-6ZM8 10V7M16 10V7M12 4v3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M8 14h8" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/>',
    "pump": '<rect x="6" y="9" width="12" height="11" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M12 9V3M9 6l3-3 3 3M9 14h6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>',
    "truck": '<path d="M2 7h11v9H2zM13 10h4l3 3v3h-7" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="6" cy="17.5" r="1.8" stroke="currentColor" stroke-width="1.5"/><circle cx="16.5" cy="17.5" r="1.8" stroke="currentColor" stroke-width="1.5"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.2 5.2L4 17l3 3 5.5-5.5a4 4 0 0 0 5.2-5.2l-2.4 2.4-2.6-.6-.6-2.6 2.6-2.2Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    "shield": '<path d="M12 2 4 5v6c0 5 3.4 8.7 8 11 4.6-2.3 8-6 8-11V5l-8-3Z" stroke="currentColor" stroke-width="1.8"/><path d="M8.5 12l2.3 2.3L15.5 9.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
}

# Ordre d'affichage : les grosses interventions d'abord.
_ORDER = ["degorgement-canalisation-var", "curage-canalisation-var", "pompage-nettoyage-cuves-var",
          "vidange-fosse-septique-var", "inspection-camera-canalisation-var", "travaux-assainissement-var",
          "pompe-de-relevage-var", "bac-a-graisse-var"]
SERVICES = sorted(SERVICES, key=lambda s: _ORDER.index(s["slug"]))
