GIFTS = {}

GIFTS[1] = "a Partridge in a Pear Tree"
GIFTS[2] = "two Turtle Doves"
GIFTS[3] = "three French Hens"
GIFTS[4] = "four Calling Birds"
GIFTS[5] = "five Gold Rings"
GIFTS[6] = "six Geese-a-Laying"
GIFTS[7] = "seven Swans-a-Swimming"
GIFTS[8] = "eight Maids-a-Milking"
GIFTS[9] = "nine Ladies Dancing"
GIFTS[10] = "ten Lords-a-Leaping"
GIFTS[11] = "eleven Pipers Piping"
GIFTS[12] = "twelve Drummers Drumming"

DAYS = ["zeroth", "first", "second",
        "third", "fourth", "fifth",
        "sixth", "seventh", "eighth",
        "ninth", "tenth",
        "eleventh", "twelfth"]

def recite(start_verse, end_verse):
    ''' Recites the lyrics from 12 days of Christmas '''
    lyrics = []

    for day in range(start_verse, end_verse + 1):
        verse = f"On the {DAYS[day]} day of Christmas my true love gave to me: "

        for gift in range(day, 0, -1):
            verse = verse + ("and " if (gift == 1 and day > 1) else "")
            verse = verse + GIFTS[gift]
            verse = verse + ("." if gift == 1 else ", ")

        lyrics.append(verse)

    return lyrics