import os
import re
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename

from analysis.similarity import build_analysis_results, read_file_content

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

analysis_results_memory = None


# 👉 NUMBRILINE SORTIMINE (1.py, 2.py, 10.py jne õigesti)
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')


def get_uploaded_python_files():
    files = []

    for name in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, name)

        if os.path.isfile(path) and name.lower().endswith(".py"):
            files.append(name)

    # 👉 SORT
    files.sort(key=extract_number)

    return files


@app.route("/")
def home():
    return redirect(url_for("upload_page"))


@app.route("/upload")
def upload_page():
    uploaded_files = get_uploaded_python_files()
    return render_template("upload.html", uploaded_files=uploaded_files)


@app.route("/upload-files", methods=["POST"])
def upload_files():
    files = request.files.getlist("files")

    for file in files:
        if file and file.filename.strip():
            safe_name = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], safe_name)
            file.save(path)

    return redirect(url_for("upload_page"))


@app.route("/delete-all-files", methods=["POST"])
def delete_all_files():
    global analysis_results_memory

    for name in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, name)
        if os.path.isfile(path):
            os.remove(path)

    analysis_results_memory = None

    return redirect(url_for("upload_page"))


@app.route("/analysis")
def analysis_page():
    uploaded_files = get_uploaded_python_files()

    return render_template(
        "analysis.html",
        results=analysis_results_memory,
        uploaded_files=uploaded_files
    )


@app.route("/run-analysis", methods=["POST"])
def run_analysis_route():
    global analysis_results_memory

    uploaded_files = get_uploaded_python_files()

    if uploaded_files:
        analysis_results_memory = build_analysis_results(
            app.config["UPLOAD_FOLDER"],
            uploaded_files
        )
    else:
        analysis_results_memory = None

    return redirect(url_for("analysis_page"))


@app.route("/comparison")
def comparison_page():
    file_a = request.args.get("file_a", "").strip()
    file_b = request.args.get("file_b", "").strip()

    uploaded_files = get_uploaded_python_files()

    if not file_a or not file_b:
        return render_template(
            "comparison.html",
            comparison_ready=False
        )

    if file_a not in uploaded_files or file_b not in uploaded_files:
        abort(404)

    path_a = os.path.join(app.config["UPLOAD_FOLDER"], file_a)
    path_b = os.path.join(app.config["UPLOAD_FOLDER"], file_b)

    return render_template(
        "comparison.html",
        file_a_name=file_a,
        file_b_name=file_b,
        file_a_content=read_file_content(path_a),
        file_b_content=read_file_content(path_b),
        comparison_ready=True
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)