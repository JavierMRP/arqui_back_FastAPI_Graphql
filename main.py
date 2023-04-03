import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

import models
from db import db_session
from schemas import BookModel, BookSchema

db = db_session.session_factory()

app = FastAPI()


class Query(graphene.ObjectType):

    all_books = graphene.List(BookModel)
    book_by_id = graphene.Field(BookModel, book_id=graphene.Int(required=True))

    def resolve_all_books(self, info):
        query = BookModel.get_query(info)
        return query.all()

    def resolve_book_by_id(self, info, book_id):
        return db.query(models.Book).filter(models.book.id == book_id).first()


class CreateNewBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, description):
        book = BookSchema(title=title, description=description)
        db_book = models.Book(title=book.title, description=book.description)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        ok = True
        return CreateNewBook(ok=ok)


class BookMutations(graphene.ObjectType):
    create_new_book = CreateNewBook.Field()


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=BookMutations)))