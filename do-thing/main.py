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
app.set_grid(5, 3)

# attach hello button

hello_btn = gp.Button(app, "Rack it!", None)
hello_lbl = gp.Label(app, 'What needs doing?')

# add them to the app
app.add(hello_btn, 4, 2, align='left')
app.add(hello_lbl, 4, 1, align='right')


# always last
app.run()
