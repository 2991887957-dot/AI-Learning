# Day 02: Python 面向对象

## 学了什么

- **class** — 创建对象的模板/蓝图。`class Student:` 定义了一个"学生"的模板
- **object（对象）** — Python 中一切皆对象。数字、字符串、你写的 class 实例都是对象
- **instance（实例）** — 用 class 创建出来的具体对象。`s1 = Student("张三")` 中 s1 就是一个实例
- **self** — 代表实例本身。调用 `s1.say_hello()` 时 Python 自动把 s1 传给 self
- **method（方法）** — 定义在 class 里的函数，第一个参数永远是 self，操作的是实例自己的数据
- **attribute（属性）** — 对象的数据，如 `self.name`、`self.age`，每个实例的值可以不同
- **为什么需要 class** — 把数据和操作数据的方法组织在一起，避免散落的字典和函数

## 核心代码

```python
class Student:
    def __init__(self, name: str, age: int, student_id: str):
        self.name = name          # 属性：这个学生的名字
        self.age = age            # 属性：这个学生的年龄
        self.student_id = student_id  # 属性：这个学生的学号

    def info(self) -> str:
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}"

# self 是怎么传进去的？
s1 = Student("张三", 20, "001")
s1.info()  # Python 内部实际是 Student.info(s1)
```

## 遇到的问题

- **UnicodeEncodeError**：Windows 终端 GBK 编码不支持 emoji（✅❌🗑️），打印报错。解决：换成纯文本标记 `[OK]`、`[ERROR]`
- **`__pycache__/` 被 git 跟踪**：Python 运行后自动生成的缓存目录不应该提交。解决：创建 `.gitignore` 排除 `__pycache__/` 和 `*.pyc`

## 今天最深的理解

- **self 不是关键字，是约定**。`self` 这个名字可以改成别的（但不应该改），关键是它永远是方法的第一个参数，指向调用这个方法的实例。`s1.info()` 等价于 `Student.info(s1)`。
