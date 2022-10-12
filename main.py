import musicdoc

n = {'C': 1, 'C#': 2, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 4, 'E': 5, 'F': 6, 'F#': 7, 'Gb': 7, 'G': 8,
     'G#': 9,
     'Ab': 9, 'A': 10, 'A#': 11, 'Bb': 11, 'B': 12}
major_accidentals = {'Cb': -7, 'C': 0, 'C#': 7, 'Db': -5, 'D': 2, 'Eb': -3, 'E': 4, 'F': -1, 'F#': 6, 'Gb': -6,
                     'G': 1, 'Ab': -4, 'A': 3, 'Bb': -2, 'B': 5}
minor_accidentals = {'A#': 7, 'C': -3, 'C#': 4, 'D#': 6, 'D': -1, 'Eb': -6, 'E': 1, 'F': -4, 'F#': 3, 'G#': 5,
                     'G': -2, 'Ab': -7, 'A': 0, 'Bb': -5, 'B': 2}
scale_types = ['major', 'minor', 'harmonic', 'melodic', 'jazz', 'chromatic']
notes = list(n)
music = musicdoc.Music(major_accidentals, minor_accidentals, n)
scales = scales.Scales(major_accidentals, minor_accidentals, n)

print("""
𝕃𝕒𝕄𝕦𝕤𝕚𝕔
_____________
""")
