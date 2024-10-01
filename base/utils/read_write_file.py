import os

from django.conf import settings


def write_to_file(str_, path: str = "path/to/writequery.txt", append=False):
    full_path = os.path.join(settings.BASE_DIR, path)

    if append:
        with open(full_path, "a") as f:
            f.writelines(f"\n{str_}")
            f.close
    else:
        with open(full_path, "w") as f:
            f.write(str_)
            f.close


def read_file(path: str = "path/to/file.txt"):
    full_path = os.path.join(settings.BASE_DIR, path)

    with open(full_path, "r") as f:
        result = f.read()

    return result
