from django.db import models



class Reserves(models.Model):
  # 予約日
  day = models.DateField(verbose_name='予約日')
  # 予約時間
  time = models.DateTimeField(verbose_name="予約時間")

  class Meta:
        verbose_name_plural = '予約一覧'
        db_table = 'reserves'
  

