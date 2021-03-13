from selenium import webdriver
from time import sleep
from datetime import datetime
import tkinter as tk
import getpass

now = datetime.now() # Get The Time
username = getpass.getuser() # Get Username
thetxt = open('c:/users/' + str(username) + '/desktop/fill.txt') # Grab config file

lineread = thetxt.readlines()

chromedriver_location = str(lineread[5])

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=XYl7mAJPm0i5TUkXBGnu90WQw_c63PZOtGrFHbAgXFNUNFFZMkxJT0FBRlMxTVpMVTBDUU1LWDZCUy4u")

date_input = '/html/body/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/input[1]'
ledate = now.strftime("%m/%d/%Y")

student_id_Input = '/html/body/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/input'
student_id = lineread[0]

first_name_input = '/html/body/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div[2]/div/div/input'
first_name = lineread[1]

Last_Name_Input = '/html/body/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[4]/div/div[2]/div/div/input'
Last_Name = lineread[2]

thegradestring = int(lineread[3]) + 1

drop_down_opener = '/html/body/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[5]/div/div[2]/div/div'
grade_clicker = '//*[@id="Select_0"]/ul/li[' + str(thegradestring) + ']'

remote_learning_clicker = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input'
hybrid_learning_clicker = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[6]/div/div[2]/div/div[2]/div/label/input'
inperson_learning_clicker = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[6]/div/div[2]/div/div[3]/div/label/input'

im_in_attendence = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[7]/div/div[2]/div/div[1]/div/label/input'
im_available = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[7]/div/div[2]/div/div[2]/div/label/input'

submit_button = '//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[3]/div[1]/button'

driver.find_element_by_xpath(date_input).send_keys(ledate) #the date field
driver.find_element_by_xpath(student_id_Input).send_keys(student_id) 
driver.find_element_by_xpath(first_name_input).send_keys(first_name)
driver.find_element_by_xpath(Last_Name_Input).send_keys(Last_Name)
driver.find_element_by_xpath(drop_down_opener).click() #open drop down
driver.find_element_by_xpath(grade_clicker).click() #click grade 6
if lineread[4] == "remote":
    driver.find_element_by_xpath(remote_learning_clicker).click()
else:
    if lineread[4] == "hybrid":
        driver.find_element_by_xpath(hybrid_learning_clicker).click()
    else:
        if lineread[4] == "inperson":
            driver.find_element_by_xpath(inperson_learning_clicker).click()
        else:
            driver.quit
            root = tk.Tk()
            T = tk.Text(root, height=5, width=30)
            T.pack()
            T.configure(font=("Arial", 16, "bold"))
            T.insert(tk.END, "You Haven't chosen a learning type yet!\nThe options for learning types ares\nremote, hybrid or inperson\n")
            tk.mainloop()
            driver.quit
driver.find_element_by_xpath(im_in_attendence).click() #click i am in attendence
driver.find_element_by_xpath(im_available).click() #click i am available
driver.find_element_by_xpath(submit_button).click() #submit
driver.quit()

root = tk.Tk()
T = tk.Text(root, height=15, width=30)
T.pack()
T.insert(tk.END, "made by noah henok")
tk.mainloop()

