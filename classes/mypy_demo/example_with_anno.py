"""
__author__ = Hagai Har-Gil
"""
from typing import List


class DataParser:
    def __init__(self, filename: str, filetype: str) -> None:
        self.filename = str(filename)
        self.filetype = filetype

    def run(self) -> None:
        pre: int = self.__preprocess()
        self.__create_global_vars()
        result: List[float] = self.__process(pre)
        self.print_result(result)

    def __preprocess(self) -> int:
        pre: int = 1
        return pre

    def __create_global_vars(self) -> None:
        self.a: int = 1
        self.b: float = 2.

    def __process(self, pre: float) -> List[int]:
        pre += 1
        pre /= 2

        return [pre, pre]

    def print_result(self, result: List[int]) -> None:
        print(result)


if __name__ == '__main__':
    DataParser('a', 'b').run()