'''
Created on 2015年9月23日

@author: AilenZou
'''
import django.forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.admin.widgets import AdminTextareaWidget
from django.conf import settings as G_SETTINGS
import os
import json

class UEditorWidget(django.forms.Textarea):
    def __init__(self, settings, **kwargs):
        self.settings = settings
        print("UEditorWidget.__init__.settings(%s)=%s" % (id(self), self.settings))
        super(UEditorWidget, self).__init__(**kwargs)
        
    class Media:
        css = {
               "all": (
                       
                       ),
               }
        js = (
              '/static/ueditor/ueditor.config.js',
              '/static/ueditor/ueditor.all.js',
              '/static/ueditor/lang/zh-cn/zh-cn.js',
              )

    def render(self, name, value, attrs=None):

        defaultSettings = getattr(G_SETTINGS, "UEDITOR_CONFIG", {})
        print("settings: %s" % self.settings)
        defaultSettings.update(self.settings)
        print("defaultSettings: %s" % defaultSettings)
        defaultSettings["serverUrl"] = os.path.join("/ueditor/upload", 
                                        defaultSettings.get("upload_to", ""))
        settingsStr = json.dumps(defaultSettings, ensure_ascii=False)
        print("settingsStr: %s" % settingsStr)
        editor = {
                  "id": "id_%s" % name.replace('-', '_'),
                  "name": name,
                  "value": value,
                  "width": defaultSettings.get("width", ""),
                  "height": defaultSettings.get("height", ""),
                }
        context = {
                   "editor": editor,
#                    "settings": {
#                                 "width": "600px",
#                                 "height": "400px",
#                                 "autoHeightEnabled": "false",
#                                 "serverUrl": "test.html",
#                                 },
                   "settings": settingsStr,
                   }
        html = mark_safe(render_to_string("ueditor.html", context))
        print("render: %s" % html)
        return html
    
class AdminUEditorWidget(AdminTextareaWidget, UEditorWidget):
    def __init__(self, **kwargs):
        UEditorWidget.__init__(self, **kwargs)