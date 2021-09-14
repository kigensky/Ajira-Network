from django.db import models


GENDER_MALE = "male"
GENDER_FEMALE = "female"
GENDER_CHOICES = (
    (GENDER_MALE, "male"),
    (GENDER_FEMALE, "female"),
)

STATUS_PENDING = "pending"
STATUS_ACCEPTED = "accepted"
STATUS_REJECTED = "rejected"
STATUS_CHOICES = (
    (STATUS_PENDING, "pending"),
    (STATUS_ACCEPTED, "accepted"),
    (STATUS_REJECTED, "rejected"),
)


# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    expected_salary = models.IntegerField()
    will_relocate = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
        
# class CandidateJobMap(models.Model):
#     candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     job = models.ForeignKey("Jobs.Job", on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
#     feedback = models.TextField(blank=True, null=True)
    
#     def __str__(self):
#         return "{} - {}".format(self.Candidate.name, self.Job.position_name)
    