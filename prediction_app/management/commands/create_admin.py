"""
Management command to create a predefined admin user.

Usage:
    python manage.py create_admin

This creates an admin with:
    Username: admin
    Password: admin@123
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from prediction_app.models import UserProfile


class Command(BaseCommand):
    help = 'Creates a predefined admin user if it does not already exist.'

    # ── Predefined Admin Credentials ──
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'admin@123'
    ADMIN_EMAIL = 'admin@agrisuitability.com'
    ADMIN_FIRST_NAME = 'Admin'

    def handle(self, *args, **options):
        if User.objects.filter(username=self.ADMIN_USERNAME).exists():
            self.stdout.write(self.style.WARNING(
                f'Admin user "{self.ADMIN_USERNAME}" already exists. Skipping creation.'
            ))
            # Ensure existing admin has correct role & staff status
            user = User.objects.get(username=self.ADMIN_USERNAME)
            user.is_staff = True
            user.is_superuser = True
            user.save()

            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.role = 'admin'
            profile.save()

            self.stdout.write(self.style.SUCCESS('Admin role & staff status verified.'))
            return

        # Create the admin user
        user = User.objects.create_user(
            username=self.ADMIN_USERNAME,
            password=self.ADMIN_PASSWORD,
            email=self.ADMIN_EMAIL,
            first_name=self.ADMIN_FIRST_NAME,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        # Set admin role on the profile
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = 'admin'
        profile.save()

        self.stdout.write(self.style.SUCCESS(
            f'\nAdmin user created successfully!'
            f'\n   Username : {self.ADMIN_USERNAME}'
            f'\n   Password : {self.ADMIN_PASSWORD}'
            f'\n   Email    : {self.ADMIN_EMAIL}'
        ))
