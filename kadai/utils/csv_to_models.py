import csv
from typing import Any, List, Type, TypeVar


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content_str = file.read()
    return content_str


class CSVMixin:
    @staticmethod
    def fromCSV(csv_dict: dict[str, Any]) -> Any:
        raise NotImplementedError


T = TypeVar("T", bound=CSVMixin)


def parse_csv_file_to_models(
    file_path: str,
    model_cls: Type[T],
) -> List[T]:
    results = []

    content_str = read_file(file_path)
    reader = csv.DictReader(content_str.splitlines())
    for row in reader:
        model = model_cls.fromCSV(row)
        results.append(model)

    return results
