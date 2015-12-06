class NelsnmpError(Exception):
    pass


class ArgumentError(NelsnmpError):
    pass


class SnmpError(NelsnmpError):
    pass
