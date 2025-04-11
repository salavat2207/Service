from django.contrib import admin
from .models import Brand, DeviceType, Device_model, Feedback

admin.site.register(DeviceType)
admin.site.register(Brand)
admin.site.register(Device_model)
admin.site.register(Feedback)