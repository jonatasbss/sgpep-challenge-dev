import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgpe.settings')
django.setup()


def create_user_admin():
    User = get_user_model()

    User.objects.create_superuser('admin@admin.com', 'admin123456')
    print('Usuário admin criado!')


if __name__ == '__main__':
    create_user_admin()
