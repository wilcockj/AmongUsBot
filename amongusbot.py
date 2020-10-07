from time import sleep
import pyautogui
import keyboard
import timeit
import platform


def main():
    # consts to make program marginally faster

    pyautogui.PAUSE = 0
    while True:
        if(keyboard.is_pressed('c') and keyboard.is_pressed('shift')):
            wiring_task()
        if(keyboard.is_pressed('q') and keyboard.is_pressed('shift')):
            break
    print("Done")


def wiring_task():
    heights = [272, 462, 647, 833]
    if platform.system() == 'Linux':
        rightcolordict = {"RGB(red=255, green=0, blue=0)": 272, "RGB(red=0, green=0, blue=255)": 462,
                          "RGB(red=255, green=235, blue=4)": 647, "RGB(red=255, green=0, blue=255)": 833}
    elif platform.system() == 'Windows':
        rightcolordict = {"(255, 0, 0)": 272, "(0, 0, 255)": 462,
                          "(255, 235, 4)": 647, "(255, 0, 255)": 833}
    print("Starting Wiring Task")
    start_time = timeit.default_timer()
    # colordict[location"] = pixel color
    # to print 272,462,647,833 could be faster probably not
    for x in range(4):
        # 1905
        pyautogui.moveTo(539, heights[x])
        try:
            pyautogui.dragTo(1353, rightcolordict[str(
                pyautogui.pixel(539, heights[x]))], .45, button='left')
            sleep(.05)
        except IndexError:
            print("no index try again")
        except KeyError:
            print("invalid key try again")
    print("Time to complete Wiring Task: " +
          str(round(timeit.default_timer() - start_time, 2)) + " seconds")


if __name__ == "__main__":
    main()
