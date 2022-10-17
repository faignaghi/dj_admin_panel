from django.contrib import admin

# Register your models here.
from .models import Product, Review
from django.utils import timezone


##5
class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)                 ### göster - gizlet
    # min_num = 3
    # max_num = 20
##5

##1
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ("create_date",)
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews")
    list_editable = ( "is_in_stock",)                           ### list_editable "editleme effekti verir"
    list_display_links = ("create_date", "update_date", )       ### list_display_links "link effekti verir"
    search_fields = ("name",)                                   ### search_fields "search etmek mumkun olur"
    prepopulated_fields = {'slug' : ('name',)}                  ### when adding product in admin site "slug yaradir"
    list_per_page = 15
    date_hierarchy = "update_date"
    inlines = (ReviewInline,)
    # fields = (('name', 'slug'), 'description', "is_in_stock")   ### fieldset kullandığımız zaman bunu kullanamayız "hansi fieldler yan-yana olsun"
    
    fieldsets = (
        ("General Fields", {
            "fields": (
                ('name', 'slug'), "is_in_stock" 
            ),
        }),
        ('Optionals Settings', {
            # "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )
    ##1

    ##2 
    actions = ("is_in_stock", "is_not_in_stock",)           ### actions'a "is_not_in_stock" sonradan elave etdim

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    
    

    def is_not_in_stock(self, request, queryset):
        count = queryset.update(is_not_in_stock=False)
        self.message_user(request, f"{count} çeşit ürün stokdan silindi")
    is_not_in_stock.short_description = 'İşaretlenen ürünleri stokdan sil'
##2
    
##3  
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
##3 

##4
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 
##4


##1
admin.site.register(Product, ProductAdmin,)
admin.site.register(Review,ReviewAdmin)


admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"

##1