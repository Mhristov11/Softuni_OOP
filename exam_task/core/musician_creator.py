from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class CreateMusician:
    @staticmethod
    def create_mus(name, age, musician_type):
        allowed_types = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
        if musician_type not in allowed_types:
            raise ValueError("Invalid musician type!")
        return allowed_types[musician_type](name, age)

