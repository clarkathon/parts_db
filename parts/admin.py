from django.contrib import admin
from parts.models import Part, Project, Board, Bom, Worker


class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']


class PartAdmin(admin.ModelAdmin):
    list_filter = ['number']
    search_fields = ['number']


class BoardAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']


class BomAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']


class WorkerAdmin(admin.ModelAdmin):
    list_filter = ['last']
    search_fields = ['last']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Bom, BomAdmin)
admin.site.register(Worker, WorkerAdmin)
