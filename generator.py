import random

capitals = {'Andhra Pradesh': 'Hyderabad', 'Arunachal Pradesh': 'Itanagar', 'Assam': 'Dispur',
            'Bihar': 'Patna', 'Chhattisgarh': 'Raipur', 'Goa': 'Panaji', 'Gujarat': 'Gandhinagar',
            'Haryana': 'Chandigarh', 'Himachal Pradesh': 'Shimla', 'Jammu and Kashmir': 'Srinagar',
            'Jharkhand': 'Ranchi', 'Karnataka': 'Bengaluru', 'Kerala': 'Thiruvananthapuram', 'Madhya Pradesh': 'Bhopal',
            'Maharashtra': 'Mumbai', 'Manipur': 'Imphal', 'Meghalaya': 'Shillong', 'Mizoram': 'Aizawl',
            'Nagaland': 'Kohima',
            'Odisha': 'Bhubaneswar', 'Punjab': 'Chandigarh', 'Rajasthan': 'Jaipur', 'Sikkim': 'Gangtok',
            'Tamil Nadu': 'Chennai',
            'Telangana': 'Hyderabad', 'Tripura': 'Agartala', 'Uttar Pradesh': 'Lucknow', 'Uttarakhand': 'Dehradun',
            'West Bengal': 'Kolkata',
            'Andaman and Nicobar Islands': 'Port Blair', 'Chandigarh': 'Chandigarh',
            'Dadar and Nagar Haveli': 'Silvassa', 'Daman and Diu': 'Daman',
            'Delhi': 'Delhi', 'Lakshadweep': 'Kavaratti', 'Puducherry': 'Pondicherry'}

for quizNum in range(10):
    que = open('Que%s.txt' % (quizNum + 1), 'w')
    ans = open('Ans%s.txt' % (quizNum + 1), 'w')

    que.write('Question Paper Number : %s' % (quizNum + 1))

    states = list(capitals.keys())
    random.shuffle(states)

    for queNum in range(len(capitals)):
        correctAnswer = capitals[states[queNum]]
        wrongAnswer = list(capitals.values())

        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongOptions = list(random.sample(wrongAnswer, 3))
        allOptions = wrongOptions + [correctAnswer]
        random.shuffle(allOptions)

        que.write('%s. What is the capital of %s\n' % (queNum + 1, states[queNum]))
        for i in range(4):
            que.write('    %s. %s\n' % ('ABCD'[i], allOptions[i]))
        que.write('\n')

        ans.write('%s. %s\n' % (queNum + 1, 'ABCD'[allOptions.index(correctAnswer)]))

    que.close()
    ans.close()
