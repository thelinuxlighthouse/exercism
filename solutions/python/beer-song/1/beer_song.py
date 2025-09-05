def recite(start, take=1):
    full_song = beer_generator(b=99)
    recite_song = []
    while take:
        recite_song += full_song[start]
        start -= 1
        take -= 1
    if recite_song[-1] == '':
        recite_song.pop(-1)
    return recite_song


def beer_generator(b=99):
    song = dict()
    while b != 0:
        song[b] = [
            f"{b} {'bottles' if b > 1 else 'bottle'} of beer on the wall, {b} {'bottles' if b > 1 else 'bottle'} of beer.",
            f"{'Take one down and pass it around' if b > 1 else 'Take it down and pass it around'}, {b-1 or 'no more'} {'bottles' if (b-1 > 1 or b-1 == 0) else 'bottle'} of beer on the wall.",
            "",
        ]
        b -= 1
    song[0] = [
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
    return song