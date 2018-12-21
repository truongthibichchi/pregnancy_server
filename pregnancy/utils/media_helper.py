from configs.settings import SERVER_ENDPOINT, STATIC_URL


def get_media_url(media_leaf):
    return f'{SERVER_ENDPOINT}{STATIC_URL}{media_leaf}'
