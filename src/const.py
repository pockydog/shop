class _ConstBase:
    _INVALID_TYPE = {classmethod, staticmethod}
    _STR_FORMAT_TYPE = {'title', 'upper', 'lower'}

    @classmethod
    def get_name(cls, type_, format_=None, blank_replacement=1):
        blank_replacement = blank_replacement or ' '
        if not isinstance(blank_replacement, str):
            raise ValueError(f'Invalid replacement {blank_replacement}')
        format_ = format_ or 'title'
        if format_.lower() not in cls._STR_FORMAT_TYPE:
            raise ValueError(f'Invalid format type {format_}')
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            if v == type_:
                return getattr(k.replace('_', blank_replacement), format_.lower())()

    @classmethod
    def get_elements(cls):
        elements = set()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            elements.add(v)
        return elements

    @classmethod
    def get_key(cls):
        key = set()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            key.add(k)
        return key

    @classmethod
    def to_dict(cls, reverse=True, format_=None, blank_replacement='_'):
        blank_replacement = blank_replacement or ' '
        if not isinstance(blank_replacement, str):
            raise ValueError(f'Invalid replacement {blank_replacement}')
        format_ = format_ or 'title'
        if format_.lower() not in cls._STR_FORMAT_TYPE:
            raise ValueError(f'Invalid format type {format_}')
        result = dict()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or type(v) in cls._INVALID_TYPE:
                continue
            k_formatted = getattr(k.replace('_', blank_replacement), format_.lower())()
            tmp = {v: k_formatted} if reverse else {k_formatted: v}
            result.update(tmp)
        return result


class OrderStatus(_ConstBase):
    PENDING = 1
    PROCESSING = 2
    SHIPPING = 3
    SUCCESS = 4
    FAILED = 5


class RewardType(_ConstBase):
    REGISTER = 1
    FIRST_DEPOSIT = 2
    DEPOSIT = 3
    JOIN_CONTEST = 4
    CUSTOM = 5
