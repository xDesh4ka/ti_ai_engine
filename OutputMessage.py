import json


class OutputMessage:
    def __init__(self, date, text):
        self.date = date
        self.text = text

    def __str__(self):
        return f"{self.date}\n{self.text}"

    def to_json(self):
        return json.dumps({"date": self.date.strftime("%Y-%m-%d"), "text": self.text}) # ensure_ascii=False - ломает запрос

