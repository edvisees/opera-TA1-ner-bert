A20_NER_MAP = {
    "BAL": [
        "ballot", "votación", "бюллетень",
    ],
    "COM": [
        "food", "comida", "еда",
        "samples", "muestra", "образец",
        "oil", "petróleo", "нефть",
        "material", "материал",
        "supplies", "supply", "suministro", "поставка",
        "product", "producto", "товар",
        "goods", "bienes",  # "товар"
        "newspaper", "periódico", "газета",
        "passport", "pasaporte",
        "paper", "papel", "бумага",
    ],
    "COM.Document": [
        "document", "documento", "документ",
    ],
    "COM.Document.Map": [
        "map", "mapa", "карта",
    ],
    "COM.Equipment": [
        "equipment", "оборудование",  # in es, one form multiple meanings!
    ],
    "COM.Equipment.MedicalEquipment": [
        "medicine", "medicamento", "лекарство",
        "drug", "droga",
        "acetaminophen", "paracetamol", "ацетаминофен",
    ],
    "COM.Equipment.Satellite": [
        "satellite", "satélite",
    ],
    "FAC.Building": [
        "hospital", "больница",
        "building", "edificio", "здание",
        "palace", "palacio", "дворец",
        "church", "iglesia", "церковь",
        "pharmacy", "farmacia", "аптека",
    ],
    "FAC.Building.ApartmentBuilding": [
        "apartment", "apartamento", "квартира",
    ],
    "FAC.Building.School": [
        "school", "escuela", "школа",
    ],
    "FAC.Building.StoreShop": [
        "supermarket", "supermercado", "супермаркет",
        "shop", "tienda", "магазин",
    ],
    "FAC.GeographicalArea.Border": [
        "border", "frontera", "граница",
    ],
    "FAC.GeographicalArea.Checkpoint": [
        "checkpoint",
    ],
    "FAC.Installation.Airport": [
        "airport", "aeropuerto", "аэропорт",
    ],
    "FAC.Structure.Barricade": [
        "barricade", "roadblock", "barricada", "баррикада",
    ],
    "FAC.Structure.Bridge": [
        "bridge", "puente", "мост",
    ],
    "FAC.Structure.Plaza": [
        "plaza",
    ],
    "FAC.Structure.Tower": [
        "tower", "torre", "башня",
    ],
    "FAC.Way.Highway": [
        "highway", "autopista", "шоссе",
    ],
    "FAC.Way.Street": [
        "street", "calle", "улицах",
    ],
    "GPE.Country.Country": [
        "venezuela", "венесуэла",
        "country", "país", "страна",
        "venezuelan", "venezolana", "venezolano", "венесуэльский",
        "colombia", "колумбия",
        "u.s.",
        "nation", "nación", "нация",
        "republic", "república", "республика",
        "cuba", "куба",
        "peru", "perú", "перу",
        "mexico", "méxico", "мексика",
        "colombian", "colombiano", "колумбийский",
        "canada", "canadá", "канада",
        "spain", "españa", "испания",
        "brazil", "brasil", "бразилия",
        "iran", "иран",
        "panama", "panamá", "панама",
        "chile", "чили",
        "usa",
        "syria", "siria", "сирия",
        "argentina", "аргентина",
        "ecuador", "эквадор",
        "india", "индия",
        "china", "китай",
        "iraq", "irak", "ирак",
        "korea", "корея",
        "france", "francia", "франция",
        "paraguay", "парагвай",
    ],
    "GPE.ProvinceState.ProvinceState": [
        "aragua", "арагуа",
        "florida", "флорида",
        "texas", "техас",
    ],
    "GPE.UrbanArea.City": [
        "caracas", "каракас",
        "maracay", "маракай",
        "city", "ciudad", "город",
        "barquisimeto", "баркисимето",
        "valencia", "валенсия",
        "miami", "майами",
        "ottawa", "оттава",
        "merida", "mérida", "мерида",
        "maracaibo", "маракайбо",
        "bogota", "bogotá", "богота",
        "sucre", "сукре",
        "barinas", "баринас",
        "london", "londres", "лондон",
        "baltimore", "балтимор",
    ],
    "LAW": [
        "law", "ley", "закон",
    ],
    "LOC.Position.Neighborhood": [
        "neighborhood", "neighbourhood", "barrio", "окрестности",
    ],
    "LOC.Position.Region": [
        "region", "región", "область",
    ],
    "MHI.SymptomPresentation.SymptomPresentation": [
        "piel", "dolor", "pain", "skin"
    ],
    "MHI.Disease.Disease": [
        "disease", "illness", "enfermedad", "болезнь", "заболевание",
        "chikungunya", "chikunguya", "chicungunya", "chikunguny", "chikungunya.", "чикунгунья",
        "dengue", "денге",
        "ebola", "ébola", "эбола",
        "meningitis", "менингит",
        "virus", "вирус", 'febril', 'meningococo',
        "fever", "лихорадка",
        "bacteria", "bacterias", "бактерии",  # is this disease?
        "cancer", "cáncer", "карцинома",
        "meningitidis", "менингитидис", "esta",
        "meningococcemia", "meningococemia", "менингококкемия",
        "sepsis", "septicemia", "сепсис",
        "symptom", "síntoma", "симптом",
        "syndrome", "síndrome", "синдром", "patologías"
    ],
    "MON": [
        "$", "dollar", "dólar", "доллар",
    ],
    "ORG.Association": [
        "association", "asociación", "ассоциация",
    ],
    "ORG.CommercialOrganization": [
        "company", "empresa", "компания",
        "smartmatic",
    ],
    "ORG.CommercialOrganization.NewsAgency": [
        "reuters", "рейтер",
        "cnn",
    ],
    "ORG.Government": [
        "government", "gobierno", "правительство",
        "regime", "régimen", "режим",
    ],
    "ORG.Government.Council": [
        "council", "consejo", "совет",
    ],
    "ORG.Government.LegislativeBody": [
        "congress", "congreso", "съезд",
        "legislature", "legislatura",
        "parliament", "parlamento", "парламент",
    ],
    "ORG.PoliticalOrganization.Court": [
        "court", "tribunal", "суд",
    ],
    "PER": [
        'case', 'fatale', 'votant', 'voters', 'caso', 'fatal', 'fatali', 'víctima',
        'victim'
    ],
    "PER.Combatant.Mercenary": [
        "mercenary", "mercenaria", "mercenario", "наемник",
    ],
    "PER.Combatant.Sniper": [
        "sniper", "francotiradora", "francotirador", "снайпер",
    ],
    "PER.MilitaryPersonnel": [
        "soldier", "soldiers", "soldado", "солдат",
        "troops", "troop", "tropa", "отряд",
    ],
    "PER.Police": [
        "police", "policeman", "policía", "полиция", "полицейский",
    ],
    "PER.Politician": [
        "politician", "política", "político", "политик",
    ],
    "PER.Politician.Governor": [
        "governor", "gobernadora", "gobernador", "губернатор",
    ],
    "PER.Politician.HeadOfGovernment": [
        "maduro", "мадуро",
        "president", "presidenta", "presidente", "президент",
    ],
    "PER.Politician.Mayor": [
        "mayor", "alcaldesa", "alcalde", "мэр",
    ],
    "PER.ProfessionalPosition": [
        "prosecutor", "прокурор",
        "judge", "jueza", "juez", "судья",
        "legislator", "legisladora", "legislador", "законодатель",
        "lawyer", "abogada", "abogado", "адвокат",
        "attorney", "поверенный",
    ],
    "PER.ProfessionalPosition.Ambassador": [
        "ambassador", "embajadora", "embajador", "посол",
    ],
    "PER.ProfessionalPosition.Firefighter": [
        "firefighter", "fireman", "bombera", "bombero", "пожарный",
    ],
    "PER.ProfessionalPosition.Journalist": [
        "journalist", "periodista", "журналистка",
        "reporter", "reportera", "reportero", "репортер",
    ],
    "PER.ProfessionalPosition.Minister": [
        "minister", "ministra", "ministro", "министр",
    ],
    "PER.ProfessionalPosition.MedicalPersonnel": [
        "doctor", "médica", "médico", "доктор",
        "nurse", "enfermera", "enfermero",
        "physician", "physicians", "врач",
        "epidemiologist", "epidemióloga", "epidemiólogo", "эпидемиолог",
        "infectologist", "infectólogo", "инфектолог",
    ],
    "PER.ProfessionalPosition.Scientist": [
        "scientist", "científica", "científico", "ученый",
    ],
    "PER.ProfessionalPosition.Spokesperson": [
        "spokesman", "spokesmen", "portavoz",  # ru 1->many
        "spokesperson",
    ],
    "PER.Protester": [
        "protester", "protesters", "protestor",
        "demonstrator", "demonstrators", "manifestante", "демонстрант",
    ],
    "RES.TurnoutVoters.TurnoutVoters": [
        "turnout",
    ],
    "SID.Political.Opposition": [
        "opposition", "oposición", "оппозиция",
    ],
    "VEH.Aircraft": [
        "aircraft", "aeronave", "самолет",
        "jet",
    ],
    "VEH.Aircraft.Airplane": [
        "plane", "airplane", "avión",  # "самолет"
    ],
    "VEH.Aircraft.Drone": [
        "drone", "drine", "drones", "дрон",
    ],
    "VEH.Aircraft.Helicopter": [
        "helicopter", "helicóptero", "вертолет",
    ],
    "VEH.MilitaryVehicle.Tank": [
        "tank", "tanque",
    ],
    "VEH.Rocket.Rocket": [
        # "rocket", "skyrocket", "cohete",  # could be weapon!!
    ],
    "VEH.Watercraft.Boat": [
        "boat", "barco", "лодка",
    ],
    "VEH.Watercraft.Yacht": [
        "yacht", "yate", "яхта",
    ],
    "VEH.WheeledVehicle": [
        "motorcycle", "motocicleta", "мотоцикл",
    ],
    "VEH.WheeledVehicle.Bus": [
        "bus", "autobús", "автобус",
    ],
    "VEH.WheeledVehicle.Car": [
        "car", "coche", "машина",
    ],
    "VEH.WheeledVehicle.Truck": [
        "truck", "camión", "грузовик",
    ],
    "WEA.Bomb": [
        "bomb", "bomba", "бомба", "explosives"
    ],
    "WEA.Bomb.Grenade": [
        "grenade", "granada", "граната",
    ],
    "WEA.Bullets": [
        "bullet", "bala", "пуля",
    ],
    "WEA.Cannon.Cannon": [
        "cannon", "пушка",
    ],
    "WEA.DaggerKnifeSword": [
        "dagger", "daga", "кинжал",
        "knife", "cuchillo", "нож",
        "sword", "espada", "меч",
    ],
    "WEA.DaggerKnifeSword.Hatchet": [
        "hatchet", "hacha", "топор",
    ],
    "WEA.Gun.Artillery": [
        "artillery", "artillería", "артиллерия",
    ],
    "WEA.Gun.Firearm": [
        "gunfire", "tiroteo", "стрельба",
        "gunshot", "cañonazo", "выстрел",
        "gun", "pistol", "pistola", "пистолет",
        "firearm",
        "rifle", "винтовка",
    ],
    "WEA.MissileSystem.Missile": [
        "missile", "misil",
    ],
}
