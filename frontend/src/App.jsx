import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
function App(){

  return(
   <div className="layout">

      <Sidebar />

      <main className="main">
        <Topbar />

      </main>

    </div>
  )

}

export default App