from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    double = "d"
    uint8 = "B"
    uint16 = "H"
    uint32 = "I"
    uint64 = "Q"
    int8 = "b"
    int16 = "h"
    int32 = "i"
    int64 = "q"
    char = "c"


class BinaryReader():
    def __init__(self, offset, buffer):
        self.offset = offset
        self.buffer = buffer

    def read(self, _pattern):
        pattern = '>' + _pattern.value
        result = unpack_from(pattern, self.buffer, self.offset)
        self.offset += calcsize(pattern)
        return result[0]

    def readWithSize(self, _pattern, size):
        res = []
        for i in range(0, size):
            pattern = '>' + _pattern.value
            result = unpack_from(pattern, self.buffer, self.offset)
            self.offset += calcsize(pattern)
            res.append(result[0])
        return res

    def copy(self, offset):
        return BinaryReader(offset, self.buffer)


def readB(reader):
    b1 = []
    for i in range(0, 4):
        b1.append(readC(reader))
    b2 = reader.readWithSize(Types.int8, 8)
    b3 = readD(reader)
    b4 = reader.read(Types.int64)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def readC(reader):
    c1 = reader.read(Types.double)
    c2 = reader.readWithSize(Types.int8, 6)
    return dict(C1=c1, C2=c2)


def readD(reader):
    d1 = reader.readWithSize(Types.int16, 6)
    size2 = reader.read(Types.uint16)
    adress2 = reader.read(Types.uint32)
    d2 = reader.copy(offset=adress2).readWithSize(Types.uint16, size2)
    d3 = reader.read(Types.int16)
    return dict(D1=d1, D2=d2, D3=d3)


def main(buffer):
    reader = BinaryReader(offset=3, buffer=buffer)
    a1 = readB(reader)
    a2 = reader.read(Types.int8)
    a3 = reader.read(Types.double)
    a4 = reader.read(Types.int16)
    a5 = reader.read(Types.int64)
    a6 = reader.read(Types.uint64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)




from struct import *


FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'int8')
    a3, offs = parse(buf, offs, 'double')
    a4, offs = parse(buf, offs, 'int16')
    a5, offs = parse(buf, offs, 'int64')
    a6, offs = parse(buf, offs, 'uint64')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1 = []
    for _ in range(4):
        val, offs = parse_c(buf, offs)
        b1.append(val)
    b2 = []
    for _ in range(8):
        val, offs = parse(buf, offs, 'int8')
        b2.append(val)
    b3, offs = parse_d(buf, offs)
    b4, offs = parse(buf, offs, 'int64')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'double')
    c2 = []
    for _ in range(6):
        val, offs = parse(buf, offs, 'int8')
        c2.append(val)
    return dict(C1=c1, C2=c2), offs


def parse_d(buf, offs):
    d1 = []
    for _ in range(6):
        val, offs = parse(buf, offs, 'int16')
        d1.append(val)
    d2_size, offs = parse(buf, offs, 'uint16')
    d2_offs, offs = parse(buf, offs, 'uint32')
    d2 = []
    for _ in range(d2_size):
        val, d2_offs = parse(buf, d2_offs, 'uint16')
        d2.append(val)
    d3, offs = parse(buf, offs, 'int16')
    return dict(D1=d1, D2=d2, D3=d3), offs


def main(buf):
    return parse_a(buf, 4)[0]