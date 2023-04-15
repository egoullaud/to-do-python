'''
main.py
  Here you will write your code while following the lessons.

hello.py
  This file contains the boilerplate code included in the GooeyPie Repl template - https://replit.com/@mrantonio/GooeyPie-Template?v=1

complete.py
  Spoiler: complete.py has a completed implementation. For your IDEAL learning experience the completed project should NOT be viewed until after the workshop is done.
'''
import gooeypie as gp

'''
def give_result(event):
    result_lbl.text = "You got it, boss!"


# name the app on top of window
app = gp.GooeyPieApp('Do the Thing')

# width of window
app.width = 700

# set up grid
app.set_grid(3, 3)

# Define label and button

add_btn = gp.Button(app, "Put it on the board", give_result)
prompt_lbl = gp.Label(app, 'What needs doing?')
result_lbl = gp.Label(app, '')

# display on app
app.add(add_btn, 2, 2, align='left')
app.add(prompt_lbl, 2, 1, align='right')
app.add(result_lbl, 3, 2, align='left')

# always last
app.run()

'''

# create application window
app = gp.GooeyPieApp("Do it")
app.width = 500
app.set_grid(5, 3)

# create functions


# create widgets
new_task_lbl = gp.Label(app, "What needs doing?")
new_task_input = gp.Input(app)
new_task_btn = gp.Button(app, "Put it on the board", None)

list_lbl = gp.Label(app, "List")
list_box = gp.Listbox(app)
delete_btn = gp.Button(app, "Not doing it", None)
all_done_btn = gp.Button(app, "Did all the things", None)


finished_label = gp.Label(app, "Kill List")
finished_box = gp.Listbox(app)
clear_btn = gp.Button(app, "Clear Killed", None)

# place widgets on grid
app.add(new_task_lbl, 1, 1, align="right")
app.add(new_task_input, 1, 2, align="left")
app.add(new_task_btn, 1, 3, align="center")

app.add(list_lbl, 2, 1, align="right")
app.add(list_box, 2, 2, align='left')
app.add(delete_btn, 3, 2, align='center')
app.add(all_done_btn, 3, 3, align='center')

app.add(finished_label, 4, 1, align='right')
app.add(finished_box, 4, 2, align='left')
app.add(clear_btn, 5, 3, align='center')


# run app
app.run()
