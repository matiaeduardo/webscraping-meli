from flask import Flask,jsonify,request
import json 
from functions import todosproductos,limite_producto

app = Flask(__name__)
@app.route('/mercadolibre',methods=['GET'])

def mercadolibre():
    data=json.loads(request.data)
    print(data['producto'])
    if 'limite' not in data:
        titulos,urls,precios=todosproductos(data['producto'])
    else:
        titulos,urls,precios=limite_producto(data['producto'],data['limite'])
    return jsonify({'Datos':{'Titulos':titulos,'Urls':urls,'Precios':precios}})

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)

