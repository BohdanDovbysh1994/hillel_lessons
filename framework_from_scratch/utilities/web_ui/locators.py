class Locator:

    def __init__(self, method, locator_string):
        self.method = method
        self.locator_string = locator_string

    def get_locator(self):
        return self.method, self.locator_string
