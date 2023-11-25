CREATE TABLE paginas (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL
);

CREATE TABLE Buscador (
    palabra varchar,
    documento INT NOT NULL REFERENCES paginas(id) ON DELETE CASCADE,
    repeticiones INT NOT NULL,
    CONSTRAINT tuplas UNIQUE (palabra, documento)
);