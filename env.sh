#!/bin/bash

# All the settings are now read from env variables.
# Before running the project you need to seet them all in your environment.
# On Linux: change the values accordin to your own settings and put these lines in .bashrc or
# in the activate script of virtualenv.
# On Heroku: heroku config:add RASPBERRYWHITE_DEBUG="True"

export ATMLOCAL_PORT="8000"
