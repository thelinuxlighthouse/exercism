def slices(series, length):
    if len(series) < length or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive integer and not bigger than series length.")
    return [series[i:i+length] for i in range(len(series)-length+1)]
