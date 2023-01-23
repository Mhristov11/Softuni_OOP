class BandNameValidator:
    @staticmethod
    def validator(name):
        if name == '':
            raise ValueError("Band name should contain at least one character!")
        return name
