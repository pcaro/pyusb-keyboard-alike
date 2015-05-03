from keyboard_alike import reader


class MotorolaReader(reader.Reader):

    def __init__(self):
        super(MotorolaReader, self).__init__(vendor_id=0x05e0, product_id=0x1200,
                                             data_size=144, chunk_size=8,
                                             should_reset=False, debug=False)


if __name__ == "__main__":
    reader = MotorolaReader()
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
