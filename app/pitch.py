class Pitch:

    all_pitches=[]

    def __init__(self,title,category):
        self.title=title
        self.category=category


@classmethod
def get_pitches(cls,id):

    response = []

    for pitch in cls.all_pitches:
            if pitch.user.id == id:
                response.append(pitch)

    return response


def save_pitch(self):
        Pitch.all_pitches.append(self)
# <h1>Categories</h1>
# <h2>Pickup Lines</h2>
# <h2>Interview Pitches</h2>
# <h2>Product Pitches</h2>
# <h2>Promotion Pitches</h2>


  