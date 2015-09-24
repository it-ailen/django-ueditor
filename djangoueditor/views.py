from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import djangoueditor.settings as UEDITOR_SETTINGS
from datetime import datetime
# Create your views here.

uploadSettings = {
                  #图片相关
                  "imageActionName": "uploadimage",
                  "imageMaxSize": 10485760,#10M
                  "imageFieldName": "upfile",
                  "imageUrlPrefix": "",
                  "imagePathFormat": "",
                  "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
                  }

def get_ueditor_settings(request, **kwargs):
    return HttpResponse(json.dumps(uploadSettings, ensure_ascii=False), 
                        content_type="application/javascript")

def upload_image(request, path=""):
    print("upload_image to path: %s" % path)
    if request.method == 'POST':
        uploadFieldName = uploadSettings["imageFieldName"]
        f = request.FILES.get(uploadFieldName, None)
        if f is None:
            return HttpResponse(json.dumps({"error": "missing file"}), 
                                content_type="application/javascript", status=400)
        baseName, ext = os.path.splitext(f.name)
        finalDir = os.path.join(UEDITOR_SETTINGS.MEDIA_ROOT, path)
        print("MEDIA_ROOT: (%s)%s %s" % (type(UEDITOR_SETTINGS.GLOBAL_SETTINGS.MEDIA_ROOT), UEDITOR_SETTINGS.GLOBAL_SETTINGS.MEDIA_ROOT, UEDITOR_SETTINGS.MEDIA_ROOT))
        print("finalDir: %s" % finalDir)
        if not os.path.exists(finalDir):
            os.makedirs(finalDir)
        finalFileName = "%s_%s%s" % (baseName, 
                            datetime.now().strftime("%Y%m%d%H%M%S"), ext)
        finalPath = os.path.join(finalDir, finalFileName)
        with open(finalPath, "wb") as fo:
            for chunk in f.chunks():
                fo.write(chunk)
        res = {
               "url": UEDITOR_SETTINGS.MEDIA_URL + "/" + path + "/" + finalFileName,
               "original": f.name,
               "type": ext[1:],
               "title": finalFileName,
               "state": "SUCCESS",
               "size": f.size,
               }
        return HttpResponse(json.dumps(res, ensure_ascii=False))
    return HttpResponse(status=405)

ACTION_MAP = {
              "config": get_ueditor_settings,
              "uploadimage": upload_image,
              }

@csrf_exempt
def ueditor_upload(request, **kwargs):
    action = request.GET.get("action", "config")
    method = ACTION_MAP.get(action, None)
    return method(request, **kwargs) if method else HttpResponse(json.dumps({}), content_type="application/javascript")
        