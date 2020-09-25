# External modules
from flask import jsonify, request
from flask_restful import Resource

# Local modules
from ...models.entity.technology_entity import TechnologyEntity
from ...resources.repository.technology_repo import TechnologyRepo


class Technology(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def post(self):
        print('request here')
        request_body = request.get_json()
        print(type(request_body['tags']))

        new_tech = TechnologyEntity(
            name=request_body['name'],
            tags=request_body['tags']
        )

        self.repository.persist(new_tech)

        return jsonify(new_tech.to_dict())


class TechnologyList(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def get(self):
        docs = self.repository.find_all()
        return jsonify(docs)
