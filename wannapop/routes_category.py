from flask import Blueprint, render_template, redirect, url_for, flash, abort
from .models import Category
from .forms import CategoryForm, ConfirmForm
from .helper_role import Action, perm_required

# Blueprint
category_bp = Blueprint("category_bp", __name__)

@category_bp.route('/categories/list')
@perm_required(Action.categories_list)
def category_list():
    # select que retorna una llista de resultats
    categories = Category.get_all()
    
    return render_template('categories/list.html', categories = categories)

@category_bp.route('/categories/create', methods = ['POST', 'GET'])
@perm_required(Action.categories_create)
def category_create(): 

    # carrego el formulari amb l'objecte categories
    form = CategoryForm()

    if form.validate_on_submit(): # si s'ha fet submit al formulari
        new_category = Category()

        # dades del formulari a l'objecte category
        form.populate_obj(new_category)

        # insert!
        new_category.save()

        # https://en.wikipedia.org/wiki/Post/Redirect/Get
        flash("Nova categoria creada", "success")
        return redirect(url_for('category_bp.category_list'))
    else: # GET
        return render_template('categories/create.html', form = form)

@category_bp.route('/categories/read/<int:category_id>')
@perm_required(Action.categories_read)
def category_read(category_id):
    # select amb 1 resultat
    category = Category.get(category_id)

    if not category:
        abort(404)

    return render_template('categories/read.html', category = category)

@category_bp.route('/categories/update/<int:category_id>',methods = ['POST', 'GET'])
@perm_required(Action.categories_update)
def category_update(category_id):
    # select amb 1 resultat
    category = Category.get(category_id)
    
    if not category:
        abort(404)

    # carrego el formulari amb l'objecte category
    form = CategoryForm(obj = category)

    if form.validate_on_submit(): # si s'ha fet submit al formulari
        # dades del formulari a l'objecte category
        form.populate_obj(category)

        # update!
        category.update()

        # https://en.wikipedia.org/wiki/Post/Redirect/Get
        flash("Categoria actualitzada", "success")
        return redirect(url_for('category_bp.category_read', category_id = category_id))
    else: # GET
        return render_template('categories/update.html', category_id = category_id, form = form)

@category_bp.route('/categories/delete/<int:category_id>',methods = ['GET', 'POST'])
@perm_required(Action.categories_delete)
def category_delete(category_id):
    # select amb 1 resultat
    category = Category.get(category_id)

    if not category:
        abort(404)

    form = ConfirmForm()
    if form.validate_on_submit(): # si s'ha fet submit al formulari
        # delete!
        category.delete()

        flash("Categoria esborrada", "success")
        return redirect(url_for('category_bp.category_list'))
    else: # GET
        return render_template('categories/delete.html', form = form, category = category)