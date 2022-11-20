import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apna_ghar"
)
c = mydb.cursor()

#complaints####################################################################################
def add_complaint(ComplaintID,ResidentUID,Complain):
    c.execute(f"INSERT INTO complaints (ComplaintID,ResidentUID,Complain) values ('{ComplaintID}','{ResidentUID}','{Complain}')")
    mydb.commit()
def view_all_complaints():
    c.execute("SELECT * FROM complaints;")
    data=c.fetchall()
    return data
def get_complaint(CompalintID):
    c.execute(f"SELECT * FROM complaints WHERE ComplaintID='{CompalintID}'")
    data=c.fetchall()
    return data
def edit_complaint(ComplaintID,ResidentUID,Complain,date,time,old_cid):
    c.execute(f"UPDATE complaints SET ComplaintID='{ComplaintID}',ResidentUID='{ResidentUID}',Complain='{Complain}',date='{date}',time='{time}' WHERE ComplaintID='{old_cid}'")
    mydb.commit()
def drop_complaint(CompalintID):
    c.execute(f"DELETE FROM complaints WHERE ComplaintID='{CompalintID}'")
    mydb.commit()

#dependent####################################################################################
def add_dependent(aadhar,ruid,fname,lname,dob,phone,gender):
    c.execute(f"INSERT INTO dependent values ('{aadhar}','{ruid}','{fname}','{lname}','{dob}','{phone}','{gender}');")
    mydb.commit()
def view_all_dependents():
    c.execute("SELECT * FROM dependent;")
    data=c.fetchall()
    return data
def get_dependent(aadhar):
    c.execute(f"SELECT * FROM dependent WHERE Aadhar='{aadhar}'")
    data=c.fetchall()
    return data
def edit_dependent(aadhar,ruid,fname,lname,dob,phone,gender,old_aadhar):
    c.execute(f"UPDATE dependent SET Aadhar='{aadhar}',residentUID='{ruid}',Fname='{fname}',Lname='{lname}',DOB='{dob}',phone='{phone}',gender='{gender}' WHERE Aadhar='{old_aadhar}'")
    mydb.commit()
def drop_dependent(aadhar):
    c.execute(f"DELETE FROM dependent WHERE Aadhar='{aadhar}'")
    mydb.commit()

#employee####################################################################################
def add_employee(employeeID,Fname,Lname,phone,doj,gender,shift,serviceID,salary):
    c.execute(f"INSERT INTO employee values ('{employeeID}','{Fname}','{Lname}','{phone}','{doj}','{gender}','{shift}','{serviceID}','{salary}');")
    mydb.commit()
def view_all_employees():
    c.execute("SELECT * FROM employee;")
    data=c.fetchall()
    return data
def get_employee(eid):
    c.execute(f"SELECT * FROM employee WHERE employeeID='{eid}';")
    data=c.fetchall()
    return data
def edit_employee(employeeID,Fname,Lname,phone,doj,gender,shift,serviceID,salary,old_eid):
    c.execute(f"UPDATE employee SET employeeID='{employeeID}',Fname='{Fname}',Lname='{Lname}',phone='{phone}',doj='{doj}',gender='{gender}',shift='{shift}',serviceID='{serviceID}',salary={salary} WHERE employeeID='{old_eid}';")
    mydb.commit()
def drop_employee(eid):
    c.execute(f"DELETE FROM employee WHERE employeeID='{eid}';")
    mydb.commit()
    
#flat#########################################################################################
def add_flat(flatid,nobhk):
    c.execute(f"INSERT INTO flat values ('{flatid}',{nobhk});")
    mydb.commit()
def view_all_flats():
    c.execute("SELECT * FROM flat;")
    data=c.fetchall()
    return data
def get_flat(id):
    c.execute(f"SELECT * FROM flat WHERE FlatID='{id}';")
    data=c.fetchall()
    return data
def edit_flat(id,nbhk,old_id):
    c.execute(f"UPDATE flat SET FlatID='{id}',no_bhk={nbhk} WHERE FlatID='{old_id}';")
    mydb.commit()
def drop_flat(id):
    c.execute(f"DELETE FROM flat WHERE FlatID='{id}';")
    mydb.commit()

#flat_has_security################################################################################
def add_fhs(fid,sid):
    c.execute(f"INSERT INTO flat_has_security values ('{fid}','{sid}');")
    mydb.commit()
def view_all_fhs():
    c.execute(f"SELECT * from flat_has_security;")
    data=c.fetchall()
    return data
def get_fhs(fid):
    c.execute(f"SELECT * from flat_has_security WHERE FlatID='{fid}' ;")
    data=c.fetchall()
    return data
def edit_fhs(fid,sid,old_fid):
    c.execute(f"UPDATE flat_has_security SET FlatID='{fid}',securityID='{sid}' WHERE FlatID='{old_fid}';")
    mydb.commit()
def drop_fhs(fid):
    c.execute(f"DELETE from flat_has_security WHERE FlatID='{fid}';")
    mydb.commit()


#parking_slot################################################################################
def add_parking(slot,vt,fid):
    c.execute(f"INSERT INTO parking_slot values({slot},'{vt}','{fid}');")
    mydb.commit()
def view_all_parking():
    c.execute(f"SELECT * FROM parking_slot;")
    data=c.fetchall()
    return data
def get_parking(slot):
    c.execute(f"SELECT * FROM parking_slot WHERE slotNo={slot};")
    data=c.fetchall()
    return data
def edit_parking(slot,vt,fid,old_slot):
    c.execute(f"UPDATE parking_slot SET slotNo={slot},vehicle_type='{vt}',flatID='{fid}' WHERE slotNo={old_slot};")
    mydb.commit()
def drop_parking(slot):
    c.execute(f"DELETE FROM parking_slot WHERE slotNo={slot}")
    mydb.commit()

#resident####################################################################################
def add_resident(aadhar,fn,ln,dob,phone,gender,pet,fid,ro):
    c.execute(f"INSERT INTO resident values ('{aadhar}','{fn}','{ln}','{dob}','{phone}','{gender}','{pet}','{fid}','{ro}');")
    mydb.commit()
def view_all_residents():
    c.execute(f"SELECT * FROM resident;")
    data=c.fetchall()
    return data
def get_resident(id):
    c.execute(f"SELECT * FROM resident WHERE Aadhar='{id}';")
    data=c.fetchall()
    return data
def view_all_residentids():
    c.execute("SELECT Aadhar FROM resident;")
    data=c.fetchall()
    return data
def edit_resident(aadhar,fn,ln,dob,phone,gender,pet,fid,ro,old_id):
    c.execute(f"UPDATE resident SET Aadhar='{aadhar}',Fname='{fn}',Lname='{ln}',DOB='{dob}',phone='{phone}',gender='{gender}',pet_info='{pet}',FlatID='{fid}',rent_owned='{ro}' WHERE Aadhar='{old_id}';")
    mydb.commit()
def drop_resident(id):
    c.execute(f"DELETE FROM resident WHERE Aadhar='{id}';")
    mydb.commit()

#resident_avails_services###################################################################################
def add_ras(rid,sid,dts):
    c.execute(f"INSERT INTO resident_avails_services values ('{rid}','{sid}','{dts}');")
    mydb.commit()
def view_all_ras():
    c.execute(f"SELECT * from resident_avails_services;")
    data=c.fetchall()
    return data
def get_ras(rid,sid):
    c.execute(f"SELECT * from resident_avails_services WHERE ResidentUID='{rid}' and serviceID='{sid}';")
    data=c.fetchall()
    return data
def edit_ras(rid,sid,dts,old_rid,old_sid):
    c.execute(f"UPDATE resident_avails_services SET ResidentUID='{rid}',serviceID='{sid}',serviceTime='{dts}' WHERE ResidentUID='{old_rid}' and serviceID='{old_sid}';")
    mydb.commit()
def drop_ras(rid,sid):
    c.execute(f"DELETE from resident_avails_services WHERE ResidentUID='{rid}' and serviceID='{sid}';")
    mydb.commit()

#security###################################################################################
def add_security(sid,fn,ln,phone,doj,shift):
    c.execute(f"INSERT INTO security values ('{sid}','{fn}','{ln}','{phone}','{doj}','{shift}');")
    mydb.commit()
def view_all_security():
    c.execute(f"SELECT * from security;")
    data=c.fetchall()
    return data
def get_security(sid):
    c.execute(f"SELECT * from security WHERE securityID='{sid}';")
    data=c.fetchall()
    return data
def edit_security(sid,fn,ln,phone,doj,shift,old_sid):
    c.execute(f"UPDATE security SET securityID='{sid}',Fname='{fn}',Lname='{ln}',phone='{phone}',doj='{doj}',shift='{shift}' WHERE securityID='{old_sid}';")
    mydb.commit()
def drop_security(sid):
    c.execute(f"DELETE from security WHERE securityID='{sid}';")
    mydb.commit()

#services###################################################################################
def add_service(id,cost,type):
    c.execute(f"INSERT INTO services values ('{id}',{cost},'{type}');")
    mydb.commit()
def view_all_services():
    c.execute("SELECT * FROM services;")
    data=c.fetchall()
    return data
def get_service(id):
    c.execute(f"SELECT * FROM services WHERE serviceID='{id}';")
    data=c.fetchall()
    return data
def view_all_serviceids():
    c.execute("SELECT serviceID FROM services;")
    data=c.fetchall()
    return data
def edit_service(id,cost,type,old_id):
    c.execute(f"UPDATE services SET serviceID='{id}',cost={cost},type='{type}' WHERE serviceID='{old_id}';")
    mydb.commit()
def drop_service(id):
    c.execute(f"DELETE FROM services WHERE serviceID='{id}';")
    mydb.commit()

#visitor###################################################################################
def add_visitor(vid,fid,fn,ln,purpose,phone,toen,toex):
    c.execute(f"INSERT INTO visitor values ('{vid}','{fid}','{fn}','{ln}','{purpose}','{phone}','{toen}','{toex}');")
    mydb.commit()
def view_all_visitors():
    c.execute(f"SELECT * FROM visitor;")
    data=c.fetchall()
    return data
def get_visitor(id):
    c.execute(f"SELECT * FROM visitor WHERE visitorID='{id}';")
    data=c.fetchall()
    return data
def edit_visitor(vid,fid,fn,ln,purpose,phone,toen,toex,old_vid):
    c.execute(f"UPDATE visitor SET visitorID='{vid}',flatID='{fid}',Fname='{fn}',Lname='{ln}',purpose='{purpose}',phonenumber='{phone}',time_of_entry='{toen}',time_of_exit='{toex}' WHERE visitorID='{old_vid}';")
    mydb.commit()
def drop_visitor(id):
    c.execute(f"DELETE FROM visitor WHERE visitorID='{id}';")
    mydb.commit()
