import json

# {
#     "date": "Дата",
#     "threatType": "Тип угрозы",
#     "countries": "Страны распространения",
#     "typeOfDistribution": "Тип распространения",
#     "description": "Краткое описание"
# }


def from_json(stringAnswer: str):
    answer = json.loads(stringAnswer)
    return Answer(**answer)


class Answer:
    def __init__(self, date, threatType, countries, typeOfDistribution, description):
        self.date = date
        self.threatType = threatType
        self.countries = countries
        self.typeOfDistribution = typeOfDistribution
        self.description = description

    def to_json(self):
        return json.dumps({"date": self.date,
                           "threatType": self.threatType,
                           "countries": self.countries,
                           "typeOfDistribution": self.typeOfDistribution,
                           "description": self.description }, ensure_ascii=False) #- ломает запрос

