from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
DEPARTMENTS = (
    ("Chemical Engineering", "Chemical Engineering"),
    ("Biotechnology", "Biotechnology"),
    ("Civil Engineering", "Civil Engineering"),
    ("Computer Science and Engineering", "Computer Science and Engineering"),
    ("Electronics and Communication Engineering", "Electronics and Communication Engineering"),
    ("Electronics and Electrical Engineering", "Electronics and Electrical Engineering"),
    ("Engineering Physics", "Engineering Physics"),
    ("Mathematics and Computing", "Mathematics and Computing"),
    ("Mechanical Engineering", "Mechanical Engineering"),
    ("Design ", "Design "),
    ("Biosciences and Bioengineering", "Biosciences and Bioengineering"),
    ("None", "None"),

)


CLUBS = (
    ("Alcheringa", "Alcheringa"),
    ("Cadence", "Cadence"),
    ("Anchorenza and RadioG (AnR)", "Anchorenza and RadioG (AnR)"),
    ("Fine Arts", "Fine Arts"),
    ("Montage", "Montage"),
    ("Lumiere", "Lumiere"),
    ("Octaves", "Octaves"),
    ("Expressions", "Expressions"),
    ("LitSoc-DebSoc", "LitSoc-DebSoc"),
    ("Aeromodelling", "Aeromodelling"),
    ("Astronomy", "Astronomy"),
    ("Coding", "Coding"),
    ("Consulting and Analytics (CnA)", "Consulting and Analytics (CnA)"),
    ("Electronics ", "Electronics "),
    ("Prakriti ", "Prakriti "),
    ("Finance and Economics", "Finance and Economics"),
    ("Robotics", "Robotics "),
    ("ACUMEN", "ACUMEN"),
    ("TechEvince", "TechEvince"),
    ("Green Automobile", "Green Automobile"),
    ("Entrepreneurial Development Cell (EDC)", "Entrepreneurial Development Cell (EDC)"),
    ("Udgam", "Udgam"),
    ("Techniche", "Techniche"),
    ("None", "None"),


)

BATCH = (
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("None", "None"),
)
ADDRESS_TYPE = (
    ("H", "Home Address"),
    ("W", "Work/Office Address")
)



class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    is_merchant = models.BooleanField(default=False)
    department = models.CharField(max_length=120, choices=DEPARTMENTS, default='None')
    club = models.CharField(max_length=120, choices=CLUBS, default='None')
    batch = models.CharField(max_length=4, choices=BATCH, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_email(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Address(models.Model):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    zip = models.CharField(max_length=10, blank=False, null=False)
    house_no = models.CharField(max_length=120, blank=False, null=False)
    area = models.CharField(max_length=120, blank=False, null=False)
    city = models.CharField(max_length=120, blank=False, null=False)
    state = models.CharField(max_length=120, blank=False, null=False)
    landmark = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120, blank=False, null=False)
    mobile_no = models.CharField(max_length=10, blank=False, null=False)
    alternate_no = models.CharField(max_length=10, blank=True, null=True)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPE, default='H')

    def __str__(self):
        return str(self.user.username)

    # def get_fulladdress(self):



class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120)

    def __str__(self):
        return str(self.stripe_id)


