import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.2'
port = 8001

server.bind((ip_address, port))
server.listen()

list_of_clients = []
print("Server has started")

questions = [
    "Who is the leader of Stray Kids?? \n a.Bhang Chahn \nb.Jungkook \nc.Hyunjin \nd.Taecyon",
    "How many memebers are there in Stray Kids?? \na.4 \nb.5 \nc.8 \n.d.3",
    "Who is not the OG avenger?? \na.Scott Lang \nb.Natasha Romanoff \nc.Bruce Banner \nd.Steve Rogers",
    "Who is Steve Roger's best-friend?? \na.Clint Barton \nb.Thor \nc. Bucky Barnes \nd.Bruce Banner",
    "Who wrote the Maxe Runner Series?? \na. James Dashner \nb.Rick Riordan \nc.J.K.Rowling \nd.C.S.Lewis"
]
answers = ['a', 'c','a','c','a']

def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will recieve a question. The answer to that question should be one of a, b,c or d".encode('utf-8'))
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message. lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your scores is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue

def remove_question(index):
    question.pop(index)
    answers.pop(index)

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer 

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()