import musicdoc
import scales
import random

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
LaMusic
_____________
Are you a musician? Want to test your skills? This is the perfect game for you!
You will be given a scale and a scale degree value. You will then have to guess
the note for that scale degree within the given scale. Get it right, that's two points. Get it 
wrong, you will lose a point. Keep playing to see if you can make it to 12!
______________
""")

points = 0
notee = ["A", "B", "C", "D", "E", "F", "G"]

print("Welcome...")
user_name = input("Please enter name: ")
print("Welcome {username}! It's great to see another fine musician!".format(username = user_name))
while points < 12:
    scale_degrees = random.randint(1, 8)
    note = random.choice(notee)
 #   print(scales.scale_builder("major", note, False))
    scale = scales.scale_builder("major", note, False)
    print("-_-_-_-_-_-_-_")
    user_response = input("You have been given the scale: {scale} Major \n Scale Degree: {num} \n What is the note?: ".format(scale = note, num = scale_degrees))
    if user_response == scale[scale_degrees-1]:
        points += 2
        print("CORRECT! |" + str(points))
    else:
        points -= 1
        print("WRONG! |" + str(points))

print("Congrats! You passed!")