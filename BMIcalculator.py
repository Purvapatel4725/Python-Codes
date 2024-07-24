#Purva Patel #100886734
from tkinter import *
import math

class BMI_Calculator:
    
    def __init__(self, xyz):
        self.master = xyz
        xyz.title("BMI Calculator")

        # Create a label frame for the inputs
        self.InputFrame = LabelFrame(xyz, text="Enter Your Details", padx=10, pady=10)
        self.InputFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Create the height input
        self.HeightLable = Label(self.InputFrame, text="Height (in \"m\"):")
        self.HeightLable.grid(row=0, column=0, padx=10, pady=10)
        self.HeightEntry = Entry(self.InputFrame, width=10)
        self.HeightEntry.grid(row=0, column=1, padx=10, pady=10)
        
        # Create the weight input
        self.WeightLable = Label(self.InputFrame, text="Weight (in \"kg\"):")
        self.WeightLable.grid(row=1, column=0, padx=10, pady=10)
        self.WeightEntry = Entry(self.InputFrame, width=10)
        self.WeightEntry.grid(row=1, column=1, padx=10, pady=10)
        
        # Create the calculate button
        self.CalcButton = Button(xyz, text="Calculate BMI", command=self.calculate_bmi_number, bg="#4CAF50", fg="red", padx=10, pady=10)
        self.CalcButton.grid(row=1, column=0, padx=20, pady=(0, 20))
        
        # Create a label frame for the results
        self.ResultFrame = LabelFrame(xyz, text="Results", padx=10, pady=10)
        self.ResultFrame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Create the result label
        self.ResultLable = Label(self.ResultFrame, text="", font=("Arial", 20))
        self.ResultLable.pack(padx=10, pady=10)
        
        # Create the BMI status label
        self.BMIlable = Label(self.ResultFrame, text="", font=("Arial", 16))
        self.BMIlable.pack(padx=10, pady=10)
        
    def calculate_bmi_number(self):
        try:
            height = float(self.HeightEntry.get())
            weight = float(self.WeightEntry.get())
            BMI = weight / math.pow(height, 2)
            self.ResultLable.config(text="{:.2f}".format(BMI))
            self.display_bmi_status(BMI)
        except ValueError:
            self.ResultLable.config(text="Enter valid height and weight!")
        
    def display_bmi_status(self, bmiValue):
        if bmiValue < 18.5:
            status = "Underweight"
        elif 18.5 <= bmiValue < 24.9:
            status = "Healthy Weight"
        else:
            status = "Overweight"
        self.BMIlable.config(text=status)
        
tkinterLib = Tk()
bmi_calc = BMI_Calculator(tkinterLib)
tkinterLib.mainloop()
