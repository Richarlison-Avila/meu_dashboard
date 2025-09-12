import React from "react";
import { Link, useLocation } from "react-router-dom";

const Sidebar = () => {
  const location = useLocation();
  const links = [
    { name: "Home", path: "/" },
    { name: "Agenda", path: "/agenda" },
    { name: "Financeiro", path: "/financeiro" },
    { name: "Vendas", path: "/vendas" },
    { name: "Configurações", path: "/configuracoes" },
  ];

  return (
    <div className="w-64 bg-blue-800 text-white flex flex-col p-4">
      <h1 className="text-2xl font-bold mb-8">Dashboard</h1>
      {links.map((link) => (
        <Link
          key={link.path}
          to={link.path}
          className={`p-2 rounded hover:bg-blue-700 mb-2 ${
            location.pathname === link.path ? "bg-blue-900" : ""
          }`}
        >
          {link.name}
        </Link>
      ))}
    </div>
  );
};

export default Sidebar;
