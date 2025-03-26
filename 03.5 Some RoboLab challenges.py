#!/usr/bin/env python
# coding: utf-8

# # 5 RoboLab challenges
# 
# In this notebook, you will be presented with a series of challenges to complete. These challenges are a bit different from the activities you have completed in earlier RoboLab sessions. We leave you to work out the details of the challenges for yourself, although you are encouraged to use the forums if you need help or if you want to share or discuss any of your ideas with other students. Essentially, the challenges define a task for you to complete and you must decide how to complete them.
# 
# The purpose of the challenges is to allow you to try your hand at writing your own RoboLab programs. Don’t spend too much time on this work. If you get stuck, take a break: it’s surprising how often a solution to a programming problem comes to mind if you take a few minutes away from the screen and the keyboard and do something completely different instead.
# 
# The challenges in the next notebook are more difficult and are completely optional. They generally require you to have had some computer programming experience before you started this module.

# ## 5.1 Configuring the simulator
# 
# To download code to the simulator, use one of the simulator magics.
# 
# For example, prefix a code cell with the `%%sim_magic_preloaded` block magic as the first line to download the code in the cell to the simulator. Remember that you can use the `%sim_magic_preloaded --preview` command to show the code that is automatically imported and the `%sim_magic --help` command to show all available magic switches.
# 
# You may find the following specific switches useful when configuring the simulator via the magic:
# 
# - `-b BACKGROUND_NAME`: load in a particular background file
# - `-x X_COORD`: specify the initial *x*-coordinate value for the simulated robot
# - `-y Y_COORD`: specify the initial *y*-coordinate value for the simulated robot
# - `-a ANGLE`: specify the initial rotation angle for the simulated robot
# - `-p`: specify pen-down mode
# - `-C`: clear the pen trace.
# 
# Load in the simulator in the usual way:

# In[1]:


from nbev3devsim.load_nbev3devwidget import roboSim, eds

get_ipython().run_line_magic('load_ext', 'nbev3devsim')


# ### 5.1.1 Challenge – Moving the simulated robot forwards
# 
# Write a program to make the simulated robot move forwards for two seconds. Download your program to the simulator and run it to check that it performs as required.
# 
# Remember to prefix the code cell with a magic command that will download the code to the simulator.

# *Make any notes/observations about how your program worked, or any issues associated with getting it to work, etc. to help you complete the task here.*

# In[4]:


get_ipython().run_cell_magic('sim_magic_preloaded', '', 'from ev3dev2.motor import Motor, SpeedPercent, OUTPUT_B, OUTPUT_C\nimport time\n\nleft_motor = Motor(OUTPUT_B)\nright_motor = Motor(OUTPUT_C)\n\n\nleft_motor.on(SpeedPercent(50))\nright_motor.on(SpeedPercent(50))\ntime.sleep(2)\n')


# ### 5.1.2 Challenge – Fitness training
# 
# *You can complete and submit this activity as part of your ePortfolio.*
# 
# Write a program to make the simulated robot move forwards a short distance and then reverse to its starting point, repeating this action another four times (so five traverses in all). Download your program to the simulator and run it to check that it performs as required.
# 
# Optionally, extend your program so that it speaks aloud a count of how many traverses it has completed so far, each time it gets back to the start.

# *Initially I did struggle with getting the robot to load but this has been discussed in the forum. I knew that as we were going to be performing the same task numerous times that I would be using a while loop for a Boolean check, I used the variable called flag to count the number of times we iterated through the loop, each time increasing the count by one, when the boolean returned False the while loop finished and the program was completed.*

# In[10]:


get_ipython().run_cell_magic('sim_magic_preloaded', '', '\ncount = 0\n\nwhile count <5:\n    tank_drive.on_for_rotations(SpeedPercent(40),\n                            SpeedPercent(40), 4)\n    tank_drive.on_for_rotations(SpeedPercent(-40),\n                            SpeedPercent(-40), 4)\n    count = count + 1\n\n')


# ### 5.1.3 Challenge – Making a countdown program
# 
# Write a program to make the simulated robot speak aloud a countdown from 10 to 0, finishing by saying ‘OK’. Download the program to the simulator and run it to check that it performs as required.

# *Make any notes to help you complete the task here.*

# In[4]:


get_ipython().run_cell_magic('sim_magic_preloaded', '', '\ncount = 10\n\nwhile count >= 0:\n    print(count)\n    say(str(count))\n    count = count - 1\n')


# *Using a simple while loop we are able to count backwards from 10, we do so as the while loop checks the condition that the count is not equal to zero, If the count is not equal to zero the loop continues and the count is adjusted by negative 1 each turn.*

# ### 5.1.4 Challenge – Fitness training take&nbsp;2
# 
# In the first fitness training challenge, the robot had to cover the same distance backwards and forwards five times.
# 
# In this challenge, the robot should only do three forwards and backwards traverses, but in a slightly different way. On the first, it should travel forward and backward a short distance; on the second, it should travel twice as far forward and backward as the first; on the third, it should travel three times as far forward and backward as the first.
# 
# Download your program to the simulator and run it to check that it performs as required.

# *Make any notes to help you complete the task here.*

# In[9]:


get_ipython().run_cell_magic('sim_magic_preloaded', '', '\ncount = 0\nrotations = 2\nspeed = 40\n#flag = 1\nwhile count <3:\n    tank_drive.on_for_rotations(SpeedPercent(speed),\n                            SpeedPercent(speed), rotations)\n    tank_drive.on_for_rotations(SpeedPercent(-speed),\n                            SpeedPercent(-speed), rotations)\n    #flag = flag + 1\n    count = count + 1 \n    #rotations = rotations * flag\n    rotations = rotations * count\n')


# *I found it a little difficult to make the robot multiply the rotations by 2 and then by 3, but I thought if I added another flag this would give better control over how far it's moving each time and this is what I first came up with. I felt that it was a little bit clunky, so I decided to just multiply the rotations by the current count instead which lead me to a cleaner piece of code.*

# In[ ]:




