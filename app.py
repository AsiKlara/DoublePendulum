from flask import Flask, render_template, request, send_from_directory, jsonify
from api import post_json_ipfs, post_ipfs
from celery_worker import celery
from doublependulum import run_simulation

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', cid=None)


@app.route("/mint_nft", methods=["POST"])
def mint_nft():
    cid = post_json_ipfs(post_ipfs())
    return render_template("index.html", cid=cid)


# Celery task for running the simulation
@celery.task
def run_simulation_task(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background):
    run_simulation(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background)
    return 'double_pendulum_animation.mp4'


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

    # Asynchronously run the simulation with Celery
    task = run_simulation_task.delay(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background)
    return jsonify({"task_id": task.id}), 202


@app.route('/task-status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': 'Completed' if task.state == 'SUCCESS' else task.state,
            'result': task.result if task.state == 'SUCCESS' else None
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info),  # Exception raised
        }
    return jsonify(response)


@app.route('/download/<task_id>', methods=['GET'])
def download_file(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return send_from_directory(".", task.result, as_attachment=True)
    return jsonify({"error": "File not ready"}), 404


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
