from django.contrib import admin
from .models import memovocab_test1,profile,vocab,Student,Vocab2

# Register your models here.

@admin.register(memovocab_test1)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(profile)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(vocab)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Vocab2)
class AuthorAdmin(admin.ModelAdmin):
    pass


