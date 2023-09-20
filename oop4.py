# توابع تعریف شده در کلاس---------------------------
class Car:
    def __init__(self, model, production_year, spead):
        self.model = model
        self.production_year = production_year
        self.spead = spead
        self.is_started = False

    def start_engine(self):
        self.is_started = True

    def stop_engine(self):
        self.is_started = False
