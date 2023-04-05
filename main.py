from database import Database
from save_json import writeAJson
from Model import LivroModel

db = Database(database = "relatorio5", collection="pessoas")
livro_model = LivroModel(db)
id_livro = livro_model.create_livro(1, "Capitães da Areia", "Jorge Amado", 1937, 65.50)
livro = livro_model.read_livro_por_id(1)
livro_model.update_livro(1, "Capitaes da Areia", "Jorge Amado", 1937, 70.00)
livro_model.delete_livro(1)