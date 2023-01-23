class AgeValidator:
    @staticmethod
    def validate(age):
        if age < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        return age

