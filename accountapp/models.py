from django.db import models

# Create your models here.
# ctrl + d -> 이 함수가 있는 곳으로 감
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)