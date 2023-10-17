from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post

@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description, **kwargs):
    try:
        today = date.today()
        post = Post(
            title=title,
            description = description,
            created_at = today.strftime("%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [
                f"Incorrect date format provided. Date should be in "
                f"the format dd-mm-yyyy",
                str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def updatePost_resolver(obj, info, id, **kwargs):
    try:
        post = Post.query.get(id)
        if post:
            post.title = kwargs["title"] if kwargs.get("title") != None else post.title
            post.description = kwargs["description"] if kwargs.get("description") != None else post.description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def deletePost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload