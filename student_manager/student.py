class Student:
    """学生类——每个实例代表一个具体的学生"""

    def __init__(self, name: str, age: int, student_id: str):
        """
        构造方法：创建学生对象时自动调用
        self 指向当前正在创建的这个实例
        """
        self.name = name
        self.age = age
        self.student_id = student_id

    def info(self) -> str:
        """返回学生信息的字符串表示"""
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}"
