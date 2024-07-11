import time

def timer(sure_saniye):
    print(f"Timer başladı! {sure_saniye} saniye bekleyecek")

    while sure_saniye:
        mins, secs = divmod(sure_saniye, 60)
        zaman_formati = '{:02d}:{:02d}'.format(mins, secs)
        print(zaman_formati, end='\r')
        time.sleep(1)
        sure_saniye -= 1

    print("Timer Bitti!")

timer(10)