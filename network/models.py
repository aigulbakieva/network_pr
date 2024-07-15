from django.db import models


class Seller(models.Model):
    TYPE = [("F", "завод"), ("RN", "розничная сеть"), ("IE", "ИП")]
    LEVEL = [("0", "0"), ("1", "1"), ("2", "2")]

    name = models.CharField(max_length=100, verbose_name="Название")
    type = models.CharField(max_length=50, choices=TYPE, verbose_name="Тип звена сети")
    contact = models.ForeignKey(
        "Contact", on_delete=models.CASCADE, verbose_name="Контакты"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Поставщик",
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
        verbose_name="Задолженность",
    )
    created_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    level = models.IntegerField(
        verbose_name="уровень звена", default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


class Contact(models.Model):
    email = models.EmailField(
        max_length=100, null=True, blank=True, verbose_name="Почта"
    )
    country = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Страна"
    )
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    street = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Улица"
    )
    building = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Дом"
    )

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.building}"

    class Mets:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    model = models.CharField(
        max_length=200, verbose_name="Модель", null=True, blank=True
    )
    date = models.DateField(
        null=True, blank=True, verbose_name="Дата выхода продукта на рынок"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
