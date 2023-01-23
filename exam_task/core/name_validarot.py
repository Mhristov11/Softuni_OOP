class NameValidator:
    @staticmethod
    def validate(name):
        if name == '' or name.strip() == '':
            raise ValueError("Musician name cannot be empty!")
        return name
