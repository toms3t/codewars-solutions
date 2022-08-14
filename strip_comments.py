import re


def solution(text=None, markers=None):
    lines = []
    mod_lines = []
    ignore = False
    mod_text = ""
    for s in text:
        if s not in markers and not ignore and s != "\n":
            mod_text += s
        elif s in markers:
            ignore = True
        elif s == "\n":
            mod_text += s
            lines.append(mod_text)
            ignore = False
            mod_text = ""
    lines.append(mod_text.rstrip())
    for line in lines:
        newline = re.sub("\s+\n", "\n", line)
        mod_lines.append(newline)
    return "".join(mod_lines)
