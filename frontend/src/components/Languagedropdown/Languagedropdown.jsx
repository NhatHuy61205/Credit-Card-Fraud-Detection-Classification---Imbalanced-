import { useState } from "react";
import React from "react"
import i18n from "i18next";
import "./Languagedropdown.css"

function changeLang(lang){
  i18n.changeLanguage(lang)
} 

export default function LanguageDropdown() {
    const [language, setLanguage] = useState("English");
    const [open, setOpen] = useState(false);

    return (
        <div className="lang-container">
            <div className="lang-btn"onClick={() => setOpen(!open)}>
                {language}
            </div>

            <div className={`lang-box ${open ? "active" : ""}`}>
                <div className="lang-option" onClick={() => {
                        setLanguage("English");
                        setOpen(false);
                        changeLang("en");
                    }}>
                    English
                </div>
                <div className="lang-option" onClick={() => {
                        setLanguage("Tiếng Việt");
                        setOpen(false);
                        changeLang("vi");
                    }}>
                    Tiếng Việt
                </div>
                <div className="lang-option" onClick={() => {
                        setLanguage("中文");
                        setOpen(false);
                        changeLang("zh");
                    }}>
                    中文
                </div>
            </div>
        </div>
    );
}
