# Sorteo Xunta Electoral - Ulloa Viva

Esta é unha aplicación web sinxela desenvolvida en Python (Flask) para realizar o sorteo dos membros da Xunta Electoral da Plataforma Ulloa Viva.

Permite cargar unha lista de socios en formato CSV, definir os nomes dos cargos (Presidencia, Secretaría, etc.) e escoller cantos suplentes se necesitan por cada cargo. A aplicación encárgase de facer o sorteo de forma aleatoria e sen repeticións.

## Requisitos do CSV

O ficheiro CSV debe ter tres columnas separadas por comas (`,`) ou puntos e comas (`;`). Non importa se inclúe unha liña de cabeceira, a aplicación ignóraa automaticamente.

Formato esperado:

```
Numero,Nome,Apelidos
1,Sabela,Otero Villar
2,Brais,Varela Seixas
3,Uxía,Piñeiro Freire

```

## Execución en Local

Se tes Python instalado na túa máquina, podes executar a aplicación directamente:

1. Crea un contorno virtual (opcional):

   ```
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   
   ```

2. Instala as dependencias:

   ```
   pip install -r requirements.txt
   
   ```

3. Executa a aplicación:

   ```
   python app.py
   
   ```

4. Abre o teu navegador e visita: `http://localhost:5000`

## Execución con Contedores

Para despregar a aplicación usando o `Containerfile` incluído:

1. Constrúe a imaxe:

   ```
   podman build -t sorteo-ulloa .
   
   ```

2. Arranca o contedor:

   ```
   podman run -d -p 5000:5000 --name sorteo-ulloa-app sorteo-ulloa
   
   ```

3. Abre o teu navegador e visita: `http://localhost:5000`