#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# manage.py
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoAadditionalPractice.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Добавляем 'runserver' и нужный порт как аргументы
    # sys.argv = ['manage.py', 'runserver', '0.0.0.0:8080']  # Замените 8001 на нужный вам порт
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
