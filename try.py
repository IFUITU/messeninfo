
class Messezentren(models.Model):
    zentren_id = models.AutoField(primary_key=True)
    firma = models.CharField(max_length=255)
    firma_en = models.CharField(max_length=255, blank=True, null=True)
    firma_fr = models.CharField(max_length=255, blank=True, null=True)
    firma_es = models.CharField(max_length=255, blank=True, null=True)
    firma_ru = models.CharField(max_length=255, blank=True, null=True)
    firma_cn = models.CharField(max_length=255, blank=True, null=True)
    qid = models.CharField(max_length=255, blank=True, null=True)
    vorname = models.CharField(max_length=255, blank=True, null=True)
    nachname = models.CharField(max_length=255, blank=True, null=True)
    strasse = models.CharField(max_length=255)
    ort = models.IntegerField()
    plz = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    text_de = models.TextField(blank=True, null=True)
    text_en = models.TextField(blank=True, null=True)
    text_fr = models.TextField(blank=True, null=True)
    text_es = models.TextField(blank=True, null=True)
    text_ru = models.TextField(blank=True, null=True)
    text_cn = models.TextField(blank=True, null=True)
    land_id = models.PositiveIntegerField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    status_id = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    angelegt = models.DateTimeField()
    m_id = models.IntegerField(blank=True, null=True)
    hotel_update = models.DateTimeField(blank=True, null=True)
    hotel_anzahl = models.PositiveSmallIntegerField(blank=True, null=True)
    synono = models.TextField(blank=True, null=True)
    hallenm2 = models.IntegerField(blank=True, null=True)
    freim2 = models.IntegerField(blank=True, null=True)
    gesamtm2 = models.IntegerField(blank=True, null=True)
    hallenanzahl = models.IntegerField(blank=True, null=True)
    parkplatzanzahl = models.IntegerField(blank=True, null=True)
    flug1 = models.IntegerField(blank=True, null=True)
    flug2 = models.IntegerField(blank=True, null=True)
    flug3 = models.IntegerField(blank=True, null=True)
    flug4 = models.IntegerField(blank=True, null=True)
    flug5 = models.IntegerField(blank=True, null=True)
    flug6 = models.IntegerField(blank=True, null=True)
    flug7 = models.IntegerField(blank=True, null=True)
    verkehr1 = models.IntegerField(blank=True, null=True)
    verkehr2 = models.IntegerField(blank=True, null=True)
    verkehr3 = models.IntegerField(blank=True, null=True)
    verkehr4 = models.IntegerField(blank=True, null=True)
    verkehr5 = models.IntegerField(blank=True, null=True)
    anfahrt_de = models.TextField(blank=True, null=True)
    anfahrt_en = models.TextField(blank=True, null=True)
    anfahrt_fr = models.TextField(blank=True, null=True)
    anfahrt_es = models.TextField(blank=True, null=True)
    entfernung_innenstadt = models.IntegerField(blank=True, null=True)
    art_id = models.PositiveIntegerField(blank=True, null=True)
    hotelsuche = models.IntegerField(blank=True, null=True)
    anfahrt_cn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messezentren'