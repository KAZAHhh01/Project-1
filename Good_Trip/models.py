from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    country = models.CharField(max_length=100,verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.TextField(blank=True,null=True,verbose_name='Адрес')

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('tour', 'Тур'),
        ('excursion', 'Экскурсия'),
        ('festival', 'Фестиваль'),
        ('hiking', 'Поход'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES,verbose_name='Тип события')
    location = models.ForeignKey(Location, on_delete=models.CASCADE,verbose_name='Локация')
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    Hotels_list = [
        ('Karlton', 'Карлтон'),
        ('Saluxe', 'Салюкс'),
        ('Hilton', 'Хилтон')
    ]
    hotels = models.CharField(max_length=20, choices= Hotels_list, verbose_name='Список отелей')
    start_date = models.DateTimeField(verbose_name='Дата заезда')
    end_date = models.DateTimeField(verbose_name='Дата выезда')

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets',verbose_name='Событие')
    name = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Цена')
    quantity_available = models.PositiveIntegerField(verbose_name='Доступное количество ')

    def __str__(self):
        return f"{self.name} — {self.event.name} ({self.price} сом)"

