from flaskext.script import Manager

from crowdmon import create_app

app = create_app()

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
