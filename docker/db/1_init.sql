CREATE TABLE client (
  client_id INT PRIMARY KEY,
  ip TEXT
);

CREATE TABLE session (
    session_id INT PRIMARY KEY,
    client_id INT,
    text TEXT,
    CONSTRAINT fk_client
        FOREIGN KEY(client_id)
        REFERENCES client(client_id)
);