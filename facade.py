#!/usr/bin/env python

"""
外观模式
"""


class RARModel:
    def cpmpress(self, src_file_path, dst_file_path):
        print(f"RAR压缩文件{src_file_path} => {dst_file_path}")

    def decpmpress(self, src_file_path, dst_file_path):
        print(f"RAR解压文件{src_file_path} => {dst_file_path}")


class ZIPModel:
    def cpmpress(self, src_file_path, dst_file_path):
        print(f"ZIP压缩文件{src_file_path} => {dst_file_path}")

    def decpmpress(self, src_file_path, dst_file_path):
        print(f"ZIP解压文件{src_file_path} => {dst_file_path}")


class File:

    def __init__(self):
        self.__rar = RARModel()
        self.__zip = ZIPModel()

    def compress(self, src_file_path, dst_file_path, typeof):
        if typeof == "zip":
            self.__zip.cpmpress(src_file_path, dst_file_path)
        elif typeof == "rar":
            self.__rar.cpmpress(src_file_path, dst_file_path)
        else:
            print("compress type error")

    def decompress(self, src_file_path, dst_file_path, typeof):
        if typeof == "zip":
            self.__zip.decpmpress(src_file_path, dst_file_path)
        elif typeof == "rar":
            self.__rar.decpmpress(src_file_path, dst_file_path)
        else:
            print("decompress type error")


if __name__ == "__main__":
    file = File()
    file.compress("a.txt", "a.zip", "zip")
    file.decompress("a.zip", "a.txt", "rar")
