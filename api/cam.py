import os

import requests


class CamApi:

    @staticmethod  # Метод который игнорирует инстантс класса
    def get_cam_info():
        return requests.get(os.environ["IP"] + "action/get?subject=devinfo",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_cam_system_info():
        return requests.get(os.environ["IP"] + "action/get?subject=devpara",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_cam_time_setting():
        return requests.get(os.environ["IP"] + "action/get?subject=systime",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_cam_smtp_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=smtp",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_cloud_plugin_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=dsslcloud",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_audio_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=audioenc",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_snap_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=snap",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_video_work_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=videowork",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_main_video_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=videoenc&stream=0",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_sub_video_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=videoenc&stream=1",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_osd_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=osd",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_image_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=videoimage",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_cam_image_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=cameraimage",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))

    @staticmethod
    def get_motion_detector_info():
        return requests.get(os.environ["IP"] + "/action/get?subject=alarm&type=2",
                            auth=(os.environ["LOGIN"], os.environ["PASSWORD"]))
