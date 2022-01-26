import PartA as pa
import sys


class Comparer():
    def __init__(self):
        pass

    # Convert token lists to hash sets and iterate the set that has shorter len to compare another set,
    # time complexity is O(max(n1, n2)) where n1 is length of first file, n2 is length of second file
    def Compare(self, File1, File2):
        t = pa.tokenizer()
        counter = 0

        l = t.Tokenize(File1)
        FileSet1 = set()
        for v in l:
            if len(v) >= 2:
                FileSet1.add(v)

        l = t.Tokenize(File2)
        FileSet2 = set()
        for v in l:
            if len(v) >= 2:
                FileSet2.add(v)

        if len(FileSet1) > len(FileSet2):
            for token in FileSet2:
                if token in FileSet1:
                    counter += 1
        else:
            for token in FileSet1:
                if token in FileSet2:
                    counter += 1

        print(counter)


if __name__ == "__main__":
    f1 = open(sys.argv[1], "r")
    f2 = open(sys.argv[2], "r")

    c = Comparer()
    c.Compare(f1, f2)

