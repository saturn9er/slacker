from datetime import date

from django.conf import settings
from django.db import models
from django.utils import timezone


class Room(models.Model):

    EMPTY = 'EPT'
    OCCUPIED = 'OCP'
    CLEANING = 'CLN'
    REPAIR = 'RPR'

    STATUS_CHOICES = (
        (EMPTY, 'Пусто'),
        (OCCUPIED, 'Занято'),
        (CLEANING, 'Уборка'),
        (REPAIR, 'Ремонт'),
    )

    name = models.CharField(
        max_length=6,
        unique=True,
    )

    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=EMPTY,
    )

    status_changed_at = models.DateTimeField()

    daily_price = models.FloatField()

    @property
    def daily_price_two_persons(self):
        return self.daily_price + 190

    @property
    def daily_price_three_persons(self):
        return self.daily_price + 190*2

    hourly_price = models.FloatField(
        null=True,
        blank=True,
    )

    @property
    def hourly_price_three_persons(self):
        if self.hourly_price:
            return self.hourly_price + 50

    bedding_configuration = models.ForeignKey(
        'BeddingConfiguration',
        on_delete=models.PROTECT
    )

    room_type = models.ForeignKey(
        'RoomType',
        on_delete=models.PROTECT,
    )

    current_accommodation = models.ForeignKey(
        'Accommodation',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='current_accommodation'
    )

    def __str__(self):
        return "%s (%s)" % (self.name, self.room_type)


class RoomType(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name


class BeddingConfiguration(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    capacity = models.PositiveSmallIntegerField(
        default=1,
    )

    def __str__(self):
        return self.name


class RoomNote(models.Model):
    content = models.TextField(
        max_length=1000,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "%s (%s)" % (self.room, self.created_at)


class Guest(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    SEX_CHOICES = (
        (MALE, 'муж.'),
        (FEMALE, 'жен.'),
        (OTHER, 'прочий')
    )

    last_name = models.CharField(
        max_length=50,
    )

    first_name = models.CharField(
        max_length=50,
    )

    patronymic = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    @property
    def fullname(self):
        if self.patronymic:
            return "%s %s %s" % (self.last_name, self.first_name, self.patronymic)
        else:
            return "%s %s" % (self.last_name, self.first_name)

    date_of_birth = models.DateField()

    @property
    def age(self):
        age = 0
        if self.date_of_birth:
            today = date.today()
            born = self.date_of_birth
            age = today.year - born.year - \
                ((today.month, today.day) < (born.month, born.day))
        return age

    place_of_birth = models.CharField(
        max_length=100,
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
    )

    citizenship = models.CharField(
        max_length=50
    )

    document_type = models.ForeignKey(
        'DocumentType',
        on_delete=models.PROTECT,
    )

    document_number = models.CharField(
        max_length=50
    )

    document_issued_by = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    document_issued_on = models.DateField(
        null=True,
        blank=True,
    )

    home_address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    first_visit = models.DateField(
        auto_now_add=True
    )

    last_visit = models.DateField(
        null=True
    )

    personal_card_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    personal_discount = models.FloatField(
        blank=True,
        null=True,
    )

    note = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('guests-detail', args=[str(self.pk)])

    def __str__(self):
        return self.fullname


class DocumentType(models.Model):
    name = models.CharField(
        max_length=70,
        unique=True,
    )

    def __str__(self):
        return self.name


class AccommodationQuerySet(models.QuerySet):
    def recent_by_room(self, room):
        return self.filter(room_id=room.id).order_by('-id')[:50]

class Accommodation(models.Model):
    HOURLY = 'H'
    DAILY = 'D'

    ACCOMMODATION_CHOICES = (
        (HOURLY, 'Почасовая'),
        (DAILY, 'Дневная')
    )
    accommodation_quantity = models.FloatField()
    check_in = models.DateTimeField(
        default=timezone.now
    )
    check_out = models.DateTimeField(
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.SET_NULL,
        null=True,
    )
    cost = models.FloatField(
        null=True,
        blank=True,
    )
    accommodation_type = models.CharField(
        max_length=1,
        choices=ACCOMMODATION_CHOICES,
        default=DAILY
    )
    guests = models.ManyToManyField(
        'Guest'
    )
    note = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('accommodation-detail', args=[str(self.pk)])


class Booking(models.Model):
    NOT_CONFIRMED = 'NC'
    CONFIRMED = 'CO'
    CANCELED = 'CN'
    NO_SHOW = 'NS'
    CHECKED_IN = 'CI'

    STATUS_CHOICES = (
        (NOT_CONFIRMED, 'Непотверждено'),
        (CONFIRMED, 'Подтверждено'),
        (CANCELED, 'Отменено'),
        (NO_SHOW, 'Не прибытие'),
        (CHECKED_IN, 'Заселен')
    )

    source = models.ForeignKey(
        'BookingSource',
        on_delete=models.SET_NULL,
        null=True
    )
    number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    room_type = models.ForeignKey(
        'RoomType',
        on_delete=models.SET_NULL,
        null=True,
    )
    number_of_guests = models.PositiveSmallIntegerField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_CONFIRMED
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(
        max_length=100
    )
    price = models.FloatField(
        blank=True,
        null=True
    )
    note = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('booking-edit', args=[str(self.pk)])


class BookingSource(models.Model):
    name = models.CharField(
        max_length=70,
        unique=True,
    )

    def __str__(self):
        return self.name


class Payment(models.Model):
    CASH = 'CASH'
    BANK_TRANSFER = 'BANK'
    POS = 'POS'

    PAYMENT_CHOICES = (
        (CASH, 'Наличные'),
        (BANK_TRANSFER, 'Банковский перевод'),
        (POS, 'Оплата картой')
    )

    payment_type = models.CharField(
        max_length=4,
        choices=PAYMENT_CHOICES,
        default=CASH,
    )

    accommodation = models.ForeignKey(
        'Accommodation',
        on_delete=models.SET_NULL,
        null=True,
    )
    amount = models.FloatField()
    made_on = models.DateTimeField(
        auto_now_add=True
    )
