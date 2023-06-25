--- 25-06-2023 11:54:02
--- teacher.db
SELECT * FROM School;

--- 25-06-2023 11:54:09
--- teacher.db
SELECT * FROM Students;

--- 25-06-2023 14:20:31
--- teacher.db
/***** ERROR ******
no such column: Students.school_name
 ----- 
SELECT Students.student_id, Students.school_name, School.school_id, School.school_name
FROM Students
JOIN School ON Students.student_id = School.student_id;
*****/

--- 25-06-2023 14:20:56
--- teacher.db
/***** ERROR ******
no such column: Students.student_id
 ----- 
SELECT Students.student_id, Students.school_name, School.school_id, School.school_name
FROM School
JOIN School ON Students.student_id = School.student_id;
*****/

--- 25-06-2023 14:23:24
--- teacher.db
/***** ERROR ******
no such column: Students.Student_Id
 ----- 
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM School
JOIN School ON Students.student_id = School.student_id;
*****/

--- 25-06-2023 14:23:46
--- teacher.db
/***** ERROR ******
no such column: School.student_id
 ----- 
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM Students
JOIN School ON Students.student_id = School.student_id;
*****/

--- 25-06-2023 14:24:22
--- teacher.db
/***** ERROR ******
no such column: School.student_id
 ----- 
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM Students
JOIN School ON Students.student_id = School.student_id;
*****/

--- 25-06-2023 14:25:16
--- teacher.db
/***** ERROR ******
no such column: School.Student_Id
 ----- 
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM Students
JOIN School ON Students.Student_Id = School.Student_Id;
*****/

--- 25-06-2023 14:25:56
--- teacher.db
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM Students
JOIN School ON Students.School_Id = School.School_Id;

