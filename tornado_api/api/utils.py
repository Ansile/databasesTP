def clear_dict(_dict):
    return {k: v for k, v in _dict.items() if v is not None}


def time_normalize(time, db_format=False):
    import arrow
    time = arrow.get(time)
    if db_format:
        return time.isoformat(sep=' ')
    time = time.to('utc')
    return time.isoformat()


def timestamp(time):
    import arrow
    time = arrow.get(time)
    return time.timestamp
