
from flask import Flask, render_template, request, send_from_directory
from doublependulum import run_simulation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        n_pendulums = int(request.form['n_pendulums'])
        d_diff = float(request.form['d_diff'])
        t_max = float(request.form['t_max'])
        g = float(request.form['g'])
        m1 = float(request.form['m1'])
        m2 = float(request.form['m2'])
        L1 = float(request.form['L1'])
        L2 = float(request.form['L2'])
        theta1 = float(request.form['theta1'])
        theta2 = float(request.form['theta2'])

        # Here you would run your simulation with the parameters
        # For now, we'll just return them to show it works
        return render_template('index.html', result={
            'n_pendulums': n_pendulums,
            'd_diff': d_diff,
            't_max': t_max,
            'g': g,
            'm1': m1,
            'm2': m2,
            'L1': L1,
            'L2': L2,
            'theta1': theta1,
            'theta2': theta2,
        })

    return render_template('index.html', result=None)


@app.route('/export', methods=['POST'])
def export():
    n_pendulums = int(request.form['n_pendulums'])
    d_diff = float(request.form['d_diff'])
    t_max = float(request.form['t_max'])
    g = float(request.form['g'])
    m1 = float(request.form['m1'])
    m2 = float(request.form['m2'])
    L1 = float(request.form['L1'])
    L2 = float(request.form['L2'])
    theta1 = float(request.form['theta1'])
    theta2 = float(request.form['theta2'])

    run_simulation(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2)

    return send_from_directory(".", 'double_pendulum_animation.mp4', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
