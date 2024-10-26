from machine import Pin, SPI
import sdcard
import uos
import wave_file

led = Pin("LED", Pin.OUT)

def blink_led(timer_one):
    led.toggle()

cs = Pin(5, Pin.OUT)
spi=SPI(
    0, 
    baudrate=4000000, 
    polarity=0,
    phase=0,
    bits=8,
    firstbit=SPI.MSB,
    sck=Pin(2), 
    mosi=Pin(3), 
    miso=Pin(4))

sd=sdcard.SDCard(spi, cs)

vfs = uos.VfsFat(sd)

uos.mount(vfs, '/sd')
print(uos.listdir('/sd'))

with open("/sd/better_way.wav", "rb") as wav:
    print("Reading header")
    wav_header = wave_file.WaveFileHeader.from_file(wav)
    print(f"Bits per sample: {wav_header.bits_per_sample}")
    print(f"Sample rate: {wav_header.sample_rate}")
    print(f"Channels: {wav_header.channels}")