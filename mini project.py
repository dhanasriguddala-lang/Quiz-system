# Sample Quiz System using dictionary

# ---------- Data Storage ----------
admin_details = {"admin": "admin123"}
questions_db = {
    "Python": [
        {"question": "Who developed Python Programming Language? a) Wick van Rossum b) Rasmus Lerdorf c) Guido van Rossum d) Niene Stom","answer": "c"},
        {"question": "Which of the following is the truncation division operator in Python? a) | b) // c) / d) % ","answer":"b"},
        {"question": "What is the keyword to define a function? a)def  b)list  c)sets", "answer": "a"},
        {"question": "Which type of Programming does Python support? a) object-oriented programming b) structured programming c) functional programming d)all of the mentioned ","answer":"d"},
        {"question": "Which of the following is the correct extension of the Python file? a) .python b) .pl c) .py d) .p","answer":"c"},
        {"question": "Is Python code compiled or interpreted? a)both compiled and interpreted b)neither compiled nor interpreted c)only compiled d)only interpreted","answer":"a"},
        {"question": "Which keyword is used for function in Python language? a) Function b) def c) Fun d) Define ","answer":"b"},
        {"question": "Which keyword is used for loops?  a)for  b)while  c)a&b  d)none of the above", "answer": "a"},
        {"question": "Which of the following is a Python tuple? a) [1, 2, 3] b) (1, 2, 3) c) {1, 2, 3} d) {} ","answer":"b"},
        {"question": "Which symbol is used for single-line comments in Python? a) // b) - c) # d) /* */ ","answer":"c"} 
        ],
    "MySQL": [
        {"question": "What does “MySQL” stand for? a) My Sequence Query Language b) My Structured Query Language c) Mine Sequence Query Language d) My Special Query Language","answer":"b"},
        {"question": "What is MySQL? a) An operating system b) A web server  c) A programming language d) A relational database management system (RDBMS)","answer":"d"},
        {"question": "Who developed MySQL? a) MySQL AB b) Microsoft c) Oracle Corporation d) Sun Microsystems","answer":"a"},
        {"question": "Which type of database management system is MySQL? a) Network b) Object-oriented c) Relational d) Hierarchical","answer":"c"},
        {"question": "How are identifiers quoted in MySQL? a) double quotes b) backticks c) can’t be quoted d) single quotes","answer":"b"},
        {"question": "What is data in a MySQL database organized into? a) Tables b) Networks c) Objects d) File systems","answer":"a"},
        {"question": "Which operator is used to perform integer divisions in MySQL? a) DIV b) / c) \ d) //","answer":"a"},
        {"question": "Which MySQL clause is used to combine rows from two or more tables? a) UNION b) COMBINE c) MERGE d) JOIN ","answer":"d"}         
        ]
}
user_scores = {}

# ---------- Admin Functions ---------
def admin_login():
    admin_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")
    if admin_details.get(admin_id) == password:
        print("\nLogin Successful as Admin!")
        admin_menu()
    else:
        print("Invalid Admin Details")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. Modify Question")
        print("3. Delete Question")
        print("4. View All Questions")
        print("5. View All User Details")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            modify_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            view_questions()
        elif choice == "5":
            view_users()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

def add_question():
    tech = input("Enter Technology (Python/MySQL): ")
    if tech in questions_db:
        q = input("Enter Question: ")
        a = input("Enter Answer: ")
        questions_db[tech].append({"question": q, "answer": a})
        print("Question Added.")
    else:
        print("Technology not found.")

def modify_question():
    tech = input("Enter Technology: ")
    if tech in questions_db:
        view_questions_by_tech(tech)
        num = int(input("Enter Question Number to Modify: "))-1
        if 0 <= num < len(questions_db[tech]):
            new_q = input("Enter new Question: ")
            new_a = input("Enter new Answer: ")
            questions_db[tech][num] = {"question": new_q, "answer": new_a}
            print("Question Modified.")
        else:
            print("Invalid Question Number.")
    else:
        print("Technology not found.")

def delete_question():
    tech = input("Enter Technology: ")
    if tech in questions_db:
        view_questions_by_tech(tech)
        num = int(input("Enter Question Number to Delete: ")) - 1
        if 0 <= num < len(questions_db[tech]):
            del questions_db[tech][num]
            print("Question Deleted.")
        else:
            print("Invalid Question Number.")
    else:
        print("Technology not found.")

def view_questions():
    for tech, q_list in questions_db.items():
        print(f"\nTechnology: {tech}")
        for i, q in enumerate(q_list, 1):
            print(f"{i}. {q['question']} (Ans: {q['answer']})")

def view_questions_by_tech(tech):
    print(f"\nQuestions in {tech}:")
    for i, q in enumerate(questions_db[tech], 1):
        print(f"{i}. {q['question']} (Ans: {q['answer']})")
    else:
        print('*'*10,"No questions availble for this technology.",'*'*10 )

def view_users():
    for user, details in user_scores.items():
        print(f"\nUser: {user}")
        print(f"Mobile: {details['mobile']}, Score: {details['score']}, Time: {details['time']}")
    else:
        print('*'*10,"Users can't be login",'*'*10 )

# ---------- User Functions ----------
def user_login():
    username = input("Enter User Name: ")

    while True:
        mobile = input("Enter Mobile Number: ")
        if len(mobile)== 10:
            break
        else:
            print("Mobile number must be exactly 10 digits. Please try again.")
    print(f"\nWelcome {username}! Let's take the quiz.")
    take_quiz(username, mobile)

def take_quiz(username, mobile):
    from datetime import datetime
    tech = input("Select Technology (Python/MySQL): ")
    if tech in questions_db and questions_db[tech]:
        score = 0
        for q in questions_db[tech]:
            print("\n" + q["question"])
            ans = input("Your Answer: ")
            if ans.strip().lower() == q["answer"].strip().lower():# strip()--> spaces remove cheyyadam.  lower()----> capital/small ignore cheyadam.
                score += 1
        else:
            print("\n"+q["question"])
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#present time ni format chesi store chesthunnaru. ex- "2025-07-17  10:15:40".
        user_scores[username] = {"mobile": mobile, "score": score, "time": time} # score + moblie + time in record chestharu.
        print(f"\n{username}, you scored {score}")
    else:
        print("No questions available for this technology.")

def get_score(item):
    return item[1]["score"]

def show_highest_scores():
    print("\n--- Top 3 Highest Scores ---")
    top_scores = sorted(user_scores.items(), key=get_score, reverse=True)[:3]
    for i, (user, detail) in enumerate(top_scores, 1):
        print(f"{i}. {user} - {detail['score']}")
'''
def show_highest_scores():
    print("\n--- Top 3 Highest Scores ---")
    top_scores = sorted(user_scores.items(), key=lambda x: x[1]["score"], reverse=True)[:3]
    for i, (user, detail) in enumerate(top_scores, 1):
        print(f"{i}. {user} - {detail['score']}")'''




# ---------- Main Menu ----------
def main():
    while True:
        print('*'*5,"Quiz System",'*'*5)
        print("1. Admin Login")
        print("2. User Login")
        print("3. View Highest Scores")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            user_login()
        elif choice == "3":
            show_highest_scores()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# ---------- Run the Program ----------
main()
