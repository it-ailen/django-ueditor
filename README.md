# django-ueditor
Integrated ueditor to Django with python3

Prerequisities:
  UEditor(http://ueditor.baidu.com/website/) PHP utf-8版(http://ueditor.baidu.com/build/build_down.php?n=ueditor&v=1_4_3_1-utf8-php)
  
  python3.5 (https://www.python.org/downloads/)
  
  django-1.8 (https://www.djangoproject.com/download/)

Usage:
  1. 下载此APP到django的根目录(目前还没有实现自动安装)
  2. settings:
  INSTALLED_APPS = (
    ...
   
  "djangoueditor",
)
  3. urls:
  urlpatterns = [
    ...

    url(r'^ueditor/', include("djangoueditor.urls")),
] 
  4. models:
  from djangoueditor.fields import UEditorField
  demo = UEditorField(upload_to="demodir", ...)

  5. configurations:
  in settings: 
UEDITOR_CONFIG = {
                  
"width": "500px",
                  
"height": "800px",
                 
 "enableContextMenu": False,
                  
"autoHeightEnabled": False,
                  
...
                  }

完整配置项请参考（http://fex.baidu.com/ueditor/#start-config）
  
