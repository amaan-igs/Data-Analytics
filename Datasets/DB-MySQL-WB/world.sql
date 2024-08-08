USE WORLD;

SELECT *
FROM city;

SELECT Name,'CountryCode'
FROM city;

SELECT Name,'CountryCode'
FROM city
WHERE CountryCode = 'PAK';

SELECT * FROM city WHERE population <100000;

SELECT *
FROM city
WHERE CountryCode = 'PAK' AND Name = 'Karachi';

SELECT *
FROM city
WHERE CountryCode = 'PAK'  AND population > 100000;

SELECT *
FROM city
WHERE population > 9269265;

SELECT DISTINCT Countrycode FROM city;

SELECT *
FROM city
WHERE CountryCode = 'PAK' OR CountryCode =  'AFG'