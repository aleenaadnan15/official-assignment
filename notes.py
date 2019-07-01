#Question num 35:

'''  Find the number of notes against an given amount  '''

amount = int(input('enter any amount = '))

notesCountDict = {
    1000 : 0, 
    500 : 1, 
    100 : 2,
    50 : 3,
    20 : 4,
    10 : 5
}

def notes_counter(amount, notes = {}):
    for a, b in notes.items():
        while amount > 0:
            if amount >= a:
                amount -= a
                notes[a] += 1
            else:
                break
    return notes


for a, b in notes_counter(amount= amount, notes= notesCountDict).items():
    print("required {x} notes of {y}".format(x = a, y = b))
