# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import diffimg as di

#di.diff('C:/Users/Dell/Downloads/CVPK4263-PhotoRoom.png', 'C:/Users/Dell/Downloads/CVPK4263(1).png')
di.diff('sample_images/img_1.jpg',
     'sample_images/img_1_1.jpg',
     delete_diff_file=False,
     diff_img_file='Output/diffimg.png',
     ignore_alpha=False)

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''