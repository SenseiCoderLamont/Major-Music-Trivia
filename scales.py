import musicdoc


class Scales(musicdoc.Music):

    def __init__(self, major_accidentals, minor_accidentals, notes, result=None, accidental_error=False):
        super().__init__(major_accidentals, minor_accidentals, notes)
        if result is None:
            result = []
        self.result = result
        self.accidental_error = accidental_error

    # Whole Whole Half Whole Whole Whole Half
    def major_scale_build(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        # 1
        new_scale.append(numeral_note)
        # Whole x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        # Half Note
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole x 3
        for i in range(3):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        return new_scale

    # Whole Half Whole Whole Half Whole Whole
    def minor_scale_build(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2)
        new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        return new_scale

    def harmonic_scale_builder(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2)
        new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole + Raise Half
        numeral_note = self.note_mover(numeral_note, 3)
        new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        return new_scale

    def melodic_scale_builder(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2)
        new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)
        # Whole x 4
        for i in range(4):
            numeral_note = self.note_mover(numeral_note, 2)
            new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1)
        new_scale.append(numeral_note)

        # || Going Backwards Now ||
        numeral_note = numeral_note - 2
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2, "down")
        new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1, "down")
        new_scale.append(numeral_note)
        # Whole x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 2, "down")
            new_scale.append(numeral_note)
        # Half
        numeral_note = self.note_mover(numeral_note, 1, "down")
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2, "down")
        new_scale.append(numeral_note)
        return new_scale

    def jazz_scale_builder(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        new_scale.append(numeral_note)
        # Whole / Half
        numeral_note = self.note_mover(numeral_note, 3)
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2)
        new_scale.append(numeral_note)
        # Half x 2
        for i in range(2):
            numeral_note = self.note_mover(numeral_note, 1)
            new_scale.append(numeral_note)
        # Whole / Half
        numeral_note = self.note_mover(numeral_note, 3)
        new_scale.append(numeral_note)
        # Whole
        numeral_note = self.note_mover(numeral_note, 2)
        new_scale.append(numeral_note)
        return new_scale

    def chromatic_scale_builder(self, note):
        new_scale = []
        numeral_note = self.notes[note]
        new_scale.append(numeral_note)
        for i in range(12):
            numeral_note = self.note_mover(numeral_note, 1)
            new_scale.append(numeral_note)
        return new_scale

    def scale_builder(self, scale_type, note, find_relative=False):
        tonic = note
        if scale_type == "major":
            self.result = []
            for note in self.major_scale_build(note):
                self.result.append(self.note_decoder(note, tonic, scale_type))
            print('Major Scale:', self.result)
            if find_relative:
                print('Relative Minor Key:', self.relative_note_finder(scale_type, tonic))
        elif scale_type == "minor":
            self.result = []
            for note in self.minor_scale_build(note):
                self.result.append(self.note_decoder(note, tonic, scale_type))
            print('Minor Scale:', self.result)
            if find_relative:
                print('Relative Minor Key:', self.relative_note_finder(scale_type, tonic))
        elif scale_type == "harmonic":
            self.result = []
            for note in self.harmonic_scale_builder(note):
                self.result.append(self.note_decoder(note, tonic, scale_type))
            print('Harmonic Scale:', self.result)
            if find_relative:
                print('Relative Minor Key:', self.relative_note_finder(scale_type, tonic))
        elif scale_type == "melodic":
            self.result = []
            for note in self.melodic_scale_builder(note):
                self.result.append(self.note_decoder(note, tonic, scale_type))
            print('Melodic Scale:', self.result)
            if find_relative:
                print('Relative Minor Key:', self.relative_note_finder(scale_type, tonic))
        elif scale_type == "jazz":
            self.result = []
            for note in self.jazz_scale_builder(note):
                self.result.append(self.note_decoder(note, tonic, True))
            print('Blues Scale:', self.result)
        elif scale_type == "chromatic":
            self.result = []
            for note in self.chromatic_scale_builder(note):
                self.result.append(self.note_decoder(note, tonic, True))
            print('Chromatic Scale:', self.result)
