import React from "react";
import UploadBox from "./components/UploadBox";
import "./styles/app.css";

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">🎬 AI Agent Video Editor</h1>
      <UploadBox />
    </div>
  );
}

export default App;