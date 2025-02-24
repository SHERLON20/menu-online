import psycopg2

conn = psycopg2.connect(
    database= 'pedidos',
    user= 'postgres',
    password='lelobarril2014',
    host= 'pedidos.ckdiuc26m3ob.us-east-1.rds.amazonaws.com',
    port = '5432',
)

if conn:
    print('conectado com sucesso')