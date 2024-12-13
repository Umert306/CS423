from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Define input data structure
class BMIInput(BaseModel):
    height: float  # Height in cm
    weight: float  # Weight in kg

# Create FastAPI app instance
app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate_bmi/")
async def calculate_bmi(input_data: BMIInput):
    try:
        height_m = input_data.height / 100  # Convert height from cm to meters
        bmi = round(input_data.weight / (height_m ** 2), 2)
        
        if bmi < 18.5:
            category = "Underweight"
            tip = "Increase calorie intake with nutrient-dense foods like nuts and seeds."
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            tip = "Maintain your current weight with a balanced diet and regular exercise."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            tip = "Reduce calorie-dense foods and increase physical activity."
        else:
            category = "Obese"
            tip = "Consult a healthcare professional for personalized advice."
        
        return {"BMI": bmi, "Category": category, "Tip": tip}
    except ZeroDivisionError:
        return {"error": "Invalid input. Height must be greater than 0."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
