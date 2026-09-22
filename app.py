import csv
import random
import io
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('csv_file')
        postos_raw = request.form.get('postos', '')
        num_suplentes = int(request.form.get('num_suplentes', 0))

        # Limpamos as liñas baleiras e gardamos os nomes dos postos nunha lista
        postos = [p.strip() for p in postos_raw.split('\n') if p.strip()]
        num_principais = len(postos)

        if not file or file.filename == '':
            return render_template('index.html', erro="Tes que seleccionar un ficheiro CSV.")
            
        if num_principais == 0:
            return render_template('index.html', erro="Tes que indicar polo menos un posto a sortear.")

        # Lemos o ficheiro en texto
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        
        primeira_lina = stream.readline()
        delimitador = ';' if ';' in primeira_lina else ','
        stream.seek(0)
        
        csv_input = csv.reader(stream, delimiter=delimitador)
        
        socios = []
        for index, row in enumerate(csv_input):
            if len(row) >= 3:
                # Ignoramos a primeira fila se parece unha cabeceira
                if index == 0 and not row[0].strip().isdigit():
                    continue
                
                socios.append({
                    'numero': row[0].strip(),
                    'nome': row[1].strip(),
                    'apelidos': row[2].strip()
                })

        total_necesarios = num_principais + (num_principais * num_suplentes)

        if len(socios) < total_necesarios:
            erro = f"Erro: Necesítanse {total_necesarios} persoas (entre titulares e suplentes) pero o CSV só ten {len(socios)} socios válidos."
            return render_template('index.html', erro=erro)

        # Sorteo
        seleccionados = random.sample(socios, total_necesarios)

        # Estruturar o resultado cos nomes dos postos escollidos
        xunta = []
        idx = 0
        for nome_posto in postos:
            principal = seleccionados[idx]
            idx += 1
            suplentes = []
            for j in range(num_suplentes):
                suplentes.append(seleccionados[idx])
                idx += 1
                
            xunta.append({
                'cargo': nome_posto,
                'principal': principal,
                'suplentes': suplentes
            })

        return render_template('resultado.html', xunta=xunta)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)