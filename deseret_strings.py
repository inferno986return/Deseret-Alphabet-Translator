import logging


def unescape(text):
    def fixup(m):
        anEntity = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    unicode = unichr(int(anEntity[3:-1], 16))
                    return unicode
                else:
                    unicode = unichr(int(anEntity[2:-1]))
                    return unicode
            except ValueError as error:
                pass
        else:
            # named entity
            try:
                unicode = unichr(htmlentitydefs.name2codepoint[anEntity[1:-1]])
                return unicode
            except KeyError:
                pass
        return anEntity # leave as is
    return re.sub("&#?\w+;", fixup, text)

def unicode_char(unicode_value):
    return ("\\U%08x" % unicode_value).decode('unicode-escape')


def is_leading_upper(text):
    found_trailing_lower = False
    if text[0].isupper():
        for letter in text[1:]:
            if not letter.isupper():
                found_trailing_lower = True
                break

    return found_trailing_lower

def is_all_upper(text):
    return text.isupper()

def leading_upper(text):
    """Convert text to leading capitalization"""
    return text[0].upper() + text[1:].lower()

def apply_capitalization(source, target):

    if not source or source is None:
        text = source
    else:
        if source.isupper():
            text = target.upper()
        elif is_leading_upper(source):
            text = leading_upper(target)
        else:
            text = target.lower()

    return text

