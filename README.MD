# Full-RAG-webapp-OpenSource-UI 🇺🇸

## Project Description

**Full-RAG-webapp-OpenSource-UI** is the frontend component of the Full-RAG system, providing an intuitive user interface for interacting with the backend services. This web application allows users to upload PDF files, manage these files, and submit questions that will be answered based on the content of the uploaded documents. The frontend is built using Flask and offers features such as drag-and-drop file uploading, file management, and interaction with a machine learning backend for document-based query responses.

## Project Structure

### 1. `app.py`
This is the main file that sets up the Flask web server and handles the routing for the application.

#### Main Routes:

- **`/`**: Serves the homepage of the application, which acts as an entry point.
- **`/index`**: Displays the main interface where users can upload and manage their PDF files.
- **`/upload`**: Handles the file upload process, allowing users to add PDF files to the system.
- **`/delete`**: Allows users to delete previously uploaded files from the system.
- **`/load`**: Sends the uploaded files to the backend service for processing and subsequently clears the temporary storage.

#### Key Functions:

- **`upload_file()`**: Processes file uploads via POST requests. The function checks for valid PDF files and saves them to a temporary directory.
- **`delete_file()`**: Deletes a specified file from the temporary directory.
- **`load_files()`**: Sends the uploaded files to the backend for processing and deletes them locally once successfully sent.

### 2. `index.html`
This is the main HTML template for the user interface. It includes the following key components:

- **File Upload Section**: A drag-and-drop area or file selection input for uploading PDFs.
- **File List**: Displays the currently uploaded files and allows users to delete them.
- **Control Panel**: Allows users to set parameters like temperature, role, and input questions before sending them to the backend.
- **Output Area**: Displays the response from the backend once the query has been processed.

### 3. JavaScript Functions in `index.html`

- **`dropHandler(event)`**: Manages the drag-and-drop functionality for file uploads.
- **`fileInputHandler(event)`**: Handles file selection through the input field.
- **`uploadFiles(formData)`**: Sends the selected files to the server via POST request.
- **`deleteFile(filename)`**: Deletes a selected file from the server.
- **`loadFiles()`**: Sends all uploaded files to the backend for processing.
- **`doIt()`**: Validates the input fields and sends a request to the backend to process the user's question based on the uploaded documents.

## Problem Solved

The **Full-RAG-webapp-OpenSource-UI** provides a user-friendly interface for interacting with the backend document processing and query system. It simplifies the process of uploading, managing, and querying documents, making it accessible even to users without technical expertise. This interface is essential for applications where users need to extract information from documents dynamically and efficiently.

## Usage and Deployment

To run this frontend, execute the `app.py` file. The Flask server will start and serve the UI at `http://localhost:5000`. Users can upload their documents, manage them, and interact with the backend through this interface. The UI is designed to be responsive and easy to use, supporting both drag-and-drop and traditional file upload methods.

---

# Full-RAG-webapp-OpenSource-UI 🇨🇴

## Descripción del proyecto

**Full-RAG-webapp-OpenSource-UI** es el componente frontend del sistema Full-RAG, proporcionando una interfaz de usuario intuitiva para interactuar con los servicios del backend. Esta aplicación web permite a los usuarios subir archivos PDF, gestionar estos archivos y enviar preguntas que serán respondidas basándose en el contenido de los documentos cargados. El frontend está construido utilizando Flask y ofrece funcionalidades como carga de archivos mediante arrastrar y soltar, gestión de archivos e interacción con un backend de aprendizaje automático para respuestas basadas en documentos.

## Estructura del proyecto

### 1. `app.py`
Este es el archivo principal que configura el servidor web Flask y maneja las rutas de la aplicación.

#### Rutas principales:

- **`/`**: Sirve la página de inicio de la aplicación, que actúa como un punto de entrada.
- **`/index`**: Muestra la interfaz principal donde los usuarios pueden cargar y gestionar sus archivos PDF.
- **`/upload`**: Maneja el proceso de carga de archivos, permitiendo a los usuarios agregar archivos PDF al sistema.
- **`/delete`**: Permite a los usuarios eliminar archivos previamente cargados del sistema.
- **`/load`**: Envía los archivos cargados al servicio backend para su procesamiento y posteriormente limpia el almacenamiento temporal.

#### Funciones clave:

- **`upload_file()`**: Procesa la carga de archivos a través de solicitudes POST. La función verifica los archivos PDF válidos y los guarda en un directorio temporal.
- **`delete_file()`**: Elimina un archivo especificado del directorio temporal.
- **`load_files()`**: Envía los archivos cargados al backend para su procesamiento y los elimina localmente una vez enviados con éxito.

### 2. `index.html`
Esta es la plantilla HTML principal para la interfaz de usuario. Incluye los siguientes componentes clave:

- **Sección de carga de archivos**: Un área de arrastrar y soltar o un input de selección de archivos para subir PDFs.
- **Lista de archivos**: Muestra los archivos actualmente cargados y permite a los usuarios eliminarlos.
- **Panel de control**: Permite a los usuarios configurar parámetros como temperatura, rol y preguntas de entrada antes de enviarlos al backend.
- **Área de resultados**: Muestra la respuesta del backend una vez que se ha procesado la consulta.

### 3. Funciones JavaScript en `index.html`

- **`dropHandler(event)`**: Gestiona la funcionalidad de arrastrar y soltar para la carga de archivos.
- **`fileInputHandler(event)`**: Maneja la selección de archivos a través del campo de input.
- **`uploadFiles(formData)`**: Envía los archivos seleccionados al servidor mediante una solicitud POST.
- **`deleteFile(filename)`**: Elimina un archivo seleccionado del servidor.
- **`loadFiles()`**: Envía todos los archivos cargados al backend para su procesamiento.
- **`doIt()`**: Valida los campos de entrada y envía una solicitud al backend para procesar la pregunta del usuario basada en los documentos cargados.

## Problema que resuelve

**Full-RAG-webapp-OpenSource-UI** proporciona una interfaz fácil de usar para interactuar con el sistema de procesamiento de documentos y consultas del backend. Simplifica el proceso de cargar, gestionar y consultar documentos, haciéndolo accesible incluso para usuarios sin conocimientos técnicos. Esta interfaz es esencial para aplicaciones donde los usuarios necesitan extraer información de documentos de manera dinámica y eficiente.

## Uso y despliegue

Para ejecutar este frontend, ejecute el archivo `app.py`. El servidor Flask comenzará y servirá la UI en `http://localhost:5000`. Los usuarios pueden cargar sus documentos, gestionarlos e interactuar con el backend a través de esta interfaz. La UI está diseñada para ser receptiva y fácil de usar, soportando tanto métodos de arrastrar y soltar como de carga de archivos tradicionales.
