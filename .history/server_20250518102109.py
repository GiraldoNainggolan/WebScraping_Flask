from flask import Flask, send_file, abort
import os

app = Flask(__name__)

# Print current working directory for debugging
print("Current working directory:", os.getcwd())

# Serve the index.html file
@app.route('/')
def serve_index():
    file_path = os.path.join(os.getcwd(), 'index.html')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path)

# Serve the ScrapingYt.jpg image
@app.route('/ScrapingYt.jpg')
def serve_scrapingyt_image():
    file_path = os.path.join(os.getcwd(), 'ScrapingYt.jpg')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='image/jpeg')



# Serve the CSV files from root directory (fallback)
@app.route('/transjatim_comments.csv')
def serve_transjatim_csv_root():
    file_path = os.path.join(os.getcwd(), 'transjatim_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='text/csv')

@app.route('/youtube_comments.csv')
def serve_youtube_csv_root():
    file_path = os.path.join(os.getcwd(), 'youtube_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='text/csv')

# Serve the CSV files from csv subdirectory
@app.route('/csv/transjatim_comments.csv')
def serve_transjatim_csv_subdir():
    file_path = os.path.join(os.getcwd(), 'csv', 'transjatim_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='text/csv')

@app.route('/csv/youtube_comments.csv')
def serve_youtube_csv_subdir():
    file_path = os.path.join(os.getcwd(), 'csv', 'youtube_comments.csv')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='text/csv')

# Serve the output.css file
@app.route('/output.css')
def serve_output_css():
    file_path = os.path.join(os.getcwd(), 'output.css')
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found", 404
    return send_file(file_path, mimetype='text/css')

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

