CREATE TABLE korisnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime CHAR(50) NOT NULL,
    prezime CHAR(50) NOT NULL,
    email CHAR(50) NOT NULL,
    password CHAR(50) NOT NULL
);

CREATE TABLE kategorija (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv VARCHAR(100)
);

CREATE TABLE trosak (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum DATE,
    id_korisnika INT,
    id_kategorije INT,
    cijena FLOAT,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (id_kategorije) REFERENCES kategorija(id) ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO korisnik (id, ime, prezime, email, password) VALUES
    (1, 'Pero', 'Peric', 'pp@tvz.hr', '1dva3');

INSERT INTO kategorija (naziv) VALUES
    ('Dnevni troskovi'),
    ('Namirnice'),
    ('Struja'),
    ('Plin'),
    ('Telefon_internet'),
    ('Tv'),
    ('Komunalno'),
    ('Kredit');

INSERT INTO trosak (datum, id_korisnika, id_kategorije, cijena) VALUES
    ('04.01.2023.', 1, 1, '8.54'),
    ('09.01.2023.', 1, 2, '78.87'),
    ('17.01.2023.', 1, 3, '23.30'),
    ('17.01.2023.', 1, 4, '134.79'),
    ('17.01.2023.', 1, 5, '14.50'),
    ('17.01.2023.', 1, 6, '8.27'),
    ('17.01.2023.', 1, 7, '11.65'),
    ('01.01.2023.', 1, 1, '6.50'),
    ('04.01.2023.', 1, 1, '13.73'),
    ('11.02.2023.', 1, 3, '25.37'),
    ('15.02.2023.', 1, 2, '54.32'),
    ('16.02.2023.', 1, 4, '104.31'),
    ('18.02.2023.', 1, 1, '5.20'),
    ('24.02.2023.', 1, 5, '16.57'),
    ('24.02.2023.', 1, 6, '8.27'),
    ('24.02.2023.', 1, 7, '11.65'),
    ('09.03.2023.', 1, 3, '21.15'),
    ('10.03.2023.', 1, 1, '4.15'),
    ('13.03.2023.', 1, 2, '97.98'),
    ('16.03.2023.', 1, 1, '11.48'),
    ('19.03.2023.', 1, 5, '12.39'),
    ('27.03.2023.', 1, 4, '159.11'),
    ('27.03.2023.', 1, 7, '11.65'),
    ('27.03.2023.', 1, 6, '8.27'),
    ('28.03.2023.', 1, 2, '43.87'),
    ('01.04.2023.', 1, 1, '25.48'),
    ('10.04.2023.', 1, 4, '117.69'),
    ('12.04.2023.', 1, 5, '14.91'),
    ('12.04.2023.', 1, 3, '19.78'),
    ('18.04.2023.', 1, 6, '8.27'),
    ('20.04.2023.', 1, 2, '137.29'),
    ('25.04.2023.', 1, 7, '11.65'),
    ('25.04.2023.', 1, 1, '23.12'),
    ('01.05.2023.', 1, 2, '44.43'),
    ('09.05.2023.', 1, 5, '19.52'),
    ('09.05.2023.', 1, 3, '19.55'),
    ('13.05.2023.', 1, 1, '5.68'),
    ('17.05.2023.', 1, 1, '15.97'),
    ('19.05.2023.', 1, 2, '34.15'),
    ('26.05.2023.', 1, 4, '45.37'),
    ('26.05.2023.', 1, 6, '8.27'),
    ('26.05.2023.', 1, 7, '11.65'),
    ('02.06.2023.', 1, 1, '9.99'),
    ('10.06.2023.', 1, 3, '29.94');


