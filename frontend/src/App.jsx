import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Sidebar from "./components/Sidebar/Sidebar";
import Topbar from "./components/Topbar/Topbar";

import Home from "./pages/Home/Home"
import Dashboard from "./pages/Dashboard/Dashboard"
import Notifications from "./pages/Notifications/Notifications"
import Transactions from "./pages/Transaction/Transactions"
import Settings from "./pages/Settings/Settings"

function App() {

  return (
    <BrowserRouter>

      <div className="layout">

        <Sidebar />

        <main className="main">

          <Topbar />

          <Routes>

            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/transactions" element={<Transactions />} />
            <Route path="/settings" element={<Settings />} />

          </Routes>

        </main>

      </div>

    </BrowserRouter>

  )

}

export default App