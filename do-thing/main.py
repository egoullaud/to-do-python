'''
main.py
  Here you will write your code while following the lessons.

hello.py
  This file contains the boilerplate code included in the GooeyPie Repl template - https://replit.com/@mrantonio/GooeyPie-Template?v=1

complete.py
  Spoiler: complete.py has a completed implementation. For your IDEAL learning experience the completed project should NOT be viewed until after the workshop is done.
'''
import gooeypie as gp

# name the app on top of window
app = gp.GooeyPieApp('Do the Thing')

# width of window
app.width = 700

# set up grid
app.set_grid(3, 3)

# Define label and button

hello_btn = gp.Button(app, "Put it on the board", None)
prompt_lbl = gp.Label(app, 'What needs doing?')

# display on app
app.add(hello_btn, 2, 2, align='left')
app.add(prompt_lbl, 2, 1, align='right')


# always last
app.run()
