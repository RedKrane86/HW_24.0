from typing import Any, Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda v: value in v, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any):
    return set(data)


def map_query(value: str, data: Iterable[str]):
    col_number = int(value)
    return map(lambda v: v.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]):
    limit: int = int(value)
    return list(data)[:limit]

