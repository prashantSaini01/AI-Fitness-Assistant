class FitnessCalculators:
    @staticmethod
    def calculate_bmi(weight, height):
        """Calculate BMI and return category"""
        try:
            bmi = weight / ((height/100) ** 2)
            
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
                
            return {
                "bmi": str(round(bmi, 2)),
                "category": category,
                "summary": f"Your BMI is {str(round(bmi, 2))} which falls into the {category} category."
            }
        except ZeroDivisionError:
            return {"error": "Height cannot be zero"}
        except Exception as e:
            return {"error": str(e)}