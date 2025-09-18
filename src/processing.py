def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    filtered_by_state_lists = [
        current_dict for current_dict in list_of_dicts if "state" in current_dict and current_dict["state"] == state
    ]

    return filtered_by_state_lists
