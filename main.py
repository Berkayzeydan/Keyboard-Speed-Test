from tkinter import *
from helpers import *

time_left = 60
words = get_words()
game_started = False
word_index = 0
window = Tk()
score = 0
highscore = get_highscore()
game_over = False

score_label = Label(window, text=f"Score: {score}", font=("Arial", 20))
score_label.grid(row=0, column=0)

timer_label = Label(window, text=f"Seconds left: {time_left}", font=("Helvetica", 15), fg="#f00")
timer_label.grid(row=0, column=1)

high_score_label = Label(window, text=f"Highscore: {highscore}", font=("Arial", 20))
high_score_label.grid(row=0, column=2)

frame = Frame(window, bd=2, relief="solid", pady=20, padx=20)
frame.grid(row=1, column=0, columnspan=3)
label = Label(frame, height=2, width=60, text=words[0], font=("Cambria", 24))
label.pack()

answer = Text(window, height=1, width=15, font=("Arial", 20))
answer.grid(row=2, column=1)



def game(key):
    global game_started, word_index, score, words, game_over, time_left
    if not game_over and game_started:
        if key.keysym == "space":
            comp_word = answer.get("1.0", END).strip().lower()
            answer.delete("1.0", END)
            if comp_word == words[word_index]:
                score += 1
                score_label.configure(text=f"Score: {score}")

            word_index += 1
            if word_index >= len(words):
                label.configure(text="No words left!")
                window.after_cancel(timer_id)
                game_finished()

            else:
                label.configure(text=words[word_index])
    elif not game_over and not game_started:
        game_started = True
        timer()


def timer():
    global time_left, game_started, timer_id
    if time_left == 0:
        label.configure(text="Times up!")
        game_finished()
    else:
        time_left -= 1
        timer_label.configure(text=f"Seconds left: {time_left}")
        timer_id = window.after(1000, timer)

def game_finished():
    global time_left, game_started, score, word_index, highscore, game_over
    game_over = True
    game_started = False
    if highscore < score:
        highscore = score
        high_score_label.configure(text=f"Highscore: {score}")
        set_higscore(score)
    timer_label.configure(text=f"Seconds left:")
    score = 0
    word_index = 0
    answer.config(state=DISABLED)
    restart.grid(row=0, column=0, columnspan=3)


def reset_game():
    global game_over, words, time_left
    game_over = False
    words = get_words()
    time_left= 60
    restart.grid_forget()
    answer.config(state=NORMAL)
    label.configure(text=words[word_index])


restart = Button(window, text="Play Again", width=30, height=2, command=reset_game)

window.bind("<Key>", game)

window.mainloop()
