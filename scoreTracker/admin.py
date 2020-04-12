from django.contrib import admin

# Register your models here.
from .models import Ludo

@admin.register(Ludo)
class  Ziya(admin.ModelAdmin):
    list_display=['PlayerName','MatchesPlayed','TotalScore','Average']
