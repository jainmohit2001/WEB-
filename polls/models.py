from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from PIL import Image

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

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    department = models.CharField(max_length=120, choices=DEPARTMENTS, default='None')
    club = models.CharField(max_length=120, choices=CLUBS, default='None')
    image = models.ImageField( default='default.jpg', upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)



    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = datetime.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Voter(models.Model):
        user = models.ForeignKey(User ,  on_delete=models.CASCADE)
        question = models.ForeignKey(Question, on_delete=models.CASCADE)