from pyproto import ProtoBuf


def decode_hex(data):
    return ProtoBuf(bytes.fromhex(data)).dump()


print(
    decode_hex(
        "08 A4 8C 90 81 04 10 02 32 60 77 34 76 82 1D E6 5C 00 6F 03 EC 3A 88 30 D3 C9 BF 24 66 AD A2 1B 2A 45 AD 21 A2 54 45 F2 62 4C 64 81 03 3A F8 59 A9 89 B4 D2 1E 88 B4 81 6A A3 F7 21 E3 81 36 43 E8 BF B6 10 63 0D 27 15 76 D1 15 F0 85 8C 76 D3 B4 21 73 C1 37 DA 22 62 E3 EC 3D 51 59 F6 C2 62 1B CC 07 56 41 8C 2B 03 CC 1A 38 D2 9A E7 B7 CE 66 40 C6 81 D6 9C A7 33"
    )
)
