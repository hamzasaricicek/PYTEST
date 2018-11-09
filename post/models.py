from django.db import models
from django.urls import reverse


# Create your models here.
# "/post/{}".format(self.id)
class post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})


class Urunler(models.Model):
    UrunAdi = models.CharField(max_length=120, verbose_name='Ürün Adı')
    Urunkodu = models.CharField(max_length=120, verbose_name='Ürün Kodu')
