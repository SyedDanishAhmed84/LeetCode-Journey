SELECT p.firstName,p.lastName,s.city,s.state
FROM Address s
RIGHT JOIN Person p
ON s.personId=p.personId;