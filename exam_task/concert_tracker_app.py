from project.band import Band
from project.concert import Concert
from project.core.find_band_and_m import FindBandAndMuscian
from project.core.member_of_band import MemberOfBand
from project.core.musician_creator import CreateMusician


class ConcertTrackerApp:
    def __init__(self):

        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")
        musician = CreateMusician.create_mus(name, age, musician_type)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(b.name == name for b in self.bands):
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if any(c.place == place for c in self.concerts):
            raise Exception(f"{place} is already registered for {genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        current_band,  current_musician = FindBandAndMuscian.find(band_name, musician_name, self.bands, self.musicians)
        current_band.members.append(current_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        MemberOfBand.find_band(band_name, self.bands)
        if MemberOfBand.find(musician_name, self.bands, band_name):
            return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        current_band = [band for band in self.bands if band.name == band_name][0]
        members_types = [member.__class__.__name__ for member in current_band.members]
        types = ["Guitarist", "Drummer", "Singer"]
        for member_type in types:
            if member_type not in members_types:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        current_concert = [concert for concert in self.concerts if concert.place == concert_place][0]

        profit = (float(current_concert.audience) *
                  float(current_concert.ticket_price)) - float(current_concert.expenses)

        return f"{band_name} gained {profit:.2f}$ from the {current_concert.genre} concert in {concert_place}."
