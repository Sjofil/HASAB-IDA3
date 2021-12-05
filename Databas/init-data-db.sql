-- initialize Types table

INSERT INTO Types (ID, Industry)
VALUES (1, "Hotell");

INSERT INTO Types (ID, Industry)
VALUES (2, "Restaurang");

INSERT INTO Types (ID, Industry)
VALUES (3, "Resebyråer");


-- Insert Users data --

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info.marinaplaza@elite.se", "Elite Hotel Marina Plaza", 1, 0);

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info.mollberg@elite.se", "Elite Hotel Mollberg", 1, 0);

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("cl.grandhelsingborg@choice.se", "Clarion Grand Hotel", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("cl.grandhelsingborg@choice.se", "Clarion Grand Hotel", 1, 0);

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("co.nouveau@choice.se", "Comfort Hotel", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("reception@thevaulthotel.se", "The Vault", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@hotellviking.se", "V Hotel", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@hotelkarnan.se", "First Hotel Kärnan", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("helsingborg@scandichotels.com", "Scandic Nord", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("helsingborg@gmorninghotels.se", "Good Morning Hotels", 1, 0);


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("kathy.adenlof@amasten.se", "Continental Apartments Hotels", 1, 0);
-- 19 apartments

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@hotellstadsparken.se", "Hotel Stadsparken", 1, 0);
-- 64 rooms

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("linnea@hotell-linnea.se", "Hotell Linnéa", 1, 0);
-- 37 rooms

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@villathalassa.se", "Villa Thalassa", 1, 0);
-- 34 rooms

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@cityvandrarhemmet.com", "Cityvandrarhem", 1, 0);
-- 41 rooms

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("boka@miatorp.nu", "STF Miatorp Hostel & Hotel", 1, 0);
-- 75 - 100 beds


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info.helsingborg@radissonblu.com", "Radisson Blu Metropol Hotel", 1, 0);
-- 205 rooms

INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("cl.seau@choice.se", "Clarion Hotel SeaU", 1, 0);
-- 250 rooms


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("info@sundsgarden.se", "Hotell Sundsgården", 1, 0);
-- 94 rooms


INSERT INTO Users (Email, Name, Type_ID, Submitted)
VALUES ("group.sweden@scandichotels.com", "Scandic Oceanhamnen", 1, 0);
-- 180 rooms


-- Insert Question data --

-- Q1 ------------------------------------------------
INSERT INTO Questions (Type_ID, Question_text)
VALUES (1, "Har ert hotell någon miljöcertifiering?");
-- Om ja:

INSERT INTO Questions (Type_ID, Question_text)
VALUES (1, "Vilken miljöcertifiering har ni?");

INSERT INTO Questions (Type_ID, Question_text)
VALUES (1, "Hur många rum har ert hotell?");


-- Q2 -------------------------------------------------
INSERT INTO Questions (Type_ID, Question_text)
VALUES (1, "Jobbar ni aktivt med att minska matsvinnet? Om ja, hur stor del i % har ni lyckats minska ert matsvinn?");
-- Om ja:


INSERT INTO Questions (Type_ID, Question_text)
VALUES (1, "Hur många procent jämfört med föregående år av ert årliga matsvinn har ni lyckats minska?");


-- Q3 -------------------------------------------------

INSERT INTO Questions (ID, Type_ID, Question_text)
VALUES (1, "Jobbar ni aktivt med att minska engångsartiklar och plastmaterial?");


INSERT INTO Questions (ID, Type_ID, Question_text)
VALUES (3, 1, "Sorterar ni organiskt avfall?");

INSERT INTO Questions (ID, Type_ID, Question_text)
VALUES (3, 1, "Finns det en publicerad publik rapport rörande resultaten av ert miljöarbete?");
-- Följdfråga finns 


-- Insert Answers --



