from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'avatar/user_{0}.jpg'.format(instance.tutor.username)

class Course(models.Model):
    course_code = models.CharField(max_length=8)
    course_name = models.CharField(max_length=20)
    def __str__(self):
        return self.course_code

class Tutor(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE) #extends User class
    private_tutor = models.BooleanField(default=False)
    time_per_slot = models.PositiveIntegerField(default=60)
    university = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=8)
    avatar = models.ImageField(upload_to=user_directory_path)
    introduction = models.TextField(max_length=100)
    hourly_rate = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    #course_taught = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_taught = models.ManyToManyField(Course)
    # not_available = models.ForeignKey(TutorNotAvailableSlot, on_delete=models.CASCADE) #Tutor with many not available timeslot
    def __str__(self):
        return self.tutor.get_username()

    def save(self, *args, **kwargs):
        if self.private_tutor:
            self.time_per_slot = 60
        elif not self.private_tutor:
            self.time_per_slot = 30
            self.hourly_rate = 0
        # Call the original save method
        super(Tutor, self).save(*args, **kwargs)

class NotAvailableSlots(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
