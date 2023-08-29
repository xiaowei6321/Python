from flask import Flask, request, jsonify, render_template, flash, send_file
from flask_bootstrap import Bootstrap
import io
import csv
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
Bootstrap(app)

notes = []

@app.route('/notes', methods=['POST'])
def add_note():
    note = request.json
    notes.append(note)
    return jsonify(note), 201

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        deleted_note = notes.pop(note_id)
        return jsonify(deleted_note), 200
    else:
        return jsonify({"error": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['PUT'])
def modify_note(note_id):
    if 0 <= note_id < len(notes):
        note = request.json
        notes[note_id] = note
        return jsonify(note), 200
    else:
        return jsonify({"error": "Note not found"}), 404

@app.route('/notes', methods=['GET'])
def search_notes():
    keyword = request.args.get('keyword', '').lower()
    filtered_notes = [note for note in notes if
                      keyword in note['title'].lower() or keyword in note['content'].lower()]
    return jsonify(filtered_notes)

@app.route('/download_note/<int:note_id>', methods=['GET'])
def download_note(note_id):
    if 0 <= note_id < len(notes):
        note = notes[note_id]
        csv_data = io.StringIO()
        writer = csv.writer(csv_data)

        writer.writerow(['Title', 'Content'])
        writer.writerow([note['title'], note['content']])

        csv_data.seek(0)
        return send_file(csv_data, mimetype='text/csv', as_attachment=True, attachment_filename='note.csv')
    else:
        flash("Note not found.")
        return render_template('index.html', notes=notes)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)