def recite(start_verse, end_verse):
    days = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
        ]
    gifts = [
        'a Partridge in a Pear Tree.',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming'
        ]
    song = []
    for x in range(start_verse-1, end_verse):
        gift_s = gifts[x::-1]
        if len(gift_s) > 1:
            gift_s[-1] = "and " + gift_s[-1]
        song.append(f"On the {days[x]} day of Christmas my true love gave to me: {', '.join(gift_s)}")

    return song
