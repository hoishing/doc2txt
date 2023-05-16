# utils
import re


def remove_empty_rows(txt: str) -> str:
    return re.sub(r"(\n\s*){3,}", r"\n\n", txt)


def remove_bad_characters(txt: str) -> str:
    pattern = r"[ \n]*—[ \n]*"
    txt = re.sub(pattern, "", txt)
    pattern = r" {1,}"
    txt = re.sub(pattern, " ", txt)
    pattern = r" {2,}"
    txt = re.sub(pattern, " ", txt)
    return txt
