from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to simulate a waiting list
waiting_list = []

@app.route('/waiting_list')
def waiting_list_view():
    count = len(waiting_list)
    return render_template('waiting_list.html', count=count, waiting_list=waiting_list)

@app.route('/register', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name')
        if patient_name:
            waiting_list.append(patient_name)
            return redirect(url_for('waiting_list_view'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)