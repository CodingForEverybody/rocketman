from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Menu


@modeladmin_register
class MenuAdmin(ModelAdmin):
    model = Menu
    menu_label = "Menus"
    menu_icon = "list-ul"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
