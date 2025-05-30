import react, { useState } from 'react';
import './App.css';
import './styles.css';

function App() {
  const [formData, setFormData] = useState({
  mood: '',
  budget: '',
  time: '',
  activity: ''
});


  const [suggestion, setSuggestion] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuggestion(''); // Clear previous suggestion

    console.log("Submitted formData:", formData);
    
    try {
      const response = await fetch("http://127.0.0.1:5000/api/decide", { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      }
      );

      const data = await response.json();
      console.log("Received suggestion:", data);
      setSuggestion(data.suggestion);
    } catch (error) {
      console.error('Error fetching suggestions:', error);
      setSuggestion('Something went wrong. Try again!')
    }
  };

  return (
    <div className="main-container">
      {/* LEFT PANEL - About */}
      <div className="left-panel">
        <h2>About PickForMe</h2>
        <p>
          Ever feel indecisive about what to do? <strong>PickForMe</strong> is your AI-powered activity recommender.
          Based on your current <em>mood</em>, <em>budget</em>, <em>time of day</em>, and <em>activity type</em>,
          it suggests something personalized and fun to do!
        </p>
        <p>✨ Let your day be inspired by smart suggestions!</p>
      </div>

      {/* RIGHT PANEL - Form */}
      <div className="right-panel">
        <h2>Get Your Suggestion</h2>
        <p>Fill out the form below to get a personalized activity suggestion:</p>

        <form onSubmit={handleSubmit}>
          <label>Mood:
            <select name="mood" value={formData.mood} onChange={handleChange}>
              <option value="">Select</option>
              <option value="happy">Happy</option>
              <option value="sad">Sad</option>
              <option value="excited">Excited</option>
              <option value="bored">Bored</option>
              <option value="relaxed">Relaxed</option>
              <option value="adventurous">Adventurous</option>
              <option value="romantic">Romantic</option>
              <option value="tired">Tired</option>
            </select>
          </label>

          <label>Budget:
            <select name="budget" value={formData.budget} onChange={handleChange}>
              <option value="">Select</option>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </label>

          <label>Time:
            <select name="time" value={formData.time} onChange={handleChange}>
              <option value="">Select</option>
              <option value="morning">Morning</option>
              <option value="afternoon">Afternoon</option>
              <option value="evening">Evening</option>
              <option value="night">Night</option>
            </select>
          </label>

          <label>Activity:
            <select name="activity" value={formData.activity} onChange={handleChange}>
              <option value="">Select</option>
              <option value="indoor">Indoor</option>
              <option value="outdoor">Outdoor</option>
              <option value="cultural">Cultural</option>
              <option value="adventure">Adventure</option>
            </select>
          </label>

          <button type="submit">🎲 Generate Itinerary</button>
        </form>

        {suggestion && (
          <div className="suggestions">
            <h3>Your Mini Itinerary</h3>
            <pre>{suggestion}</pre>
            {/* <strong>Suggestion:</strong> {suggestion} */}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
