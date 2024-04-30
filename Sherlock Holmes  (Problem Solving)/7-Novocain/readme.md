## Challenge script

Remember? Did you Forgot about Sherlock main mission ? it was building quantum computers it is true that he tracks to find the scientists but also do what ever it takes to keep them on track.Quantum Computer is built in estimated time of 10 Sprints.After period of hard working the Vegapunk came to check about the work and asked sherlock for progress , Sherlock is just a Detective so help him out in some SQL queries to get the sprints done knowing that the Sprints has Multiple Tasks Or just One Task.The Statement Of the Challenge and details are included in Challenge drive file .

## Difficulty

HARD

Statement and details:
Tables: Sprint(Task_ID, week, leader_task,End_week,Team_ID)
//id is the assigned task of certain sprint , each sprint contains bunch of id or maybe one 
leader_task :Task Leader is Person .
Week:where the task started in work
Team_ID:the team who worked in the task
End_week where the task is finished ,

//Table 2:
Person(id,Name,Team_ID,age,work_days)
//Table 3: 
Team(id,Leader_Name)

Each task has 1 week of work ofcourse so we call it sprint when the end week of rows are consecutive we call it a sprint if it changed and not consecutive we are on another sprint
Give a SQL query give as an output the week and End week for sprints and  list them by weeks to finish the sprint then by Team_ID and sort them with Desc order so from the sprint has more weeks to the less one
hint: the listing by Team_Id will give you the team who started the first task of specific sprint .

SQL queries:
create table Sprints(Task_ID integer,week integer,leader_task varchar(255),End_week integer,Team_ID integer);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (1, 1, 'Tesla',2,1);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (2, 2,'Marie', 3,5);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (3, 4, 'James',5,3);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (4, 5, 'Marie',6,2);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (5, 6, 'luffy',7,2);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (6, 10,'mark', 11,8);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (7, 11, 'jeef',12,4);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (8, 13, 'vega',14,6);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (9, 15, 'Tesla',16,1);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (10, 16,'james', 17,4);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (11, 18,'vega', 19,2);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 19,'Bélanger', 20,5);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 20,'Marie', 21,1);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 21,'Bélanger', 22,9);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 22,'jeef', 23,3);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 25,'Tesla', 26,8);
INSERT INTO Sprints (Task_ID, week, leader_task,End_week,Team_ID) VALUES (12, 26,'Marie', 27,1);
INSERT INTO Sprints (Task_ID, week,leader_task, End_week,Team_ID) VALUES (12, 28,'Tesla', 29,4);



CREATE TABLE Person (id INTEGER PRIMARY KEY,Name VARCHAR(255),Team_ID INTEGER,age INTEGER,work_days VARCHAR(255));

INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (1, 'Tesla', 1, 30, 'Monday, Wednesday, Friday');
INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (2, 'James', 2, 28, 'Tuesday, Thursday');
INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (3, 'vega', 3, 35, 'Monday, Tuesday, Thursday');
INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (4, 'Bélanger', 8, 32, 'Wednesday, Friday');
INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (5, 'jeef', 5, 27, 'Monday, Wednesday, Friday');
INSERT INTO Person (id, Name, Team_ID, age, work_days) VALUES (6, 'Marie', 4, 29, 'Tuesday, Thursday');


CREATE TABLE Team (id INTEGER PRIMARY KEY,Leader_Name VARCHAR(255));
INSERT INTO Team (id, Leader_Name) VALUES (1, 'Tesla');
INSERT INTO Team (id, Leader_Name) VALUES (2, 'James');
INSERT INTO Team (id, Leader_Name) VALUES (3, 'vega');
INSERT INTO Team (id, Leader_Name) VALUES (4, 'Marie');
INSERT INTO Team (id, Leader_Name) VALUES (5, 'jeef');
INSERT INTO Team (id, Leader_Name) VALUES (6, 'Bélanger');
INSERT INTO Team (id, Leader_Name) VALUES (7, 'Tesla');
INSERT INTO Team (id, Leader_Name) VALUES (8, 'Bélanger');
INSERT INTO Team (id, Leader_Name) VALUES (9, 'vega');