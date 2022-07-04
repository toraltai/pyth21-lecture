def login_required(obj):
    if not obj.is_auth:
        raise Exception("Юзер не авторизован")