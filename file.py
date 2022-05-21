def greeter(func):
    def inner(*args):
        names = func(*args).split()
        string = "Aloha"

        for n in range(len(names)):
            names[n] = " " + names[n].lower().capitalize()
            string += names[n]
        return string
    return inner


def sums_of_str_elements_are_equal(func):
    def summer(num1, num2):
        if sum(num1) == sum(num2):
            return f'{sum(num1)} == {sum(num2)}'
        else:
            return f'{sum(num1)} != {sum(num2)}'

    def splitter(*args):
        numbers = func(*args).split()

        if numbers[0][0] != '-':
            num1 = [int(n) for n in numbers[0]]
        else:
            num1 = [-int(n) for n in numbers[0][1:]]
        
        if numbers[1][0] != '-':
            num2 = [int(n) for n in numbers[1]]
        else:
            num2 = [-int(n) for n in numbers[1][1:]]
        
        return summer(num1, num2)
    return splitter


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
