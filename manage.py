from app import create_app
from flask_script import Manager,Server

app = create_app('development')

manager = Manager(app)

manager.add_command('server',Server)

@manager.command
def test():
    
    import unittest
    tests = unittest.TestLoader()
    unittest.TextTestRunner(verbosity=2).run(test)
    
if __name__ == '__main__':
    manager.run()