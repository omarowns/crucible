from models.factories import AnimationFactory

class Effect():
    def __init__(self, name=None, arguments={}):
        self.id = id
        self.name = name
        self.arguments = arguments

    def stage(self):
       self.animation = AnimationFactory().build(self.name, self.arguments)

    def render(self):
        if self.animation:
            self.animation.render()
