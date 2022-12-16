import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        music_data = open(file, 'rb')
    except FileNotFoundError:
        print(
            f"FileNotFoundError: [Errno 2] No such file or directory: '{file}'")
    else:
        # print(music_data.read())
        param = music_data.read()
        music_data.close()
    finally:
        finish_time = time.time()
        time_dur = finish_time - start_time
        print(f"Time required for {file} = {time_dur}")


video_data = read_file_timed('Лера Массква - 7 этаж.mp3')
video_data = read_file_timed('Нет такого файла тут.mp3')
