from flask import Flask
import time

app = Flask(__name__)

@app.route('/test')
def simulate_execution():
    # Simula uma execução de 35 minutos
    time.sleep(2100)
    return 'Execução completa!'

if __name__ == '__main__':
    app.run()