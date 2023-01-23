class AudienceValidator:
    @staticmethod
    def validate(audience):
        if audience < 1:
            raise ValueError("At least one person should attend the concert!")
        return audience
