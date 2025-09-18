def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    filtered_by_state_lists = [
        current_dict for current_dict in list_of_dicts if "state" in current_dict and current_dict["state"] == state
    ]

    return filtered_by_state_lists


def sort_by_date(list_of_dicts: list[dict], is_reversed: bool = True) -> list[dict]:
    sorted_by_date_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=is_reversed)

    return sorted_by_date_list
