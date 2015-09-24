'''
Created on 2015年9月24日

@author: AilenZou
'''

from django.conf import settings as GLOBAL_SETTINGS
import os

MEDIA_ROOT = getattr(GLOBAL_SETTINGS, "MEDIA_ROOT", os.path.join(GLOBAL_SETTINGS.BASE_DIR + "ueditor_media"))
MEDIA_URL = getattr(GLOBAL_SETTINGS, "MEDIA_URL", "/ueditor/media")