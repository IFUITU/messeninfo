# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminRegionen(models.Model):
    aid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    iso_land = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    de = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    en = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    es = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fr = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ru = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cn = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_regionen'


class Airports(models.Model):
    airport_id = models.AutoField(primary_key=True)
    db_id = models.IntegerField()
    art = models.CharField(max_length=100, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    iata = models.CharField(db_column='IATA', max_length=15, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    icao = models.CharField(db_column='ICAO', max_length=15, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    name_de = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    name_en = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    name_fr = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    name_es = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_cn = models.CharField(max_length=255, blank=True, null=True)
    anzahl_runways = models.IntegerField(blank=True, null=True)
    strasse = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    ort_id = models.IntegerField(blank=True, null=True)
    plz = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    tel = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    fax = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    url = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    text_de = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    text_en = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    text_fr = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    text_es = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    text_ru = models.TextField(blank=True, null=True)
    text_cn = models.TextField(blank=True, null=True)
    land_id = models.PositiveIntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    status_id = models.PositiveIntegerField(blank=True, null=True)
    status_entfernung = models.IntegerField(blank=True, null=True)
    status_pilot = models.IntegerField(blank=True, null=True)
    status_x = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    angelegt = models.DateTimeField(blank=True, null=True)
    geonameid = models.IntegerField(blank=True, null=True)
    land_iso = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    stadt = models.CharField(max_length=255, blank=True, null=True)
    var1 = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    var2 = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    sprit1 = models.CharField(db_column='Sprit1', max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    sprit2 = models.CharField(db_column='Sprit2', max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    sprit3 = models.CharField(db_column='Sprit3', max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    fis = models.PositiveIntegerField(db_column='FIS', blank=True, null=True)  # Field name made lowercase.
    fcat = models.PositiveIntegerField(blank=True, null=True)
    up_date = models.DateField(blank=True, null=True)
    hotel_update = models.DateTimeField(blank=True, null=True)
    hotel_anzahl = models.PositiveSmallIntegerField(blank=True, null=True)
    landegewicht = models.PositiveIntegerField(blank=True, null=True)
    pprlandegewicht = models.PositiveIntegerField(blank=True, null=True)
    pprtel = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    opening = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    zoom = models.PositiveSmallIntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    hotelsuche = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'airports'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)





class Btom(models.Model):
    messe_id = models.PositiveIntegerField()
    b_id = models.PositiveIntegerField()
    bsort = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btom'


class Country(models.Model):
    land_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=2)
    id2 = models.CharField(max_length=3)
    id3 = models.CharField(max_length=3)
    de = models.CharField(max_length=255)
    en = models.CharField(max_length=255)
    es = models.CharField(max_length=255)
    fr = models.CharField(max_length=255)
    cn = models.CharField(max_length=255, blank=True, null=True)
    cnsort = models.CharField(max_length=10, blank=True, null=True)
    ru = models.CharField(max_length=255, blank=True, null=True)
    wikilink = models.CharField(max_length=255, blank=True, null=True)
    qid = models.CharField(max_length=255, blank=True, null=True)
    continent = models.CharField(max_length=2)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class HauptRegionen(models.Model):
    rid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    iso_land = models.CharField(max_length=255, blank=True, null=True)
    de = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    en = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    es = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fr = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ru = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cn = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    iso_region = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    iso_3166_2 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    qid = models.CharField(max_length=255, blank=True, null=True)
    flaeche_km2 = models.IntegerField(blank=True, null=True)
    adminlevel2 = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    karte_oben = models.FloatField(blank=True, null=True)
    karte_unten = models.FloatField(blank=True, null=True)
    karte_links = models.FloatField(blank=True, null=True)
    karte_rechts = models.FloatField(blank=True, null=True)
    hoch_punkt_m = models.IntegerField(blank=True, null=True)
    tief_punkt_m = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'haupt_regionen'


class KleinRegionen(models.Model):
    kid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    iso_land = models.CharField(max_length=255, blank=True, null=True)
    de = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    en = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    es = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fr = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ru = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    cn = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    iso_region = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    iso_3166_2 = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    qid = models.CharField(max_length=255, blank=True, null=True)
    flaeche_km2 = models.IntegerField(blank=True, null=True)
    zuordnung_level0 = models.IntegerField(blank=True, null=True)
    adminlevel2 = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    karte_oben = models.FloatField(blank=True, null=True)
    karte_unten = models.FloatField(blank=True, null=True)
    karte_links = models.FloatField(blank=True, null=True)
    karte_rechts = models.FloatField(blank=True, null=True)
    hoch_punkt_m = models.IntegerField(blank=True, null=True)
    tief_punkt_m = models.IntegerField(blank=True, null=True)
    autoinsert = models.IntegerField(db_column='autoInsert', blank=True, null=True)  # Field name made lowercase.
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'klein_regionen'




class Messe(models.Model):
    messe_id = models.AutoField(primary_key=True)
    veranstalter_id = models.PositiveIntegerField()
    zentren_id = models.IntegerField(blank=True, null=True)
    gruendung = models.PositiveSmallIntegerField(blank=True, null=True)
    messe_logo = models.CharField(max_length=255, blank=True, null=True)
    messe_url = models.CharField(max_length=255)
    messe_tel = models.CharField(max_length=255, blank=True, null=True)
    messe_fax = models.CharField(max_length=255, blank=True, null=True)
    messe_land = models.PositiveIntegerField(blank=True, null=True)
    messe_ort = models.IntegerField(blank=True, null=True)
    messe_plz = models.CharField(max_length=255, blank=True, null=True)
    messe_email = models.CharField(max_length=255)
    messe_strasse = models.CharField(max_length=255, blank=True, null=True)
    messe_firma = models.CharField(max_length=255, blank=True, null=True)
    messe_adresse = models.TextField(blank=True, null=True)
    regional = models.PositiveIntegerField()
    empfehlung = models.PositiveIntegerField(blank=True, null=True)
    turnus_id = models.PositiveIntegerField(blank=True, null=True)
    zutritt_id = models.PositiveIntegerField(blank=True, null=True)
    zutritt_text_id = models.IntegerField(blank=True, null=True)
    zutritt_covid_id = models.PositiveIntegerField(blank=True, null=True)
    messe_angelegt = models.DateTimeField()
    messe_angelegt_von = models.PositiveIntegerField()
    messe_update = models.DateTimeField(blank=True, null=True)
    messe_termin_email = models.DateTimeField(blank=True, null=True)
    messe_status = models.CharField(max_length=1)
    eintritt_frei = models.IntegerField(blank=True, null=True)
    bemerkung = models.TextField(blank=True, null=True)
    google = models.IntegerField(blank=True, null=True)
    timetable = models.CharField(max_length=255)
    oeffnungurl = models.CharField(max_length=255, blank=True, null=True)
    messe_geprueft = models.DateTimeField(blank=True, null=True)
    freelancer_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messe'


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
    anfahrt_cn = models.TextField(blank=True, null=True)
    anfahrt_ru = models.TextField(blank=True, null=True)
    entfernung_innenstadt = models.IntegerField(blank=True, null=True)
    art_id = models.PositiveIntegerField(blank=True, null=True)
    hotelsuche = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messezentren'


class Staedte(models.Model):
    de = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    en = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    fr = models.CharField(max_length=255)
    es = models.CharField(max_length=255)
    ru = models.CharField(max_length=255, blank=True, null=True)
    cn = models.CharField(max_length=255, blank=True, null=True)
    cnsort = models.CharField(max_length=10, blank=True, null=True)
    geohoehe = models.IntegerField(blank=True, null=True)
    geobreite = models.IntegerField(blank=True, null=True)
    utc = models.IntegerField(blank=True, null=True)
    bundesland = models.CharField(max_length=255, blank=True, null=True)
    land_id = models.IntegerField()
    up_date = models.DateTimeField(blank=True, null=True)
    location_no = models.IntegerField(db_column='Location_No', blank=True, null=True)  # Field name made lowercase.
    zoom = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    einwohner = models.IntegerField(blank=True, null=True)
    gruendung = models.CharField(max_length=255, blank=True, null=True)
    einwohnerjahr = models.IntegerField(blank=True, null=True)
    flaeche = models.IntegerField(blank=True, null=True)
    wiki_page = models.IntegerField(blank=True, null=True)
    qid = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    autoinsert = models.IntegerField(db_column='autoInsert', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staedte'
