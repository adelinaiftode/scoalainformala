import simplejson as simplejson
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
import json


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '2. Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="shop/", null=True)

    # class Meta:
    #     verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="30" height="30" />' % self.image.url)


products = [
    {
        "title": "Senzor1",
        "price": "10",
        "category": "senzor de nivel",
        "image": "senzor1.jpg"
    },
    {
        "title": "Senzor2",
        "price": "8",
        "category": "senzor de nivel",
        "image": "senzor2.jpg"
    },
    {
        "title": "Senzor3",
        "price": "20",
        "category": "senzor de nivel",
        "image": "senzor3.jpg"
    },
    {
        "title": "Senzor4",
        "price": "30",
        "category": "senzor de presiune",
        "image": "senzor4.jpg"
    },
    {
        "title": "Senzor5",
        "price": "80",
        "category": "senzor de presiune",
        "image": "senzor5.jpg"
    },
    {
        "title": "Senzor6",
        "price": "100",
        "category": "senzor de debit",
        "image": "senzor6.jpg"
    },
    {
        "title": "Senzor7",
        "price": "200",
        "category": "senzor de debit",
        "image": "senzor7.jpg"
    },
    {
        "title": "Senzor8",
        "price": "400",
        "category": "senzor de debit",
        "image": "senzor8.jpg"
    }
]

category = [
    {
        "title": "Senzori de nivel",
        "products": [
            {
                "title": "Senzor1",
                "price": "10",
                "category": "senzor de nivel",
                "image": "senzor1.jpg"
            },
            {
                "title": "Senzor2",
                "price": "8",
                "category": "senzor de nivel",
                "image": "senzor2.jpg"
            },
            {
                "title": "Senzor3",
                "price": "20",
                "category": "senzor de nivel",
                "image": "senzor3.jpg"
            }
        ],
        "title": "Senzori de presiune",
        "products": [
            {
                "title": "Senzor4",
                "price": "30",
                "category": "senzor de presiune",
                "image": "senzor4.jpg"
            },
            {
                "title": "Senzor5",
                "price": "80",
                "category": "senzor de presiune",
                "image": "senzor5.jpg"
            }
        ],
        "title": "Senzori de debit",
        "products": [
            {
                "title": "Senzor6",
                "price": "100",
                "category": "senzor de debit",
                "image": "senzor6.jpg"
            },
            {
                "title": "Senzor7",
                "price": "200",
                "category": "senzor de debit",
                "image": "senzor7.jpg"
            },
            {
                "title": "Senzor8",
                "price": "400",
                "category": "senzor de debit",
                "image": "senzor8.jpg"
            }
        ]
    }
]
