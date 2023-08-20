import tkinter as tk
import requests

h = 700
w = 950

root = tk.Tk()
root.title("Co-Aid")
icon = tk.PhotoImage(file = "first-aid-symbol.png")
root.iconphoto(False, icon)
def format_response(case):
    try:
        continent = case['response'][0]['continent']
        country = case['response'][0]['country']
        pop = case['response'][0]['population']
        total = case['response'][0]['cases']['total']
        active = case['response'][0]['cases']['active']
        recover = case['response'][0]['cases']['recovered']

        final_str = '\nContinent: %s \nCountry: %s \nPopulation: %s \nTotal: %s \nCases acitve : %s \nRecovered : %s\n\n\nImportant Ways to Slow the Spread\n\n👉 Wear a mask that covers your nose and mouth.\n👉 Stay 6 feet apart from others who don’t live with you.\n👉 Get a COVID-19 vaccine when it is available to you.\n👉 Avoid crowds and poorly ventilated indoor spaces.\n👉 Wash your hands often with soap and water.\n👉 Use hand sanitizer if soap and water aren’t available' % (continent,country,pop,total,active,recover)

    except:
         final_str = 'There was a problem retrieving that information'

    return final_str

def get_country(country):
    headers = {
        'x-rapidapi-key': "05b8447828mshe0b636df50c3edbp1dda4fjsn9e10e707238f",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"}
    url = "https://covid-193.p.rapidapi.com/statistics?country=" + country
    response = requests.get(url, headers=headers)
    case = response.json()
    print(case)
    label['text'] = format_response(case)
   
canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

background_image = tk.PhotoImage(file='covid.png') 
background_label = tk.Label(root,image=background_image)
background_label.place(relx=0,rely=0,relwidth=1,relheight=1)

frame = tk.Frame(root, bg='#FF4040', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 20))
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Enter Country', font=('Courier', 12), command=lambda: get_country(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

frame2 = tk.Frame(root, bg='#FFD700', bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame2, font=('Courier', 15))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()