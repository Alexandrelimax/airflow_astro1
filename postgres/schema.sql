CREATE TABLE IF NOT EXISTS vehicle_fipe (
    id SERIAL PRIMARY KEY,
    valor NUMERIC(10, 2) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(200) NOT NULL,
    ano_modelo CHAR(5) NOT NULL,
    combustivel CHAR(10) NOT NULL,
    codigo_fipe CHAR(20) NOT NULL,
    mes_referencia VARCHAR(100) NOT NULL, -- aprimorar para DATE futuramente
    autenticacao VARCHAR(100) NOT NULL,
    tipo_veiculo VARCHAR(100) NOT NULL, -- aprimorar para ENUM futuramente
    sigla_combustivel CHAR(1) NOT NULL,
    data_consulta VARCHAR(100) NOT NULL -- aprimorar para DATE futuramente
);