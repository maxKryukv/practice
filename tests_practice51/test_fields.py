"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

import subprocess
import traceback
import sys
from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout_file = stdout
        self.stderr_file = stderr

    def __enter__(self):
        if self.stdout_file:
            self.old_stdout = sys.stdout
            sys.stdout = self.stdout_file
        if self.stderr_file:
            self.old_stderr = sys.stderr
            sys.stderr = self.stderr_file


    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if self.stdout_file:
            sys.stdout.close()
            sys.stdout = self.old_stdout
        if self.stderr_file:
            sys.stderr.write(traceback.format_exc())
            sys.stderr.close()
            sys.stderr = self.old_stderr


if __name__ == "__main__":
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')