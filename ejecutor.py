import os, time, sys
pipe_name = 'pipe_test'

pipeout = os.open(pipe_name, os.O_WRONLY)
time.sleep(1)
os.write(pipeout,'0.001')
