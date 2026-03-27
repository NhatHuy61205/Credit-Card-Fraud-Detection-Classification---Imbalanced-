import React from "react"
import { useTranslation } from "react-i18next"
import { NavLink } from "react-router-dom"
import "./Sidebar.css"

export default function Sidebar() {
  const { t } = useTranslation()
  
  return (
    <aside className="sidebar">
      <div className="logo">Fraud Detection</div>
      <nav className="menu">
        <NavLink to="/" className="menu-item">
          <i class="fa-solid fa-chart-line"></i> {t("dashboard")} <i class="fa-solid fa-angle-right arrow"></i>
        </NavLink>
        <NavLink to="/transactions" className="menu-item">
          <i class="fa-regular fa-credit-card"></i> {t("transactions")} <i class="fa-solid fa-angle-right arrow"></i>
        </NavLink>
        <NavLink to="/payments" className="menu-item">
          <i class="fa-solid fa-dollar-sign"></i> {t("payments")} <i class="fa-solid fa-angle-right arrow"></i>
        </NavLink>
      </nav>
    </aside>
  );
}