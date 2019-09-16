from rest_framework.generics import ValidationError, get_object_or_404
from django.shortcuts import get_list_or_404 as _get_list_or_404


def get_list_or_404(queryset, *filter_args, **filter_kwargs):
    """
    Same as Django's standard shortcut, but make sure to also raise 404
    if the filter_kwargs don't match the required types.
    """
    try:
        return _get_list_or_404(queryset, *filter_args, **filter_kwargs)
    except (TypeError, ValueError, ValidationError):
        raise Http404
