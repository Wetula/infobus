from django.db import models


# Create your models here.


class Buses(models.Model):
    IS_IN_ORDER = (
        (1, 'Operuje'),
        (2, 'Nie operuje')
    )
    busname = models.IntegerField(db_column='busName', primary_key=True, verbose_name='Linia')
    inorder = models.IntegerField(db_column='inOrder', blank=True, null=True, choices=IS_IN_ORDER,
                                  verbose_name='Czy linia operuje?')

    class Meta:
        managed = True
        db_table = 'Buses'
        verbose_name = 'Linia'
        verbose_name_plural = 'Linie'

    def __str__(self):
        return str(self.busname)


class Routes(models.Model):
    idroute = models.AutoField(db_column='idRoute', primary_key=True, default=-1)
    busname = models.ForeignKey(Buses, models.DO_NOTHING, db_column='busName', blank=True, null=True,
                                verbose_name='Linia')
    stopnumber = models.IntegerField(db_column='stopNumber', blank=True, null=True, verbose_name='Numer przystanku')
    stopid = models.ForeignKey('Stops', models.DO_NOTHING, db_column='stopId', blank=True, null=True,
                               verbose_name='Nazwa przystanku')

    class Meta:
        managed = True
        db_table = 'Routes'
        verbose_name = 'Trasa'
        verbose_name_plural = 'Trasy'

    def __str__(self):
        s = ''
        s += str(self.busname)
        s += ' '
        s += str(self.stopid)
        return str(s)


class Stops(models.Model):
    idstops = models.IntegerField(db_column='idStops', primary_key=True)
    stopname = models.TextField(db_column='stopName', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Stops'
        verbose_name = 'Przystanek'
        verbose_name_plural = 'Przystanki'

    def __str__(self):
        return str(self.stopname)


class Times(models.Model):
    idtime = models.AutoField(db_column='idTime', primary_key=True, default=-1)
    stopid = models.ForeignKey(Stops, models.DO_NOTHING, db_column='stopId', blank=True, null=True)
    busname = models.ForeignKey(Buses, models.DO_NOTHING, db_column='busName', blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Times'
        verbose_name = 'Godzina odjazdu'
        verbose_name_plural = 'Godziny odjazdu'

    def __str__(self):
        s = ''
        s += str(self.stopid)
        s += ' '
        s += self.time.strftime('%H:%M')
        s += ' '
        s += str(self.busname)
        return str(s)
