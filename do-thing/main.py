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
app = gp.GooeyPieApp("Do the things")
app.width = 700
app.set_grid(7, 7)

# create functions


def add_task(event):
    # add new task when enter is pressed
    if event.key['name'] == 'Return':
        list_box.add_item(new_task_input.text)
        new_task_input.clear()
        result_add_lbl.text = "As you wish, my liege"


def add_task_btn(event):
    list_box.add_item(new_task_input.text)
    new_task_input.clear()
    result_add_lbl.text = "As you wish, my liege"


def delete_task(event):
    list_box.remove_selected()


def one_done(event):
    if event.widget == list_box:
        finished_box.add_item(list_box.remove_selected())


def clear_all(event):
    finished_box.items = []
    clear_result_lbl.text = "My god, man. You've killed them all!"


# create widgets
new_task_lbl = gp.Label(app, "What needs doing?")
new_task_input = gp.Input(app)
new_task_btn = gp.Button(app, "Put it on the board", add_task_btn)
result_add_lbl = gp.Label(app, "")

list_lbl = gp.Label(app, "Live List")
list_box = gp.Listbox(app)
delete_btn = gp.Button(app, "Not doing it", delete_task)
all_done_btn = gp.Button(app, "Did all the things", None)


finished_label = gp.Label(app, "Kill List")
finished_box = gp.Listbox(app)
clear_btn = gp.Button(app, "Clear Killed", clear_all)
clear_result_lbl = gp.Label(app, "")


# Set up Events
new_task_input.add_event_listener('key_press', add_task)
list_box.add_event_listener('double_click', one_done)


# place widgets on grid
app.add(new_task_lbl, 1, 1, align="right")
app.add(new_task_input, 1, 2,  align="left", fill=True, stretch=True)
app.add(new_task_btn, 1, 3, align="center")
app.add(result_add_lbl, 2, 2, align='center')

app.add(list_lbl, 3, 1, align="right")
app.add(list_box, 3, 2, column_span=2, fill=True, stretch=True)
app.add(delete_btn, 4, 2, align='center')
app.add(all_done_btn, 4, 3, align='center')

app.add(finished_label, 5, 1, align='right')
app.add(finished_box, 5, 2, column_span=2, fill=True, stretch=True)
app.add(clear_btn, 6, 3, align='center')
app.add(clear_result_lbl, 6, 2, align='center')


# run app
app.run()
