import React from "react"

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="logo">Fraud Detection</div>
      <nav className="menu">
        <a className="menu-item active"><i class="fa-solid fa-house"></i> Home <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-chart-line"></i> Dashboard <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-regular fa-bell"></i> Notifications <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-dollar-sign"></i> Transactions <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-gear"></i> Settings <i class="fa-solid fa-angle-right arrow"></i></a>
      </nav>
    </aside>
  );
}