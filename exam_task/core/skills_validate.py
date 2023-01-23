class SkillsValidate:
    @staticmethod
    def validator(type_of_musician, skill):
        allowed_skills = {
            'Singer': ["sing high pitch notes", "sing low pitch notes"],
            'Drummer': ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"],
            'Guitarist': ["play metal", "play rock", "play jazz"],
            }
        if skill not in allowed_skills[type_of_musician]:
            raise ValueError(f"{skill} is not a needed skill!")
        return skill
