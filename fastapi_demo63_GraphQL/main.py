import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == "__main__":
    """
     http://127.0.0.1:8000 打开浏览器 ,将看到GraphiQL Web用户界面
     具体细节学习需要到： 
        https://www.starlette.io/graphql/
    """
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
