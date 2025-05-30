from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Print current working directory for debugging
print("Current working directory:", os.getcwd())

# Ensure the static folder exists
static_folder = os.path.join(os.getcwd(), 'static')
if not os.path.exists(static_folder):
    os.makedirs(static_folder, exist_ok=True)
    print(f"Created static folder at: {static_folder}")

# Serve the index.html file from the root directory
@app.route('/')
def serve_index():
    file_path = os.path.join(os.getcwd(), 'index.html')
    if not os.path.exists(file_path):
        abort(404, description=f"Error: {file_path} not found")
    return send_file(file_path)

# Serve static files (images, CSS, CSVs) from the static folder
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_folder, filename)

# Custom routes for specific files (optional fallback or override)
@app.route('/ScrapingYt.jpg')
def serve_scrapingyt_image():
    return send_from_directory(static_folder, 'ScrapingYt.jpg', mimetype='image/jpeg')

@app.route('/Trans_Jatim.png')
def serve_trans_jatim_image():
    return send_from_directory(static_folder, 'Trans_Jatim.png', mimetype='image/png')

@app.route('/transjatim_comments.csv')
def serve_transjatim_csv():
    return send_from_directory(static_folder, 'transjatim_comments.csv', mimetype='text/csv')

@app.route('/youtube_comments.csv')
def serve_youtube_csv():
    return send_from_directory(static_folder, 'youtube_comments.csv', mimetype='text/csv')

@app.route('/output.css')
def serve_output_css():
    return send_from_directory(static_folder, 'output.css', mimetype='text/css')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')


# from flask import Flask, send_file
# import os

# app = Flask(__name__)

# # Print current working directory for debugging
# print("Current working directory:", os.getcwd())

# # Serve the index.html file
# @app.route('/')
# def serve_index():
#     file_path = 'index.html'
#     if not os.path.exists(file_path):
#         return f"Error: {file_path} not found in {os.getcwd()}", 404
#     return send_file(file_path)

# Serve the output.css file
@app.route('/output.css')
def serve_output_css():
    file_path = 'output.css'
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found in {os.getcwd()}", 404
    return send_file(file_path)

# Serve the CSV files from csv subdirectory
@app.route('/csv/transjatim_comments.csv')
def serve_transjatim_csv():
    file_path = os.path.join('csv', 'transjatim_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found in {os.getcwd()}", 404
    return send_file(file_path)

@app.route('/csv/youtube_comments.csv')
def serve_youtube_csv():
    file_path = os.path.join('csv', 'youtube_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found in {os.getcwd()}", 404
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 


# from flask import Flask, send_file
# import os

# app = Flask(__name__)

# # Print current working directory for debugging
# print("Current working directory:", os.getcwd())

# # Serve the index.html file
# @app.route('/')
# def serve_index():
#     file_path = 'indeks.html'
#     if not os.path.exists(file_path):
#         return f"Error: {file_path} not found in {os.getcwd()}", 404
#     return send_file(file_path)

# # Serve the CSV files
# @app.route('/transjatim_comments.csv')
# def serve_transjatim_csv():
#     file_path = 'transjatim_comments.csv'
#     if os.path.exists(file_path):
#         return send_file(file_path)
#     return f"Error: {file_path} not found in {os.getcwd()}", 404

# @app.route('/youtube_comments.csv')
# def serve_youtube_csv():
#     file_path = 'youtube_comments.csv'
#     if os.path.exists(file_path):
#         return send_file(file_path)
#     return f"Error: {file_path} not found in {os.getcwd()}", 404

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

