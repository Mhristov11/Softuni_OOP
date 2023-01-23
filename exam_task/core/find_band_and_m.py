class FindBandAndMuscian:
    @staticmethod
    def find(band_name, musician_name, bands, musicians):
        if band_name in [band.name for band in bands]:
            current_band = [band for band in bands if band.name == band_name][0]
        else:
            raise Exception(f"{band_name} isn't a band!")

        if musician_name in [musician.name for musician in musicians]:
            current_musician = [musician for musician in musicians if musician.name == musician_name][0]
        else:
            raise Exception(f"{musician_name} isn't a musician!")
        return current_band, current_musician
