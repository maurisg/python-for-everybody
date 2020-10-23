def add_time(start, duration):
    i = 0
    count = 0
    time, clock = start.split()
    start_hour, start_minutes = time.split(":")
    duration_hour, duration_minutes = duration.split(":")

    start_hour = int(start_hour)
    start_minutes = int(start_minutes)
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    if duration_hour > 12:
        while i <= duration_hour:
            i += 1
            if i % 12 == 0:
                count += 1
                continue
        hours_left = duration_hour - (count*12)

        new_hour = start_hour + hours_left
        new_minute = start_minutes + duration_minutes

        if clock == 'PM':
            if new_hour >= 12:
                new_hour = new_hour - 12
                count = count + 1

                days_later = (count // 2) + 1

                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    count = count + 1

                    days_later = (count // 2) + 1

                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock \
                                   + " ({days_later} days later)".format(days_later=days_later)

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " AM" \
                                   + " ({days_later} days later)".format(days_later=days_later)

                else:
                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock \
                                   + " ({days_later} days later)".format(days_later=days_later)

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " AM" \
                                   + " ({days_later} days later)".format(days_later=days_later)
            else:
                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    count = count + 1

                    days_later = (count // 2) + 1

                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock + " (next day)"

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " AM" \
                                   + " ({days_later} days later)".format(days_later=days_later)

        else:
            if new_hour >= 12:
                new_hour = new_hour - 12
                count = count + 1

                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    count = count + 1

                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"

                else:
                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"
            else:
                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    count = count + 1

                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"

                else:
                    if count % 2 == 0:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock + " (next day)"

                    else:
                        new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"

    else:
        new_hour = start_hour + duration_hour
        new_minute = start_minutes + duration_minutes

        if clock == "AM":
            if new_hour > 12:
                new_hour = new_hour - 12

                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"

                else:
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

            else:
                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " PM"

                else:
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

        else:
            if new_hour > 12:
                new_hour = new_hour - 12

                if new_minute >= 60:
                    new_minute = new_minute - 60
                    new_hour = new_hour + 1
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " AM"

                else:
                    new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " AM" + " (next day)"

            else:
                new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + clock

    return new_time
