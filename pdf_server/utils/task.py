import app_config
import uuid
import os


WORKPLACE = app_config.WORKPLACE
assert os.path.exists(WORKPLACE)


def get_task_dir(uid: uuid.UUID, check_exist: bool = False) -> str:
    """
    获取某次任务的目录
    :param uid: id of the task
    :param check_exist: to sure the directory exist
    """
    dir = os.path.join(WORKPLACE, 'tasks', str(uid))
    exists = os.path.exists(dir)
    if exists:
        assert os.path.isdir(dir)

    if check_exist:
        assert exists

    return dir


def create_task() -> uuid.UUID:
    """
    使用uuid１，参考链接：https://juejin.im/post/6844903783219085319
    """
    uid = uuid.uuid1()
    dir = get_task_dir(uid)

    assert not os.path.exists(dir)
    os.makedirs(dir)
    return uid

def _get_absolute_path(uid: uuid.UUID, relative_path: str,check_exist: bool = False) -> str:
    """
    根据任务编号和相对路径，返回绝对路径，并在此之前可以校验文件是否存在
    :param uid: id of the task
    :param relative_path: relative path of the task
    :param check_exist: check wheather the file exist
    """
    task_dir = get_task_dir(uid, True)
    path = os.path.join(task_dir, relative_path)
    if check_exist:
        assert os.path.exists(path)
    return path


def get_pdf_path(uid: uuid.UUID, check_exist: bool=False) -> str:
    """
    返回pdf文件的路径
    :param uid: id of the task
    :param check_exist: check wheather the file exist
    """
    return _get_absolute_path(uid, 'report.pdf', check_exist)

def get_download_path(uid: uuid.UUID, filename:str, check_exist: bool=False) -> str:
    """
    返回可下载文件的路径，只有在指定任务的根目录的文件才可以被下载
    :param uid: id of the task
    :param filename: filename
    :param check_exist: check wheather the file exist
    """
    return _get_absolute_path(uid, filename, check_exist)


def get_template_path(uid: uuid.UUID, check_exist: bool=False) -> str:
    """
    返回模板文件的路径
    :param uid: id of the task
    :param check_exist: check wheather the file exist
    """
    return _get_absolute_path(uid, 'template.html', check_exist)

def get_report_html_path(uid: uuid.UUID, check_exist: bool=False) -> str:
    """
    返回report.html文件路径
    :param uid: id of the task
    :param check_exist: check wheather the file exist
    """
    return _get_absolute_path(uid, 'report.html', check_exist)

def prepare_assets(uid: uuid.UUID):
    """
    prepare some assets for the pdf generation
    Nothing to prepare currently
    :param uid: id of the task
    """
    fonts_path = _get_absolute_path(uid, 'fonts')
    os.symlink(app_config.FONTS_PATH, fonts_path)
