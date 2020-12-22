class LocatorTypeError(Exception):
    pass


class ElementNotFound(Exception):
    pass


def try_exception_re(func):
    def function(args):
        if not isinstance(args, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                return func(args)
            except ElementNotFound as e:
                raise ElementNotFound("元素没有找到，定位超时")

    return function


def try_exception(func):
    def function(args):
        if not isinstance(args, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                func(args)
            except ElementNotFound as e:
                raise ElementNotFound("元素没有找到，定位超时")

    return function
