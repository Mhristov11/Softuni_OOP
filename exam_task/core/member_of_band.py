class MemberOfBand:
    @staticmethod
    def find(name, bands, band_name):
        for band in bands:
            for member in band.members:
                if member.name == name:
                    band.members.remove(member)
                    return True
        raise Exception(f"{name} isn't a member of {band_name}!")

    @staticmethod
    def find_band(band_name, bands):
        if band_name in [band.name for band in bands]:
            return
        else:
            raise Exception(f"{band_name} isn't a band!")