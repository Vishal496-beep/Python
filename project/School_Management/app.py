import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="EduTrack - School Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database file
DATABASE_FILE = "school_database.json"

# Initialize session state
def init_session_state():
    if "data" not in st.session_state:
        st.session_state.data = load_database()
    if "page" not in st.session_state:
        st.session_state.page = "Home"

# Load database
def load_database():
    if Path(DATABASE_FILE).exists():
        with open(DATABASE_FILE, "r") as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {"students": [], "teachers": [], "classes": [], "attendance": []}

# Save database
def save_database(data):
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    st.session_state.data = data

# Email validation
def validate_email(email):
    return "@" in email and "." in email

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    .success-box {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        color: #155724;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 10px;
        border-radius: 5px;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

# Initialize
init_session_state()
data = st.session_state.data

# Sidebar Navigation
st.sidebar.title("🎓 EduTrack")
st.sidebar.write("School Management System")
st.sidebar.markdown("---")

nav_option = st.sidebar.radio(
    "Navigation Menu",
    ["🏠 Home", "👤 Students", "🧑‍🏫 Teachers", "📊 Analytics", "⚙️ Settings"]
)

# Display statistics in sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("📈 Quick Stats")
st.sidebar.metric("Total Students", len(data["students"]))
st.sidebar.metric("Total Teachers", len(data["teachers"]))
avg_grade = 0
all_grades = []
for student in data["students"]:
    grades = student.get("grades", {})
    if grades:
        all_grades.extend(grades.values())
if all_grades:
    avg_grade = sum(all_grades) / len(all_grades)
st.sidebar.metric("School Average", f"{avg_grade:.2f}")

# ==================== HOME PAGE ====================
if nav_option == "🏠 Home":
    st.title("🎓 Welcome to EduTrack")
    st.write("Complete School Management System")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📚 Total Students", len(data["students"]), delta=None)
    
    with col2:
        st.metric("👨‍🏫 Total Teachers", len(data["teachers"]), delta=None)
    
    with col3:
        st.metric("📊 Average Grade", f"{avg_grade:.2f}", delta=None)
    
    st.markdown("---")
    
    # Recent Activities
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Recent Students")
        if data["students"]:
            for student in data["students"][-5:]:
                grades = student.get("grades", {})
                student_avg = sum(grades.values()) / len(grades) if grades else 0
                st.write(f"**{student['name']}** (Roll: {student['roll_no']}) - Avg: {student_avg:.2f}")
        else:
            st.info("No students registered yet")
    
    with col2:
        st.subheader("👨‍🏫 Recent Teachers")
        if data["teachers"]:
            for teacher in data["teachers"][-5:]:
                st.write(f"**{teacher['name']}** - {teacher['subject']}")
        else:
            st.info("No teachers registered yet")

# ==================== STUDENTS PAGE ====================
elif nav_option == "👤 Students":
    st.title("👤 Student Management")
    st.markdown("---")
    
    student_menu = st.tabs(["Register Student", "View Students", "Update Student", "Delete Student"])
    
    # Register Student
    with student_menu[0]:
        st.subheader("Register New Student")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", key="student_name")
            age = st.number_input("Age", min_value=5, max_value=25, value=15, key="student_age")
        
        with col2:
            email = st.text_input("Email Address", key="student_email")
            roll_no = st.text_input("Roll Number", key="student_roll")
        
        if st.button("Register Student", key="register_btn"):
            # Validation
            if not name or not email or not roll_no:
                st.error("❌ All fields are required!")
            elif not validate_email(email):
                st.error("❌ Invalid email format!")
            elif any(s["roll_no"] == roll_no for s in data["students"]):
                st.error(f"❌ Roll number '{roll_no}' already exists!")
            else:
                # Add student
                new_student = {
                    "name": name,
                    "age": age,
                    "email": email,
                    "roll_no": roll_no,
                    "grades": {},
                    "registered_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                data["students"].append(new_student)
                save_database(data)
                st.success(f"✅ Student '{name}' registered successfully!")
                st.balloons()
    
    # View Students
    with student_menu[1]:
        st.subheader("View All Students")
        
        if not data["students"]:
            st.warning("⚠️ No students registered yet")
        else:
            # Create DataFrame
            students_list = []
            for student in data["students"]:
                grades = student.get("grades", {})
                avg = sum(grades.values()) / len(grades) if grades else 0
                students_list.append({
                    "Name": student["name"],
                    "Roll No": student["roll_no"],
                    "Age": student["age"],
                    "Email": student["email"],
                    "Avg Grade": f"{avg:.2f}",
                    "Subjects": len(grades)
                })
            
            df = pd.DataFrame(students_list)
            st.dataframe(df, use_container_width=True)
            
            # Export to CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Students List (CSV)",
                data=csv,
                file_name="students_list.csv",
                mime="text/csv"
            )
    
    # Update Student
    with student_menu[2]:
        st.subheader("Update Student Information")
        
        if not data["students"]:
            st.warning("⚠️ No students available")
        else:
            student_names = [f"{s['name']} (Roll: {s['roll_no']})" for s in data["students"]]
            selected_student = st.selectbox("Select Student to Update", student_names)
            
            # Find student
            selected_idx = next(i for i, s in enumerate(data["students"]) if f"{s['name']} (Roll: {s['roll_no']})" == selected_student)
            student = data["students"][selected_idx]
            
            st.write(f"**Current Details:**")
            st.write(f"- Name: {student['name']}")
            st.write(f"- Roll No: {student['roll_no']}")
            st.write(f"- Age: {student['age']}")
            st.write(f"- Email: {student['email']}")
            
            st.write("**Update Details:**")
            col1, col2 = st.columns(2)
            with col1:
                new_name = st.text_input("New Name", value=student['name'])
                new_age = st.number_input("New Age", min_value=5, max_value=25, value=student['age'])
            with col2:
                new_email = st.text_input("New Email", value=student['email'])
            
            if st.button("Update Student"):
                if not new_name or not new_email:
                    st.error("❌ All fields are required!")
                elif not validate_email(new_email):
                    st.error("❌ Invalid email format!")
                else:
                    data["students"][selected_idx]["name"] = new_name
                    data["students"][selected_idx]["age"] = new_age
                    data["students"][selected_idx]["email"] = new_email
                    save_database(data)
                    st.success("✅ Student updated successfully!")
    
    # Delete Student
    with student_menu[3]:
        st.subheader("Delete Student")
        
        if not data["students"]:
            st.warning("⚠️ No students available")
        else:
            student_names = [f"{s['name']} (Roll: {s['roll_no']})" for s in data["students"]]
            selected_student = st.selectbox("Select Student to Delete", student_names, key="delete_student")
            
            if st.button("Delete Student", key="delete_btn"):
                selected_idx = next(i for i, s in enumerate(data["students"]) if f"{s['name']} (Roll: {s['roll_no']})" == selected_student)
                deleted_name = data["students"][selected_idx]["name"]
                data["students"].pop(selected_idx)
                save_database(data)
                st.success(f"✅ Student '{deleted_name}' deleted successfully!")

# ==================== TEACHERS PAGE ====================
elif nav_option == "🧑‍🏫 Teachers":
    st.title("🧑‍🏫 Teacher Management")
    st.markdown("---")
    
    teacher_menu = st.tabs(["Register Teacher", "View Teachers", "Update Teacher", "Delete Teacher"])
    
    # Register Teacher
    with teacher_menu[0]:
        st.subheader("Register New Teacher")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", key="teacher_name")
            age = st.number_input("Age", min_value=22, max_value=70, value=35, key="teacher_age")
        
        with col2:
            email = st.text_input("Email Address", key="teacher_email")
            subject = st.text_input("Subject", key="teacher_subject")
        
        emp_id = st.text_input("Employee ID", key="teacher_emp_id")
        
        if st.button("Register Teacher", key="register_teacher_btn"):
            # Validation
            if not name or not email or not subject or not emp_id:
                st.error("❌ All fields are required!")
            elif not validate_email(email):
                st.error("❌ Invalid email format!")
            elif any(t["employee_id"] == emp_id for t in data["teachers"]):
                st.error(f"❌ Employee ID '{emp_id}' already exists!")
            else:
                # Add teacher
                new_teacher = {
                    "name": name,
                    "age": age,
                    "email": email,
                    "subject": subject,
                    "employee_id": emp_id,
                    "registered_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                data["teachers"].append(new_teacher)
                save_database(data)
                st.success(f"✅ Teacher '{name}' registered successfully!")
                st.balloons()
    
    # View Teachers
    with teacher_menu[1]:
        st.subheader("View All Teachers")
        
        if not data["teachers"]:
            st.warning("⚠️ No teachers registered yet")
        else:
            # Create DataFrame
            teachers_list = []
            for teacher in data["teachers"]:
                teachers_list.append({
                    "Name": teacher["name"],
                    "Employee ID": teacher["employee_id"],
                    "Age": teacher["age"],
                    "Email": teacher["email"],
                    "Subject": teacher["subject"]
                })
            
            df = pd.DataFrame(teachers_list)
            st.dataframe(df, use_container_width=True)
            
            # Export to CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Teachers List (CSV)",
                data=csv,
                file_name="teachers_list.csv",
                mime="text/csv"
            )
    
    # Update Teacher
    with teacher_menu[2]:
        st.subheader("Update Teacher Information")
        
        if not data["teachers"]:
            st.warning("⚠️ No teachers available")
        else:
            teacher_names = [f"{t['name']} (ID: {t['employee_id']})" for t in data["teachers"]]
            selected_teacher = st.selectbox("Select Teacher to Update", teacher_names)
            
            # Find teacher
            selected_idx = next(i for i, t in enumerate(data["teachers"]) if f"{t['name']} (ID: {t['employee_id']})" == selected_teacher)
            teacher = data["teachers"][selected_idx]
            
            st.write(f"**Current Details:**")
            st.write(f"- Name: {teacher['name']}")
            st.write(f"- Employee ID: {teacher['employee_id']}")
            st.write(f"- Age: {teacher['age']}")
            st.write(f"- Email: {teacher['email']}")
            st.write(f"- Subject: {teacher['subject']}")
            
            st.write("**Update Details:**")
            col1, col2 = st.columns(2)
            with col1:
                new_name = st.text_input("New Name", value=teacher['name'])
                new_age = st.number_input("New Age", min_value=22, max_value=70, value=teacher['age'])
                new_email = st.text_input("New Email", value=teacher['email'])
            with col2:
                new_subject = st.text_input("New Subject", value=teacher['subject'])
            
            if st.button("Update Teacher"):
                if not new_name or not new_email or not new_subject:
                    st.error("❌ All fields are required!")
                elif not validate_email(new_email):
                    st.error("❌ Invalid email format!")
                else:
                    data["teachers"][selected_idx]["name"] = new_name
                    data["teachers"][selected_idx]["age"] = new_age
                    data["teachers"][selected_idx]["email"] = new_email
                    data["teachers"][selected_idx]["subject"] = new_subject
                    save_database(data)
                    st.success("✅ Teacher updated successfully!")
    
    # Delete Teacher
    with teacher_menu[3]:
        st.subheader("Delete Teacher")
        
        if not data["teachers"]:
            st.warning("⚠️ No teachers available")
        else:
            teacher_names = [f"{t['name']} (ID: {t['employee_id']})" for t in data["teachers"]]
            selected_teacher = st.selectbox("Select Teacher to Delete", teacher_names, key="delete_teacher")
            
            if st.button("Delete Teacher", key="delete_teacher_btn"):
                selected_idx = next(i for i, t in enumerate(data["teachers"]) if f"{t['name']} (ID: {t['employee_id']})" == selected_teacher)
                deleted_name = data["teachers"][selected_idx]["name"]
                data["teachers"].pop(selected_idx)
                save_database(data)
                st.success(f"✅ Teacher '{deleted_name}' deleted successfully!")

# ==================== GRADES PAGE ====================
elif nav_option == "📊 Analytics":
    st.title("📊 Grades & Analytics")
    st.markdown("---")
    
    analytics_menu = st.tabs(["Add/Update Grades", "Student Performance", "Class Analytics"])
    
    # Add/Update Grades
    with analytics_menu[0]:
        st.subheader("Add or Update Student Grades")
        
        if not data["students"]:
            st.warning("⚠️ No students available. Register a student first!")
        else:
            student_names = [f"{s['name']} (Roll: {s['roll_no']})" for s in data["students"]]
            selected_student = st.selectbox("Select Student", student_names)
            
            # Find student
            selected_idx = next(i for i, s in enumerate(data["students"]) if f"{s['name']} (Roll: {s['roll_no']})" == selected_student)
            student = data["students"][selected_idx]
            
            st.write(f"**Student:** {student['name']} (Roll: {student['roll_no']})")
            
            col1, col2 = st.columns(2)
            with col1:
                subject = st.text_input("Subject Name")
            with col2:
                marks = st.number_input("Marks (0-100)", min_value=0.0, max_value=100.0, step=0.5)
            
            if st.button("Save Grade"):
                if not subject:
                    st.error("❌ Subject name is required!")
                else:
                    data["students"][selected_idx]["grades"][subject] = marks
                    save_database(data)
                    st.success(f"✅ Grade added: {subject} - {marks}")
            
            # Display current grades
            if student["grades"]:
                st.markdown("---")
                st.subheader(f"Current Grades for {student['name']}")
                
                grades_df = pd.DataFrame({
                    "Subject": list(student["grades"].keys()),
                    "Marks": list(student["grades"].values())
                })
                
                st.dataframe(grades_df, use_container_width=True)
                
                avg_grade = sum(student["grades"].values()) / len(student["grades"])
                st.metric("Average Grade", f"{avg_grade:.2f}")
                
                # Delete grade option
                if st.checkbox("Delete a grade"):
                    grade_to_delete = st.selectbox("Select subject to delete", list(student["grades"].keys()))
                    if st.button("Delete Grade"):
                        del data["students"][selected_idx]["grades"][grade_to_delete]
                        save_database(data)
                        st.success(f"✅ Grade for {grade_to_delete} deleted!")
    
    # Student Performance
    with analytics_menu[1]:
        st.subheader("Student Performance Report")
        
        if not data["students"]:
            st.warning("⚠️ No students available")
        else:
            performance_data = []
            for student in data["students"]:
                grades = student.get("grades", {})
                avg = sum(grades.values()) / len(grades) if grades else 0
                performance_data.append({
                    "Name": student["name"],
                    "Roll No": student["roll_no"],
                    "Subjects": len(grades),
                    "Average": f"{avg:.2f}",
                    "Status": "Pass" if avg >= 40 else "Fail"
                })
            
            df = pd.DataFrame(performance_data)
            st.dataframe(df, use_container_width=True)
            
            # Statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                passed = len([p for p in performance_data if p["Status"] == "Pass"])
                st.metric("Students Passed", passed)
            with col2:
                failed = len([p for p in performance_data if p["Status"] == "Fail"])
                st.metric("Students Failed", failed)
            with col3:
                overall_avg = sum([float(p["Average"]) for p in performance_data]) / len(performance_data)
                st.metric("Overall Average", f"{overall_avg:.2f}")
    
    # Class Analytics
    with analytics_menu[2]:
        st.subheader("Class Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Total Students:** " + str(len(data["students"])))
            st.write("**Total Teachers:** " + str(len(data["teachers"])))
        
        with col2:
            all_grades = []
            for student in data["students"]:
                grades = student.get("grades", {})
                all_grades.extend(grades.values())
            
            if all_grades:
                avg_class = sum(all_grades) / len(all_grades)
                st.write(f"**Class Average:** {avg_class:.2f}")
                st.write(f"**Total Subjects:** {len(set(subject for s in data['students'] for subject in s.get('grades', {}).keys()))}")

# ==================== SETTINGS PAGE ====================
elif nav_option == "⚙️ Settings":
    st.title("⚙️ Settings & Database")
    st.markdown("---")
    
    settings_menu = st.tabs(["Database", "Export/Import"])
    
    with settings_menu[0]:
        st.subheader("Database Information")
        
        st.write(f"**Database File:** {DATABASE_FILE}")
        st.write(f"**Total Records:** {len(data['students']) + len(data['teachers'])}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Students in Database", len(data["students"]))
        with col2:
            st.metric("Teachers in Database", len(data["teachers"]))
        
        st.markdown("---")
        
        st.subheader("Backup & Restore")
        
        if st.button("📥 Download Database Backup"):
            json_str = json.dumps(data, indent=4)
            st.download_button(
                label="Download JSON Backup",
                data=json_str,
                file_name=f"school_database_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        
        if st.checkbox("⚠️ Clear All Data"):
            if st.button("🗑️ Delete All Data (Cannot be undone!)", key="clear_data"):
                data = {"students": [], "teachers": [], "classes": [], "attendance": []}
                save_database(data)
                st.success("✅ All data has been cleared!")
                st.rerun()
    
    with settings_menu[1]:
        st.subheader("Export Data")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if data["students"]:
                students_df = pd.DataFrame(data["students"])
                csv = students_df.to_csv(index=False)
                st.download_button(
                    label="📥 Export Students",
                    data=csv,
                    file_name="students_export.csv",
                    mime="text/csv"
                )
            else:
                st.info("No students to export")
        
        with col2:
            if data["teachers"]:
                teachers_df = pd.DataFrame(data["teachers"])
                csv = teachers_df.to_csv(index=False)
                st.download_button(
                    label="📥 Export Teachers",
                    data=csv,
                    file_name="teachers_export.csv",
                    mime="text/csv"
                )
            else:
                st.info("No teachers to export")
        
        with col3:
            json_str = json.dumps(data, indent=4)
            st.download_button(
                label="📥 Export All (JSON)",
                data=json_str,
                file_name="school_data_export.json",
                mime="application/json"
            )
        
        st.markdown("---")
        st.subheader("Import Data")
        st.warning("⚠️ Importing will merge with existing data. Back up first!")
        
        uploaded_file = st.file_uploader("Upload JSON or CSV file", type=["json", "csv"])
        if uploaded_file:
            if st.button("Import Data"):
                try:
                    if uploaded_file.type == "application/json":
                        imported_data = json.load(uploaded_file)
                        # Merge data
                        data["students"].extend(imported_data.get("students", []))
                        data["teachers"].extend(imported_data.get("teachers", []))
                        save_database(data)
                        st.success("✅ Data imported successfully!")
                    else:
                        st.error("❌ Please upload a JSON file")
                except Exception as e:
                    st.error(f"❌ Error importing data: {str(e)}")

# Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: gray; font-size: 12px;'>
    <p>EduTrack © 2024 | School Management System</p>
    <p>Database: {DATABASE_FILE} | Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</div>
""", unsafe_allow_html=True)