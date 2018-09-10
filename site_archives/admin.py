# -*- coding: utf-8 -*-
from django import template
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin import helpers
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from background_task import background
from django.contrib.auth.models import User

from datetime import timedelta
import subprocess

# Register your models here.
from .models import Archive 

@background(queue='archive')
def do_archive(siteurl):
    p=subprocess.Popen(["httrack", "-w", siteurl, "-%v" , "-s0"], stdout=subprocess.PIPE,cwd=r"/code/archived_site/")    
#    logger.debug(p.communicate())

    # lookup user by id and send them a message
#    user = User.objects.get(pk=user.id)
#    user.email_user('Starting archiving', 'You have been notified that archiving is started')


def start_archiving(modeladmin, request, queryset):
    # Populate archiving_objects, with ids to export
    archiving_objects = queryset.values_list('id', flat=True)
    ct = ContentType.objects.get_for_model(queryset.model)
    model_class = ContentType.objects.get(id=ct.pk).model_class()
    model_fields = model_class._meta.fields
    
    for t in queryset:
    	do_archive(t.old_url)
    #do_archive(t.old_url,t.user)

    title = "Elenco siti da archiviare:"
    

    context = {
        "title": title,
        "archiving_objects": [archiving_objects],
        'queryset': queryset,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        'model_name': model_class._meta.verbose_name,
        'fields': model_fields,
    }
 
    # Display the confirmation page where you choose columns to export
    return render(request, 'admin/summary_archiving_sites.html', context)
start_archiving.short_description = "Start archiving site(s)"

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ( 'old_url', 'new_url','status','archive_online', 'short_desc','thumb')
    list_filter = ['status','archive_online']
    list_editable = ['archive_online']
    search_fields = ['old_url', 'new_url','short_desc','description']
    actions = ['start_archiving']

    def thumb(self, obj):
        return  render_to_string('thumb.html',{
        'image': obj.screenshot
    })

admin.site.add_action(start_archiving)
admin.site.register(Archive,ArchiveAdmin)

