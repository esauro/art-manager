from django.db import models

MOTIVOS_CHOICES = ((1, "Retirado"),
                   (2, "Vendido"),)


# Create your models here.
class Painting(models.Model):
    author = models.ForeignKey("Author")
    size = models.CharField(max_length=200, blank=True, null=True)
    technique = models.ForeignKey("Technique")
    title = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)
    date_in = models.DateField()
    date_out = models.DateField(blank=True, null=True)
    out_reasons = models.IntegerField(choices=MOTIVOS_CHOICES,
        blank=True, null=True)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="paints")
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.author)


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.surname)


class Technique(models.Model):
    technique = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.technique
