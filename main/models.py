from PIL import Image #compress img!?!?
from io import BytesIO # cmpress
from django.core.files import File #new to compress uploading file !
from django.db import models

from messeninfo.helpers import upload_file_name


class Languages(models.Model):
    languages_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=2)
    site_domain = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/lang_img", blank=True, null=True)
    directory = models.CharField(max_length=32, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    language_charset = models.TextField()

    class Meta:
        managed = False
        db_table = 'languages'

    def __str__(self):
        return self.name

class b(models.Model):
    small_img = models.ImageField(upload_to="b_id", blank=True, null=True)
    big_img = models.ImageField(upload_to="b_id", blank=True, null=True)


class Branchen(models.Model):
    b = models.ForeignKey(b, on_delete=models.RESTRICT)
    sprach = models.ForeignKey(Languages, on_delete=models.RESTRICT)
    text = models.CharField(max_length=255)
    cnsort = models.CharField(max_length=10, blank=True, null=True)
    messe_text = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True, null=True)
    google = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'branchen'

    # def save(self,**kwargs):                         # to compress the img files!!
    #     if not self.small_img.closed:                #if img exists
    #         img = Image.open(self.small_img)               #open img via Pillow
    #         img.thumbnail((450,240),Image.ANTIALIAS) #compress px till 100 to 100 saves proporsion donot worry!
    #         tmp = BytesIO()                          #Buffer massive!
    #         img.save(tmp,"jpg")                      #save img to massive that created before! & and change type of file to png
    #         #tmp.seek(0)
    #         self.small_img = File(tmp,'t.jpg') #telling django upload to img new file tmp-file <<t>> does not metter because we have uploaded_file_name

    #     if not self.big_img.closed:
    #         img = Image.open(self.big_img)
    #         img.thumbnail((1900,400),Image.ANTIALIAS)
    #         tmp = BytesIO()
    #         img.save(tmp,"jpg")
    #         self.big_img = File(tmp,'t.jpg')

    #     return super().save(**kwargs)
