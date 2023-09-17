from tkinter import *

def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles*1.609) #마일을 킬로미터로 변환
    kilometer_result_label.config(text=f"{km}") #결과 텍스트 변환

window=Tk()
window.title("마일을 킬로미터로 바꾸기")
window.config(padx=20,pady=20) #창 사이즈 조절.

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0) #grid로 각각의 변수 위치를 조정함.

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=mile_to_km) #command에 함수를 연결해서 버튼 누를 때 함수가 실행되도록 함.
calculate_button.grid(column=1,row=2)

window.mainloop()
