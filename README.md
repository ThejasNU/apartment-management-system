# Apartment management system

Web app built using streamlit, using which the user can select a table and select any operation among CRUD operations to perform on it

### How to run it on your system

1. Clone the repo and create the database using the SQL commands in `queries` directory
2. In the root directory open a terminal and execute `pip install -r requirements.txt`
3. Change the username,password,database name in `/src/database.py` according to what you have set
4. Start the mysql server
5. Open terminal in `src` directory and execute the command `streamlit run main.py`
6. Now open `localhost:8501` on your browser to see the web app
