from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

#칼럼모양 '순번' '제목' '글쓴이' '날짜'
#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','auther','created_date']