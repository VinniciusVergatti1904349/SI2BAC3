import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def qtd_divisores(n):
    qtd = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            qtd += 1
    return qtd

def primo(n):
    return  qtd_divisores(n) == 2

def intervalo_primos():
    a = 0
    b = 541
    for num in range (a, b+1):
        if primo(num):print(num)
    return
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
