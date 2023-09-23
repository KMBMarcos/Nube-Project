
# Guia usada: https://developer.mozilla.org/es/docs/Learn/Server-side/Django/skeleton_website

# ---> Django's command-line utility for administrative tasks. <---

# Para la migracion de la base de datos: python manage.py migrate
# Para correr el servidor: python manage.py runserver
# Creción del usuario admin del sitio: python manage.py createsuperuser

#!/usr/bin/env python

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
