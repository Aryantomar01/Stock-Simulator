from taipy import Gui
import pandas as pd
data = {
    "Date": pd.date_range("2024-04-04", periods=4, freq="D"),
    "Min": [22,19.7,2.7,6.5],
    "Max": [8.6,8.2,12.,13.5]
}

title="Stock Simulator By Aryan"
path="stock.png"
Company_name="TCS"
Company_minp=500
Company_maxp=1000

def Aryan(state):
    print("Aryan")
    print(state.path)
    print(state.Company_minp)

    with open("data.txt","w") as f:
        f.write(f"{state.Company_name},{state.Company_minp},{state.Company_maxp}")

page="""
<|text-center|
<|{path}|image|>

<|{title}|hover_text="Welcome To Stock Screen"|>

Name Of Stock: <|{Company_name}|input|>

Min Prize: <|{Company_minp}|input|>

Max Prize: <|{Company_maxp}|input|>

<|Run Simulation|button|on_action=Aryan|>

<|{title}|hover_text="Your Simulation"|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>
>
"""

if __name__=="__main__":
    app=Gui(page)
    app.run(use_reloader=True)
