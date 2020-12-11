from flask import render_template, request, redirect, url_for
from models.db_products import Product
from config import app, db


@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            price=request.form['price'],
            amount=request.form['amount'],
            comment=request.form['comment'], )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('all_products'))
    return render_template('create.html')


@app.route('/detail_product/<int:product_id>', methods=['GET'])
def detail_product(product_id):
    if request.method == 'GET':
        product = Product.query.filter_by(id=product_id).first()
        if product is not None:
            return render_template('detail.html', product=product)
        return redirect(url_for('all_products'))
    return redirect(url_for('all_products'))


@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if request.method == 'GET':
        product = Product.query.filter_by(id=product_id).first()
        if product is not None:
            return render_template('edit.html', product=product)
        return redirect(url_for('all_products'))
    elif request.method == 'POST':
        product = Product.query.filter_by(id=product_id).first()
        if product is not None:
            product.name = request.form['name']
            product.price = request.form['price']
            product.amount = request.form['amount']
            product.comment = request.form['comment']
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('all_products'))
        return redirect(url_for('all_products'))
    return redirect(url_for('all_products'))


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if request.method == 'POST':
        product = Product.query.filter_by(id=product_id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
            return redirect(url_for('all_products'))
        return redirect(url_for('all_products'))
    return redirect(url_for('all_products'))


@app.route('/')
def all_products():
    return render_template('show.html', products=Product.query.all())
