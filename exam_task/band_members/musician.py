from abc import ABC, abstractmethod

from project.core.age_validator import AgeValidator
from project.core.name_validarot import NameValidator
from project.core.skills_validate import SkillsValidate


class Musician(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = NameValidator.validate(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = AgeValidator.validate(value)

    def learn_new_skill(self, new_skill: str):
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(SkillsValidate.validator(self.__class__.__name__, new_skill))
        return f"{self.name} learned to {new_skill}."
