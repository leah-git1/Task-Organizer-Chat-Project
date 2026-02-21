import React, { useState } from "react";
import axios from "axios";

export default function ChatBot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    setMessages([...messages, { sender: "user", text: input }]);

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        message: input,
      });

      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: response.data.response },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "❌ קרתה שגיאה בשרת" },
      ]);
    }

    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div style={styles.container}>
      <h2>צ'אט ניהול משימות</h2>
      <div style={styles.chatBox}>
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              ...styles.message,
              alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
              backgroundColor: msg.sender === "user" ? "#DCF8C6" : "#EEE",
            }}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="כתוב כאן..."
        style={styles.input}
      />
      <button onClick={sendMessage} style={styles.button}>
        שלח
      </button>
    </div>
  );
}

const styles = {
  container: { width: "400px", margin: "50px auto", display: "flex", flexDirection: "column", fontFamily: "Arial, sans-serif" },
  chatBox: { height: "400px", border: "1px solid #ccc", padding: "10px", overflowY: "scroll", display: "flex", flexDirection: "column", marginBottom: "10px" },
  message: { padding: "8px", borderRadius: "8px", margin: "5px 0", maxWidth: "70%" },
  input: { padding: "10px", fontSize: "16px", marginBottom: "10px" },
  button: { padding: "10px", fontSize: "16px", cursor: "pointer" },
};