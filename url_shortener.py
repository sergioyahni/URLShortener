from flask import Flask, request, jsonify, redirect
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)


# db.create_all()


class URLShortener(Resource):
    def get(self, short_url):
        url = URL.query.filter_by(short_url=short_url).first()
        if url:
            return redirect(url.original_url)
        else:
            return {'error': 'URL not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('original_url', type=str, required=True, help='Original URL cannot be blank')
        args = parser.parse_args()
        original_url = args['original_url']

        short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        url = URL(original_url=original_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()

        return {'original_url': original_url, 'short_url': short_url}, 201


api.add_resource(URLShortener, '/<string:short_url>', '/')

if __name__ == '__main__':
    app.run(debug=True)

