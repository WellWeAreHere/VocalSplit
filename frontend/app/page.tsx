"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      alert(response.data.message);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-6">
      <h1 className="text-5xl font-bold">🎤 VocalSplit</h1>

      <input
        type="file"
        accept=".mp3,audio/*"
        onChange={(e) => {
          if (e.target.files) {
            setFile(e.target.files[0]);
          }
        }}
      />

      <button
        onClick={uploadFile}
        className="bg-black text-white px-6 py-3 rounded-xl"
      >
        Upload
      </button>
    </main>
  );
}