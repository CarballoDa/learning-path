VALID_DAYS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]


class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day: str) -> None:
        if day not in VALID_DAYS:
            raise WeekDayError("Sorry, request can not be processed.")
        self.__day = VALID_DAYS.index(day)
        
    def __str__(self) -> str:
        return VALID_DAYS[int(self.__day)]
    
    def add_days(self, n: int) -> None:
        self.__day = round(( self.__day + n ) % 7)
    
    def substract_days(self, n: int) -> None:
        self.__day = round(( self.__day - n ) % 7)
    
    
try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.substract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")