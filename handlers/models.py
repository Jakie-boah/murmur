from django.db import models

# Create your models here.
# admin 100

class MskContacts(models.Model):
    operator = models.CharField(verbose_name='Оператор', max_length=150)
    support = models.CharField(verbose_name='Тех. поддержка', max_length=150)
    work = models.CharField(verbose_name='Трудоустройство', max_length=150)
    bot_1 = models.CharField(verbose_name='Бот №1', max_length=150)
    bot_2 = models.CharField(verbose_name='Бот №2', max_length=150)
    bot_3 = models.CharField(verbose_name='Бот №3', max_length=150)
    bot_4 = models.CharField(verbose_name='Бот №4', max_length=150)
    bot_5 = models.CharField(verbose_name='Бот №5', max_length=150)
    bot_account = models.CharField(verbose_name='Бот-аккаунт', max_length=150)

    def __str__(self):
        return 'Контакты Москва'

    class Meta:
        verbose_name = 'Контакты Москва'
        verbose_name_plural = 'Контакты Москва'


class SpbContacts(models.Model):
    operator = models.CharField(verbose_name='Оператор', max_length=150)
    support = models.CharField(verbose_name='Тех. поддержка', max_length=150)
    work = models.CharField(verbose_name='Трудоустройство', max_length=150)
    bot_1 = models.CharField(verbose_name='Бот №1', max_length=150)
    bot_2 = models.CharField(verbose_name='Бот №2', max_length=150)
    bot_3 = models.CharField(verbose_name='Бот №3', max_length=150)
    bot_4 = models.CharField(verbose_name='Бот №4', max_length=150)
    bot_5 = models.CharField(verbose_name='Бот №5', max_length=150)

    def __str__(self):
        return 'Контакты Спб'

    class Meta:
        verbose_name = 'Контакты Спб'
        verbose_name_plural = 'Контакты Спб'


class MainUrl(models.Model):
    main_url = models.CharField(verbose_name='Ссылка на главной странице', max_length=150)

    def __str__(self):
        return 'Ссылка на главной странице'

    class Meta:
        verbose_name = 'Ссылка на главной странице'
        verbose_name_plural = 'Ссылка на главной странице'
