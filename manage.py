#!/usr/bin/env python
"""Django yönetim komut satırı aracı."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ozdemir_servis.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django içe aktarılamadı. Kurulu ve PYTHONPATH'te olduğundan, "
            "sanal ortamı etkinleştirdiğinizden emin olun."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
