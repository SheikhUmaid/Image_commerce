from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email,name, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        if not name:
            raise ValueError("Name is required")
        user = self.model(
            name = name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, password,name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        return self.create_user(email,name, password, **extra_fields)

        # user = self.create_user(
        #     email=email,
        #     phone_number=phone_number,
        #     password=password,
        #     **extra_fields
        # )
        # user.is_admin = True
        # user.is_staff = True
        # user.is_superuser = True
        # user.is_active = True
        # user.save()
        # return user