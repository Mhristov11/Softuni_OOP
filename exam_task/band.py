from project.core.band_name_validator import BandNameValidator


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = BandNameValidator.validator(value)

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
