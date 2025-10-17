create database clinica;
use clinica;
create table pacientes(
id_paciente int auto_increment primary key,
nombre varchar(50),
edad int,
genero varchar(10),
diagnostico varchar(159)
);
insert into pacientes(nombre,edad,genero,diagnostico) values ('Ana Pérez',30,'Femenino','Hipertencion');
insert into pacientes(nombre,edad,genero,diagnostico) values ('Mel Brenan',18,'Femenino','Ninguno');
insert into pacientes(nombre,edad,genero,diagnostico) values ('Adriana Lima',25,'Femenino','Anemia');
insert into pacientes(nombre,edad,genero,diagnostico) values ('Roberto Lopez',25,'Masculino','Hipotiroidismo');
update pacientes set diagnostico="Anemia" where id_paciente=1;
delete from pacientes where id_paciente=1;
select*from pacientes;
create table doctores(
id_doctor int auto_increment primary key,
nombre varchar(50),
carnetIdentidad varchar(10),
correo varchar(50),
fechaIngreso date
);
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Fabi Perez',24356879,'fabi@gmail.com','2000-02-2');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Ana Gabriel',12121221,'anitamimol@gmail.com','2003-08-25');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Adriana Lima',43658709,'DRinia@est.univalle.edu','1999-09-19');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Rodrigo Rodriguez',59283614,'rr@gmail.com','2006-12-01');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Isabel Pantoja',25361489,'ip@gmail.com','1958-09-19');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Rosario Tijeras',20001112,'tijeritaspriv@gmail.com','2025-10-25');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Lucas Paz',25262429,'pazEnElMundo@gmail.com','1685-09-16');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Kimberly Loaiza',89868214,'linduritaCorazon@gmail.com','1935-04-27');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('Kenia Oz',25689147,'kenini@gmail.com','2012-06-20');
insert into doctores(nombre,carnetIdentidad,correo,fechaIngreso) values ('JD Pantoja',35363124,'amores@gmail.com','2008-08-8');
select*from doctores;
delete from doctores where id_doctor=3;
update doctores set fechaIngreso="2025-10-17" where id_doctor=5;
select*from doctores;










