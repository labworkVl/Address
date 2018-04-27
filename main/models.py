from django.db import models

# Create your models here.


class DT(models.Model):
    date_create = models.DateTimeField()
    date_update = models.DateTimeField()

    class Meta:
        abstract = True


#class MyManager(models.Model):
        #    def get_queryset(self):
    #return super(MyManager, self).get_queryset().filter(name='sta')


class Street(models.Model):
    name = models.CharField(max_length=100)
    prim = models.CharField(max_length=100)
    #sta = MyManager()

    #vivod
    def __str__(self):
        return '%s' % (self.name, )

    # pereopredelyaem save
    def save(self, *args, **kwargs):
        super(Street, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'streets'


class Dom(models.Model):
    name = models.CharField(max_length=10)
    num = models.IntegerField()
    buk = models.CharField(max_length=5)
    prim = models.CharField(max_length=100)
    dom_street = models.ForeignKey(Street)

    class Meta:
        ordering = ['num', 'buk']
        verbose_name_plural = 'doma'


class Kw(models.Model):
    name = models.CharField(max_length=10)
    num = models.IntegerField()
    buk = models.CharField(max_length=5)
    prim = models.CharField(max_length=100)
    kw_dom = models.ForeignKey(Dom)

    class Meta:
        ordering = ['num', 'buk']
        verbose_name_plural = 'kws'
