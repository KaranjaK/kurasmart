#first we will tke input of what nominnee we want to keep
nominee1 = input("Enter the name of the 1st nominee:")
nominee2 = input("Enter the name of the 2nd nominee:")

#initial vote count for both must be 0

nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter) #we will remove so that again voter can't vote
        print("to give vote to ",nominee1,"press 1 ")
        print("to give vote to ",nominee2,"press 2 ")


