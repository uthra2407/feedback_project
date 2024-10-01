from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    feedback_curriculum = models.TextField()
    feedback_delivery = models.TextField()
    feedback_methods = models.TextField()
    feedback_resources = models.TextField()
    feedback_evaluation = models.TextField()
    feedback_support = models.TextField()
    feedback_overall = models.TextField()

     


    def __str__(self):
        return f"{self.name} ({self.email})"
