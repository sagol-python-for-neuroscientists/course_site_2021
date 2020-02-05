"""
__author__ = Hagai Har-Gil
"""
class DataParser:
    def __init__(self, filename, filetype):
        self.filename = str(filename)
        self.filetype = filetype

    def run(self):
        pre = self.__preprocess()
        self.__create_global_vars()
        result = self.__process(pre)
        self.print_result(result)

    def __preprocess(self):
        pre = 1
        return pre

    def __create_global_vars(self):
        self.a = 1
        self.b = 2.

    def __process(self, pre):
        pre += 1
        pre /= 2

        return [pre, pre]

    def print_result(self, result):
        print(result)


if __name__ == '__main__':
    DataParser('a', 'b').run()