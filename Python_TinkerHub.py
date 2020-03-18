# Created By Sharun
# Time 17/3/2020 14:48 IST

class Tech_Learners_Mentors :
    intrest=[]
    def addStack(self,intrest_take):         #Add paticular stack of intrest or expertise
        exit=''
        choice=0
        i=0
        intrest_take=''
        while choice==0 :
            intrest_take=input('Enter the Intrests and Expertise  :')
            self.intrest.append(intrest_take)    
            i=i+1
            exit=input('Do you want to continue (y/n)?')
            if exit=='y':
                choice=0
            else:
                choice=1

    def setMentorOrLearner(self,job):   #Set whether the participant is learner or mentor
        if job.casefold()=='Learner' :
            self.parti_cat='Learner'
        else:
            if job.casefold()=='Mentor' :
                self.parti_cat='Mentor'

    def setAvailableTime(self,job): #if person is mentor set available time
        if job.casefold()=='mentor' :
            time=input('Enter the available time you can spend')
            return time
        
    def getMentor(self,type,Time):        #takes stack and time as parameters and find available mentors
        for i in range(len(type)) :
            if self.setAvailableTime(type,Time)==Time :
                return i
        
intr=input('Sharun ! Enter your area of intrest  :')
Tech_Learners_Mentors.addStack(intr)
cat=input('Enter the category you belong Learner or Mentor  :')
sharun_cat = Tech_Learners_Mentors.setMentorOrLearner(cat)
time_return = Tech_Learners_Mentors.setAvailableTime(cat)
mentorGet = Tech_Learners_Mentors.getMentor(sharun_cat.intrest,time_return)
print(mentorGet)