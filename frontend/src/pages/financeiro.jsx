import React from "react";
import "../styles/Financeiro.css";

export default function Financeiro() {
  const movimentos = [
    { id: 1, descricao: "Venda produto A", valor: 500, tipo: "entrada" },
    { id: 2, descricao: "Compra material", valor: -150, tipo: "saida" },
    { id: 3, descricao: "Venda produto B", valor: 700, tipo: "entrada" },
  ];

  return (
    <div className="financeiro">
      <h1>Financeiro</h1>
      <div className="cards">
        <div className="card entrada">
          <h3>Entradas</h3>
          <p>R$ {movimentos.filter(m => m.tipo === "entrada").reduce((acc,m)=>acc+m.valor,0)}</p>
        </div>
        <div className="card saida">
          <h3>Saídas</h3>
          <p>R$ {Math.abs(movimentos.filter(m => m.tipo === "saida").reduce((acc,m)=>acc+m.valor,0))}</p>
        </div>
        <div className="card saldo">
          <h3>Saldo</h3>
          <p>R$ {movimentos.reduce((acc,m)=>acc+m.valor,0)}</p>
        </div>
      </div>
    </div>
  );
}
