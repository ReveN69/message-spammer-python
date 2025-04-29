import pyautogui
text = input("Enter the text: ")
counttext = int(input("Enter number:"))
for i in range (0, counttext):
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
