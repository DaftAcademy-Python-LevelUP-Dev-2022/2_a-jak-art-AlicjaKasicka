from types import MethodType


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
    keys = []
    for key in required_keys:
        keys.append(key.split("__"))
    
    def real_decorator(func):
        def checker(*args):
            funct_keys = func(*args)
            new_dict = {}
            
            for key in keys:
                if len(key) == 1:
                    if key[0] not in funct_keys.keys():
                        raise ValueError
                    else:
                        if not funct_keys[key[0]]:
                            new_dict[key[0]] = "Empty value"
                        else:
                            new_dict[key[0]] = funct_keys[key[0]]
                else:
                    new_str = ""
                    for k in key:
                        if k not in funct_keys.keys():
                            raise ValueError
                        else:
                            new_str += " " + funct_keys[k]

                    new_key = "__".join(key)
                    if not new_str:
                        new_dict[new_key] = "Empty value"
                    else:
                        new_dict[new_key] = new_str[1:]
            return new_dict
        return checker
    return real_decorator


def add_method_to_instance(klass):
    def real_decorator(func):
        def wrapper(*args):
            return func
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return real_decorator
