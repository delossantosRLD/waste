from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(ClientInformation)
admin.site.register(BuyerInformation)
admin.site.register(RecycableMaterialsReport)
admin.site.register(FeedbackReport)
admin.site.register(PaymentMethod)
admin.site.register(PaymentInformation)