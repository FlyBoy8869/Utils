__author__ = 'charles'


def debug(callable):
    """Decorate a callable to display the arguments it was called with.

    The debug decorator will display the positional and keyword arguments
    that a function or method is called with.

    For example, with the following function definition:

        @debug
        def function(arg1, arg2, keyword1='value1', keyword2='value2')
      ...

    and usage:

        function(2, 5, keyword2='testing 1 2 3')

    will result in:

    ----------  function  ----------
    p_args: (2, 5)
    kwargs defaults: ('value1', 'value2')
    kwargs supplied: {'keyword2': 'testing 1 2 3'}


    If the function or method does not take keyword arguments,
    nothing will be displayed for kwargs.
    """

    def wrapper(*args, **kwargs):
        print("----------  " + callable.__name__ + "  -------------")
        print("p_args:" , args)
        if callable.__defaults__ is not None:
            print("kwargs defaults:", callable.__defaults__)
            print("kwargs supplied:", kwargs)

        return callable(*args, **kwargs)

    return wrapper
