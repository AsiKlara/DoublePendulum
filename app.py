
from flask import Flask, render_template, request, send_from_directory
from api import post_ipfs, post_json_ipfs
from doublependulum import run_simulation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', cid=None, video=False)


@app.route("/mint_nft", methods=["POST"])
def mint_nft():
    cid = post_json_ipfs(post_ipfs())

    return render_template("index.html", cid=cid, video=True)


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
    colormap = request.form['colormap']
    background = request.form['background']

    # Run the simulation with the provided parameters and colormap
    run_simulation(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background)
    return render_template("index.html", cid=None, video=True)


@app.route('/save', methods=['POST'])
def save():
    return send_from_directory(".", 'double_pendulum_animation.mp4', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

