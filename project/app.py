import streamlit as st
from pathlib import Path
import os

# --- Page Configuration ---
st.set_page_config(page_title="Python File Manager", page_icon="📁", layout="centered")

# --- Sidebar Navigation ---
st.sidebar.title("📁 File Manager")
st.sidebar.markdown("Choose an operation from the menu below:")
menu = ["Create File", "Read File", "Update File", "Delete File"]
choice = st.sidebar.radio("Navigation", menu)

st.sidebar.divider()
st.sidebar.caption("Built with ❤️ using Streamlit")

# --- 1. CREATE FILE ---
if choice == "Create File":
    st.header("📝 Create a New File")
    
    with st.form("create_form", clear_on_submit=True):
        name = st.text_input("Enter file name (e.g., 'notes.txt'):")
        content = st.text_area("What do you want to write in the file?")
        submit_btn = st.form_submit_button("Create File")
        
        if submit_btn:
            if not name:
                st.warning("⚠️ Please enter a file name.")
            else:
                try:
                    path = Path(name)
                    if not path.exists():
                        with open(path, "w") as fs:
                            fs.write(content)
                        st.success(f"🎉 File '{name}' created successfully!")
                    else:
                        st.error("❌ Error: A file with this name already exists.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# --- 2. READ FILE ---
elif choice == "Read File":
    st.header("📖 Read a File")
    
    name = st.text_input("Enter the name of the file you want to read:")
    if st.button("Read Content"):
        if not name:
            st.warning("⚠️ Please enter a file name.")
        else:
            try:
                path = Path(name)
                if path.exists():
                    with open(path, "r") as fs:
                        content = fs.read()
                    st.success("File loaded successfully!")
                    st.text_area("File Content:", value=content, height=250, disabled=True)
                else:
                    st.error("❌ Error: File doesn't exist.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# --- 3. UPDATE FILE ---
elif choice == "Update File":
    st.header("✏️ Update an Existing File")
    
    name = st.text_input("Enter the file name you want to update:")
    
    if name:
        path = Path(name)
        if path.exists():
            st.info(f"Targeting file: **{name}**")
            
            # Select update operation
            update_choice = st.selectbox(
                "What would you like to do?", 
                ["Select an operation", "Rename the file", "Append to the file", "Overwrite the file"]
            )
            
            # Sub-menu logic based on selection
            if update_choice == "Rename the file":
                new_name = st.text_input("Enter the new file name:")
                if st.button("Rename"):
                    try:
                        new_path = Path(new_name)
                        if not new_path.exists():
                            path.rename(new_path)
                            st.success(f"✅ Successfully renamed '{name}' to '{new_name}'!")
                        else:
                            st.error("❌ A file with that name already exists.")
                    except Exception as err:
                        st.error(f"Error: {err}")
                        
            elif update_choice == "Append to the file":
                with st.form("append_form", clear_on_submit=True):
                    append_data = st.text_area("What do you want to append?")
                    if st.form_submit_button("Append Data"):
                        try:
                            with open(path, "a") as fs:
                                fs.write("\n" + append_data)
                            st.success("✅ Successfully appended data to the file!")
                        except Exception as err:
                            st.error(f"Error: {err}")
                            
            elif update_choice == "Overwrite the file":
                with st.form("overwrite_form", clear_on_submit=True):
                    overwrite_data = st.text_area("What do you want to write? (This deletes old content)")
                    if st.form_submit_button("Overwrite Data"):
                        try:
                            with open(path, "w") as fs:
                                fs.write(overwrite_data)
                            st.success("✅ Successfully overwritten the file!")
                        except Exception as err:
                            st.error(f"Error: {err}")
        else:
            if name != "":
                st.error("❌ File doesn't exist. Please check the name.")

# --- 4. DELETE FILE ---
elif choice == "Delete File":
    st.header("🗑️ Delete a File")
    
    name = st.text_input("Enter the file name you want to delete:")
    if st.button("Delete File", type="primary"):
        if not name:
            st.warning("⚠️ Please enter a file name.")
        else:
            try:
                path = Path(name)
                if path.exists():
                    path.unlink()
                    st.success(f"✅ File '{name}' deleted successfully!")
                else:
                    st.error("❌ Error: File doesn't exist.")
            except Exception as err:
                st.error(f"An error occurred while deleting: {err}")