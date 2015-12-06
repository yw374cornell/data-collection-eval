import sys
import logging
from uuid import UUID

def setupPaths():
    sys.path.insert(0, "/Users/shankari/e-mission/e-mission-server/")    
    logging.getLogger().setLevel(logging.DEBUG)
    iphone_ids = [UUID("079e0f1a-c440-3d7c-b0e7-de160f748e35"), UUID("c76a0487-7e5a-3b17-a449-47be666b36f6"), UUID("c528bcd2-a88b-3e82-be62-ef4f2396967a")]
    android_ids = [UUID("e471711e-bd14-3dbe-80b6-9c7d92ecc296"), UUID("fd7b4c2e-2c8b-3bfa-94f0-d1e3ecbd5fb7"), UUID("86842c35-da28-32ed-a90e-2da6663c5c73")]
    phone_labels = ["ucb.sdb.ios.1", "ucb.sdb.ios.2", "ucb.sdb.ios.3", "ucb.sdb.android.1", "ucb.sdb.android.2", "ucb.sdb.android.3"]
    return (iphone_ids, android_ids, phone_labels)
   
def get_display_name(label):
    parts = label.split('.')
    return parts[2] + '.' + parts[3] 
