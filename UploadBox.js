import React, { useState } from "react";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);
  const [videoURL, setVideoURL] = useState("");

  const handleUpload = async () => {
    if (!file) return alert("Please select a file first");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      setVideoURL(data.video_url);
      alert("✅ Upload and AI processing completed!");
    } catch (error) {
      console.error("Error:", error);
      alert("❌ Something went wrong!");
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-96 mx-auto mt-12">
      <h2 className="text-xl font-bold mb-4">Upload Audio</h2>
      <input
        type="file"
        accept="audio/*"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Upload & Process
      </button>

      {videoURL && (
        <div className="mt-6">
          <h3 className="font-semibold">Generated Video:</h3>
          <video
            src={`http://127.0.0.1:8000${videoURL}`}
            controls
            className="w-full mt-2 rounded"
          ></video>
        </div>
      )}
    </div>
  );
}

export default UploadBox;