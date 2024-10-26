import struct
class WaveFileHeader:
    @staticmethod
    def from_file(file_source):
        ident = file_source.read(4)
        if ident != b"RIFF":
            raise ValueError(f"Expected RIFF header, got {ident}.")
        file_size = struct.unpack("I",
            file_source.read(4))
        file_type = file_source.read(8)
        if file_type[:7] != b"WAVEfmt":
            raise ValueError(f"Not WAVE type. Got {file_type}")
        fmt = "IHHIIHHHI"
        fmt_size, wave_fmt, channels, sample_rate, byte_rate, block_align, bits_per_sample, extra, data_size = struct.unpack(fmt,
            file_source.read(struct.calcsize(fmt)))

        header = WaveFileHeader()
        header.wave_fmt = wave_fmt
        header.channels = channels
        header.sample_rate = sample_rate
        header.bits_per_sample = bits_per_sample
        header.data_size = data_size
        return header

    def __init__(self):
        self.data_size = 0xFFFF
        self.wave_fmt = 1 # PCM
        self.channels = 1
        self.sample_rate = 22_050
        self.bits_per_sample = 16