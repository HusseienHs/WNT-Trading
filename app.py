import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Directory where uploaded files will be saved
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Create the uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/invoices', methods=['GET', 'POST'])
def invoices():
    if request.method == 'POST':
        if 'invoice_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['invoice_file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Save the file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        flash('Invoice uploaded successfully!')

    # List all uploaded invoices
    invoices_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('invoice.html', invoices=invoices_list)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
