import tabula
import pandas as pd
import PyPDF2
# pip install jpype1(Pacote permite executar código java diretamente de ambiente Python)

# Extraia as tabelas do PDF e salve em um arquivo CSV
tabula.convert_into(r"C:\Users\tecno\Downloads\pis.pdf", r"C:\Users\tecno\Downloads\pis.csv", output_format="csv", pages="all")

# Carregue o CSV em um DataFrame do pandas
df = pd.read_csv(r"C:\Users\tecno\Downloads\pis.csv")
print(df.head())

df = pd.read_csv(r"C:\Users\tecno\Downloads\pis.csv", delimiter=';') 

# Salve o DataFrame em um arquivo Excel
df.to_excel(r"C:\Users\tecno\Downloads\cofins.xlsx", index=False)

with open(r"C:\Users\tecno\Downloads\pis.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    texto = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        texto += page.extract_text()

# Exibe o texto extraído
print(texto)
