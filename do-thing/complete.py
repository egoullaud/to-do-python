import gooeypie as gp


def add_new_task(event):
    """Adds a new task from when the Enter/Return key is pressed"""
    if event.key['name'] == 'Return' and new_task_inp.text != "":
        todo_lst.add_item(new_task_inp.text)
        new_task_inp.clear()
        new_task_inp.focus()


def move_task(event):
    """Moves a task from one listbox to another"""
    if event.widget == todo_lst:
        # move the task from the todo list to the done list
        done_lst.add_item(todo_lst.remove_selected())
    else:
        # move the task back from the done list to the todo list
        todo_lst.add_item(done_lst.remove_selected())


def delete_task(event):
    """Deletes a task from the todo list"""
    todo_lst.remove_selected()
    new_task_inp.focus()


def all_done(event):
    """Moves all tasks from the todo list to the done list"""
    done_lst.items += todo_lst.items
    todo_lst.items = []


def clear_all(event):
    """Remove all tasks from the done list"""
    done_lst.items = []


app = gp.GooeyPieApp('Simple Todo')
app.width = 400

# Create all widgets
new_task_lbl = gp.Label(app, 'New task')
new_task_inp = gp.Input(app)
todo_lbl = gp.Label(app, 'Todo list')
todo_lst = gp.Listbox(app)
delete_task_btn = gp.Button(app, 'Delete task', delete_task)
all_done_btn = gp.Button(app, 'All done!', all_done)
done_lbl = gp.Label(app, 'Done!')
done_lst = gp.Listbox(app)
clear_all_btn = gp.Button(app, 'Clear all', clear_all)

# Set up events
new_task_inp.add_event_listener('key_press', add_new_task)
todo_lst.add_event_listener('double_click', move_task)
done_lst.add_event_listener('double_click', move_task)

# Add widgets to window
app.set_grid(5, 3)
app.set_column_weights(0, 1, 1)
app.set_row_weights(0, 1, 0, 1, 0)
app.add(new_task_lbl, 1, 1, align='right')
app.add(new_task_inp, 1, 2, column_span=2, fill=True)
app.add(todo_lbl, 2, 1, align='right')
app.add(todo_lst, 2, 2, column_span=2, fill=True, stretch=True)
app.add(delete_task_btn, 3, 2, fill=True)
app.add(all_done_btn, 3, 3, fill=True)
app.add(done_lbl, 4, 1, align='right')
app.add(done_lst, 4, 2, column_span=2, fill=True, stretch=True)
app.add(clear_all_btn, 5, 3, fill=True)

new_task_inp.focus()
app.run()
