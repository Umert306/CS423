import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
    const [height, setHeight] = useState("");
    const [weight, setWeight] = useState("");
    const [result, setResult] = useState(null);

    const calculateBMI = async () => {
        try {
            const response = await axios.post("http://16.171.132.193:8000/calculate_bmi/", {
                height: parseFloat(height),
                weight: parseFloat(weight),
            });
            setResult(response.data);
        } catch (error) {
            console.error(error);
            setResult({ error: "Failed to calculate BMI. Please try again." });
        }
    };

    return (
        <div className="app">
            <h1>BMI Calculator</h1>
            <div className="form">
                <input
                    type="number"
                    placeholder="Height (cm)"
                    value={height}
                    onChange={(e) => setHeight(e.target.value)}
                />
                <input
                    type="number"
                    placeholder="Weight (kg)"
                    value={weight}
                    onChange={(e) => setWeight(e.target.value)}
                />
                <button onClick={calculateBMI}>Calculate BMI</button>
            </div>
            {result && (
                <div className="result">
                    {result.error ? (
                        <p>{result.error}</p>
                    ) : (
                        <>
                            <p>BMI: {result.BMI}</p>
                            <p>Category: {result.Category}</p>
                            <p>Tip: {result.Tip}</p>
                        </>
                    )}
                </div>
            )}
        </div>
    );
};

export default App;
