class CsvReader:
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.file = None
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def getdata(self):
        data = []
        try:
            for line in self.file:
                data.append(list(line.rstrip("\n\r").split(sep=self.sep)))
            if self.skip_bottom != 0:
                length = len(data) - self.skip_bottom
                data = data[:length]
        except OSError as e:
            print(f"{e}\nCould not open file {str(self)}")
            data = None
        return data

    def getheader(self):
        try:
            f = open(self.filename, mode='r')
            head = (f.readline().split(sep=self.sep))
            head[len(head) - 1] = head[len(head) - 1].replace("\n", "")
        except OSError as e:
            print(f"{e}\nCould not open file {str(self)}")
            head = None
        return head

    def __enter__(self):
        try:
            self.file = open(self.filename, mode='r')
            test = open(self.filename, mode='r')
            len_head = len(test.readline().split(sep=self.sep))
            for line in test:
                linelist = line.rstrip("\n\r").split(sep=self.sep)
                len_data = len([x for x in linelist if x != ''])
                if len_data != len_head:
                    self.file = None
                    return self.file
            if self.header is True:
                next(self.file)
            if self.skip_top != 0:
                for top in range(0, self.skip_top):
                    next(self.file)
        except OSError as e:
            print(f"{e}\nCould not open file {str(self)}")
            self.file = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            if not self.file.closed:
                self.file.close()


# if __name__ == "__main__":
#     with CsvReader('good.csv', skip_top=0, header=True, skip_bottom=2) as file:
#         if file is None:
#             print("File is corrupted")
#         else:
#             datas = file.getdata()
#             header = file.getheader()
#             if datas:
#                 for elem in datas:
#                     print(elem)
#             print()
#             print(header)
