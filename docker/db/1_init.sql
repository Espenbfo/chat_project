CREATE TABLE client (
  client_id TEXT PRIMARY KEY,
  ip TEXT
);

CREATE TABLE session (
    session_id SERIAL PRIMARY KEY,
    client_id TEXT NOT NULL,
    created_time TIMESTAMP NOT NULL DEFAULT NOW(),
    query TEXT,
    response TEXT,
    CONSTRAINT fk_client
        FOREIGN KEY(client_id)
        REFERENCES client(client_id)
);