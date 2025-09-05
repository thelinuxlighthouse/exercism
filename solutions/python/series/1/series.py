def slices(series, length):
    if len(series) < length or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive integer and not bigger than series length.")
    slice = []
    for i in range(len(series)):
        s = series[i:]
        if len(s) >= length:
            slice.append(s[:length])
    return slice