from student import Student


class Manager:
    """学生管理器——管理所有学生的增删查改"""

    def __init__(self):
        """初始化一个空的学生列表"""
        self.students: list[Student] = []

    def add_student(self, name: str, age: int, student_id: str) -> Student:
        """增加一个学生"""
        student = Student(name, age, student_id)
        self.students.append(student)
        print(f"[OK] 已添加: {student.info()}")
        return student

    def delete_student(self, student_id: str) -> bool:
        """根据学号删除学生，返回是否删除成功"""
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print(f"[OK] 已删除: {s.info()}")
                return True
        print(f"[ERROR] 未找到学号为 {student_id} 的学生")
        return False

    def query_student(self, student_id: str) -> Student | None:
        """根据学号查询学生，找不到返回 None"""
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def list_all(self) -> list[Student]:
        """返回所有学生"""
        return self.students
