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
    dir = os.path.join(WORKPLACE, str(uid))
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
    os.mkdir(dir)
    return uid

