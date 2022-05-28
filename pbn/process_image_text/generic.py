def pb_info(text):
    current_time = get_current_time(text)
    last_delta = get_last_delta(text)
    pb = get_pb(text)

    is_pb_pace = True if last_delta < 0 else False
    fraction_of_run = get_fraction_of_time(current_time, pb)

    data = {
        "current_time": current_time,
        "last_delta": last_delta,
        "pb": pb,
        "is_pb_pace": is_pb_pace,
        "fraction_of_run": fraction_of_run
    }

    return data
