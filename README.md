# MySQL-Database-Management-GUI
Overview
This project is a graphical user interface (GUI) application for managing MySQL databases, created using Python with the customtkinter and tkinter libraries. The application provides functionalities to log in to a MySQL server, select databases and tables, view table data, and perform basic CRUD (Create, Read, Update, Delete) operations.

# Features
#### Login Page:
- Users can log in with their MySQL credentials.
- The application verifies credentials before granting access.

#### Database Selection:
- Displays a list of all databases on the server.
- Users can select a database to work with.

#### Table Selection:

- Lists all tables within the selected database.
- Users can select a table to view and manage its data.

#### View Table Data:

- Displays data from the selected table.
- Shows the first 10 rows of data by default.

#### Column Names Display:

- Automatically retrieves and displays column names for the selected table.

#### Data Operations:

* Insert Data: Allows users to add new rows to the selected table.
* Delete Data: Users can delete rows based on a specified primary key.
* Update Data: Provides an interface for updating existing rows (currently, functionality to be implemented).

### Show Databases:

Click the `Show Databases` button to display a list of databases.
Select a database from the list.
#### Show Tables:

Click the `Select Table` button to display tables within the selected database.
Select a table to view its data.
#### View Data:

Data from the selected table is displayed in a list format.
Column names are displayed at the top of the table.
#### Insert Data:

Click `INSERT` to open a form for adding new rows to the table.
Enter values for each column and click "SUBMIT."
#### Delete Data:

Click `DELETE` to open a form for deleting rows based on the primary key.
Enter the primary key value and click "SUBMIT."

#### Update Data:
Click `UPDATE` to open the update interface (currently, functionality to be implemented).
Error Handling
The application displays error messages using tkinter's messagebox for various issues like failed login attempts, database connection errors, and SQL query errors.

---


#### Future Improvements
Implement the update functionality to modify existing rows.
Enhance the user interface for better usability and aesthetics.
Add more data validation and error handling mechanisms.


> # Contributions
> ### Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
