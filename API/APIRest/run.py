from app import app

# importnando routes
from app.routes import *

# importando models -> a ordem da importacao se relaciona com a relação entre tabelas
from app.models import endereco
from app.models import usuario

if __name__ == '__main__':
    app.run(port=8080, debug=True)
