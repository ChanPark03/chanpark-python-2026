# chanpark-python-2026

Python studying repo  

## 가상환경

### conda

- 가상환경이란 프로젝트마다 독립된 Python 환경을 만들어주는 시스템입니다. 가상환경을 사용하면 프로젝트마다 필요한 패키지와 버전을 격리하여 관리할 수 있어, 패키지 충돌 문제를 방지할 수 있습니다.

- conda는 Anaconda에서 제공하는 패키지 관리 시스템이자 환경 관리 시스템입니다. conda를 사용하면 프로젝트마다 독립된 가상환경을 쉽게 만들고 관리할 수 있습니다.  

### `.venv`

- `.venv`는 Python의 표준 가상환경 디렉토리 이름입니다. 프로젝트 루트 디렉토리에 `.venv` 폴더를 만들어 가상환경을 관리할 수 있습니다. `.venv` 폴더 안에는 해당 프로젝트에서 사용하는 Python 인터프리터와 패키지들이 설치됩니다. `.venv`를 사용하면 프로젝트마다 독립된 환경을 유지할 수 있어, 패키지 충돌 문제를 방지할 수 있습니다.

### Docker

- Docker는 컨테이너화된 애플리케이션을 개발, 배포 및 실행하기 위한 플랫폼입니다. Docker를 사용하면 애플리케이션과 그 종속성을 컨테이너라는 격리된 환경에서 실행할 수 있습니다. Docker는 가상환경과 유사한 개념이지만, 더 가볍고 빠르게 실행됩니다. Docker를 사용하면 프로젝트마다 독립된 환경을 유지할 수 있어, 패키지 충돌 문제를 방지할 수 있습니다. Docker는 시스템 수준에서 격리된 환경을 제공하므로, 가상환경보다 더 강력한 격리를 제공합니다. 환경변수

## 파이썬이란

- 파이썬의 문법은 c언어를 기반으로 만들어졌다. 하지만 c언어보다 훨씬 간결하고 읽기 쉬운 문법을 가지고 있다. 파이썬은 인터프리터 언어로, 코드를 한 줄씩 실행할 수 있다. 또한, 동적 타이핑을 지원하여 변수의 타입을 명시적으로 선언할 필요가 없다. 파이썬은 다양한 라이브러리와 프레임워크를 제공하여, 웹 개발, 데이터 분석, 인공지능 등 다양한 분야에서 활용되고 있다.  

### cpython

- CPython은 파이썬의 가장 널리 사용되는 구현체입니다. CPython은 C 언어로 작성된 인터프리터로, 파이썬 코드를 바이트코드로 컴파일한 후 실행합니다. CPython은 파이썬의 표준 구현체로, 대부분의 파이썬 라이브러리와 프레임워크가 CPython을 지원합니다. CPython은 성능이 뛰어나며, 다양한 플랫폼에서 사용할 수 있습니다.

이외에도 pypy, jython, ironpython 등 다양한 파이썬 구현체가 존재합니다. 각 구현체는 특정 용도나 환경에 맞게 최적화되어 있으며, 개발자들은 프로젝트의 요구사항에 따라 적절한 구현체를 선택할 수 있습니다.

### 파이썬의 장점

- 자동화, 데이터분석, 웹, ai
- 문법이 간결하고 읽기 쉽다
- 동적 타이핑을 지원하여 변수의 타입을 명시적으로 선언할 필요가 없다
- 파이썬에서는 `primitive type`이 존재하지 않는다. 모든 것이 객체로 취급된다. 예를 들어, 숫자, 문자열, 리스트 등은 모두 객체로 간주된다. 이는 파이썬의 유연성과 편리성을 높여준다.
- C++의 `class`와 파이썬의 `class`는 다르다. 파이썬의 `class`는 C언어의 구조체와 유사하지만, 더 많은 기능과 유연성을 제공한다. 파이썬의 `class`는 메서드와 속성을 가질 수 있으며, 상속과 다형성을 지원한다. 또한, 파이썬의 `class`는 런타임에 동적으로 생성되고 수정될 수 있다. 이는 파이썬의 동적 타이핑과 결합하여, 개발자에게 더 많은 자유와 편리함을 제공한다.
- 다양한 라이브러리와 프레임워크를 제공하여, 다양한 분야에서 활용되고 있다.  

### 주요 자료형  

- `int` 정수  
- `float` 실수  
- `str` 문자열  
- `bool` 논리값
- `list` 리스트  
- `tuple` 튜플  
- `dict` 딕셔너리  
- `set` 집합  

### 키워드  

- `if`, `else`, `elif` 조건문  
- `for`, `while` 반복문
- `def` 함수 정의
- `class` 클래스 정의
- `import` 모듈 가져오기
- `return` 함수 반환
- `break` 반복문 종료
- `continue` 반복문 건너뛰기
- `pass` 아무것도 하지 않음
- `lambda` 익명 함수
- `try`, `except` 예외 처리
- `with` 컨텍스트 관리자
- `global` 전역 변수 선언
- `nonlocal` 중첩 함수에서 외부 변수 선언
- `assert` 조건이 참인지 검사
- `is` 객체 동일성 검사
- `finally` 예외 발생 여부와 상관없이 항상 실행되는 블록
- `||` 논리 OR 연산자
- `&&` 논리 AND 연산자
- `not` 논리 NOT 연산자
- `in` 멤버십 연산자
- `is` 객체 동일성 검사
- `raise` 예외 발생
- `yield` 제너레이터 함수에서 값을 반환하고 일시 중지
- `return` 함수 반환

### 오퍼레이터

- 덧셈 뺄셈 곱셈은 C와 같다. 나누기는 `/` 연산자를 사용한다. 나머지 연산자는 `%` 연산자를 사용한다. 거듭제곱 연산자는 `**` 연산자를 사용한다. 비교 연산자는 `==`, `!=`, `<`, `>`, `<=`, `>=`를 사용한다. 논리 연산자는 `and`, `or`, `not`을 사용한다. 비트 연산자는 `&`, `|`, `^`, `~`, `<<`, `>>`를 사용한다. 대입 연산자는 `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`를 사용한다. 멤버십 연산자는 `in`, `not in`을 사용한다. 식별 연산자는 `is`, `is not`을 사용한다.  
  
  ### 파라미터, argument  

  - 파라미터는 함수 정의에서 사용되는 변수로, 함수가 호출될 때 전달되는 값을 받는 역할을 합니다. 예를 들어, `def add(a, b):`에서 `a`와 `b`는 파라미터입니다. 함수가 호출될 때, 전달된 값이 파라미터에 할당되어 함수 내부에서 사용됩니다.
  - `argument`는 함수 호출 시 전달되는 실제 값입니다. 예를 들어, `add(2, 3)`에서 `2`와 `3`은 `argument`입니다. 파라미터와 `argument`는 함수의 입력과 출력을 관리하는 중요한 개념입니다.
  - 파라미터와 argument의 차이점은 파라미터는 함수 정의에서 사용되는 변수이고, argument는 함수 호출 시 전달되는 실제 값입니다. 파라미터는 함수 내부에서 사용되며, argument는 함수 외부에서 전달됩니다. 파라미터는 함수의 입력을 정의하는 역할을 하고, argument는 함수의 입력으로 전달되는 실제 값을 나타냅니다.
  
- 튜플은 변경 불가능한 시퀀스 자료형입니다. 튜플은 소괄호 `()`로 묶어서 정의하며, 여러 개의 값을 하나의 그룹으로 묶을 수 있습니다. 튜플은 리스트와 유사하지만, 리스트는 변경 가능하고 튜플은 변경 불가능합니다. 튜플은 주로 여러 개의 값을 반환하거나, 여러 개의 값을 하나의 변수에 저장할 때 사용됩니다. 예를 들어, `def get_coordinates(): return (x, y)`에서 `(x, y)`는 튜플입니다. 튜플은 리스트보다 메모리 효율적이며, 해시 가능한 자료형이므로 딕셔너리의 키로 사용할 수 있습니다.  
  
- `dict`는 키-값 쌍으로 데이터를 저장하는 자료형입니다. `dict`는 중괄호 `{}`로 묶어서 정의하며, 각 키와 값은 콜론 `:`으로 구분됩니다. `dict`는 리스트와 달리 순서가 없으며, 키는 고유해야 합니다. `dict`는 주로 데이터를 빠르게 검색하거나, 키를 사용하여 값을 저장하고 조회할 때 사용됩니다. 예를 들어, `person = {"name": "Alice", "age": 30}`에서 `"name"`과 `"age"`는 키이고, `"Alice"`와 `30`은 값입니다. `dict`는 다양한 메서드를 제공하여 데이터를 조작할 수 있습니다.

### 리스트  

- `list`는 순서가 있는 변경 가능한 시퀀스 자료형입니다. `list`는 대괄호 `[]`로 묶어서 정의하며, 여러 개의 값을 하나의 그룹으로 묶을 수 있습니다. `list`는 다양한 데이터 타입을 포함할 수 있으며, 중첩된 리스트도 가능합니다. `list`는 주로 데이터를 순차적으로 저장하거나, 여러 개의 값을 하나의 변수에 저장할 때 사용됩니다. 예를 들어, `numbers = [1, 2, 3, 4, 5]`에서 `[1, 2, 3, 4, 5]`는 리스트입니다. `list`는 다양한 메서드를 제공하여 데이터를 조작할 수 있습니다.  

### 모듈과 패키지  

- 모듈은 파이썬 코드가 저장된 파일입니다. 모듈은 함수, 클래스, 변수 등을 포함할 수 있으며, 다른 파이썬 코드에서 `import`하여 사용할 수 있습니다. 모듈을 사용하면 코드를 재사용하고, 코드의 구조를 개선할 수 있습니다. 예를 들어, `math` 모듈은 수학 관련 함수와 상수를 제공하는 모듈입니다. 패키지는 여러 개의 모듈을 포함하는 디렉토리입니다. 패키지는 `__init__.py` 파일을 포함하여 패키지로 인식됩니다. 패키지를 사용하면 관련된 모듈을 그룹화하여 관리할 수 있습니다. 예를 들어, `numpy` 패키지는 과학 계산에 필요한 다양한 모듈을 포함하는 패키지입니다.

### 메서드

- 메서드는 클래스의 함수입니다. 메서드는 클래스의 인스턴스에서 호출되며, 해당 인스턴스의 데이터를 조작하거나, 특정 동작을 수행하는 역할을 합니다. 메서드는 클래스 정의 내에서 정의되며, 첫 번째 매개변수로 `self`를 사용하여 인스턴스에 접근할 수 있습니다. 예를 들어, `class Person: def greet(self): print("Hello!")`에서 `greet`는 `Person` 클래스의 메서드입니다. 메서드는 객체 지향 프로그래밍에서 중요한 개념으로, 클래스의 행동을 정의하는 데 사용됩니다.

- 주요 메서드 `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, `clear()`, `copy()`, `setdefault()` 등이 있다. `keys()`는 딕셔너리의 모든 키를 반환하는 메서드입니다. `values()`는 딕셔너리의 모든 값을 반환하는 메서드입니다. `items()`는 딕셔너리의 모든 키-값 쌍을 반환하는 메서드입니다. `get()`은 딕셔너리에서 특정 키에 대한 값을 반환하는 메서드입니다. `update()`는 딕셔너리에 다른 딕셔너리의 키-값 쌍을 추가하는 메서드입니다. `pop()`은 딕셔너리에서 특정 키에 대한 값을 제거하고 반환하는 메서드입니다. `clear()`는 딕셔너리의 모든 항목을 제거하는 메서드입니다. `copy()`는 딕셔너리의 얕은 복사본을 반환하는 메서드입니다. `setdefault()`는 딕셔너리에 특정 키가 없으면 해당 키에 대한 값을 설정하고, 있으면 해당 값을 반환하는 메서드입니다.

- `hash()` 함수는 객체의 해시 값을 반환하는 내장 함수입니다. 해시 값은 객체를 고유하게 식별하는 정수입니다. 해시 값은 딕셔너리의 키로 사용될 수 있으며, 집합(`set`)의 요소로도 사용될 수 있습니다. 해시 값은 객체의 내용에 따라 결정되며, 동일한 내용의 객체는 동일한 해시 값을 가집니다. 예를 들어, `hash("hello")`는 문자열 `"hello"`의 해시 값을 반환합니다. 해시 함수는 객체의 불변성에 의존하므로, 변경 가능한 객체는 해시할 수 없습니다.

### 집합(set)

- `set`는 중복되지 않는 요소들의 모음입니다. `set`는 중괄호 `{}`로 묶어서 정의하며, 각 요소는 콤마로 구분됩니다. `set`는 순서가 없으며, 변경 가능한 자료형입니다. `set`는 주로 중복된 요소를 제거하거나, 집합 연산을 수행할 때 사용됩니다. 예를 들어, `unique_numbers = {1, 2, 3, 4, 5}`에서 `{1, 2, 3, 4, 5}`는 집합입니다. `set`는 다양한 메서드를 제공하여 데이터를 조작할 수 있습니다.

### 튜플

- `tuple`은 변경 불가능한 시퀀스 자료형입니다. `tuple`은 소괄호 `()`로 묶어서 정의하며, 여러 개의 값을 하나의 그룹으로 묶을 수 있습니다. `tuple`은 리스트와 유사하지만, 리스트는 변경 가능하고 `tuple`은 변경 불가능합니다. `tuple`은 주로 여러 개의 값을 반환하거나, 여러 개의 값을 하나의 변수에 저장할 때 사용됩니다. 예를 들어, `def get_coordinates(): return (x, y)`에서 `(x, y)`는 튜플입니다. `tuple`은 리스트보다 메모리 효율적이며, 해시 가능한 자료형이므로 딕셔너리의 키로 사용할 수 있습니다.  
- `tuple`을 리스트로 바꾼 다음 다시 `tuple`로 바꿔주는 방법이 있다. 예를 들어, `my_tuple = (1, 2, 3)`에서 `my_list = list(my_tuple)`로 튜플을 리스트로 변환한 후, `my_tuple = tuple(my_list)`로 다시 튜플로 변환할 수 있다. 이 방법은 튜플의 요소를 변경하거나 추가할 때 유용하다. 하지만, 이 방법은 성능에 영향을 줄 수 있으므로, 가능한 한 튜플을 직접 사용하는 것이 좋다.

## `uv`  

- `uv`는 Python 패키지 관리 도구입니다. `uv`를 사용하면 Python 패키지를 쉽게 설치하고 관리할 수 있습니다. `uv`는 `pip`와 유사한 기능을 제공하지만, 더 빠르고 효율적인 패키지 설치를 지원합니다. `uv`는 또한 가상환경을 자동으로 생성하고 관리할 수 있는 기능도 제공합니다. `uv`를 사용하면 프로젝트마다 독립된 환경을 유지할 수 있어, 패키지 충돌 문제를 방지할 수 있습니다. `uv`는 다양한 플랫폼에서 사용할 수 있으며, Python 개발자들 사이에서 인기를 얻고 있습니다.  
  
- 사용방법  
  - `uv install 패키지명`: 패키지를 설치하는 명령어입니다. 예를 들어, `uv install numpy`는 `numpy` 패키지를 설치합니다.
  - `uv uninstall 패키지명`: 패키지를 제거하는 명령어입니다. 예를 들어, `uv uninstall numpy`는 `numpy` 패키지를 제거합니다.
  - `uv list`: 현재 설치된 패키지 목록을 보여주는 명령어입니다.
  - `uv update 패키지명`: 패키지를 최신 버전으로 업데이트하는 명령어입니다. 예를 들어, `uv update numpy`는 `numpy` 패키지를 최신 버전으로 업데이트합니다.
  - `uv create 가상환경명`: 새로운 가상환경을 생성하는 명령어입니다. 예를 들어, `uv create myenv`는 `myenv`라는 이름의 가상환경을 생성합니다.
  - `uv activate 가상환경명`: 가상환경을 활성화하는 명령어입니다. 예를 들어, `uv activate myenv`는 `myenv` 가상환경을 활성화합니다.
  - `uv deactivate`: 현재 활성화된 가상환경을 비활성화하는 명령어입니다.  
  
## `pypi`

- `pypi`는 Python Package Index의 약자로, Python 패키지의 공식 저장소입니다. `pypi`에는 수많은 Python 패키지가 등록되어 있으며, 개발자들은 `pypi`를 통해 패키지를 검색하고 설치할 수 있습니다. `pypi`는 `pip`와 같은 패키지 관리 도구를 사용하여 패키지를 설치할 때 기본적으로 참조되는 저장소입니다. `pypi`에 등록된 패키지는 다양한 분야에서 활용되고 있으며, Python 개발자들 사이에서 중요한 리소스입니다.

- `setup.py`는 Python 패키지를 배포하기 위한 설정 파일입니다. `setup.py` 파일에는 패키지의 이름, 버전, 설명, 저자 정보, 라이선스, 의존성 등 패키지에 대한 메타데이터가 포함됩니다. `setup.py` 파일을 사용하여 패키지를 빌드하고 배포할 수 있습니다. 예를 들어, `python setup.py sdist` 명령어를 사용하여 소스 배포판을 생성할 수 있습니다. `setup.py` 파일은 Python 패키지의 배포와 관리를 위한 중요한 도구입니다.  

- `pypi` 계정을 만들어야 한다.

## 클래스와 객체  

- 클래스는 객체를 생성하기 위한 청사진입니다. 클래스는 속성과 메서드를 정의하여 객체의 상태와 행동을 나타냅니다. 객체는 클래스의 인스턴스로, 클래스에서 정의된 속성과 메서드를 사용할 수 있습니다. 예를 들어, `class Person: def __init__(self, name, age): self.name = name self.age = age def greet(self): print(f"Hello, my name is {self.name} and I am {self.age} years old.")`에서 `Person`은 클래스이고, `name`과 `age`는 속성이며, `greet`는 메서드입니다. `person1 = Person("Alice", 30)`에서 `person1`은 `Person` 클래스의 객체입니다. 객체 지향 프로그래밍에서는 클래스를 사용하여 코드의 재사용성과 유지보수성을 높일 수 있습니다.  

- `self`는 클래스의 인스턴스 메서드에서 첫 번째 매개변수로 사용되는 예약어입니다. `self`는 해당 메서드가 호출된 객체를 참조하는 역할을 합니다. `self`를 사용하여 클래스의 속성과 메서드에 접근할 수 있습니다. 예를 들어, `class Person: def __init__(self, name): self.name = name def greet(self): print(f"Hello, my name is {self.name}.")`에서 `self.name`은 해당 객체의 `name` 속성을 참조합니다. `self`는 클래스의 인스턴스 메서드에서 반드시 첫 번째 매개변수로 사용되어야 하며, 다른 이름으로 사용할 수도 있지만, 관례적으로 `self`를 사용하는 것이 일반적입니다.  
- `__init__` 메서드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 메서드입니다. `__init__` 메서드는 클래스의 속성을 초기화하는 역할을 합니다. 예를 들어, `class Person: def __init__(self, name, age): self.name = name self.age = age`에서 `__init__` 메서드는 `name`과 `age` 속성을 초기화합니다. `__init__` 메서드는 클래스의 인스턴스를 생성할 때 필요한 매개변수를 받아서 객체의 상태를 설정하는 데 사용됩니다. `__init__` 메서드는 클래스의 인스턴스가 생성될 때 자동으로 호출되므로, 객체를 생성할 때 필요한 초기화 작업을 수행할 수 있습니다.  
- `__init__` 함수는 생성자가 아니다.  
- `attribute`는 클래스의 속성을 나타내며, `method`는 클래스의 행동을 나타냅니다. `attribute`는 클래스의 인스턴스에서 데이터를 저장하는 데 사용되며, `method`는 클래스의 인스턴스에서 특정 동작을 수행하는 데 사용됩니다. 예를 들어, `class Person: def __init__(self, name): self.name = name def greet(self): print(f"Hello, my name is {self.name}.")`에서 `name`은 `attribute`이고, `greet`는 `method`입니다. `attribute`와 `method`는 객체 지향 프로그래밍에서 중요한 개념으로, 클래스를 정의할 때 함께 사용됩니다.  

### 객체 생성과 속성 저장

- `a63_class_student.py`에서는 `Student` 클래스를 만들고 학생의 이름, 국어, 수학, 영어, 과학 점수를 객체의 속성으로 저장합니다. `self.name`, `self.korean`처럼 `self`를 사용하면 각각의 객체가 자기 자신의 데이터를 따로 보관할 수 있습니다.
- `students` 리스트에는 `Student` 객체 여러 개가 저장됩니다. 반복문에서 `student.name`, `student.korean`처럼 객체의 속성에 접근하여 학생 정보를 출력합니다.

### 인스턴스 메서드와 객체 출력

- `a64_class_method.py`에서는 클래스 안에 `get_sum()`, `get_average()`, `to_string()` 같은 메서드를 추가하여 객체가 자기 점수를 직접 계산하도록 만듭니다. `get_sum()`은 네 과목 점수의 합계를 구하고, `get_average()`는 총점을 `4`로 나누어 평균을 구합니다.
- `__repr__()`은 객체를 출력할 때 보여줄 문자열을 정하는 특수 메서드입니다. `print(student)`를 실행하면 객체 주소 대신 학생 이름, 점수, 총점, 평균이 보기 좋게 출력됩니다.

### 객체 타입 확인

- `a65_isinstance.py`에서는 `isinstance(객체, 클래스)`를 사용하여 어떤 객체가 특정 클래스의 인스턴스인지 확인합니다. `isinstance(student, Student)`는 `student`가 `Student` 객체이면 `True`를 반환합니다.
- `classroom` 리스트에는 `Student` 객체와 `Teacher` 객체가 함께 들어 있습니다. 반복문에서 `isinstance()`로 객체의 종류를 구분한 뒤, `Student`이면 `study()`, `Teacher`이면 `teach()`를 실행합니다.
- 파이썬에서는 `int`, `list` 같은 기본 자료형도 모두 `object`를 기반으로 만들어진 객체입니다. 그래서 `isinstance(1, object)`, `isinstance([1, 2, 3], object)`도 `True`가 됩니다.

### 특수 메서드와 연산자 오버로딩

- `a66_special_method.py`에서는 `__str__()`, `__repr__()`, `__add__()`, `__sub__()`, `__mul__()`, `__truediv__()`, `__gt__()` 같은 특수 메서드를 사용하여 객체의 출력, 사칙연산, 비교 연산을 직접 정의합니다.
- `__add__()`는 `student1 + student2`를 했을 때 두 학생의 총점을 더하도록 만들고, `__truediv__()`는 `/` 연산자를 사용했을 때 총점끼리 나누도록 만듭니다.
- `__gt__()`는 `>` 연산자를 정의합니다. 예제에서는 두 `Student` 객체의 총점을 비교합니다. 비교 대상이 `Student`가 아니면 `"error"`를 반환하도록 작성되어 있습니다.
- `self.__aa = "secret key"`처럼 이름 앞에 밑줄 두 개를 붙이면 `name mangling`이 적용되어 외부에서 바로 접근하기 어렵게 됩니다. 완전한 보안 기능은 아니고, 클래스 내부에서 사용하는 값이라는 의미에 가깝습니다.

### 클래스 변수와 클래스 메서드

- `a67_class_variable.py`의 `count`와 `students`는 클래스 변수입니다. 클래스 변수는 각각의 객체가 따로 가지는 값이 아니라 `Student` 클래스 전체가 공유하는 값입니다.
- `Student.count += 1`은 `Student` 객체가 생성될 때마다 전체 학생 수를 `1`씩 증가시킵니다. `Student.students.append(self)`는 새로 생성된 학생 객체 자기 자신을 전체 학생 목록에 추가합니다.
- `@classmethod`는 객체가 아니라 클래스에서 직접 호출할 수 있는 메서드를 만들 때 사용합니다. `Student.print()`는 등록된 학생 수와 학생 목록을 한 번에 출력합니다.
- 인스턴스 변수는 `self.name`, `self.korean`처럼 객체마다 따로 저장되는 값이고, 클래스 변수는 `Student.count`, `Student.students`처럼 클래스 전체가 공유하는 값입니다.

### 객체 삭제와 소멸자

- `a69_destructor.py`에서는 객체가 생성될 때 실행되는 `__init__()`과 객체가 더 이상 사용되지 않아 파괴될 때 실행되는 `__del__()`을 확인합니다.
- `a = Test("a")`를 실행하면 `a` 객체가 생성되고 `"__ 생성 되었습니다"` 메시지가 출력됩니다. `del c`를 실행하면 `c`라는 이름이 삭제되고, 그 객체를 더 이상 참조하지 않으면 `"__ 이 파괴 되었습니다"` 메시지가 출력됩니다.
- 파이썬의 `del`은 C++의 `delete`처럼 객체를 직접 삭제하는 명령이 아니라, 변수가 객체를 가리키는 연결을 끊는 명령입니다. 같은 객체를 다른 변수가 아직 참조하고 있다면 `__del__()`이 바로 실행되지 않을 수 있습니다.
- C++ 소멸자는 스코프를 벗어날 때 실행 시점이 비교적 명확하지만, 파이썬의 `__del__()`은 가비지 컬렉션과 참조 상태에 따라 실행 시점이 달라질 수 있습니다. 중요한 자원 정리는 `__del__()`보다 `with` 문이나 명시적인 `close()` 방식이 더 안전합니다.

### 프로퍼티와 캡슐화

- `a70_property.py`에서는 `Circle` 클래스의 반지름을 `self.__radius`에 저장합니다. `__radius`처럼 이름 앞에 밑줄 두 개를 붙이면 `name mangling`이 적용되어 클래스 밖에서 바로 접근하기 어렵습니다.
- `@property`는 메서드를 속성처럼 사용할 수 있게 해주는 데코레이터입니다. `circle.radius`를 호출하면 `radius` getter가 실행되고, `circle.radius = 20`처럼 값을 넣으면 `radius` setter가 실행됩니다.
- setter에서는 `isinstance(value, int) and value > 0` 조건을 검사하여 양의 정수만 반지름으로 저장합니다. `3.14`나 `-5`처럼 조건에 맞지 않는 값은 저장하지 않고 `"양의 정수만 넣으시오."`를 출력합니다.
- `get_area()`는 `math.pi * (반지름 ** 2)` 공식을 사용하여 원의 넓이를 구합니다. 내부에서는 `self.__radius`를 사용하므로 setter를 통과한 유효한 값으로 계산됩니다.
- `__dict__`와 `vars(객체)`는 객체가 가지고 있는 속성 정보를 딕셔너리 형태로 확인할 때 사용합니다. `getattr(객체, "이름")`은 문자열로 속성이나 메서드를 찾아올 때 사용합니다.

### 상속과 오버라이딩

- `a71_class_inheritance.py`에서는 `Child` 클래스가 `Parent` 클래스를 상속받습니다. `class Child(Parent)`는 `Child`가 `Parent`의 속성과 메서드를 물려받는다는 뜻입니다.
- `Child`의 `__init__()` 안에서 `super().__init__(value)`를 호출하면 부모 클래스인 `Parent`의 `__init__()`이 먼저 실행됩니다. 그래서 `child` 객체는 `Parent`에서 만든 `value`, `value2` 속성을 사용할 수 있습니다.
- `Parent`에도 `test()`가 있고 `Child`에도 `test()`가 있습니다. 이 경우 `child.test()`를 호출하면 부모의 `test()`가 아니라 자식 클래스에서 다시 정의한 `test()`가 실행됩니다. 이것을 오버라이딩이라고 합니다.
- 파이썬은 C++처럼 함수 이름은 같고 매개변수만 다른 일반적인 오버로딩을 지원하지 않습니다. 같은 이름의 메서드를 다시 정의하면 뒤에 정의한 메서드가 앞의 메서드를 덮어씁니다. 예제에서는 `*args`를 사용하여 여러 개의 인자를 받을 수 있게 처리합니다.

### 다중 상속과 MRO

- `a72_multiple_inheritance.py`에서는 `Undergraduate` 클래스가 `Person`과 `University`를 동시에 상속받습니다. `class Undergraduate(Person, University)`는 `Undergraduate`가 `Person`의 `greeting()`과 `University`의 `massage_credit()`을 모두 사용할 수 있다는 뜻입니다.
- `Undergraduate`의 `__init__()`에서는 `Person.__init__(self, 1)`과 `University.__init__(self, 2)`를 직접 호출합니다. 그 결과 `james.b`에는 `1`이 저장되고, `james.a`에는 `2`가 저장됩니다.
- `james.greeting()`은 `Person`에서 물려받은 메서드이고, `james.massage_credit()`은 `University`에서 물려받은 메서드이며, `james.study()`는 `Undergraduate` 자기 자신이 가진 메서드입니다.
- `MRO`는 `Method Resolution Order`의 약자로, 메서드 탐색 순서를 의미합니다. `Undergraduate.__mro__`를 보면 파이썬이 `Undergraduate`, `Person`, `University`, `object` 순서로 메서드와 속성을 찾는다는 것을 확인할 수 있습니다.
- `Undergraduate.__mro__[1].__dict__`는 `MRO` 순서에서 `1`번째에 있는 `Person` 클래스의 내부 정보를 출력합니다. `__dict__`에는 클래스가 가진 메서드와 여러 내부 속성 정보가 들어 있습니다.

## 파일 입출력과 예외 처리

### 파일 쓰기

- `a42_file_write.py`에서는 `pathlib`의 `Path`를 사용하여 파일 경로를 다룹니다. `Path(r"...\data")`처럼 폴더 경로를 만들고, `path / "text.txt"`처럼 `/` 연산자로 파일 경로를 이어 붙일 수 있습니다.
- `with open(path / "text.txt", "a") as f:`는 `text.txt` 파일을 추가 모드로 여는 코드입니다. `"a"`는 `append`의 의미로, 기존 내용을 지우지 않고 파일의 마지막에 새 내용을 이어 씁니다.
- `f.write("hello!!!")`는 열린 파일에 문자열을 직접 기록합니다. `with` 문을 사용하면 작업이 끝난 뒤 `f.close()`를 직접 호출하지 않아도 파일이 자동으로 닫힙니다.

### 파일 읽기와 표준 입출력

- `a43_file_read.py`에서는 `with open(path / "text.txt", "r") as f:`로 파일을 읽기 모드로 엽니다. `"r"`은 `read`의 의미이며, 파일이 없으면 오류가 발생합니다.
- `f.readline()`은 파일에서 한 줄씩 읽는 메서드입니다. `while data := f.readline():`처럼 작성하면 더 이상 읽을 줄이 없을 때까지 반복해서 파일 내용을 출력할 수 있습니다.
- `:=`는 walrus operator라고 부르며, 값을 변수에 대입하면서 동시에 조건식에서 사용할 때 쓰입니다. 예제에서는 한 줄을 읽은 값을 `data`에 저장하고, 그 값이 비어 있지 않으면 반복을 계속합니다.
- `sys.stdin`, `sys.stdout`, `sys.stderr`는 표준 입력, 표준 출력, 표준 에러를 의미합니다. `print("error message", file=sys.stderr)`처럼 작성하면 일반 출력이 아니라 에러 출력 쪽으로 메시지를 보낼 수 있습니다.
- `print("이것은 프린트로 파일을 쓴 데이터이다.", file=f)`처럼 `print()`의 `file` 인자에 파일 객체를 넣으면 화면이 아니라 파일에 출력할 수 있습니다.

### 예외 처리

- `a47_try_except.py`에서는 `try`, `except`, `else`, `finally`를 사용하여 오류 상황을 처리합니다. 사용자가 입력한 값은 `input()` 때문에 항상 문자열로 들어오므로, `int(user_input)`으로 정수 변환을 시도합니다.
- `ValueError`는 정수로 바꿀 수 없는 값이 들어왔을 때 발생합니다. 예를 들어 `"abc"`를 입력하면 `int("abc")`가 실패하고 `except ValueError as e:` 블록이 실행됩니다.
- `NegativeError(Exception)`은 직접 만든 사용자 정의 예외 클래스입니다. 입력된 숫자가 음수이면 `raise NegativeError()`로 예외를 직접 발생시킵니다.
- `else` 블록은 `try` 안에서 예외가 발생하지 않았을 때 실행됩니다. 예제에서는 양의 정수가 들어왔을 때 원의 반지름, 둘레, 넓이를 출력합니다.
- `finally` 블록은 예외 발생 여부와 상관없이 항상 실행됩니다. 예제에서는 마지막에 `"----- 프로그램이 끝났습니다. -----"`를 출력합니다.

## 패키지와 데이터 저장

### 패키지 import

- `a90_package_import.py`에서는 직접 만든 `test_package` 패키지를 불러와서 사용하는 방법을 확인합니다. `import test_package`는 패키지 이름을 통해 내부 변수와 함수에 접근하는 방식입니다.
- `from test_package import *`는 패키지의 `__all__`에 등록된 이름들을 현재 파일로 가져옵니다. `test_package/__init__.py`의 `__all__`에는 `Module_a`, `Module_b`, `module_var_a`, `module_var_b`, `module_a_func`, `module_b_func`, `package_func`가 들어 있습니다.
- `from test_package import package_func`처럼 특정 함수만 직접 가져올 수도 있습니다. 이 경우 `package_func()`처럼 패키지 이름 없이 바로 호출할 수 있습니다.
- `test_package/module_a.py`와 `test_package/module_b.py`에는 각각 변수, 함수, 클래스가 정의되어 있습니다. `__init__.py`에서 이 이름들을 모아주면 패키지 밖에서 더 편하게 사용할 수 있습니다.

### pickle 직렬화

- `student_model.py`는 `Student` 클래스를 정의하고, 임의의 학생 데이터를 여러 개 만든 뒤 `pickle.dump(students, f)`로 파일에 저장하는 예제입니다. `pickle.dump()`는 파이썬 객체를 파일에 저장 가능한 바이너리 형태로 바꿔줍니다.
- `a97_pickle_load_student.py`는 `data/test.pickle` 파일을 `"rb"` 모드로 열고 `pickle.load(f)`로 저장된 객체를 다시 읽어옵니다. `"rb"`는 `read binary`의 의미이며, `pickle` 파일처럼 바이너리 데이터로 저장된 파일을 읽을 때 사용합니다.
- `pickle.load(f)`는 파일에서 객체를 하나씩 복원합니다. 파일 끝까지 읽으면 `EOFError`가 발생할 수 있으므로, 예제에서는 `except EOFError:`로 파일 끝 상황을 처리합니다.
- `test.pickle`은 사람이 직접 읽기 위한 텍스트 파일이 아니라, 파이썬 객체를 다시 복원하기 위한 데이터 파일입니다. 믿을 수 없는 `pickle` 파일은 실행 중 위험한 동작을 포함할 수 있으므로 신뢰할 수 있는 파일만 읽어야 합니다.
- 현재 `student_model.py` 안에는 `pickle.dump()`를 사용하면서 경로가 `test.json`으로 되어 있습니다. `pickle` 데이터라면 확장자를 `test.pickle`처럼 맞추는 것이 더 명확하고, `a97_pickle_load_student.py`의 읽기 경로와도 일치합니다.

### dataclass

- `a98_dataclass.py`에서는 `from dataclasses import dataclass`로 `dataclass` 기능을 가져옵니다. `@dataclass`를 클래스 위에 붙이면 `__init__()`, `__repr__()` 같은 기본 메서드를 자동으로 만들어줍니다.
- `Student` 클래스 안에서 `name: str`, `korean: int`, `math: int`처럼 타입 힌트를 사용하여 어떤 속성이 필요한지 선언합니다. 일반 클래스로 직접 `__init__()`을 작성하지 않아도 `Student("abc", 90, 63, 14, 13)`처럼 객체를 만들 수 있습니다.
- `print(students[0])`을 실행하면 `dataclass`가 자동으로 만든 `__repr__()` 덕분에 객체의 속성 값이 보기 좋게 출력됩니다.
- `dataclass`를 사용해도 클래스 안에 직접 메서드를 추가할 수 있습니다. 예제에서는 `get_sum()`을 작성하여 국어, 수학, 영어, 과학 점수의 합계를 계산합니다.

### JSON과 YAML 읽기

- `a101_json_serialization.py`에서는 `json` 모듈을 사용하여 `data/test.json` 파일을 읽습니다. `json.load(f)`는 JSON 파일의 내용을 파이썬 자료형으로 변환합니다.
- `data/test.json`에는 `"abc"`, `"name"`, `"subject"` 같은 키가 들어 있습니다. `data["abc"]`는 최상위 키의 값을 읽고, `data["subject"]["korean"]`은 중첩된 딕셔너리 안의 값을 읽습니다.
- `a102_yaml_serialization.py`에서는 `yaml.safe_load(f)`를 사용하여 파일 내용을 읽습니다. `safe_load()`는 YAML 데이터를 파이썬 자료형으로 안전하게 변환할 때 사용합니다.
- 현재 `a102_yaml_serialization.py`의 경로는 `test.json`을 가리키고 있습니다. JSON 문법은 YAML에서도 읽히는 경우가 많기 때문에 예제가 동작할 수 있지만, YAML 예제로 명확히 보이게 하려면 `test.yaml`을 읽도록 경로를 맞추는 것이 좋습니다.

## 함수 고급 문법

### 명령행 인자

- `103_main_argument.py`에서는 `sys.argv`를 사용하여 터미널에서 실행할 때 전달된 인자를 확인합니다. `sys.argv[0]`에는 실행한 파일 이름이 들어가고, 그 뒤부터 사용자가 입력한 값이 순서대로 들어갑니다.
- `if len(sys.argv) < 2:`는 사용자가 필요한 인자를 넣지 않았는지 검사하는 조건입니다. 인자가 부족하면 `"사용법: 로드할 파일을 명시하시오!"`를 출력하고 `sys.exit()`으로 프로그램을 종료합니다.
- C언어의 `int main(int argc, char *argv[])`에서 `argc`가 인자 개수, `argv`가 인자 목록을 의미하는 것처럼, 파이썬에서는 `len(sys.argv)`와 `sys.argv`로 비슷한 정보를 확인할 수 있습니다.

### wrapper 함수

- `a101_wrapper_function.py`에서는 함수를 다른 함수로 감싸는 기본 구조를 확인합니다. `simple_rapper(print_hello)`를 호출하면 `print_hello`를 바로 실행하지 않고, 실행 전후에 코드를 추가한 `wrapper` 함수를 만들어 반환합니다.
- `wrapper()` 안에서는 `"func 실행전 코드..."`를 먼저 출력하고, 전달받은 `func()`를 실행한 뒤, `"func 실행후 코드..."`를 출력합니다. 즉 원래 함수 코드를 고치지 않고 바깥에서 기능을 덧붙이는 구조입니다.
- 이런 wrapper 구조는 로깅, 실행 시간 측정, 권한 검사, 예외 처리처럼 여러 함수에 공통으로 붙이고 싶은 기능을 만들 때 사용됩니다.

### decorator와 `@`

- `a102_decorator.py`에서는 `@hi("hi")`처럼 값을 받는 데코레이터를 사용합니다. 이 문법은 내부적으로 `print_hello = hi("hi")(print_hello)`처럼 원래 함수를 감싼 새 함수로 바꾸는 것과 비슷합니다.
- `hi(value)`는 먼저 데코레이터에 전달할 값 `"hi"`를 받고, 안쪽의 `my_decorator(func)`는 감쌀 함수 `print_hello`를 받습니다. 마지막의 `wrapper(*args, **kwargs)`는 실제 함수 호출 시 실행되는 함수입니다.
- `*args`와 `**kwargs`를 사용하면 원래 함수가 어떤 위치 인자나 키워드 인자를 받더라도 wrapper가 그대로 받아서 `func(*args, **kwargs)`로 전달할 수 있습니다.
- `@wraps(func)`는 데코레이터를 사용해도 원래 함수의 이름과 설명 정보를 보존합니다. 그래서 `print(print_hello.__name__)`을 실행하면 `wrapper`가 아니라 `print_hello`가 출력됩니다.

### 실행 시간 측정 decorator

- `a103_time_decorator.py`에서는 `runtime_check(10)` 데코레이터를 사용하여 함수를 10번 실행하고 평균 실행 시간을 구합니다.
- `start_time = time.time()`으로 시작 시간을 기록하고, 반복문에서 `func(*args, **kwargs)`를 여러 번 실행한 뒤, `end_time = time.time()`으로 종료 시간을 기록합니다.
- `(end_time - start_time) / n`은 전체 실행 시간을 실행 횟수 `n`으로 나눈 평균 실행 시간입니다. `:.3` 또는 `:.3f` 같은 포맷을 사용하면 소수점 자릿수를 조절하여 출력할 수 있습니다.
- 데코레이터 안에서 `return result`를 해주기 때문에, 실행 시간 측정 기능을 붙여도 원래 함수의 반환값은 그대로 바깥으로 전달됩니다.

### 재귀 함수와 피보나치

- `a80_fibonacci.py`에서는 재귀 함수로 피보나치 수를 계산합니다. `fibonacci(n)`이 자기 자신인 `fibonacci(n-1)`과 `fibonacci(n-2)`를 다시 호출하여 결과를 만듭니다.
- `n == 1` 또는 `n == 2`일 때 `1`을 반환하는 부분은 재귀가 멈추는 종료 조건입니다. 종료 조건이 없으면 함수가 계속 자기 자신을 호출하다가 오류가 발생합니다.
- `cnt` 전역 변수는 `fibonacci()` 함수가 몇 번 호출되었는지 세기 위해 사용합니다. 단순 재귀 피보나치는 같은 값을 반복해서 다시 계산하기 때문에 호출 횟수가 매우 빠르게 늘어납니다.

### 캐시와 `lru_cache`

- `a82_lru_cache.py`에서는 `@lru_cache(maxsize=None)`를 사용하여 함수의 계산 결과를 저장합니다. 한 번 계산한 `fibonacci(n)` 결과를 기억해두면, 같은 `n`이 다시 들어왔을 때 함수를 다시 계산하지 않고 저장된 값을 바로 돌려줍니다.
- `from functools import cache, lru_cache`에서 `cache`는 크기 제한 없이 결과를 저장하는 간단한 캐시이고, `lru_cache`는 최근에 사용한 값을 중심으로 저장하는 캐시입니다.
- `maxsize=None`을 사용하면 저장 개수 제한 없이 캐시합니다. 피보나치처럼 같은 입력이 반복되는 재귀 함수에서는 캐시를 붙이면 호출 횟수와 실행 시간이 크게 줄어듭니다.

### generator와 `yield`

- `a86_generator.py`에서는 `yield`가 들어간 함수가 generator가 되는 것을 확인합니다. `test()`를 호출하면 함수 내부 코드가 바로 실행되는 것이 아니라 generator 객체가 만들어집니다.
- `next(generated_func)`를 호출할 때마다 함수가 다음 `yield`까지 실행됩니다. 첫 번째 `next()`에서는 `"test A"`를 출력하고 `0`을 반환한 뒤 멈추며, 두 번째 `next()`에서는 멈춘 위치 다음부터 이어서 `"test B"`를 출력하고 `1`을 반환합니다.
- 더 이상 `yield`할 값이 없을 때 `next()`를 호출하면 `StopIteration` 예외가 발생합니다. 직접 `next()`를 사용할 때는 `try`, `except StopIteration`으로 끝나는 상황을 처리할 수 있습니다.
- `for re in test():`처럼 generator를 `for`문에 넣으면 `for`문이 내부에서 자동으로 `next()`를 호출합니다. generator가 끝나면 `StopIteration`을 조용히 처리하고 반복문을 종료합니다.

## 로깅과 실행기록 남기기  

- logging 을해줘야 디버깅을 수월하게 할 수 있다 

```python
import logging 을 통해 파이썬 기본 로깅 기능 사용.  
```

- `a104_logger_example.py`에서는 `logging.basicConfig()`로 로그 출력 방식을 설정합니다. `level=logging.INFO`는 INFO 이상 수준의 로그를 기록한다는 뜻이므로, `logging.debug()` 메시지는 출력되지 않고 `info`, `warning` 메시지는 기록됩니다.
- `format="%(asctime)s [%(levelname)s] %(message)s"`는 로그에 시간, 로그 레벨, 메시지를 함께 남기는 형식입니다. `datefmt="%Y-%m-%d %H:%M:%S"`는 시간 표시 모양을 정합니다.
- `filename="logger.log"`를 지정했기 때문에 로그는 화면이 아니라 `logger.log` 파일에 저장됩니다. `encoding="utf-8"`은 한글 로그 메시지가 깨지지 않도록 하기 위한 설정입니다.

## 데이터 분석과 시각화

### CSV 읽기와 matplotlib 그래프

- `a105_matplotlib.py`에서는 `pandas`로 CSV 파일을 읽고, `matplotlib`으로 그래프를 그립니다. `pd.read_csv(csv_path / "ta_20260527093833.csv", skipinitialspace=True)`는 CSV 데이터를 `DataFrame`으로 읽어옵니다.
- `csv_path = Path(...)`처럼 `pathlib.Path`를 사용하면 폴더 경로와 파일 이름을 `/` 연산자로 이어 붙일 수 있습니다.
- `df.info()`는 읽어온 데이터의 컬럼 이름, 결측치 여부, 자료형 같은 기본 정보를 출력합니다. CSV에는 `timestamp`, `location`, `average`, `low`, `high` 컬럼이 들어 있습니다.
- `plt.plot(df['timestamp'], df['average'])`는 날짜(`timestamp`)를 x축, 평균 기온(`average`)을 y축으로 하는 선 그래프를 그립니다. `plt.show()`를 호출하면 그래프 창이 화면에 표시됩니다.

## Flask

native app (플랫폼 종속)

- Windows (.NET, C#)
- Linux (X11, GTK, Qt, tkinter)
- Mac (Cocoa/AppKit, SwiftUI, Objective-C, Swift, Mac Catalyst)

일렉트론(chrome)

- web 기술 (html, css, flask)
- webview2  
- tauri(rust 기반)
- pywebview  
- C++ webview  속도는 가장 빠름.  
- 
