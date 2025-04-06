class BurnInputStream:
    def get_next_burn(self, status):
        while True:
            note = "Must Enter a int (0-200)"
            try:
                tokens = input().split()
                if tokens:
                    burn = int(tokens[0])
                    if 0 <= burn <= 200:
                        return burn
                    else:
                        print(note)
            except ValueError:
                print(note)

#Example usage:
# burn_input_stream = BurnInputStream()
# status = None  # Replace with actual DescentEvent object
# burn = burn_input_stream.get_next_burn(status)
# print(burn)
