def _is_image(url):
    guess = mimetypes.guess_type(url)[0]
    return guess.startswith('image') if guess else False
