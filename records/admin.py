from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Implement your custom logic here, for example:
        pass  # Do nothing to prevent actual deletion

    def has_delete_permission(self, request, obj=None):
        return False  # Disable the delete permission for individual records

    def has_delete_selected_permission(self, request, queryset=None):
        return False  # Disable the delete permission for bulk deletion

    def has_change_permission(self, request, obj=None):
        return False  # Disable the change permission for individual records

    def has_change_selected_permission(self, request, queryset=None):
        return False  # Disable the change permission for bulk changes

admin.site.register(Record, RecordAdmin)