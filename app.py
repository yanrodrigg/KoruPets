from flask import Flask, jsonify, request
import repositorios

app = Flask(__name__)

#ROTA PARA CADASTRAR UM PRODUTO
@app.route("/produto", methods=["POST"])
def set_produtos():
    produto = request.json
    id = repositorios.criar_produto(**produto)
    produto["id"] = id
    return jsonify(produto), 201

# Rota para retornar todos os produtos
@app.route("/produtos", methods=['GET'])
def get_produtos():
    lista_produtos = repositorios.retornar_produtos()
    return jsonify(lista_produtos)

# Rota para retornar um único produto
@app.route("/produto/<int:id>", methods=['GET'])
def get_produto(id):
    produto = repositorios.retornar_produto(id)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado!"}), 404 

#Rota para atualizar um produto
@app.route("/produto/<int:id>", methods=["PUT"])
def update_produto(id):
    produto = repositorios.retornar_produto(id)
    if produto:
        dados_atualizados = request.json
        dados_atualizados['id'] = id
        if repositorios.atualizar_produto(**dados_atualizados):
            return jsonify(dados_atualizados), 200 
        else:
            return jsonify({"message":"Não foi possível atualizar"}), 500  
    else:
            return jsonify({"message": "Produto não foi localizado"}), 404

#Rota para deletar um produto    
@app.route("/produto/<int:id>", methods=['DELETE'])
def delete_produto(id):
    produto = repositorios.retornar_produto(id)
    if produto:
        repositorios.remover_produto(id) 
        return jsonify({"message": "Produto deletado com sucesso!"})
    else:
        return jsonify({"message": "Produto não encontrado!"}), 404

app.run(debug=True)




