# main.py
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        form_data = request.form
        search = form_data.get('search')
        if search == 'google':
            google_data = ['1', '2', '3', '4']
            return render_template('data.html', form_data=form_data, context=google_data)
        elif search == 'tiktok':
            tiktok_data = ['a', 'b', 'c', 'd']
            return render_template('data.html', form_data=form_data, context=tiktok_data)
        else:
            return render_template('404.html')


        # Process the form data (e.g., save to a database)
        # ...

        # Display the form data on a separate page (data.html)
        
    

# @app.route('/search', methods=['GET'])
# def landing_search():
#     # Process form data (e.g., validate, save to database, etc.)
#     form_data = request.form
#     query = form_data.get('eula')
    
#     # Determine the target page based on the form input
#     if query == 'facebook':
#         target_page = '/facebook'
#     else:
#         target_page = '/not_found'

#     # Redirect to the appropriate page
#     return redirect(target_page)

# @app.route('/facebook')
# def admin_dashboard():
#     return "Welcome to the Admin Dashboard!"

# @app.route('/not_found')
# def user_dashboard():
#     return "Welcome to the User Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)

