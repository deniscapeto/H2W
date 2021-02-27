class Amplifier:

    def init(self):
        self.instrument_input = None

    def play_instrument(self):
        if self.instrument_input:
            self.instrument_input.play()


class Guitar:

    def play(self):
        print('Playing the guitar...whah whah!')


class Keyboard:

    def play(self):
        print('Playing the keyboard...tada!')


class Saxophone:

    def play(self):
        print('Playing the saxophone...Wow!')


if __name__ == "__main__":

    amp = Amplifier()

    # Changing the behavior

    amp.instrument_input = Guitar()
    amp.play_instrument()

    amp.instrument_input = Keyboard()
    amp.play_instrument()

    amp.instrument_input = Saxophone()
    amp.play_instrument()
