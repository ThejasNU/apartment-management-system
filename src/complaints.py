import streamlit as st
import pandas as pd
import datetime as dt
from database import add_complaint,view_all_complaints,get_complaint,edit_complaint,drop_complaint

def create_complaint():
    complaintID=st.text_input("Complaint ID:")
    residentUID=st.text_input("Resident UID:")
    complain=st.text_input("Write your complaint here:")

    if st.button("Add complaint"):
        add_complaint(complaintID, residentUID, complain)
        st.success("Successfully added the complaint")

def show_complaints():
    result=view_all_complaints()
    df=pd.DataFrame(result,columns=["ComplaintID","ResidentUID","Complain","date","time"],dtype=str)
    st.table(df)

def update_complaint():
    result=view_all_complaints()
    df=pd.DataFrame(result,columns=["ComplaintID","ResidentUID","Complain","date","time"],dtype=str)
    with st.expander("Current complaints:"):
        st.table(df)
    list_of_complaints=[i for i in df['ComplaintID']]
    select_complaint=st.selectbox("Select a complaint to edit:",list_of_complaints)
    selected_result=get_complaint(select_complaint)

    if selected_result:
        complaintid=selected_result[0][0]
        residentuid=selected_result[0][1]
        complain=selected_result[0][2]
        date=selected_result[0][3]
        time=str(selected_result[0][4])

        with st.expander("Edit complaint:"):
            new_cid=st.text_input("ComplaintID:",complaintid)
            new_ruid=st.text_input("ResidentUID:",residentuid)
            new_comp=st.text_input("Complain:",complain)
            new_date=st.date_input("Date:",value=date,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
            new_time=st.time_input("Time:",dt.time(int(time.split(':')[0]),int(time.split(':')[1]),int(time.split(':')[2])))

            if st.button("Update complaint"):
                edit_complaint(new_cid, new_ruid, new_comp, new_date, new_time, complaintid)
                st.success("Successfully updated the complaint")

def delete_complaint():
    result=view_all_complaints()
    df=pd.DataFrame(result,columns=["ComplaintID","ResidentUID","Complain","date","time"],dtype=str)
    with st.expander("Current complaints:"):
        st.table(df)
    list_of_complaints=[i for i in df['ComplaintID']]
    selected_complaint=st.selectbox("Complaint to delete:",list_of_complaints)
    st.warning(f"Do you want to delete complaint {selected_complaint}?")
    if st.button("Delete complaint"):
        drop_complaint(selected_complaint)
        st.success("Complaint deleted successfully")






