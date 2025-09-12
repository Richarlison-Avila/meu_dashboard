import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import "../styles/Layout.css";
import { FaHome, FaCalendarAlt, FaMoneyBillWave, FaShoppingCart, FaCog, FaBars } from "react-icons/fa";

export default function Layout({ children }) {
  const location = useLocation();
  const [collapsed, setCollapsed] = useState(false);

  const menuItems = [
    { path: "/", label: "Home", icon: <FaHome /> },
    { path: "/agenda", label: "Agenda", icon: <FaCalendarAlt /> },
    { path: "/financeiro", label: "Financeiro", icon: <FaMoneyBillWave /> },
    { path: "/vendas", label: "Vendas", icon: <FaShoppingCart /> },
    { path: "/configuracoes", label: "Configurações", icon: <FaCog /> },
  ];

  return (
    <div className={`layout ${collapsed ? "collapsed" : ""}`}>
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>Meu Dashboard</h2>
          <button className="collapse-btn" onClick={() => setCollapsed(!collapsed)}>
            <FaBars />
          </button>
        </div>
        <nav>
          {menuItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={location.pathname === item.path ? "active" : ""}
            >
              <span className="icon">{item.icon}</span>
              {!collapsed && <span className="label">{item.label}</span>}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="content">{children}</main>
    </div>
  );
}
