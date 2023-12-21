from datetime import time
WORKING_HOURS_START = time(8,0)
WORKING_HOURS_END = time(20,0)

DEFAULT_SLOT = {
    'start_time' : WORKING_HOURS_START,
    'end_time' : WORKING_HOURS_END
}