def not_string(s):
    if s.startswith("not"):
        return s
    else:
        s = "not " + s
        return s
