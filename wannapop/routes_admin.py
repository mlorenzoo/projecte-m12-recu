from flask import Blueprint, render_template, abort, flash, redirect, url_for
from .models import User, BlockedUser, Product, BannedProduct
from .helper_role import Role, role_required
from .forms import ConfirmForm, BlockUserForm, BanProductForm

# Blueprint
admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route('/admin')
@role_required(Role.admin, Role.moderator)
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/admin/users')
@role_required(Role.admin)
def admin_users():
    users = User.get_all_with(join_cls=[], outerjoin_cls=BlockedUser)
    return render_template('admin/users/list.html', users=users)

@admin_bp.route('/admin/users/<int:user_id>/block', methods=["GET", "POST"])
@role_required(Role.admin)
def block_user(user_id):
    result = User.get_with(user_id, join_cls=[], outerjoin_cls=BlockedUser)
    if not result:
        abort(404)
    
    (user, blocked) = result

    if blocked:
        flash("Compte d'usuari/a ja bloquejat", "error")
        return redirect(url_for('admin_bp.admin_users'))

    if user.is_admin_or_moderator():
        flash("Sols es poden bloquejar els usuaris wanner", "error")
        return redirect(url_for('admin_bp.admin_users'))

    form = BlockUserForm()
    if form.validate_on_submit():
        new_block = BlockedUser();
        # carregar dades de la URL
        new_block.user_id = user.id
        # carregar dades del formulari
        form.populate_obj(new_block)
        # insert!
        new_block.save()
        # retornar al llistat
        flash("Compte d'usuari/a bloquejat", "success")
        return redirect(url_for('admin_bp.admin_users'))

    return render_template('admin/users/block.html', user=user, form=form)

@admin_bp.route('/admin/users/<int:user_id>/unblock', methods=["GET", "POST"])
@role_required(Role.admin)
def unblock_user(user_id):
    result = User.get_with(user_id, join_cls=[], outerjoin_cls=BlockedUser)
    if not result:
        abort(404)
    
    (user, blocked) = result

    if not blocked:
        flash("Compte d'usuari/a no bloquejat", "error")
        return redirect(url_for('admin_bp.admin_users'))

    if user.is_admin_or_moderator():
        flash("Sols es poden bloquejar els usuaris wanner", "error")
        return redirect(url_for('admin_bp.admin_users'))
    
    form = ConfirmForm()
    if form.validate_on_submit():
        blocked.delete()
        flash("Compte d'usuari/a desbloquejat", "success")
        return redirect(url_for('admin_bp.admin_users'))
    
    return render_template('admin/users/unblock.html', user=user, form=form)

@admin_bp.route('/admin/products/<int:product_id>/ban', methods=["GET", "POST"])
@role_required(Role.moderator)
def ban_product(product_id):
    result = Product.get_with(product_id, join_cls=[], outerjoin_cls=BannedProduct)
    if not result:
        abort(404)
    
    (product, banned) = result

    if banned:
        flash("Producte ja prohibit", "error")
        return redirect(url_for('products_bp.product_list'))

    form = BanProductForm()
    if form.validate_on_submit():
        new_banned = BannedProduct();
        # carregar dades de la URL
        new_banned.product_id = product.id
        # carregar dades del formulari
        form.populate_obj(new_banned)
        # insert!
        new_banned.save()
        # retornar al llistat
        flash("Producte prohibit", "success")
        return redirect(url_for('products_bp.product_list'))

    return render_template('admin/products/ban.html', product=product, form=form)

@admin_bp.route('/admin/products/<int:product_id>/unban', methods=["GET", "POST"])
@role_required(Role.moderator)
def unban_product(product_id):
    result = Product.get_with(product_id, join_cls=[], outerjoin_cls=BannedProduct)
    if not result:
        abort(404)
    
    (product, banned) = result
    
    if not banned:
        flash("Producte no prohibit", "error")
        return redirect(url_for('products_bp.product_list'))
    
    form = ConfirmForm()
    if form.validate_on_submit():
        banned.delete()
        flash("Producte permès", "success")
        return redirect(url_for('products_bp.product_list'))

    return render_template('admin/products/unban.html', product=product, form=form)
