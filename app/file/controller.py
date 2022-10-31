from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from app.file.models import File
from app.file.schemas import FileSchema
from app.extensions import db
from sqlalchemy import exc
import uuid
from app.author.models import Author
from app.tag.models import Tag
from app.user.models import User
from app.category.model import Category
from app.area.model import Area
import json



# /file
class FileAll(MethodView):
    
    ''' Cadastra um novo arquivo no banco de dados '''
    def post(self):
        schema = FileSchema()
        dados = request.json

        author_id = dados.pop('author', None)
        creator_id = dados.pop('creator', None)
        tag_id = dados.pop('tag', None)
        category_id = dados.pop('category', None)
        area_id = dados.pop('area', None)
        
        arquivo = schema.load(dados)
        
        # Association
        for id in author_id:
            author = Author.query.get(id)
            arquivo.authors_associated.append(author)

        for id in tag_id:
            tag = Tag.query.get(id)
            arquivo.tags_associated.append(tag)

        for id in category_id:
            category = Category.query.get(id)
            arquivo.categories_associated.append(category)
        
        for id in area_id:
            area = Area.query.get(id)
            arquivo.areas_associated.append(area)

        creator = User.query.get(creator_id)
        arquivo.creator_id = creator.id
        
        db.session.add(arquivo)

        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))

        return schema.dump(arquivo), 201


    ''' Pega todos arquivos do banco de dados '''
    def get(self):
        schema = FileSchema(many = True)
        title = request.args.get('title')
        type = request.args.get('type')
        min_click_quantity = request.args.get('min_click')
        max_click_quantity = request.args.get('max_click')
        min_year = request.args.get('min_year')
        max_year = request.args.get('max_year')
        awarded = request.args.get('awarded')
        tag_list = request.args.get('tags')
        author_list = request.args.get('authors')
        categories_list = request.args.get('category')
        areas_list = request.args.get('area')

        try:
            tag_list = json.loads(tag_list)
        except:
            tag_list = None
        
        try:
            author_list = json.loads(author_list)
        except:
            author_list = None
        
        try:
            categories_list = json.loads(categories_list)
        except:
            categories_list = None
        
        try:
            areas_list = json.loads(areas_list)
        except:
            areas_list = None
        

        filter_list = []
        if(title):
            title = f'%{title}%'
            filter_list.append(File.title.ilike(title))
        if(type):
            filter_list.append(File.type == type)
        if(min_click_quantity):
            filter_list.append(File.click_quantity >= min_click_quantity)
        if(max_click_quantity):
            filter_list.append(File.click_quantity <= max_click_quantity)
        if(min_year):
            filter_list.append(File.year >= min_year)
        if(max_year):
            filter_list.append(File.year <= max_year)
        if(awarded):
            filter_list.append(File.awarded == awarded)
        if(tag_list != None):
            filter_list.append(File.tags_associated.any(Tag.id.in_(tag_list)))
        if(author_list != None):
            filter_list.append(File.authors_associated.any(Author.id.in_(author_list)))
        if(categories_list != None):
            filter_list.append(File.categories_associated.any(Category.id.in_(categories_list)))
        if(areas_list != None):
            filter_list.append(File.areas_associated.any(Area.id.in_(areas_list)))
        
        query = File.query
        for choosen_filter in filter_list:
            query = query.filter(choosen_filter)
 
        return jsonify(schema.dump(query)),200

# /file/<int:id>
class FileDetails(MethodView):

    ''' Altera dados de arquivo especifico do banco de dados '''
    def patch(self, id):
        file = File.query.get_or_404(id)
        schema = FileSchema()
        dados = request.json

        author_id = dados.pop('author', None)
        creator_id = dados.pop('creator', None)
        tag_id = dados.pop('tag', None)
        category_id = dados.pop('category', None)
        area_id = dados.pop('area', None)

        file = schema.load(dados, instance=file, partial = True)
        
        # Association
        if(author_id != None):
            file.authors_associated = []
            for id in author_id:
                author = Author.query.get(id)
                file.authors_associated.append(author)

        if(tag_id != None):
            file.tags_associated = []
            for id in tag_id:
                tag = Tag.query.get(id)
                file.tags_associated.append(tag)
            
        if(category_id != None):
            file.categories_associated = []
            for id in category_id:
                category = Category.query.get(id)
                file.categories_associated.append(category)
        
        if(area_id != None):
            file.areas_associated = []
            for id in area_id:
                area = Area.query.get(id)
                file.areas_associated.append(area)

        if(creator_id != None):
            creator = User.query.get(creator_id)
            file.creator_id = creator.id

        db.session.add(file)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(file),200
    
    
    ''' Pega arquivo especifico do banco de dados '''
    def get(self, id):
        schema = FileSchema()
        file = File.query.filter_by(id=id).first_or_404()

        file.click_quantity += 1
        file.save()

        return schema.dump(file), 200

    def delete(self, id):
        file = File.query.get_or_404(id)
        db.session.delete(file)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))
        return {"msg":"Arquivo deletado!"},200

#/file/top-access
class TopAccess(MethodView):
    def get(self):
        schema = FileSchema(many = True)
        files = File.query.order_by(File.click_quantity.desc()).limit(10).all()

        return schema.dump(files),200