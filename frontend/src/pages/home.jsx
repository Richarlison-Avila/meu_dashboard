import React from "react";

export default function Home() {
  return (
    <div className="home">
      <h1>Bem-vindo ao Dashboard</h1>
      <div className="cards-container" style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        <div className="card">
          <h3>Vendas Hoje</h3>
          <p>R$ 1.250,00</p>
        </div>
        <div className="card">
          <h3>Entradas</h3>
          <p>R$ 2.000,00</p>
        </div>
        <div className="card">
          <h3>Saídas</h3>
          <p>R$ 750,00</p>
        </div>
        <div className="card">
          <h3>Saldo</h3>
          <p>R$ 1.250,00</p>
        </div>
      </div>
    </div>
  );
}
