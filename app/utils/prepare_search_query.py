from fastapi import Request


def prepare_query_params_for_custome_field(request: Request):
    _static_query_filter_parameters = ("name", "status", "skip", "limit")
    return {
        key: value
        for key, value in dict(request.query_params).items()
        if key not in _static_query_filter_parameters
    }
