from datetime import datetime
from .constant import WORKING_HOURS_START, WORKING_HOURS_END, DEFAULT_SLOT

def get_end_time(start_time, duration):
    start_hour, start_minute = start_time.split(':')
    end_hour = str(int(start_hour) + int(duration/60))
    end_minute = str(int(start_minute) + int(duration%60))
    return end_hour+":"+end_minute
    

def validate_slot_duration(start, end, duration):
    start = start.hour*60 + start.minute
    end = end.hour*60 + end.minute
    return end-start >= duration

def get_available_slots(bookings, duration):
    available_slots =[]
    bookings=list(bookings)

    if not bookings:
        return DEFAULT_SLOT
    
    start = WORKING_HOURS_START
    first_booking = bookings[0]['start_time']
    if first_booking > start and validate_slot_duration(start, first_booking, duration):
        slot = {
            'start_time': start,
            'end_time': first_booking
        }
        available_slots.append(slot)

    for i in range(0,len(bookings)-1):
        start_time = bookings[i]['end_time']
        end_time = bookings[i+1]['start_time']
        if  start_time< end_time and validate_slot_duration(start_time, end_time, duration):
            slot = {
                'start_time': start_time,
                'end_time': end_time
            }
            available_slots.append(slot)


    last_booking = bookings[-1]['end_time']
    end = WORKING_HOURS_END
    if last_booking < end and validate_slot_duration(last_booking, end, duration):
        slot = {
            'start_time': last_booking,
            'end_time': end
        }
        available_slots.append(slot)

    return available_slots


def convert_to_dmy(input_date_string):
    # List of date format patterns to try
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y", "%Y%m%d", "%d %B %Y", "%Y/%m/%d"]

    # Try parsing the input date with each format
    for format_pattern in date_formats:
        try:
            input_date = datetime.strptime(input_date_string, format_pattern)
            output_date_string = input_date.strftime("%Y-%m-%d")
            return output_date_string
        except Exception as e:
            print("error", e)
            print(format_pattern)
            pass  # Continue to the next format if parsing fails
    
    print("for done")
    # Return None if no valid format is found
    return None