from django.db import models

# Create your models here.
class WalkingTrails(models.Model):
    category = models.CharField(max_length=50, verbose_name='카테고리')
    region = models.CharField(max_length=50,verbose_name='지역구')
    distance = models.CharField(max_length=50,verbose_name='거리')
    time_required = models.CharField(max_length=50,verbose_name='소요시간')
    _level = models.IntegerField(verbose_name='코스레벨')
    subway = models.CharField(max_length=255,verbose_name='연계 지하철')
    Transportation = models.CharField(max_length=5000,verbose_name='교통편')
    course_name = models.CharField(max_length=255,verbose_name='코스명')
    course_detail = models.CharField(max_length=5000,verbose_name='세부코스')
    _explain = models.CharField(max_length=5000,verbose_name='포인트설명')
    point_number = models.IntegerField(primary_key=True, verbose_name='포인트순번')
    point_name = models.CharField(max_length=255,verbose_name='포인트명칭')
    longitude = models.DecimalField(decimal_places=14,max_digits=17,verbose_name='경도')
    latitude  = models.DecimalField(decimal_places=14,max_digits=16,verbose_name='위도')
    class Meta:
        managed = False
        db_table = 'walkingtrails'

class Review():
    id = models.IntegerField(primary_key=True,verbose_name="리뷰 id")
    point_id = models.ForeignKey("WalkingTrails",related_name="walkingtrails", on_delete=models.CASCADE, db_column='point_id', verbose_name="산책로 id")
    # user_id = models.ForeignKey("User",related_name="user", on_delete=models.CASCADE, db_column='user_id', verbose_name="User id")
    content = models.TextField(null=True, verbose_name="내용")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    image = models.ImageField(null=True, verbose_name="이미지")
    point = (
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
    )
    dog=(
        ('가능'),
        ('불가능'),
    )

    objects = models.Manager()

    def __str__(self):
        pass
    class Meta:
        managed = False
        db_table = 'review'