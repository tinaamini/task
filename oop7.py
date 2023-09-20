# استفاده از ویژیگی خصوصی_________________________________
class Employee:
    def __init__(self, name, user_id):
        self._name = name
        self.__user_id = user_id

    @property
    def show_information(self):
        return self._name + self.__user_id
