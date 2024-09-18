from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/') 
def index():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Services Page
@app.route('/services')
def services():
    return render_template('services.html')
  
# Products Page
@app.route('/products')
def products():
    return render_template('products.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
