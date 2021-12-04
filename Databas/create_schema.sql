SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE Types;
DROP TABLE Users;
DROP TABLE Questions;
DROP TABLE Answers;

CREATE TABLE Types (
  ID int NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE Users (
  Email varchar(45),
  Name varchar (45),
  Type_ID int DEFAULT NULL,
  Submitted tinyint DEFAULT NULL,
  PRIMARY KEY (Email),
  KEY type_idx (Type_ID),
  FOREIGN KEY (Type_ID) REFERENCES Types (ID)
);

CREATE TABLE Questions (
  ID int NOT NULL AUTO_INCREMENT,
  Type_ID int DEFAULT NULL,
  Next_question longtext,
  PRIMARY KEY (ID),
  KEY type_idx (Type_ID)
  -- CONSTRAINT `typek` FOREIGN KEY (`Type_ID`) REFERENCES `type` (`ID`)
);


CREATE TABLE Answers (
  ID int NOT NULL AUTO_INCREMENT,
  Answer varchar(45) NOT NULL,
  Question_ID int DEFAULT NULL,
  User_ID int DEFAULT NULL,
  UNIQUE KEY index_UNIQUE (ID),
  KEY qtype_idx (Question_ID),
  KEY utype_idx (User_id),
  CONSTRAINT qtype FOREIGN KEY (Question_ID) REFERENCES questions (ID), 
  CONSTRAINT utype FOREIGN KEY (User_id) REFERENCES user (ID)
);

SET FOREIGN_KEY_CHECKS = 1;


