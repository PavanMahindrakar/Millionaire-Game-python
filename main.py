questions = [
    ["who is MS Dhoni?", "cricketer","actor","politician","scientist", 1],
    ["who is the president of India?", "Narendra Modi", "Droupadi Murmu", "Amit Shah", "Sonia Gandhi",2],
    ["which is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai",1],
    ["who is the CEO of Tesla?", "Jeff Bezos", "Bill Gates", "Tim Cook","Elon Musk",4],
    ["who is the founder of Microsoft?", "Steve Jobs", "Larry Page","Bill Gates", "Sergey Brin",3],
    ["who is the author of Harry Potter?", "J.R.R. Tolkien","J.K. Rowling", "George R.R. Martin", "Agatha Christie",2],
    ["who is the director of Inception?", "Steven Spielberg", "James Cameron", "Martin Scorsese","Christopher Nolan",4],
    ["who is the lead singer of Coldplay?", "Chris Martin", "Bono", "Freddie Mercury", "Axl Rose",1],
    ["who is the founder of Facebook?", "Jack Dorsey", "Larry Page", "Mark Zuckerberg","Sergey Brin",3],
    ["who is the current Prime Minister of UK?", "Rishi Sunak", "Boris Johnson", "Theresa May", "David Cameron",1]]

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
i=0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")  
    print(f"d. {question[4]}")

    #check whether the answer is correct or not
    answer = int(input("Enter your answer (1-4)... 1 for a, 2 for b, 3 for c, 4 for d: "))
    if answer == question[5]:
        print(f"Correct! You win {prizes[i]} rupees.")
        i += 1
    else:
        print(f"Wrong answer! The correct answer was option {question[5]}: {question[question[5]]}")
        print(f"You won {prizes[i-1]} rupees.")
        break


    
