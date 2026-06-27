from dataclasses import dataclass
@dataclass
class Student:
    """学生类——每个实例代表一个具体的学生"""
    name: str
    age: int
    student_id: str
        
    def info(self) -> str:
        """返回学生信息的字符串表示"""
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}"
