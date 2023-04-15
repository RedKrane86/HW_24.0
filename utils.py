import re
from typing import Any, Iterable, List


def filter_query(value: str, data: Iterable[str]) -> object:
    return filter(lambda v: value in v, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set:
    return set(data)


def map_query(value: str, data: Iterable[str]) -> object:
    col_number = int(value)
    return map(lambda v: v.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit: int = int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterable[str]) -> object:
    response = re.compile(value)
    return filter(lambda v: re.search(response, v), data)

