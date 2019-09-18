from functools import wraps


def add_count_to_list(method):
    @wraps(method)
    def _decorator(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = len(queryset)

        response = method(self, *args, **kwargs)
        response.data = {
            'count': count,
            'data': response.data
        }

        return response

    return _decorator
