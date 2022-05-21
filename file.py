def greeter(func):
    def inner(*args):
        names = func(*args).split()
        string = "Aloha"

        for n in range(len(names)):
            names[n] = " " + names[n].capitalize()
            string += names[n]
        return string
    return inner

@greeter
def name_surname():
    return "jarek kon"

name_surname()


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
