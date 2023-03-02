from django.contrib import admin
from .models import Church_Gallery, Church_Podcasts, Contact, Church_Event, Church_Sermon, Charity, Church_Pastors, Church_Event_Gallery
from .forms import ContactForm, CharityForm
# Register your models here.


class ChurchGalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image', )
    search_fields = ['title','image',]



class ChurchEventAdmin(admin.ModelAdmin):
    list_display = ('title','message', 'date',)
    search_fields = ['title','image','date',]



class ChurchPodcastAdmin(admin.ModelAdmin):
    list_display = ('title','audio_image', 'audio_file', 'date',)
    search_fields = ['title','audio_image', 'audio_file', 'date',]



class ChurchSermonAdmin(admin.ModelAdmin):
    list_display = ('title','video_link', 'date', 'image',)
    search_fields = ['title','image', 'date', 'image',]



class ChurchPastorAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'position', 'fb_account','twitter_account','ig_account',)
    search_fields = ['name','image','position','fb_account','twitter_account','ig_account',]



class ChurchEvent_GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'title','date',)
    search_fields = ['image1', 'title1','date',]


class CharityAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email','website','message')
    Donation = CharityForm
    search_fields = ['name','phone', 'email','amount']

class ContactAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email','website','message')
    contact = ContactForm
    search_fields = ['name', 'email','website','message']

admin.site.register(Church_Gallery,ChurchGalleryAdmin )
admin.site.register(Church_Event_Gallery,ChurchEvent_GalleryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Church_Podcasts, ChurchPodcastAdmin)
admin.site.register(Church_Event, ChurchEventAdmin)
admin.site.register(Church_Sermon, ChurchSermonAdmin)
admin.site.register(Charity, CharityAdmin)
admin.site.register(Church_Pastors, ChurchPastorAdmin)