from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Category, Product, Review
from django.utils import timezone
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter


##5
class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 3
    classes = ('collapse',)                 ### göster - gizlet
    # min_num = 3                           ### min-max review alani
    # max_num = 20  
##5

##1
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ("create_date",)
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list")
    list_editable = ( "is_in_stock",)                                               ### list_editable "editleme effekti verir"
    list_filter = ("is_in_stock", "create_date", ("name", DropdownFilter))
    list_display_links = ("name", )                                                 ### list_display_links "link effekti verir"
    search_fields = ("name",)                                                       ### search_fields "search etmek mumkun olur"
    prepopulated_fields = {'slug' : ('name',)}                                      ### when adding product in admin site "slug yaradir"
    list_per_page = 15
    date_hierarchy = "update_date"
    inlines = (ReviewInline,)
    readonly_fields = ("bring_image",)
    # fields = (('name', 'slug'), 'description', "is_in_stock")                     ### fieldset kullandığımız zaman bunu kullanamayız "hansi fieldler yan-yana olsun"
    
    fieldsets = (
        ("General Fields", {
            "fields": (
                ('name', 'slug'), "is_in_stock" 
            ),
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories", "product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        })
    )
    ##1
    
    # filter_horizontal = ("categories", )      ### another example
    filter_vertical = ("categories", )          ### example
    

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
    
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    
    # def bring_image(self, obj):       ### def bring_image model'de istifade edende self, admin.py'da ise (self, obj) ve self'ler obj olur
    #     if obj.product_img:
    #             return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
    #     return mark_safe(f"<h3>{obj.name} has not image </h3>")
##3 

##4
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 
    list_filter = (('product', RelatedDropdownFilter),)
##4


##1
admin.site.register(Product, ProductAdmin,)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Category)



admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"

##1