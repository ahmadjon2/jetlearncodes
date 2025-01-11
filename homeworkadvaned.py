class Footballteams():
    def __init__(self,money,rating,number_in_league):
        self.rating = rating
        self.money = money
        self.number_in_league = number_in_league
    def show_Footballteams(self):
        print("The football team's rating is {} ,number in premeur lrague is{} ,worth in money{},"
              .format(self.rating,self.number_in_league,self.money,))
mancity = Footballteams(" 1.3 billion"," 9/10"," 6")
mancity.show_Footballteams()
mancity1=(input("what is the team?  "))
if mancity1 == "mancity":
    print("correct")
else :
    print("new question, the other question was incorrect  ")
Arsenal = Footballteams(" 0.6 billion"," 9/10"," 2")
Arsenal.show_Footballteams()
Arsenal1=(input("what is the team?  "))
if Arsenal1 == "arsenal":
    print("correct")