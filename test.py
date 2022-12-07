class Footy:
    def __init__(self):
        pass

    def pass_ball(self):
        print("pass the ball")
    
    def catchball(self):
        print("I caught the ball")
        Footy.endgame()
    
    def scoregoal(self):
        print("I scored a goal")
    
    @staticmethod
    def calcsalary(salary):
        print(f" {salary * 1.2}")

    @classmethod
    def endgame(cls):
        print("Red card")
    
game = Footy()
game.pass_ball()
game.catchball()
game.endgame()