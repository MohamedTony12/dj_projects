
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    keyword = models.CharField(_("keyword"), max_length=150)
    slug = models.SlugField(_("slug"), max_length=150)
    parent = models.ForeignKey(
        "self", verbose_name="childern", null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=150)
    slug = models.SlugField(_("slug"), max_length=150)
    in_stock = models.BooleanField(_("in_stock"), default=True)
    date_add = models.DateTimeField(_("date add"), auto_now_add=True)
    update_at = models.DateTimeField(_("updated at"), auto_now=True)
    selling_price = models.FloatField(_("selling price"), default=0)
    discount_price = models.FloatField(_("discount price"), default=0)
    quantity = models.IntegerField(_("quantity"), default=1)
    warranty = models.CharField(
        _("warranty"), max_length=250, null=True, blank=True)
    policy = models.CharField(
        _("policy"), max_length=250, null=True, blank=True)
    keyword = models.CharField(_("keyword"), max_length=150)
    description = models.TextField(_("description"), null=True, blank=True)
    main_pic = models.ImageField(_("main image"), upload_to='product')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(_("main image"), upload_to='product')

    def __str__(self):
        return self.product.name


