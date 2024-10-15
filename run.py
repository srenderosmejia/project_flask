from flask import render_template
from todor import create_app

def pagina_no_encontrada(error):
    return render_template('html_404.html'),404

if __name__ == '__main__':
    app = create_app()
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
