from collections import defaultdict

from actor_libs.types import CacheDictCode


__all__ = ['dict_code_cache']


def dict_code_cache() -> CacheDictCode:
    from app.models import DictCode

    record = defaultdict(dict)
    dict_code_values = DictCode.query.all()

    for dict_code in dict_code_values:
        int_value = dict_code.codeValue
        code_value = int_value if int_value is not None else dict_code.codeStringValue
        record[dict_code.code][code_value] = {
            'enLabel': dict_code.enLabel,
            'zhLabel': dict_code.zhLabel
        }
    return record
