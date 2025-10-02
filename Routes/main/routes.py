from flask import(
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from src.models import db, User

main_bp = Blueprint('main',__name__)

@main_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main_bp.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('El usuario ya existe.', 'danger')
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario creado.', 'success')
            return redirect(url_for('main.users'))
    return render_template('user_form.html', action='Crear')

@main_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.commit()
        flash('Usuario actualizado.', 'success')
        return redirect(url_for('main.users'))
    return render_template('user_form.html', user=user, action="Editar")

@main_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado.', 'success')
    return redirect(url_for('main.users'))