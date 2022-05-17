from __future__ import annotations

from typing import Iterator


class Pixel:
    def __init__(self, data: tuple[int, int, int, int]):
        self._data = data
        self.blue, self.green, self.red, self.alpha = data

    def tuple(self) -> tuple:
        return self.blue, self.green, self.red, self.alpha

    def hide_byte(self, byte):
        self.blue = self.blue & 0xFC | (byte >> 6) & 0x3
        self.green = self.green & 0xFC | (byte >> 4) & 0x3
        self.red = self.red & 0xFC | (byte >> 2) & 0x3
        self.alpha = self.red & 0xFC | byte & 0x3
        return self

    def get_hidden(self) -> int:
        result = self.blue & 0x3
        result = result << 2 | self.green & 0x3
        result = result << 2 | self.red & 0x3
        result = result << 2 | self.alpha & 0x3
        return result

    @staticmethod
    def iterator(data: bytes) -> Iterator:
        count_pixels = len(data) // 4
        for i in range(count_pixels):
            yield Pixel((data[4 * i], data[4 * i + 1], data[4 * i + 2], data[4 * i + 3]))
