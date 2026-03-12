import React from "react"
import { useTranslation } from "react-i18next"

export default function Sidebar() {
  const { t } = useTranslation()

  return (
    <aside className="sidebar">
      <div className="logo">Fraud Detection</div>
      <nav className="menu">
        <a className="menu-item active"><i class="fa-solid fa-house"></i> {t("home")} <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-chart-line"></i> {t("dashboard")} <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-regular fa-bell"></i> {t("notifications")} <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-dollar-sign"></i> {t("transactions")} <i class="fa-solid fa-angle-right arrow"></i></a>
        <a className="menu-item"><i class="fa-solid fa-gear"></i> {t("settings")} <i class="fa-solid fa-angle-right arrow"></i></a>
      </nav>
    </aside>
  );
}