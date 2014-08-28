hello_nr_pies
=============

Testing new relic with pies2overrides

```
git clone git@github.com:bearnard/hello_nr_pies.git
virtualenv --no-site-packages venv
. ./venv/bin/activate
cd hello_nr_pies
pip install -r requirements.txt
newrelic-admin run-python server.py
curl -v http://127.0.0.1:8080/hello
curl -v http://127.0.0.1:8080/hello

```

