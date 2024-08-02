# Library Database Management System

## Overview

The Library Database Management System (LibraryDB) is a comprehensive SQL-based project designed to manage library 
operations effectively. This system includes functionalities for managing authors, books, members, loans, and 
reservations. Additionally, it incorporates advanced SQL features such as functions, stored procedures, events, 
and triggers to automate and streamline library management tasks.

## Features

- **Author Management**: Store and manage detailed information about authors.
- **Book Management**: Keep track of books, including details about genre, publication year, ISBN, and more.
- **Member Management**: Handle member data, including personal details and membership status.
- **Loan Management**: Manage book loans, including loan dates, due dates, return dates, and fines.
- **Reservation Management**: Allow members to reserve books and manage reservation statuses.
- **Automated Processes**: Use events, functions, and triggers to automate tasks such as fine calculation and reservation expiry.

## Project Structure

The project is organized as follows:

```
library-database/
├── sql/
│   ├── librarydb.sql
│   ├── functions.sql
│   ├── events.sql
│   ├── procedures.sql
│   ├── triggers.sql
├── images/
│   ├── ERD.png
├── README.md
```

### File Descriptions

- **librarydb.sql**: Contains SQL commands to create the database and tables, and to insert sample data.
- **functions.sql**: Contains SQL commands to create stored functions for the database.
- **events.sql**: Contains SQL commands to create events for automated tasks within the database.
- **procedures.sql**: Contains SQL commands to create stored procedures for complex operations in the database.
- **triggers.sql**: Contains SQL commands to create triggers that automatically perform actions in response to database changes.
- **images/ERD.png**: Contains the image for the ERD
- **README.md**: Provides an overview of the project, setup instructions, and usage information.


### Database Schema

The LibraryDB database schema is designed to capture all necessary information related to the library's operations. 
An Entity-Relationship Diagram (ERD) is included to illustrate the relationships between different entities in the 
database.

#### ERD

The ERD includes the following tables:

- **Authors**: Stores detailed information about authors.
- **Books**: Contains information about books, including their authors, genres, and publication details.
- **Members**: Stores member details, including personal information and membership status.
- **Loans**: Manages book loans, tracking loan dates, due dates, and fines.
- **Reservations**: Handles book reservations, tracking reservation dates and statuses.

<img src="https://github.com/mrowurakwarteng/library-management-system/blob/main/images/ERD.png">

### Sample Data

The database includes sample data for authors, books, members, loans, and reservations to help you get started quickly.

### Functions

Functions are used to perform specific operations within the database. Two key functions are provided:

- **AddReservation**: Adds a new reservation for a book by a member.
- **ExpireReservation**: Updates the status of a reservation to 'Expired'.

### Events

Events automate recurring tasks within the database. One key event is provided:

- **DailyFineCalculation**: Calculates fines for overdue loans on a daily basis.

### Procedures

Stored procedures perform complex operations that might require multiple SQL statements. Two key procedures are provided:

- **CalculateFine**: Calculates fines for overdue books.
- **ExtendLoan**: Extends the loan period for a book.

### Triggers

Triggers are used to automatically perform actions in response to certain changes in the database. One key trigger is 
provided:

- **ExpireReservationsTrigger**: Automatically expires reservations that are past their pickup date.

## Setup Instructions

To set up the LibraryDB system, follow these steps:

1. **Create the Database and Tables**:
    - Execute the SQL commands in `librarydb.sql` to create the database and tables.
    
2. **Insert Sample Data**:
    - Insert sample data using the provided SQL commands in `librarydb.sql` to populate the database with initial records.

3. **Create Functions, Events, Procedures, and Triggers**:
    - Execute the SQL commands in `functions.sql`, `events.sql`, `procedures.sql`, and `triggers.sql` to create the necessary 
      functions, events, procedures, and triggers.

4. **Verify the Setup**:
    - Verify the setup by querying the tables and checking the data to ensure everything is working correctly.

## Usage

Once the database is set up, you can perform various operations such as:

- Adding new authors, books, and members.
- Recording book loans and returns.
- Managing book reservations.
- Automatically calculating fines for overdue books.
- Extending loan periods for members.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License: [LICENSE.md](LICENSE.md).

---