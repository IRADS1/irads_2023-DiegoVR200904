create database greengrocer;

use greengrocer;

create table Employees(
	EmployeeID int not null auto_increment,
	LastName varchar(30),
	FirstName varchar(25),
	BirthDate date,
	Sex varchar(1),
	Title varchar(20),
	Salary float,
	Constraint PK_Employee Primary Key (EmployeeID)
);

insert into Employees(EmployeeID, LastName, FirstName, BirthDate, Sex, Title, Salary)
values(1, 'Valenzuela Chavez', 'Abel', '1967-12-31', 'M', 'Owner', 5000);

insert into Employees(EmployeeID, LastName, FirstName, BirthDate, Sex, Title, Salary)
values(2, 'Rivera', 'Carlos', '1998-06-23', 'M', 'Manager', 2000);

insert into Employees(EmployeeID, LastName, FirstName, BirthDate, Sex, Title, Salary)
values(3, 'Hernandez', 'Yamileth', '1996-06-14', 'F', 'Cashier', 1500);

insert into Employees(EmployeeID, LastName, FirstName, BirthDate, Sex, Title, Salary)
values(4, 'Gonzales', 'Ramiro', '2000-04-09', 'M', 'Loader', 1500);

insert into Employees(EmployeeID, LastName, FirstName, BirthDate, Sex, Title, Salary)
values(5, 'Portillo', 'Hernan', '1999-07-24', 'M', 'Loader', 1500);

create table Suppliers(
	SupplierID int not null auto_increment,
	Name varchar(35),
	Address varchar(25),
	Contact varchar(25),
	Constraint PK_Supplier Primary Key (SupplierID)
);

insert into Suppliers(SupplierID, Name, Address, Contact)
values(1, 'Frutas Oliver', 'Riveras 1234', 'Mary Hernandez');

insert into Suppliers(SupplierID, Name, Address, Contact)
values(2, 'Surtifrut', 'Jardines Aeropuerto 2345', 'Luis Carrillo');

insert into Suppliers(SupplierID, Name, Address, Contact)
values(3, 'Disfruta', 'Altavista 1367', 'Rosalina Rivera');

insert into Suppliers(SupplierID, Name, Address, Contact)
values(4, 'Agrofruts', 'Blvd. Zaragoza 5631', 'James Field');

insert into Suppliers(SupplierID, Name, Address, Contact)
values(5, 'Danys', 'Blvd. Independencia', 'Daniel Arreola');

create table Products(
	ProductID int not null auto_increment,
	ProductName varchar(30),
	UnitPrice float,
	Unit varchar(20),
	Stock float,
	SupplierID int null,
	Constraint PK_Products Primary Key (ProductID)
);

insert into Products(ProductID, ProductName, UnitPrice, Unit, Stock, SupplierID)
values(1, 'Tomate', 35, 'Kilogramos', 40, 1);

insert into Products(ProductID, ProductName, UnitPrice, Unit, Stock, SupplierID)
values(2, 'Pera', 25, 'Kilogramos', 20, 2);

insert into Products(ProductID, ProductName, UnitPrice, Unit, Stock, SupplierID)
values(3, 'Manzana', 20, 'Kilogramos', 60, 2);

insert into Products(ProductID, ProductName, UnitPrice, Unit, Stock, SupplierID)
values(4, 'Mango', 30, 'Kilogramos', 50, 3);

insert into Products(ProductID, ProductName, UnitPrice, Unit, Stock, SupplierID)
values(5, 'Chile Jalapenio', 30, 'Kilogramos', 40, 4);

create table Costumers(
	CostumerID int not null auto_increment,
	CostumerName varchar(30),
	PhoneNumber varchar(20),
	Address varchar(25),
    Constraint PK_Costumers Primary Key (CostumerID)
);

insert into Costumers(CostumerID, CostumerName, PhoneNumber, Address)
values(1, 'Carmen Herrera', '123-456-7890', 'Francisco Villa 1234');

insert into Costumers(CostumerID, CostumerName, PhoneNumber, Address)
values(2, 'Emilia Hernandez', '121-452-7893', 'Av. De la Madrid 2434');

insert into Costumers(CostumerID, CostumerName, PhoneNumber, Address)
values(3, 'Luis Ramirez', '125-446-7230', 'Av. Aztecas 1294');

insert into Costumers(CostumerID, CostumerName, PhoneNumber, Address)
values(4, 'Ernesto Rios', '112-456-7898', 'Av. Tecnologico 9864');

insert into Costumers(CostumerID, CostumerName, PhoneNumber, Address)
values(5, 'Maya Granada', '113-874-7120', 'Gladolias 6728');
