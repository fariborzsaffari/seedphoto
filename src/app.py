from flask import Flask
from prometheus_client import start_http_server, Gauge
from controller import GetBalance


app = Flask(__name__)

balance_metric = Gauge('bsc_balance', 'Balance of BSC wallet')

@app.route('/metrics')
def metrics():
    try:
        balance = GetBalance()
        balance_metric.set(balance.get_balance())
        return str(balance_metric.collect()[0])
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8015)
    # Start Flask web server
    app.run()
