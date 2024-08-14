from flask import Flask, render_template, request, redirect, url_for
import os

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
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('main'))
    
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
