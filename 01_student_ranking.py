# 🏆 CHALLENGE — Student Ranking System
# Use:
# 1. filter() -> score >= 60
# 2. sorted() -> highest score first
# 3. map() -> strings like "Sara: 95"
#
# Bonus: put everything inside get_passed_students(students).

students = [
    {"name": "Ali", "score": 75},
    {"name": "Sara", "score": 95},
    {"name": "Omar", "score": 45},
    {"name": "Mona", "score": 88},
    {"name": "Hany", "score": 55},
]
num=list(filter(lambda x: x["score"]>=60,students))
sorted_stu=sorted(num,key=lambda x:x["score"],reverse=True)
result=list(map(lambda x:f"{x["name"]}:{x["score"]}",sorted_stu))

print(list(result))
