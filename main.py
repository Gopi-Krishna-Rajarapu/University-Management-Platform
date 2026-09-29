# Python + Streamlit Project, Streamlit -> creating UI
# project on concepts of python
# University Management System

import streamlit as st

# config the main page
st.set_page_config(
    page_title="University Management System",
    layout="wide",
)

st.title("University Management System")

# create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice = st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "List of Colleges"
    )
)

class College:
    def __init__(self,c_name):
        self.c_name=c_name
        self.students=[]
        self.teachers=[]

    def add_student(self,s):
        self.students.append(s)
    
    def add_teacher(self,t):
        self.teachers.append(t)

# based upon clg name, clg class obj is extracted/find
def find_college(c_name):     # We not need to write self bec it is outside class ot inside
    for c in st.session_state.colleges:
        if c.c_name == c_name:
            return c
    return None

class Person:
    def __init__(self,  branch): # removed name parameter
        self.branch = branch
        # self.name = name

class Student(Person):
    def __init__(self, roll, s_name, branch):
        self.s_name = s_name
        self.rollno = roll   # err -> rollno= is called as var,need to give space 
        super().__init__( branch)

class Teacher(Person):
    def __init__(self, subject, t_name, branch):
        self.subject = subject
        self.t_name=t_name
        super().__init__(branch)


if menu_choice=="Create College":
    c_name = st.text_input("Enter a new College name:")
    if st.button("CREATE"):
        clg_obj=College(c_name)
        st.session_state.colleges.append(clg_obj)
        st.success(f"College created successfully: {c_name}")

elif menu_choice=="Add Student":
    if not st.session_state.colleges:
        st.info("Please add / create college  first")
    else:
        clg_name = st.selectbox("Choose College:",[c.c_name for c in st.session_state.colleges])  # List Comprehension

        roll = st.number_input("Enter your roll number:", min_value=1, max_value=100)
        s_name=st.text_input("Enter student name:")
        branch=st.text_input("Enter your branch:")
        if st.button("ADD STUDENT"):
            if not (roll and s_name and clg_name):
                st.error("Please don't leave any information None / blank")
            clg_obj = find_college(clg_name)
            stu_obj = Student(roll,s_name,branch)
            clg_obj.add_student(stu_obj)
            st.success("Student added successfully")
elif menu_choice=="Add Teacher":
    if not st.session_state.colleges:
        st.info("Please add / create college  first")
    else:
        clg_name = st.selectbox("Choose College:",[c.c_name for c in st.session_state.colleges])  # List Comprehension
        subject = st.text_input("Enter subject name:")
        t_name=st.text_input("Enter teacher name:")
        branch=st.text_input("Enter your branch:")
        if st.button("ADD Teacher"):
            if not (subject and t_name and clg_name):
                st.error("Please don't leave any information None / blank")
            clg_obj = find_college(clg_name)
            teacher_obj = Teacher(subject,t_name,branch)
            clg_obj.add_teacher(teacher_obj)
            st.success("Student added successfully")

            # print(clg_obj.teachers)
            # for c in clg_obj.teachers:
            #     print(c,end=" ")
elif menu_choice=="Display Students":
    if not st.session_state.colleges:
        st.info("Please add / create college  first") 
    else:
        clg_name = st.selectbox("Choose College:",[c.c_name for c in st.session_state.colleges]) 
        clg_obj=find_college(clg_name)
        st.subheader(f"List of Students in {clg_name}")
        if clg_obj.students:
            for i,s in enumerate(clg_obj.students,1):
                st.write(i,":",s.s_name)
                # print(i,":",s.s_name)
elif menu_choice=="Display Teachers":
    if not st.session_state.colleges:
        st.info("Please add / create college  first") 
    else:
        clg_name = st.selectbox("Choose College:",[c.c_name for c in st.session_state.colleges]) 
        clg_obj=find_college(clg_name)
        st.subheader(f"List of Teachers in {clg_name}")
        if clg_obj.teachers:
            for i,t in enumerate(clg_obj.teachers,1):
                st.write(i,":",t.t_name)
                # print(i,":",s.s_name)   
        else:
            st.warning("Teacher not found")
elif menu_choice=="List of Colleges":
    st.subheader("List of Colleges")
    if not st.session_state.colleges:
        st.info("Please add the college first..!")
    else:
        for i,c in enumerate(st.session_state.colleges,1):
            st.write(f"{1} : {c.c_name}")

