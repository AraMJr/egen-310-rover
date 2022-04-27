import test as test
from goprocam import GoProCamera, constants

gopro = GoProCamera.GoPro(constants.gpcontrol)

# TODO: Integrate and test GoPro


def initialize():
    try:
        gopro.power_on()
        gopro.KeepAlive()
        return True
    except Exception:
        return False


def shut_down():
    try:
        gopro.power_off()
        return True
    except Exception:
        return False


def take_photo():
    try:
        gopro.take_photo()
        return True
    except Exception:
        return False


def take_video():
    try:
        gopro.shoot_video()
        return True
    except Exception:
        return False


def save_last():
    try:
        gopro.getStatusRaw()
        gopro.downloadLastMedia("pic.JPG")
        return True
    except Exception:
        return False


if __name__ == "__main__":
    test.test(initialize(), True)
    test.test(take_photo(), True)
    test.test(take_video(), True)
    test.test(save_last(), True)
    test.test(shut_down(), True)
