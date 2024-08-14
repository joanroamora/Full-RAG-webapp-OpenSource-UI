import os
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp/'

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/index')
def main():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=uploaded_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return redirect(request.url)
    
    files = request.files.getlist('files[]')
    
    for file in files:
        if file.filename == '':
            continue
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
    
    return redirect(url_for('main'))

@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')
    if filename:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'status': 'File deleted'}), 200
    return jsonify({'status': 'File not found'}), 404

@app.route('/load', methods=['POST'])
def load_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])

    if not files:
        return jsonify({'status': 'error', 'message': 'Agregue o arrastre archivos pdf al sistema.'})

    files_to_send = {}
    file_handlers = []

    try:
        for filename in files:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file_data = open(filepath, 'rb')
            files_to_send[filename] = file_data
            file_handlers.append(file_data)  # Guardar el manejador de archivo para cerrarlo después

        response = requests.post('http://127.0.0.1:5001/upload', files=files_to_send)
        
        if response.status_code == 200:
            # Eliminar archivos de la carpeta temp después de un envío exitoso
            for filepath in files_to_send.values():
                filepath.close()  # Cerrar el archivo después de que se haya enviado
                os.remove(filepath.name)
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Error al enviar los archivos.'})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
    finally:
        # Asegurarse de que todos los archivos se cierren incluso si hay un error
        for file_data in file_handlers:
            file_data.close()

if __name__ == "__main__":
    app.run(debug=True)
