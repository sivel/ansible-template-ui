import sys

PY3 = sys.version_info[0] == 3

if PY3:
    def b(s):
        if not isinstance(s, bytes):
            return s.encode('utf-8')
        return s

    def u(s):
        if not isinstance(s, str):
            return s.decode('utf-8')
        return s

    native = u
else:
    def b(s):
        if not isinstance(s, str):
            return s.encode('utf-8')
        return s

    def u(s):
        if not isinstance(s, unicode):
            return s.decode('utf-8')
        return s

    native = b
