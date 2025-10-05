# mypy: ignore-errors

from src.decorators import log


@log()
def get_dif(a, b):
    return a / b


def test_log_without_filename_without_error(capsys):
    get_dif(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "Успех! Имя функции : get_dif\nРезультат : 0.5\n"


def test_log_without_filename_with_error(capsys):
    get_dif(1, 0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Исключение!\nИмя функции : get_dif\nОшибка : division by zero\nВходные параметры : ((1, 0), {})\n"
    )


def test_log_in_file_no_error(tmp_path):
    file = tmp_path / "test_log.txt"

    @log(file)
    def get_dif(a, b):
        return a / b

    get_dif(1, 2)
    assert file.read_text(encoding="UTF-8") == "Успех! Имя функции : get_dif\nРезультат : 0.5\n"


def test_log_in_file_with_error(tmp_path):
    file = tmp_path / "test_log.txt"

    @log(file)
    def get_dif(a, b):
        return a / b

    get_dif(1, 0)
    assert (
        file.read_text(encoding="UTF-8")
        == "Исключение!\nИмя функции : get_dif\nОшибка : division by zero\nВходные параметры : ((1, 0), {})\n"
    )
