from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    """
    PropertyType Table will provide a list of the different types
    of Propertys that are for sale.
    """

    name = models.CharField(verbose_name=_("Property Name"), help_text=_("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Property Type")
        verbose_name_plural = _("Property Types")

    def __str__(self):
        return self.name


class PropertySpecification(models.Model):
    """
    The Property Specification Table contains Property
    specifiction or features for the Property types.
    """

    Property_type = models.ForeignKey(PropertyType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Property Specification")
        verbose_name_plural = _("Property Specifications")

    def __str__(self):
        return self.name


class Property(models.Model):
    """
    The Property table contining all Property items.
    """

    Property_type = models.ForeignKey(PropertyType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Property visibility"),
        help_text=_("Change Property visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Property")
        verbose_name_plural = _("Propertys")

    def get_absolute_url(self):
        return reverse("store:Property_detail", args=[self.slug])

    def __str__(self):
        return self.title


class PropertySpecificationValue(models.Model):
    """
    The Property Specification Value table holds each of the
    Propertys individual specification or bespoke features.
    """

    Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    specification = models.ForeignKey(PropertySpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Property specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Property Specification Value")
        verbose_name_plural = _("Property Specification Values")

    def __str__(self):
        return self.value


class PropertyImage(models.Model):
    """
    The Property Image table.
    """

    Property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="Property_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a Property image"),
        upload_to="properties/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Property Image")
        verbose_name_plural = _("Property Images")

