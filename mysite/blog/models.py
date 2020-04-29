from django.conf import settings
from django.db import models
from django.utils import timezone

# Post는 내가 이 모델의 이름을 Post로 하겠다는 클래스 네임
# 매개변수의 models는 Post가 장고 모델임을 의미. 장고가 Post는 데이터베이스에 저장되어야 한다고 알리는 역할
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
