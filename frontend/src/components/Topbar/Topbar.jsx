import React, { useState } from "react";
import LanguageDropdown from "../Languagedropdown/Languagedropdown";
import "./Topbar.css";

export default function Topbar() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Chọn file trước!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log(data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <header className="topbar">
      <div>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload</button>
      </div>
      <LanguageDropdown />
    </header>
  );
}