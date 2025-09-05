def recite(start_verse, end_verse):
    days_gifts = [
        ('first', 'a Partridge in a Pear Tree.'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
        ]
    song = []
    for x in range(start_verse-1, end_verse):
        gifts = []
        for y in reversed(range(x+1)):
            gifts.append(days_gifts[y][1])
        if len(gifts) > 1:
            gifts[-1] = "and " + gifts[-1]
        song.append(f"On the {days_gifts[x][0]} day of Christmas my true love gave to me: " + ', '.join(gifts))

    return song
