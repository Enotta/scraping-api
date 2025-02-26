def extract_features(text):
    if text is None:
        return []
    else:
        result = []
        all_features = {
            "Россия": ["РФ", "Российская Федерация", "Росси"],
            "Путин": ["Путин", "Президент России", "В.В. Путин", "Глава государства"],
            "Украина": ["украин", "Укр", "Украинская Республика", "Киевская Русь"],
            "США": ["Соединенные Штаты Америки", "Америк", "америк", "Штат", "US", "США"],
            "Европа": ["Европейский Союз", "ЕС", "Европейское сообщество"],
            "Германия": ["Германи", "Deutschland", "ФРГ", "Берлин"],
            "Китай": ["КНР", "Кита", "China", "Китайская Народная Республика"],
            "Турция": ["Турецкая Республика", "Türkiye", "Анатолия", "Анкар", "Турци", "турец"],
            "Сирия": ["САР", "Syrian Arab Republic", "дамаск", "Ближний Восток", "Сири"],
            "Экономика": ["хозяйств", "экономическая сфера", "рынок", "эконом", "финанс"],
            "Политика": ["государственная деятельность", "политическая сфера", "власт", "дипломат"],
            "Общество": ["социум", "населени", "граждане", "социальная сфера"],
            "Культура": ["искусств", "культурная сфера", "наследи", "традици"],
            "Спорт": ["физическая культура", "спортивные мероприятия", "игры", "чемпионат"],
            "Наука": ["научная деятельность", "исследовани", "технологи", "инноваци"],
            "Технологии": ["техно", "инноваци", "ИТ", "разработк"],
            "Здравоохранение": ["медицин", "система здравоохранения", "больниц", "врач", "поликлинник"],
            "Образование": ["учеб", "система образования", "школ", "вуз", "образован"],
            "Москва": ["столица России", "Moscow", "мегаполис", "москв"],
            "Санкт-Петербург": ["Питер", "Северная столица", "Ленинград", "СПб", "Санкт-Петербург"],
            "Крым": ["Крымский полуостров", "Crimea", "Севастополь", "Черное море"],
            "Донбасс": ["Донецкий бассейн", "Donbas", "ДНР", "ЛНР"],
            "НАТО": ["Североатлантический альянс", "NATO", "Блок НАТО", "Военный союз"],
            "ООН": ["Организация Объединенных Наций", "UN", "United Nations", "Генассамблея ООН"],
            "Газпром": ["газовая промышленность", "Gazprom", "энергетик", "газовый гигант", "газпром"],
            "Роснефть": ["нефтяная промышленность", "Rosneft", "нефть", "ТНК", "роснефт"],
            "Сбербанк": ["сбер", "Sberbank", "финансовая организация", "сбербанк"],
            "COVID-19": ["коронавирус", "ковид", "пандемия", "вирус"],
            "Выборы": ["голосовани", "избирательная кампания", "президентские выборы", "дум", "выбор"],
            "Армия": ["вооруженные силы", "военны", "солдат", "оборон", "арми"],
            "Госдума": ["парламент", "законодательная власть", "депутат", "ГД РФ", "госдум"],
            "Космос": ["вселенная", "астронавтика", "космонавтика", "МКС", "НАСА", "Роскосмос", "космические исследования"],
            "Климат": ["погод", "изменение климата", "экологи", "природные условия", "климат"],
            "Цены": ["стоимост", "тариф", "рынок", "экономическая ситуация"],
            "Банки": ["финансовые учреждения", "кредит", "депозит", "банковская система", "банк"],
            "Нефть": ["углеводород", "нефтяной рынок", "бензин", "баррел", "нефт"],
            "Газ": ["природный газ", "топлив", "газовая промышленность", "энергоресурс", "газ"],
            "Энергетика": ["электричеств", "ТЭК", "энергосистем", "ресурс"],
            "Преступность": ["криминал", "правонарушени", "мафи", "преступные группировки", "преступност"],
            "Полиция": ["правоохранительные органы", "МВД", "силовик", "стражи порядка", "полици"],
            "МВД": ["Министерство внутренних дел", "правоохранител", "полици", "органы безопасности"],
            "Минобороны": ["Министерство обороны", "военное ведомство", "арми", "МО РФ"],
            "ФСБ": ["Федеральная служба безопасности", "контрразведк", "силовые структуры", "спецслужб"],
            "Туризм": ["путешествия", "отдых", "курорты", "туристический бизнес"],
            "Авто": ["автомобил", "транспорт", "автопром", "машины"],
            "ЖКХ": ["коммунальные услуги", "жилищно-коммунальное хозяйство", "тарифы", "ремонт", "ЖКХ"],
            "Интернет": ["сеть", "всемирная паутина", "онлайн", "интернет", "соцсет", "digital"],
            "Искусственный интеллект": ["ИИ", "AI", "машинное обучение", "нейросет"]
        }
        for feature, triggers in all_features.items():
            for trigger in triggers:
                if trigger.lower() in text.lower():
                    result.append(feature)
                    break
        return result

# Подсчёт количества каждых реакций
def extract_reactions(message):
    result = {}
    if message.reactions is not None: 
        for reaction in message.reactions.reactions:
            if not reaction.emoji in result:
                result[reaction.emoji] = reaction.count
    return result