def clear_dict(_dict):
    return {k: v for k, v in _dict.items() if v is not None}


def time_normalize(time, json_format=False, db_format=False):
    import arrow
    time = arrow.get(time,)
    time = time.to('+03:00')

    if db_format:
        return time.isoformat(sep=' ')
    if json_format:
        return time.for_json()
    return time.isoformat()


def timestamp(time):
    import arrow
    time = arrow.get(time)
    return time.timestamp


def int_convert(num):
    if num is None:
        return 0
    else:
        return int(num)


def slug_and_id(slug_or_id):
    try:
        thread_id = int(slug_or_id)
        return None, thread_id
    except:
        thread_slug = slug_or_id
        return thread_slug, None