import React, { useState } from "react";
import axios from "axios";
import './App.css'

const ImageGeneratorForm = () => {
  const [words, setWords] = useState([]);
  const [input, setInput] = useState("");
  const [response, setResponse] = useState(null);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleAddWord = () => {
    if (input && words.length < 10) {
      setWords([...words, input]);
      setInput("");  // Clear input after adding
    }
  };

  const handleSubmit = async () => {
    if (words.length === 0) {
      alert("Please add some words!");
      return;
    }

    // Send the words list to the FastAPI server
    try {
      const res = await axios.post("http://localhost:8000/", {
        image_list: words,
      });

      setResponse(res.data); // Set response to display after successful API call
    } catch (error) {
      console.error("Error sending request:", error);
      alert("An error occurred while generating images.");
    }
  };

  const handleRemoveWord = (index) => {
    const newWords = words.filter((_, i) => i !== index);
    setWords(newWords);
  };

  return (
    <div>
      <h1>Image Generator</h1>

      <div>
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Enter a word"
        />
        <button onClick={handleAddWord} disabled={words.length >= 10}>
          Add Word
        </button>
      </div>

      <div>
        <h2>Words List:</h2>
        <ul>
          {words.map((word, index) => (
            <li key={index}>
              {word}{" "}
              <button onClick={() => handleRemoveWord(index)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>

      <button onClick={handleSubmit}>Generate Images</button>

      {response && (
        <div>
          <h2>Response:</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default ImageGeneratorForm;
