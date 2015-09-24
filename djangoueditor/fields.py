'''
Created on 2015年9月23日

@author: AilenZou
'''
from django.db import models
from .widgets import UEditorWidget
from django.contrib.admin import widgets as admin_widgets
from djangoueditor.widgets import AdminUEditorWidget
# Create your models here.

class UEditorField(models.TextField):
    def __init__(self, **kwargs):
        self.ueditorSettings = kwargs.pop("ueditorSettings", {})
        self.upload_to = kwargs.pop("upload_to", "")
        self.ueditorSettings["upload_to"] = self.upload_to
        print("UEditorField.ueditorSettings=%s" % self.ueditorSettings)
        self.widget = UEditorWidget(settings=self.ueditorSettings)
        super(UEditorField, self).__init__(**kwargs)
        
    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        print("UEditorField.formfield.ueditorSettings=%s" % self.ueditorSettings)
        print("UEditorField.formfield.defaults=%s" % defaults)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminUEditorWidget(settings=self.ueditorSettings)
#             defaults['widget'] = self.widget
        return super(UEditorField, self).formfield(**defaults)