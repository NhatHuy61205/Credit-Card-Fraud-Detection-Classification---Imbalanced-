import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Sidebar from "./components/Sidebar/Sidebar";
import Topbar from "./components/Topbar/Topbar";

import Dashboard from "./pages/Dashboard/Dashboard"
import Payments from "./pages/Payments/Payments";
function App() {

  return (
    <BrowserRouter>

      <div className="layout">

        <Sidebar />

        <main className="main">

          <Topbar />

          <Routes>

            <Route path="/" element={<Dashboard />} />
            <Route path="/payments" element={<Payments />} />

          </Routes>

        </main>

      </div>

    </BrowserRouter>

  )

}

export default App