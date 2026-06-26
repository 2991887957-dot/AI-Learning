from manager import Manager


def show_menu():
    """显示操作菜单"""
    print("\n" + "=" * 30)
    print("  学生管理系统")
    print("=" * 30)
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 查询学生")
    print("4. 显示全部")
    print("0. 退出")
    print("=" * 30)


def main():
    manager = Manager()

    while True:
        show_menu()
        choice = input("请选择操作: ").strip()

        if choice == "1":
            name = input("姓名: ").strip()
            age_str = input("年龄: ").strip()
            student_id = input("学号: ").strip()

            if not name or not age_str or not student_id:
                print("[WARN] 信息不能为空")
                continue

            age = int(age_str)
            manager.add_student(name, age, student_id)

        elif choice == "2":
            student_id = input("请输入要删除的学号: ").strip()
            manager.delete_student(student_id)

        elif choice == "3":
            student_id = input("请输入要查询的学号: ").strip()
            result = manager.query_student(student_id)
            if result:
                print(f"[FOUND] {result.info()}")
            else:
                print(f"[ERROR] 未找到学号为 {student_id} 的学生")

        elif choice == "4":
            all_students = manager.list_all()
            if not all_students:
                print("[INFO] 暂无学生")
            else:
                print(f"\n共 {len(all_students)} 名学生:")
                for s in all_students:
                    print(f"  {s.info()}")

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("[WARN] 无效选项，请重新输入")


if __name__ == "__main__":
    main()
