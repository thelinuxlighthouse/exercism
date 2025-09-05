def convert(number):
    raindrops = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }
    
    string = ''
    for n in raindrops.keys():
        if number % n == 0:
            string += raindrops[n]
    return string or str(number)
