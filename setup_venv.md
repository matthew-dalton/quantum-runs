## To create a virtual environment with the correct dependencies:

(inside of repository directory, e.g. `qiskit_algorithms`)

- `python3 -m venv venv` — creates virtual environment
- `source venv/bin/activate` — enters virtual environment
- `pip install -r requirements.txt` — installs dependencies from requirements.txt

Now, carry out all tasks with python programs *inside* the virtual environment.

When done:

`deactivate` — exits virtual environment
