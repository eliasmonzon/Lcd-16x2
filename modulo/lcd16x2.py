import machine
import utime

class LCD_16x2:
    def __init__(self, rs_pin, e_pin, d4_pin, d5_pin, d6_pin, d7_pin):
        self.rs = machine.Pin(rs_pin, machine.Pin.OUT)
        self.e = machine.Pin(e_pin, machine.Pin.OUT)
        self.d4 = machine.Pin(d4_pin, machine.Pin.OUT)
        self.d5 = machine.Pin(d5_pin, machine.Pin.OUT)
        self.d6 = machine.Pin(d6_pin, machine.Pin.OUT)
        self.d7 = machine.Pin(d7_pin, machine.Pin.OUT)

        self.rs.value(0)
        self.e.value(0)

        self.init()

    def init(self):
        self.command(0x33)
        self.command(0x32)
        self.command(0x28)
        self.command(0x0C)
        self.command(0x06)
        self.command(0x01)

    def command(self, cmd):
        self.rs.value(0)
        self.nibble(cmd >> 4)
        self.nibble(cmd & 0x0F)
        utime.sleep_us(200)

    def data(self, data):
        self.rs.value(1)
        self.nibble(data >> 4)
        self.nibble(data & 0x0F)
        utime.sleep_us(200)

    def nibble(self, nibble):
        self.d4.value(nibble & 1)
        self.d5.value((nibble >> 1) & 1)
        self.d6.value((nibble >> 2) & 1)
        self.d7.value((nibble >> 3) & 1)
        self.e.value(1)
        utime.sleep_us(200)
        self.e.value(0)
        utime.sleep_us(200)

    def clear(self):
        self.command(0x01)

    def display_string(self, string, row=1, col=0):
        if row == 1:
            self.command(0x80 + col)
        elif row == 2:
            self.command(0xC0 + col)

        for char in string:
            self.data(ord(char))

    def create_char(self, location, pattern):
        self.command(0x40 + (location * 8))  # Set CGRAM address
        for line in pattern:
            self.data(line)
