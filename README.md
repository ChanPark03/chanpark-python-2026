# chanpark-python-2026

Python 학습 저장소입니다.

이 README는 짧은 소개 문서가 아니라, 공부한 주제를 다시 찾기 위한 **hyperlinked study map**입니다.
위에서 원하는 주제를 클릭하면 해당 설명과 관련 파일로 바로 이동할 수 있게 구성했습니다.

## Quick Table of Contents

- [Study Roadmap](#study-roadmap)
- [Repository Structure](#repository-structure)
- [Subject Index](#subject-index)
- [Environment](#environment)
- [Python Basics](#python-basics)
- [Data Types](#data-types)
- [Functions](#functions)
- [Class and OOP](#class-and-oop)
- [Files and Exceptions](#files-and-exceptions)
- [Serialization](#serialization)
- [Logging](#logging)
- [Recursion and Cache](#recursion-and-cache)
- [Generator and Iterator](#generator-and-iterator)
- [Decorator](#decorator)
- [Threading](#threading)
- [Asyncio and Requests](#asyncio-and-requests)
- [Data Analysis and Matplotlib](#data-analysis-and-matplotlib)
- [Native Extension Binding](#native-extension-binding)
- [Flask and GUI Notes](#flask-and-gui-notes)
- [More Study Topics](#more-study-topics)

## Study Roadmap

이 저장소는 아래 흐름으로 보면 좋습니다.

| Step | Topic | Main folder | Goal |
| --- | --- | --- | --- |
| 1 | Python 기본 문법 | [`python_example/basic`](python_example/basic) | 변수, 출력, 문자열, 조건문, 반복문, 자료형을 익힙니다. |
| 2 | 함수와 모듈 | [`python_example/basic`](python_example/basic) | 함수 정의, 인자, 패키지 import, 실행 인자를 이해합니다. |
| 3 | 객체 지향 | [`python_example/basic`](python_example/basic) | class, instance, method, inheritance, property를 익힙니다. |
| 4 | 파일과 데이터 | [`python_example/basic/data`](python_example/basic/data) | 파일 입출력, JSON, YAML, pickle, CSV를 다룹니다. |
| 5 | 고급 함수 문법 | [`python_example/basic`](python_example/basic) | recursion, cache, generator, iterator, decorator를 익힙니다. |
| 6 | 동시성 | [`python_example/basic`](python_example/basic) | threading, lock, asyncio, HTTP 요청 흐름을 비교합니다. |
| 7 | Native extension | [`python_example/native_extension`](python_example/native_extension) | C, C++, Rust 코드를 Python module로 연결합니다. |

## Repository Structure

| Path | Purpose |
| --- | --- |
| [`python_example/basic`](python_example/basic) | 수업에서 배운 Python 개념을 작은 파일 단위로 정리한 예제 모음입니다. |
| [`python_example/basic/data`](python_example/basic/data) | 파일 입출력, JSON, YAML, pickle, CSV 예제에서 사용하는 데이터 파일입니다. |
| [`python_example/basic/test_package`](python_example/basic/test_package) | 직접 만든 패키지를 import하는 연습용 패키지입니다. |
| [`python_example/native_extension`](python_example/native_extension) | C, C++, Rust로 만든 Python extension module 예제입니다. |

생성 파일은 학습 대상이 아닙니다. 예를 들어 `__pycache__/`, `target/`, `build/`, `.so`, `.pyd` 같은 파일은 실행 또는 빌드 중 만들어지는 결과물이므로 README의 주요 학습 파일로 다루지 않습니다.

## Subject Index

| Subject | Files | What to study |
| --- | --- | --- |
| [Environment](#environment) | README notes | conda, `.venv`, Docker, package manager |
| [Python Basics](#python-basics) | [a00_default.py](python_example/basic/a00_default.py), [a04_print.py](python_example/basic/a04_print.py), [a08_str_indexing.py](python_example/basic/a08_str_indexing.py), [a13_comparison.py](python_example/basic/a13_comparison.py) | 실행 흐름, 출력, 문자열, 비교 연산 |
| [Data Types](#data-types) | [a21_list.py](python_example/basic/a21_list.py), [a22_list_function.py](python_example/basic/a22_list_function.py), [a23_list_method.py](python_example/basic/a23_list_method.py), [a25_dictionary.py](python_example/basic/a25_dictionary.py) | list, tuple, dict, set, hash |
| [Functions](#functions) | [a31_function.py](python_example/basic/a31_function.py), [a32_argument.py](python_example/basic/a32_argument.py), [a33_default_argument.py](python_example/basic/a33_default_argument.py), [a35_variable_length_keyward_argument.py](python_example/basic/a35_variable_length_keyward_argument.py), [103_main_argument.py](python_example/basic/103_main_argument.py) | parameter, argument, return, `*args`, `**kwargs`, `sys.argv` |
| [Class and OOP](#class-and-oop) | [a63_class_student.py](python_example/basic/a63_class_student.py), [a64_class_method.py](python_example/basic/a64_class_method.py), [a65_isinstance.py](python_example/basic/a65_isinstance.py), [a66_special_method.py](python_example/basic/a66_special_method.py), [a70_property.py](python_example/basic/a70_property.py), [a71_class_inheritance.py](python_example/basic/a71_class_inheritance.py), [a72_multiple_inheritance.py](python_example/basic/a72_multiple_inheritance.py) | class, instance, method, special method, property, inheritance, MRO |
| [Files and Exceptions](#files-and-exceptions) | [a42_file_write.py](python_example/basic/a42_file_write.py), [a43_file_read.py](python_example/basic/a43_file_read.py), [a47_try_except.py](python_example/basic/a47_try_except.py) | file mode, `with`, standard stream, exception flow |
| [Serialization](#serialization) | [student_model.py](python_example/basic/student_model.py), [a97_pickle_load_student.py](python_example/basic/a97_pickle_load_student.py), [a98_dataclass.py](python_example/basic/a98_dataclass.py), [a101_json_serialization.py](python_example/basic/a101_json_serialization.py), [a102_yaml_serialization.py](python_example/basic/a102_yaml_serialization.py) | pickle, dataclass, JSON, YAML |
| [Logging](#logging) | [a104_logger_example.py](python_example/basic/a104_logger_example.py) | log level, format, file logging |
| [Recursion and Cache](#recursion-and-cache) | [a80_fibonacci.py](python_example/basic/a80_fibonacci.py), [a82_lru_cache.py](python_example/basic/a82_lru_cache.py) | recursive call, base condition, repeated work, `lru_cache` |
| [Generator and Iterator](#generator-and-iterator) | [a86_generator.py](python_example/basic/a86_generator.py), [a87_iteration.py](python_example/basic/a87_iteration.py) | `yield`, `next()`, `StopIteration`, `__iter__`, `__next__` |
| [Decorator](#decorator) | [a101_wrapper_function.py](python_example/basic/a101_wrapper_function.py), [a102_decorator.py](python_example/basic/a102_decorator.py), [a103_time_decorator.py](python_example/basic/a103_time_decorator.py) | wrapper, decorator, `@`, `@wraps`, runtime check |
| [Threading](#threading) | [a104_multithreading.py](python_example/basic/a104_multithreading.py) | `Thread`, `start()`, `join()`, `Lock`, GIL |
| [Asyncio and Requests](#asyncio-and-requests) | [a105_asyncio.tasks.py](python_example/basic/a105_asyncio.tasks.py), [a106_asyncio_http.py](python_example/basic/a106_asyncio_http.py), [a107_request.py](python_example/basic/a107_request.py) | coroutine, task, await, aiohttp, requests |
| [Data Analysis and Matplotlib](#data-analysis-and-matplotlib) | [a115_matplotlib.py](python_example/basic/a115_matplotlib.py), [ta_20260527093833.csv](python_example/basic/data/ta_20260527093833.csv) | CSV, pandas DataFrame, matplotlib plot |
| [Native Extension Binding](#native-extension-binding) | [a116_c_binding_example.py](python_example/basic/a116_c_binding_example.py), [a117_cpp_binding.py](python_example/basic/a117_cpp_binding.py), [a118_rust_binding.py](python_example/basic/a118_rust_binding.py) | CPython API, pybind11, PyO3, `.pyi`, `py.typed` |
| [Flask and GUI Notes](#flask-and-gui-notes) | README notes | Flask, native app, Electron, WebView, Tauri |

## Environment

Python 프로젝트는 실행 환경이 중요합니다. 같은 파일이어도 어떤 Python interpreter를 쓰는지, 어떤 패키지가 설치되어 있는지에 따라 결과가 달라질 수 있습니다.

Related files:

- [numpy_test.py](python_example/basic/numpy_test.py)

### conda

`conda`는 패키지 관리와 가상환경 관리를 함께 해주는 도구입니다.
프로젝트마다 독립된 Python 환경을 만들 수 있으므로 패키지 충돌을 줄일 수 있습니다.

공부할 때 중요한 점:

- 터미널에 `(base)`가 보여도 실제 `python`이 conda Python인지 확인해야 합니다.
- 가장 확실한 확인은 `python -c "import sys; print(sys.executable)"`입니다.
- `numpy`, `yaml`, `pandas`, `matplotlib`, `aiohttp` 같은 외부 패키지는 현재 활성화된 환경에 설치되어 있어야 합니다.

### `.venv`

`.venv`는 Python 표준 가상환경 폴더 이름으로 자주 사용됩니다.
프로젝트 루트에 `.venv`를 만들면 해당 프로젝트 전용 interpreter와 패키지를 둘 수 있습니다.

### Docker

Docker는 Python 실행 환경뿐 아니라 OS 수준의 환경까지 컨테이너로 묶을 수 있습니다.
가상환경보다 더 넓은 범위를 격리할 수 있지만, 학습 초기에는 conda나 `.venv`보다 설정이 복잡할 수 있습니다.

### uv and PyPI

`uv`, `pip`, `PyPI`는 Python 패키지를 설치하고 관리할 때 나오는 중요한 개념입니다.

- `PyPI`: Python 패키지 공식 저장소입니다.
- `pip`: PyPI 등에서 패키지를 설치하는 기본 도구입니다.
- `uv`: 빠른 Python 패키지 및 환경 관리 도구입니다.
- `setup.py`, `pyproject.toml`: 패키지를 빌드하거나 설치할 때 사용하는 설정 파일입니다.

## Python Basics

Python은 코드를 위에서 아래로 실행하는 interpreter 언어입니다.
변수 타입을 미리 선언하지 않아도 되고, 대부분의 값은 객체로 다뤄집니다.

Related files:

- [a00_default.py](python_example/basic/a00_default.py)
- [a02_keyward.py](python_example/basic/a02_keyward.py)
- [a04_print.py](python_example/basic/a04_print.py)
- [a08_str_indexing.py](python_example/basic/a08_str_indexing.py)
- [a13_comparison.py](python_example/basic/a13_comparison.py)
- [a19_range_enumerate.py](python_example/basic/a19_range_enumerate.py)

Key notes:

- `print()`는 값을 화면에 출력합니다.
- 문자열은 indexing과 slicing으로 일부를 꺼낼 수 있습니다.
- `if`, `elif`, `else`는 조건에 따라 실행 흐름을 나눕니다.
- `for`, `while`은 반복 실행에 사용합니다.
- `range()`는 반복 횟수나 숫자 범위를 만들 때 자주 사용합니다.
- `enumerate()`는 반복하면서 index와 값을 함께 받을 때 사용합니다.

주의할 점:

- Python의 논리 연산자는 C 스타일의 `&&`, `||`가 아니라 `and`, `or`입니다.
- `=`는 대입이고, `==`는 비교입니다.
- `is`는 값 비교가 아니라 객체 동일성 비교입니다.

### CPython and interpreter

CPython은 가장 널리 쓰이는 Python 구현체입니다. C 언어로 작성된 interpreter이고, Python 코드를 bytecode로 컴파일한 뒤 실행합니다.

이 저장소에서 C binding을 공부할 때 CPython을 알아야 하는 이유:

- [C extension source](python_example/native_extension/C_binding/simple_wrapper/simple_hello/_hello_core.c)는 `Python.h`를 include합니다.
- `PyObject`, `PyModuleDef`, `PyMethodDef` 같은 이름은 CPython API에서 나옵니다.
- Python에서 `import simple_hello`를 해도 내부적으로는 CPython이 native module을 로드합니다.

CPython 말고도 PyPy, Jython, IronPython 같은 구현체가 있지만, 일반적인 Python 수업과 대부분의 패키지는 CPython 기준으로 설명되는 경우가 많습니다.

### Keywords and operators

Python keyword는 언어가 이미 특별한 의미로 예약한 단어입니다.

| Keyword group | Examples | Meaning |
| --- | --- | --- |
| 조건 | `if`, `elif`, `else` | 조건에 따라 실행 흐름을 나눕니다. |
| 반복 | `for`, `while`, `break`, `continue` | 반복 실행과 반복 제어를 합니다. |
| 함수 | `def`, `return`, `lambda`, `yield` | 함수를 만들고 값을 반환하거나 generator를 만듭니다. |
| class | `class`, `self` 관례, `super` | 객체 지향 구조를 만듭니다. |
| 예외 | `try`, `except`, `raise`, `finally` | 오류 상황을 처리합니다. |
| import | `import`, `from`, `as` | module과 package를 가져옵니다. |
| scope | `global`, `nonlocal` | 변수 탐색 범위를 명시합니다. |

Operator는 값을 계산하거나 비교하는 기호입니다.

| Operator type | Examples | Note |
| --- | --- | --- |
| 산술 | `+`, `-`, `*`, `/`, `%`, `**` | `/`는 나눗셈, `**`는 거듭제곱입니다. |
| 비교 | `==`, `!=`, `<`, `>`, `<=`, `>=` | 결과는 `True` 또는 `False`입니다. |
| 논리 | `and`, `or`, `not` | C의 `&&`, `||`, `!`와 다릅니다. |
| 멤버십 | `in`, `not in` | 값이 container 안에 있는지 확인합니다. |
| 식별 | `is`, `is not` | 값이 아니라 같은 객체인지 확인합니다. |

## Data Types

Python의 자료형은 값을 어떤 형태로 보관하고 다룰지를 정합니다.
자료형을 잘 알아야 함수, 클래스, 파일 처리, API 응답 처리까지 자연스럽게 이어집니다.

Related files:

- [a21_list.py](python_example/basic/a21_list.py)
- [a22_list_function.py](python_example/basic/a22_list_function.py)
- [a23_list_method.py](python_example/basic/a23_list_method.py)
- [a25_dictionary.py](python_example/basic/a25_dictionary.py)
- [a30_list_comporehension.py](python_example/basic/a30_list_comporehension.py)

Main types:

| Type | Meaning | Main use |
| --- | --- | --- |
| `int` | 정수 | 개수, 순서, 계산 |
| `float` | 실수 | 평균, 비율, 소수 계산 |
| `str` | 문자열 | 이름, 문장, 파일 내용 |
| `bool` | 참/거짓 | 조건 판단 |
| `list` | 순서 있는 변경 가능 묶음 | 여러 값을 순서대로 저장 |
| `tuple` | 순서 있는 변경 불가능 묶음 | 바뀌면 안 되는 값 묶음 |
| `dict` | key-value 묶음 | 이름으로 값 찾기 |
| `set` | 중복 없는 묶음 | 중복 제거, 집합 연산 |

### list

`list`는 여러 값을 순서대로 저장합니다.

공부 포인트:

- index는 `0`부터 시작합니다.
- `append()`, `pop()`, `remove()`, `sort()` 같은 method를 사용합니다.
- list comprehension은 반복문과 조건문을 짧게 표현할 수 있습니다.

### tuple

`tuple`은 list와 비슷하지만 값을 직접 바꿀 수 없습니다.

공부 포인트:

- 함수에서 여러 값을 반환할 때 자주 사용합니다.
- 변경 불가능하기 때문에 dict key로 사용할 수 있습니다.
- 꼭 바꿔야 한다면 list로 변환한 뒤 다시 tuple로 만들 수 있습니다.

### dict

`dict`는 key로 value를 찾는 자료형입니다.

공부 포인트:

- `data["name"]`은 key가 없으면 오류가 납니다.
- `data.get("name")`은 key가 없어도 기본적으로 `None`을 반환합니다.
- `keys()`, `values()`, `items()`로 key, value, key-value 쌍을 순회할 수 있습니다.

### set

`set`은 중복을 허용하지 않는 자료형입니다.

공부 포인트:

- 중복 제거가 필요할 때 사용합니다.
- 순서가 중요한 자료형이 아니므로 index로 접근하지 않습니다.
- 합집합, 교집합, 차집합 같은 집합 연산을 할 수 있습니다.
- set의 원소는 hash 가능한 값이어야 합니다.

### hash

`hash()`는 객체를 식별하는 정수값을 만드는 함수입니다.

중요한 점:

- dict의 key와 set의 원소는 hash 가능한 값이어야 합니다.
- 문자열, 숫자, tuple처럼 변경 불가능한 값은 보통 hash 가능합니다.
- list, dict처럼 변경 가능한 값은 hash할 수 없습니다.
- 같은 내용의 불변 객체는 같은 hash 값을 가질 수 있습니다.

hash를 이해하면 dict가 key로 빠르게 값을 찾는 이유와, mutable 객체를 key로 쓰기 어려운 이유를 이해하기 좋습니다.

## Functions

함수는 반복되는 코드를 이름으로 묶는 방법입니다.
입력을 받고, 처리하고, 결과를 반환하는 단위로 생각하면 됩니다.

Related files:

- [a31_function.py](python_example/basic/a31_function.py)
- [a32_argument.py](python_example/basic/a32_argument.py)
- [a33_default_argument.py](python_example/basic/a33_default_argument.py)
- [a35_variable_length_keyward_argument.py](python_example/basic/a35_variable_length_keyward_argument.py)
- [103_main_argument.py](python_example/basic/103_main_argument.py)

### parameter and argument

- `parameter`: 함수를 정의할 때 받겠다고 적는 이름입니다.
- `argument`: 함수를 호출할 때 실제로 넣는 값입니다.

예시:

```python
def add(a, b):
    return a + b

add(2, 3)
```

여기서 `a`, `b`는 parameter이고, `2`, `3`은 argument입니다.

### `*args`

`*args`는 여러 개의 위치 인자를 tuple로 받습니다.

예를 들어 `func(1, 2, 3)`으로 호출하면 함수 안에서 `args == (1, 2, 3)`처럼 됩니다.
값이 하나여도 `args == (1,)`처럼 tuple입니다.

### `**kwargs`

`**kwargs`는 여러 개의 keyword argument를 dict로 받습니다.

예를 들어 `func(name="park", course="python")`으로 호출하면 함수 안에서 `kwargs == {"name": "park", "course": "python"}`처럼 됩니다.

### command line argument

[103_main_argument.py](python_example/basic/103_main_argument.py)는 `sys.argv`를 사용합니다.

- `sys.argv[0]`: 실행한 파일 이름
- `sys.argv[1:]`: 사용자가 터미널에서 넘긴 값
- `len(sys.argv)`: 인자 개수 확인

C 언어의 `argc`, `argv`와 비슷한 역할입니다.

### argparse

`argparse`는 터미널에서 받은 실행 인자를 더 구조적으로 처리할 때 사용하는 Python 표준 라이브러리입니다.

`sys.argv`는 인자 목록을 직접 보여주는 낮은 수준의 방식이고, `argparse`는 그 인자에 이름, 타입, 기본값, 도움말을 붙여서 프로그램의 command line interface를 만들 수 있게 해줍니다.

예를 들어 아래처럼 실행하는 프로그램을 만들고 싶을 때 유용합니다.

```bash
python app.py --name park --count 3 --verbose
```

기본 흐름:

```python
import argparse

parser = argparse.ArgumentParser(description="간단한 argparse 예제")
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--count", type=int, default=1)
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()

for _ in range(args.count):
    if args.verbose:
        print(f"hello, {args.name}!")
    else:
        print(args.name)
```

공부 포인트:

- `ArgumentParser(...)`는 인자 해석기를 만듭니다.
- `add_argument("--name")`은 사용자가 입력할 옵션을 등록합니다.
- `type=int`처럼 타입 변환을 지정할 수 있습니다.
- `default=1`처럼 값이 없을 때 사용할 기본값을 정할 수 있습니다.
- `required=True`는 반드시 입력해야 하는 옵션을 뜻합니다.
- `action="store_true"`는 `--verbose`처럼 값 없이 켜고 끄는 flag에 사용합니다.
- `parse_args()`는 실제 터미널 입력을 읽어서 `args.name`, `args.count`처럼 접근 가능한 객체로 바꿉니다.

`sys.argv`와 `argparse` 비교:

| Tool | Good for | Example |
| --- | --- | --- |
| `sys.argv` | 인자가 적고 구조가 단순할 때 | 파일명 하나 받기 |
| `argparse` | 옵션, 타입, 기본값, 도움말이 필요할 때 | `--name`, `--count`, `--verbose` |

정리하면, 처음에는 [103_main_argument.py](python_example/basic/103_main_argument.py)처럼 `sys.argv`로 실행 인자가 어떻게 들어오는지 이해하고, 그 다음에는 `argparse`로 실제 CLI 프로그램처럼 옵션을 설계하는 흐름으로 공부하면 좋습니다.

### Modules and packages

Python file 하나는 module이 될 수 있고, 여러 module을 폴더로 묶으면 package가 됩니다.

Related files:

- [a90_package_import.py](python_example/basic/a90_package_import.py)
- [test_package/__init__.py](python_example/basic/test_package/__init__.py)
- [test_package/module_a.py](python_example/basic/test_package/module_a.py)
- [test_package/module_b.py](python_example/basic/test_package/module_b.py)

공부 포인트:

- `import test_package`는 package 이름으로 접근합니다.
- `from test_package import package_func`는 특정 이름만 가져옵니다.
- `from test_package import *`는 `__all__`에 등록된 이름들을 가져옵니다.
- `__init__.py`는 package가 처음 import될 때 실행되는 파일입니다.
- package를 잘 나누면 파일이 많아져도 역할별로 코드를 관리할 수 있습니다.

## Class and OOP

class는 데이터와 행동을 함께 묶는 방법입니다.
객체를 만들면 각 객체가 자기 속성을 가지고, class 안에 정의된 method를 사용할 수 있습니다.

Related files:

- [a63_class_student.py](python_example/basic/a63_class_student.py)
- [a64_class_method.py](python_example/basic/a64_class_method.py)
- [a65_isinstance.py](python_example/basic/a65_isinstance.py)
- [a66_special_method.py](python_example/basic/a66_special_method.py)
- [a67_class_variable.py](python_example/basic/a67_class_variable.py)
- [a69_destructor.py](python_example/basic/a69_destructor.py)
- [a70_property.py](python_example/basic/a70_property.py)
- [a71_class_inheritance.py](python_example/basic/a71_class_inheritance.py)
- [a72_multiple_inheritance.py](python_example/basic/a72_multiple_inheritance.py)

### object and attribute

[a63_class_student.py](python_example/basic/a63_class_student.py)는 `Student` 객체를 만들고, 이름과 점수를 `self.name`, `self.korean` 같은 attribute로 저장합니다.

`self`는 현재 method를 호출한 객체 자신을 가리킵니다.
그래서 같은 class로 여러 객체를 만들어도 각 객체는 자기 데이터를 따로 가집니다.

### method

[a64_class_method.py](python_example/basic/a64_class_method.py)는 class 안에 `get_sum()`, `get_average()`, `to_string()` 같은 method를 둡니다.
객체가 자기 점수를 직접 계산하도록 만드는 구조입니다.

### `isinstance`

[a65_isinstance.py](python_example/basic/a65_isinstance.py)는 객체가 어떤 class에서 만들어졌는지 확인합니다.

```python
isinstance(student, Student)
```

이 코드는 `student`가 `Student` class의 instance이면 `True`입니다.

### special method

[a66_special_method.py](python_example/basic/a66_special_method.py)는 `__str__`, `__repr__`, `__add__`, `__sub__`, `__gt__` 같은 special method를 사용합니다.

공부 포인트:

- `print(obj)`가 어떤 문자열을 보여줄지 class에서 정할 수 있습니다.
- `obj1 + obj2` 같은 연산의 의미도 class에서 정할 수 있습니다.
- Python의 연산자는 내부적으로 special method를 호출합니다.

### class variable

[a67_class_variable.py](python_example/basic/a67_class_variable.py)의 `Student.count`처럼 class 전체가 공유하는 값이 class variable입니다.

- instance variable: 객체마다 따로 있음
- class variable: class 전체가 공유함

### destructor

[a69_destructor.py](python_example/basic/a69_destructor.py)는 `__del__()`을 확인합니다.
Python의 `del`은 객체를 직접 파괴하는 명령이라기보다, 이름과 객체의 연결을 끊는 명령에 가깝습니다.

중요한 자원 정리는 `__del__()`보다 `with` 문이나 명시적인 `close()`를 사용하는 편이 더 안전합니다.

### property

[a70_property.py](python_example/basic/a70_property.py)는 `@property`를 사용해 method를 attribute처럼 사용합니다.

공부 포인트:

- getter: 값을 읽을 때 실행
- setter: 값을 넣을 때 실행
- 잘못된 값이 들어오는 것을 setter에서 막을 수 있음

### inheritance and MRO

[a71_class_inheritance.py](python_example/basic/a71_class_inheritance.py)는 상속과 overriding을 보여줍니다.
[a72_multiple_inheritance.py](python_example/basic/a72_multiple_inheritance.py)는 다중 상속과 MRO를 보여줍니다.

MRO는 `Method Resolution Order`입니다.
다중 상속에서 Python이 어떤 순서로 method를 찾는지 보여줍니다.

## Files and Exceptions

파일 입출력과 예외 처리는 프로그램이 외부 데이터와 만날 때 꼭 필요합니다.

Related files:

- [a42_file_write.py](python_example/basic/a42_file_write.py)
- [a43_file_read.py](python_example/basic/a43_file_read.py)
- [a47_try_except.py](python_example/basic/a47_try_except.py)
- [data/text.txt](python_example/basic/data/text.txt)

### file write

[a42_file_write.py](python_example/basic/a42_file_write.py)는 파일에 문자열을 씁니다.

공부 포인트:

- `"w"`: 기존 내용을 지우고 새로 씀
- `"a"`: 기존 내용 뒤에 추가
- `with open(...) as f:`: 작업 후 파일을 자동으로 닫음
- `pathlib.Path`: 경로를 객체처럼 다룸

### file read

[a43_file_read.py](python_example/basic/a43_file_read.py)는 파일을 읽습니다.

공부 포인트:

- `"r"`: 읽기 모드
- `readline()`: 한 줄씩 읽기
- `while data := f.readline():`: 값을 읽으면서 조건에도 사용
- `sys.stdin`, `sys.stdout`, `sys.stderr`: 표준 입력, 출력, 에러

### exception

[a47_try_except.py](python_example/basic/a47_try_except.py)는 `try`, `except`, `else`, `finally` 구조를 사용합니다.

흐름:

1. `try`에서 오류가 날 수 있는 코드를 실행합니다.
2. 오류가 나면 맞는 `except`로 이동합니다.
3. 오류가 없으면 `else`가 실행됩니다.
4. 오류 여부와 상관없이 `finally`는 실행됩니다.

사용자 정의 예외를 만들 때는 보통 `class MyError(Exception):`처럼 `Exception`을 상속합니다.

## Serialization

Serialization은 Python 객체나 데이터를 파일에 저장 가능한 형태로 바꾸는 것입니다.
반대로 파일에서 다시 Python 데이터로 복원하는 과정을 deserialization이라고 볼 수 있습니다.

Related files:

- [student_model.py](python_example/basic/student_model.py)
- [a97_pickle_load_student.py](python_example/basic/a97_pickle_load_student.py)
- [a98_dataclass.py](python_example/basic/a98_dataclass.py)
- [a101_json_serialization.py](python_example/basic/a101_json_serialization.py)
- [a102_yaml_serialization.py](python_example/basic/a102_yaml_serialization.py)
- [data/test.pickle](python_example/basic/data/test.pickle)
- [data/test.json](python_example/basic/data/test.json)
- [data/test.yaml](python_example/basic/data/test.yaml)

### pickle

`pickle`은 Python 객체를 binary 형태로 저장합니다.

공부 포인트:

- `pickle.dump(obj, f)`: 객체를 파일에 저장
- `pickle.load(f)`: 파일에서 객체를 읽어 복원
- pickle 파일은 사람이 읽는 텍스트가 아닙니다.
- 믿을 수 없는 pickle 파일은 실행 중 위험할 수 있으므로 조심해야 합니다.

### dataclass

[a98_dataclass.py](python_example/basic/a98_dataclass.py)는 `@dataclass`를 사용합니다.

`dataclass`는 `__init__`, `__repr__` 같은 기본 method를 자동으로 만들어줍니다.
간단히 데이터를 담는 class를 만들 때 코드가 줄어듭니다.

### JSON and YAML

[a101_json_serialization.py](python_example/basic/a101_json_serialization.py)는 JSON을 읽고, [a102_yaml_serialization.py](python_example/basic/a102_yaml_serialization.py)는 YAML을 읽습니다.

- JSON은 API나 설정 파일에서 자주 사용됩니다.
- YAML은 사람이 읽기 쉬운 설정 파일에서 자주 사용됩니다.
- `json.load(f)`, `yaml.safe_load(f)`처럼 파일 객체에서 데이터를 읽습니다.

## Logging

Logging은 프로그램 실행 기록을 남기는 방법입니다.
`print()`는 잠깐 확인할 때 좋지만, 실제 디버깅이나 실행 기록 관리에는 `logging`이 더 적합합니다.

Related files:

- [a104_logger_example.py](python_example/basic/a104_logger_example.py)

[a104_logger_example.py](python_example/basic/a104_logger_example.py)는 2026-05-27에 추가된 logging 예제입니다.

공부 포인트:

- `logging.basicConfig()`로 로그 설정을 정합니다.
- `level=logging.INFO`는 INFO 이상 로그를 기록합니다.
- `logging.debug()`는 level이 INFO이면 출력되지 않습니다.
- `format="%(asctime)s [%(levelname)s] %(message)s"`처럼 시간, 레벨, 메시지를 함께 남길 수 있습니다.
- `filename="logger.log"`를 지정하면 화면이 아니라 파일에 로그를 남깁니다.
- `encoding="utf-8"`은 한글 로그가 깨지는 것을 막는 데 중요합니다.

정리:

- `print()`: 지금 눈으로 확인
- `logging`: 나중에 원인을 추적하기 위한 기록

## Recursion and Cache

재귀 함수는 함수가 자기 자신을 다시 호출하는 구조입니다.
재귀는 문제를 작게 나누어 풀 수 있지만, 종료 조건이 없으면 끝나지 않습니다.

Related files:

- [a80_fibonacci.py](python_example/basic/a80_fibonacci.py)
- [a82_lru_cache.py](python_example/basic/a82_lru_cache.py)

### Fibonacci recursion

[a80_fibonacci.py](python_example/basic/a80_fibonacci.py)는 재귀로 Fibonacci 수를 계산합니다.

핵심 흐름:

```python
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
```

종료 조건:

- `n == 1`
- `n == 2`

주의할 점:

- 단순 재귀 Fibonacci는 같은 값을 여러 번 다시 계산합니다.
- `cnt` 전역 변수로 함수가 몇 번 호출되는지 확인할 수 있습니다.
- `fibonacci(36)`처럼 숫자가 커지면 호출 횟수가 빠르게 늘어납니다.

### `lru_cache`

[a82_lru_cache.py](python_example/basic/a82_lru_cache.py)는 `@lru_cache(maxsize=None)`를 사용합니다.

공부 포인트:

- 이미 계산한 입력값의 결과를 저장합니다.
- 같은 입력이 다시 오면 함수를 다시 실행하지 않고 저장된 값을 반환합니다.
- Fibonacci처럼 같은 부분 문제가 반복되는 재귀에서 효과가 큽니다.
- `maxsize=None`은 캐시 크기 제한을 두지 않는다는 의미입니다.

비교:

| File | Behavior |
| --- | --- |
| [a80_fibonacci.py](python_example/basic/a80_fibonacci.py) | 같은 Fibonacci 값을 반복 계산합니다. |
| [a82_lru_cache.py](python_example/basic/a82_lru_cache.py) | 이미 계산한 값을 기억해서 호출 수를 줄입니다. |

## Generator and Iterator

Generator와 iterator는 값을 한 번에 모두 만들지 않고, 필요할 때 하나씩 꺼내는 흐름을 이해할 때 중요합니다.

Related files:

- [a86_generator.py](python_example/basic/a86_generator.py)
- [a87_iteration.py](python_example/basic/a87_iteration.py)

### generator

[a86_generator.py](python_example/basic/a86_generator.py)는 `yield`를 사용합니다.

핵심:

- `yield`가 들어간 함수는 generator function입니다.
- generator function을 호출하면 함수 본문이 바로 실행되지 않고 generator 객체가 만들어집니다.
- `next(generator)`를 호출할 때마다 다음 `yield`까지 실행됩니다.
- 더 이상 `yield`할 값이 없으면 `StopIteration`이 발생합니다.
- `for`문은 내부적으로 `next()`를 호출하고, 끝날 때 `StopIteration`을 처리합니다.

### iterator

[a87_iteration.py](python_example/basic/a87_iteration.py)는 직접 iterator class를 만듭니다.

필요한 method:

- `__iter__()`: iterator 객체 자신을 반환합니다.
- `__next__()`: 다음 값을 반환하거나 끝나면 `StopIteration`을 발생시킵니다.

공부 포인트:

- `Iterable`인지 확인할 때 `isinstance(obj, Iterable)`을 사용할 수 있습니다.
- for문에서 동작하려면 iterator protocol을 만족해야 합니다.

## Decorator

Decorator는 기존 함수를 직접 고치지 않고, 함수 실행 전후에 기능을 덧붙이는 방법입니다.
logging, 실행 시간 측정, 권한 검사, retry, call count 같은 공통 기능에 자주 사용됩니다.

Related files:

- [a101_wrapper_function.py](python_example/basic/a101_wrapper_function.py)
- [a102_decorator.py](python_example/basic/a102_decorator.py)
- [a103_time_decorator.py](python_example/basic/a103_time_decorator.py)

### wrapper function

[a101_wrapper_function.py](python_example/basic/a101_wrapper_function.py)는 decorator의 가장 기본 구조를 보여줍니다.

흐름:

1. 원래 함수 `print_hello`가 있습니다.
2. `simple_rapper(print_hello)`가 원래 함수를 받습니다.
3. 내부의 `wrapper()`가 실행 전 코드, 원래 함수, 실행 후 코드를 묶습니다.
4. 바깥에서는 `wrapper()`를 호출합니다.

핵심은 원래 함수를 직접 수정하지 않고 기능을 감싸는 것입니다.

### decorator with `@`

[a102_decorator.py](python_example/basic/a102_decorator.py)는 `@hi("hi")`처럼 값을 받는 decorator를 사용합니다.

이 문법은 아래 흐름과 비슷합니다.

```python
print_hello = hi("hi")(print_hello)
```

공부 포인트:

- 바깥 함수는 decorator 설정값을 받습니다.
- 중간 함수는 원래 함수를 받습니다.
- 안쪽 `wrapper(*args, **kwargs)`는 실제 호출 시 실행됩니다.
- `*args`, `**kwargs`로 원래 함수의 인자를 그대로 전달합니다.
- `@wraps(func)`는 원래 함수 이름과 metadata를 보존합니다.

### runtime decorator

[a103_time_decorator.py](python_example/basic/a103_time_decorator.py)는 함수를 여러 번 실행하고 평균 실행 시간을 계산합니다.

공부 포인트:

- `time.time()`으로 시작과 끝 시간을 잽니다.
- 여러 번 실행한 뒤 평균을 구합니다.
- decorator를 붙여도 원래 함수의 반환값을 유지하려면 `return result`가 필요합니다.

## Threading

Threading은 여러 작업을 동시에 진행하는 것처럼 실행하는 방법입니다.
I/O 대기 시간이 있는 작업이나 독립적인 작업을 나누어 실행할 때 유용합니다.

Related files:

- [a104_multithreading.py](python_example/basic/a104_multithreading.py)

[a104_multithreading.py](python_example/basic/a104_multithreading.py)는 2026-05-27에 추가된 threading 예제입니다.

공부 포인트:

- `threading.Thread(target=task, args=(...))`로 thread를 만듭니다.
- `t.start()`는 thread에서 실제 함수를 실행합니다.
- `t.join()`은 해당 thread가 끝날 때까지 main thread를 기다리게 합니다.
- 여러 thread가 같은 전역 변수 `total`을 바꾸면 race condition이 생길 수 있습니다.
- `threading.Lock()`과 `with lock:`을 사용하면 동시에 한 thread만 특정 코드를 실행하게 할 수 있습니다.
- GIL은 CPython에서 한 번에 하나의 thread만 Python bytecode를 실행하게 만드는 lock입니다.

정리:

- `start()`: thread 시작
- `join()`: thread 완료 대기
- `Lock`: 공유 데이터 보호
- GIL: Python thread가 CPU 작업에서 항상 빨라지지는 않는 이유 중 하나

## Asyncio and Requests

동기 요청과 비동기 요청은 실행 흐름이 다릅니다.
HTTP 요청처럼 기다리는 시간이 많은 작업에서는 async 구조가 유용할 수 있습니다.

Related files:

- [a105_asyncio.tasks.py](python_example/basic/a105_asyncio.tasks.py)
- [a106_asyncio_http.py](python_example/basic/a106_asyncio_http.py)
- [a107_request.py](python_example/basic/a107_request.py)

### asyncio task

[a105_asyncio.tasks.py](python_example/basic/a105_asyncio.tasks.py)는 `asyncio.create_task()`를 사용합니다.

공부 포인트:

- `async def`로 coroutine function을 정의합니다.
- `await`는 coroutine이 끝날 때까지 기다립니다.
- `asyncio.create_task()`는 coroutine을 task로 등록하여 동시에 진행되게 합니다.
- `asyncio.run(main())`은 async 프로그램의 진입점으로 자주 사용됩니다.

중요한 흐름:

1. `main()`이 실행됩니다.
2. `create_task()`로 `hello()` 작업 여러 개를 등록합니다.
3. 각 task가 `await asyncio.sleep()`에서 대기합니다.
4. 마지막에 `await t1`, `await t2`, `await t3`로 완료를 기다립니다.

### aiohttp

[a106_asyncio_http.py](python_example/basic/a106_asyncio_http.py)는 `aiohttp.ClientSession()`을 사용해 비동기 HTTP 요청을 보냅니다.

공부 포인트:

- `async with`는 비동기 context manager입니다.
- `await session.get(...)` 또는 `async with session.get(...)` 형태로 요청 흐름을 다룹니다.
- `await response.text()`는 응답 본문을 비동기로 읽습니다.

### requests

[a107_request.py](python_example/basic/a107_request.py)는 `requests.get()`을 사용하는 동기 HTTP 요청 예제입니다.

비교:

| File | Style | Main idea |
| --- | --- | --- |
| [a107_request.py](python_example/basic/a107_request.py) | synchronous | 요청이 끝날 때까지 다음 줄로 가지 않습니다. |
| [a106_asyncio_http.py](python_example/basic/a106_asyncio_http.py) | asynchronous | 기다리는 동안 다른 async task를 진행할 수 있습니다. |

## Data Analysis and Matplotlib

Python은 데이터 분석과 시각화에도 많이 사용됩니다.
CSV를 읽고 그래프로 나타내는 흐름은 데이터 처리의 기본입니다.

Related files:

- [a115_matplotlib.py](python_example/basic/a115_matplotlib.py)
- [ta_20260527093833.csv](python_example/basic/data/ta_20260527093833.csv)

[a115_matplotlib.py](python_example/basic/a115_matplotlib.py)는 2026-05-27에 추가된 pandas/matplotlib 예제입니다.

공부 포인트:

- `Path(...)`로 CSV가 있는 폴더를 표현합니다.
- `pd.read_csv(...)`로 CSV를 `DataFrame`으로 읽습니다.
- `skipinitialspace=True`는 쉼표 뒤 공백을 정리할 때 사용합니다.
- `df.info()`는 column, null 여부, dtype을 확인합니다.
- `plt.plot(df["timestamp"], df["average"])`는 날짜와 평균값으로 선 그래프를 그립니다.
- `plt.show()`는 그래프 창을 띄웁니다.

주의할 점:

- 이 예제의 경로는 WSL 기준 `/home/chan/chanpark-python-2026/...`로 작성되어 있습니다.
- 다른 환경에서 실행할 때는 상대 경로나 현재 프로젝트 루트 기준 경로로 조정해야 할 수 있습니다.

## Native Extension Binding

Native extension binding은 C, C++, Rust 같은 언어로 만든 코드를 Python에서 import해서 사용하는 방법입니다.
성능이 중요한 부분을 native language로 작성하고, Python에서는 편한 interface만 사용하는 구조를 만들 수 있습니다.

Related files:

- [a116_c_binding_example.py](python_example/basic/a116_c_binding_example.py)
- [a117_cpp_binding.py](python_example/basic/a117_cpp_binding.py)
- [a118_rust_binding.py](python_example/basic/a118_rust_binding.py)
- [C binding README](python_example/native_extension/C_binding/simple_wrapper/readme.md)
- [C extension source](python_example/native_extension/C_binding/simple_wrapper/simple_hello/_hello_core.c)
- [C extension setup.py](python_example/native_extension/C_binding/simple_wrapper/setup.py)
- [C++ binding README](python_example/native_extension/Cpp_binding/pybind11_hello/README.md)
- [C++ source](python_example/native_extension/Cpp_binding/pybind11_hello/src/cpp_hello.cpp)
- [C++ setup.py](python_example/native_extension/Cpp_binding/pybind11_hello/setup.py)
- [Rust binding README](python_example/native_extension/Rust_binding/pyo3_hello/README.md)
- [Rust source](python_example/native_extension/Rust_binding/pyo3_hello/src/lib.rs)
- [Rust Cargo.toml](python_example/native_extension/Rust_binding/pyo3_hello/Cargo.toml)
- [Rust pyproject.toml](python_example/native_extension/Rust_binding/pyo3_hello/pyproject.toml)

### C extension with CPython API

Folder:

- [`python_example/native_extension/C_binding/simple_wrapper`](python_example/native_extension/C_binding/simple_wrapper)

Main files:

- [_hello_core.c](python_example/native_extension/C_binding/simple_wrapper/simple_hello/_hello_core.c)
- [hello.py](python_example/native_extension/C_binding/simple_wrapper/simple_hello/hello.py)
- [setup.py](python_example/native_extension/C_binding/simple_wrapper/setup.py)
- [a116_c_binding_example.py](python_example/basic/a116_c_binding_example.py)

What happens:

- `_hello_core.c` uses `Python.h`.
- C functions are exposed as Python-callable functions.
- `PyMethodDef` lists functions that Python can call.
- `PyModuleDef` defines the module.
- `PyInit__hello_core()` creates the extension module.
- `setup.py` builds `simple_hello._hello_core`.
- Python wrapper files make the native function easier to use.

[a116_c_binding_example.py](python_example/basic/a116_c_binding_example.py) imports `simple_hello`, calls `print_hello()`, creates `Hello("park")`, and calls `greet()`.

### C++ binding with pybind11

Folder:

- [`python_example/native_extension/Cpp_binding/pybind11_hello`](python_example/native_extension/Cpp_binding/pybind11_hello)

Main files:

- [cpp_hello.cpp](python_example/native_extension/Cpp_binding/pybind11_hello/src/cpp_hello.cpp)
- [setup.py](python_example/native_extension/Cpp_binding/pybind11_hello/setup.py)
- [pyproject.toml](python_example/native_extension/Cpp_binding/pybind11_hello/pyproject.toml)
- [cpp_hello.pyi](python_example/native_extension/Cpp_binding/pybind11_hello/cpp_hello.pyi)
- [a117_cpp_binding.py](python_example/basic/a117_cpp_binding.py)

What happens:

- `pybind11` lets C++ functions and classes look like Python module members.
- `module.def("add", &add, ...)` exposes a C++ function.
- `py::class_<Hello>(module, "Hello")` exposes a C++ class as a Python class.
- `setup.py` builds the C++ extension.
- `.pyi` describes the API for Python type checkers and editors.

[a117_cpp_binding.py](python_example/basic/a117_cpp_binding.py) imports `cpp_hello`, calls `add(45, 34)`, creates `Hello("park")`, and calls `greet()`.

### Rust binding with PyO3 and maturin

Folder:

- [`python_example/native_extension/Rust_binding/pyo3_hello`](python_example/native_extension/Rust_binding/pyo3_hello)

Main files:

- [src/lib.rs](python_example/native_extension/Rust_binding/pyo3_hello/src/lib.rs)
- [Cargo.toml](python_example/native_extension/Rust_binding/pyo3_hello/Cargo.toml)
- [pyproject.toml](python_example/native_extension/Rust_binding/pyo3_hello/pyproject.toml)
- [rust_hello.pyi](python_example/native_extension/Rust_binding/pyo3_hello/rust_hello.pyi)
- [a118_rust_binding.py](python_example/basic/a118_rust_binding.py)

What happens:

- `#[pyfunction]` marks a Rust function as callable from Python.
- `#[pymodule]` defines the Python module.
- `wrap_pyfunction!` adds Rust functions to the Python module.
- `Cargo.toml` defines the Rust crate.
- `pyproject.toml` tells Python build tools to use `maturin`.
- `maturin develop` builds and installs the extension into the active Python environment.

[a118_rust_binding.py](python_example/basic/a118_rust_binding.py) imports `rust_hello`, calls `make_greeting("Python")`, and calls `add(10, 20)`.

### Binding file roles

| File | Role |
| --- | --- |
| `setup.py` | Python packaging/build script. C or C++ extension build settings can be defined here. |
| `pyproject.toml` | Modern Python build configuration. Build backend and project metadata are defined here. |
| `Cargo.toml` | Rust package configuration. Crate name, edition, dependency, crate type are defined here. |
| `.pyi` | Type stub file. It tells Python tools what functions/classes exist in a binary module. |
| `py.typed` | Marker file. It tells type checkers that the package includes typing information. |
| `.c`, `.cpp`, `.rs` | Native source code. These are the real C, C++, Rust implementation files. |

### Binding comparison

| Binding style | Main tool | Good for | Example |
| --- | --- | --- | --- |
| C extension | CPython API | Python 내부 구조를 직접 배우기 | [C binding](python_example/native_extension/C_binding/simple_wrapper) |
| C++ binding | pybind11 | C++ class/function을 Python처럼 노출 | [C++ binding](python_example/native_extension/Cpp_binding/pybind11_hello) |
| Rust binding | PyO3 + maturin | Rust 코드를 Python module로 빌드 | [Rust binding](python_example/native_extension/Rust_binding/pyo3_hello) |

## Flask and GUI Notes

기존 README에는 Flask와 desktop app 방식에 대한 짧은 비교 메모가 있었습니다. 이 저장소의 핵심 예제가 Python basic 중심이라 자세한 구현 파일은 많지 않지만, Python이 웹과 GUI 쪽으로 확장될 때 어떤 선택지가 있는지 알아두면 좋습니다.

### Flask

Flask는 Python으로 web server를 만들 때 사용하는 가벼운 web framework입니다.

공부 포인트:

- browser는 HTTP 요청을 보냅니다.
- Flask app은 route를 통해 요청을 받습니다.
- route 함수는 HTML, JSON, text 같은 응답을 반환합니다.
- Python 코드는 server에서 실행되고, browser는 결과를 받아 화면에 표시합니다.

Flask를 공부할 때 연결되는 Python 개념:

- 함수: route 함수는 결국 Python 함수입니다.
- decorator: `@app.route(...)`는 decorator 문법입니다.
- dict/list: JSON 응답을 만들 때 자주 사용합니다.
- file path: template, static file을 다룰 때 경로 개념이 필요합니다.
- exception/logging: server 오류를 추적할 때 필요합니다.

### Native app and WebView choices

Desktop app을 만들 때는 여러 방식이 있습니다.

| Approach | Main technologies | Note |
| --- | --- | --- |
| Native app | Windows `.NET`, Linux GTK/Qt/tkinter, macOS Cocoa/AppKit/SwiftUI | OS에 가까운 방식이라 성능과 통합성이 좋지만 platform별 지식이 필요합니다. |
| Electron | HTML, CSS, JavaScript, Chromium | web 기술로 desktop app을 만들 수 있지만 실행 크기가 커질 수 있습니다. |
| WebView2 | Windows WebView runtime | Windows에서 web UI를 native window 안에 넣을 때 사용합니다. |
| Tauri | Rust + WebView | Electron보다 가볍게 desktop app을 만들 수 있는 선택지입니다. |
| pywebview | Python + WebView | Python backend와 web frontend를 연결하는 실험에 좋습니다. |
| C++ WebView | C++ + platform WebView | 속도와 제어력은 좋지만 구현 난도가 올라갑니다. |

이 내용은 [Native Extension Binding](#native-extension-binding)과도 이어집니다. Python만으로 느리거나 platform 기능 접근이 어려운 부분은 C/C++/Rust 또는 native app 기술과 연결해서 해결할 수 있습니다.

## More Study Topics

다음 단계로 더 공부하면 좋은 주제입니다.

| Topic | Why it matters | Related files |
| --- | --- | --- |
| Package design | 예제 파일을 import 가능한 package로 정리하는 능력 | [test_package](python_example/basic/test_package) |
| Type hinting | 큰 프로젝트에서 함수 입력과 반환을 명확히 이해하기 | `.pyi`, `py.typed` files in [native_extension](python_example/native_extension) |
| Testing | 함수와 module의 결과를 자동으로 검증하기 | `pytest`, `unittest`, small function examples |
| Async networking | 여러 HTTP 요청을 효율적으로 처리하기 | [a106_asyncio_http.py](python_example/basic/a106_asyncio_http.py) |
| GUI and WebView | Python backend와 화면을 연결하기 | [Flask and GUI Notes](#flask-and-gui-notes) |
| Native performance | 느린 부분을 C/C++/Rust로 옮기기 | [Native Extension Binding](#native-extension-binding) |

## README Maintenance Notes

새 파일을 추가할 때는 아래 순서로 README도 같이 업데이트하면 찾기 쉽습니다.

1. [Subject Index](#subject-index)에 주제와 파일을 추가합니다.
2. 관련 topic section의 `Related files`에 링크를 추가합니다.
3. 파일이 C/C++/Rust binding이면 [Native Extension Binding](#native-extension-binding)에 build 흐름과 실행 파일을 추가합니다.
4. 생성 파일은 README 주요 목록에 넣지 않습니다.
