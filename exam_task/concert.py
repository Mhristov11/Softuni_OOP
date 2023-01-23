from project.core.audience_validator import AudienceValidator
from project.core.expenses_validator import ExpensesValidator
from project.core.genre_validator import GenreValidate
from project.core.place_validator import PlaceValidator
from project.core.ticket_price_validator import TicketPriceValidator


class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = GenreValidate.validator(value)

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        self.__audience = AudienceValidator.validate(value)
    
    @property
    def ticket_price(self):
        return self.__ticket_price
    
    @ticket_price.setter
    def ticket_price(self, value):
        self.__ticket_price = TicketPriceValidator.validate(value)
        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        self.__expenses = ExpensesValidator.validate(value)

    @property
    def place(self):
        return self.__place
    
    @place.setter
    def place(self, value):
        self.__place = PlaceValidator.validate(value)

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
