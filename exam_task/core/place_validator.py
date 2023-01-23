class PlaceValidator:
    @staticmethod
    def validate(place):
        if len(place) < 2 or place.strip() == '':
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        return place
