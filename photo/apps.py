import sys
import threading

from django.apps import AppConfig

from photo import background_tasks


class PhotoConfig(AppConfig):
    name = 'photo'

    def ready(self):
        if "runserver" not in sys.argv:
            return True

        t = threading.Thread(target=background_tasks.scan_dir_to_record, name="bg-disk-photo-scanner")
        t.start()
