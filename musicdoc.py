class Music:
    def __init__(self, major_accidentals, minor_accidentals, notes):
        self.major_accidentals = major_accidentals
        self.minor_accidentals = minor_accidentals
        self.notes = notes

    def note_mover(self, numeral_note, half_steps, position="up"):
        if position == "up":
            numeral_note = numeral_note + half_steps
            if numeral_note > 12:
                numeral_note = numeral_note - 12
        elif position == "down":
            numeral_note = numeral_note - half_steps
            if numeral_note < 1:
                numeral_note = numeral_note + 12
        return numeral_note

    def note_decoder(self, note, tonic, type, skip=False):
        if type == "minor" or type == "harmonic" or type == "melodic":
            accidentals = self.minor_accidentals
        else:
            accidentals = self.major_accidentals
        notes = self.notes
        try:
            if accidentals[tonic] >= 0 and not skip:
                if notes['C'] == note:
                    return 'C'
                elif notes['C#'] == note and notes['Db'] == note:
                    return 'C#'
                elif notes['D'] == note:
                    return 'D'
                elif notes['D#'] == note and notes['Eb'] == note:
                    return 'D#'
                elif notes['E'] == note:
                    return 'E'
                elif notes['F'] == note:
                    return 'F'
                elif notes['F#'] == note and notes['Gb'] == note:
                    return 'F#'
                elif notes['G'] == note:
                    return 'G'
                elif notes['G#'] == note and notes['Ab'] == note:
                    return 'G#'
                elif notes['A'] == note:
                    return 'A'
                elif notes['A#'] == note and notes['Bb'] == note:
                    return 'A#'
                elif notes['B'] == note:
                    return 'B'
            elif accidentals[tonic] < 0 and not skip:
                if notes['C'] == note:
                    return 'C'
                elif notes['C#'] == note and notes['Db'] == note:
                    return 'Db'
                elif notes['D'] == note:
                    return 'D'
                elif notes['D#'] == note and notes['Eb'] == note:
                    return 'Eb'
                elif notes['E'] == note:
                    return 'E'
                elif notes['F'] == note:
                    return 'F'
                elif notes['F#'] == note and notes['Gb'] == note:
                    return 'Gb'
                elif notes['G'] == note:
                    return 'G'
                elif notes['G#'] == note and notes['Ab'] == note:
                    return 'Ab'
                elif notes['A'] == note:
                    return 'A'
                elif notes['A#'] == note and notes['Bb'] == note:
                    return 'Bb'
                elif notes['B'] == note:
                    return 'B'
            elif skip:
                if notes['C'] == note:
                    return 'C'
                elif notes['C#'] == note and notes['Db'] == note:
                    return 'C#/Db'
                elif notes['D'] == note:
                    return 'D'
                elif notes['D#'] == note and notes['Eb'] == note:
                    return 'D#/Eb'
                elif notes['E'] == note:
                    return 'E'
                elif notes['F'] == note:
                    return 'F'
                elif notes['F#'] == note and notes['Gb'] == note:
                    return 'F#/Gb'
                elif notes['G'] == note:
                    return 'G'
                elif notes['G#'] == note and notes['Ab'] == note:
                    return 'G#/Ab'
                elif notes['A'] == note:
                    return 'A'
                elif notes['A#'] == note and notes['Bb'] == note:
                    return 'A#/Bb'
                elif notes['B'] == note:
                    return 'B'
        except KeyError:
            if notes['C'] == note:
                return 'C'
            elif notes['C#'] == note and notes['Db'] == note:
                return 'C#/Db'
            elif notes['D'] == note:
                return 'D'
            elif notes['D#'] == note and notes['Eb'] == note:
                return 'D#/Eb'
            elif notes['E'] == note:
                return 'E'
            elif notes['F'] == note:
                return 'F'
            elif notes['F#'] == note and notes['Gb'] == note:
                return 'F#/Gb'
            elif notes['G'] == note:
                return 'G'
            elif notes['G#'] == note and notes['Ab'] == note:
                return 'G#/Ab'
            elif notes['A'] == note:
                return 'A'
            elif notes['A#'] == note and notes['Bb'] == note:
                return 'A#/Bb'
            elif notes['B'] == note:
                return 'B'

    def relative_note_finder(self, note_type, tonic):
        numeral_note = self.notes[tonic]
        if note_type == "major":
            numeral_note = numeral_note + 9
            if numeral_note > 12:
                numeral_note = numeral_note - 12
            relative_minor = self.note_decoder(numeral_note, tonic, note_type)
            return relative_minor
        if note_type == "minor" or note_type == "harmonic" or note_type == "melodic":
            numeral_note = numeral_note - 9
            if numeral_note < 1:
                numeral_note = numeral_note + 12
            relative_major = self.note_decoder(numeral_note, tonic, note_type)
            return relative_major
