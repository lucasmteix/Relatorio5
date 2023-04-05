from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_livro(self, _id: int, titulo: str, autor: str, ano: int,
                     preco: float) -> str:
        try:
            result = self.collection.insert_one({"_id": _id, "titulo": titulo, "autor": autor,
                                                 "ano": ano, "preco": preco})
            livro_id = _id
            print(f"Livro {titulo} creado com id: {livro_id}")
            return livro_id
        except Exception as error:
            print(f"Um erro ocorreu ao criar a pessoa: {error}")
            return None

    def read_livro_por_id(self, livro_id: int) -> dict:
        try:
            livro = self.collection.find_one({"_id": ObjectId(livro_id)})
            if livro:
                print(f"Person found: {livro}")
                return livro
            else:
                print(f"No person found with id {livro_id}")
                return None
        except Exception as error:
            print(f"Um erro ocorreu ao tentar ler o livro: {error}")
            return None

    def update_livro(self, livro_id: int, titulo: str, autor: str,ano: int,
                     preco: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(livro_id)}, {"$set": {"titulo": titulo,
                                                                                       "autor": autor,
                                                                                       "ano": ano,
                                                                                       "preco": preco}})
            if result.modified_count:
                print(f"Livro {livro_id} updated com o titulo {titulo}, autor {autor}, ano {ano},"
                      f"preco {preco}")
            else:
                print(f"Nenhum livro achado com o id {livro_id}")
            return result.modified_count
        except Exception as error:
            print(f"Um erro ocorreu ao atualizar a pessoa: {error}")
            return None

    def delete_livro(self, livro_id: int) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(livro_id)})
            if result.deleted_count:
                print(f"Livro {livro_id} deletado")
            else:
                print(f"Nenhum livro achado com o id {livro_id}")
            return result.deleted_count
        except Exception as error:
            print(f"Um erro ocorreu ao deletar a pessoa: {error}")
            return None