import React from "react";
import "../styles/Vendas.css";

export default function Vendas() {
  const vendas = [
    { id: 1, produto: "Produto A", quantidade: 10, valor: 500 },
    { id: 2, produto: "Produto B", quantidade: 5, valor: 700 },
    { id: 3, produto: "Produto C", quantidade: 2, valor: 300 },
  ];

  return (
    <div className="vendas">
      <h1>Vendas</h1>
      <table>
        <thead>
          <tr>
            <th>Produto</th>
            <th>Quantidade</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          {vendas.map((v) => (
            <tr key={v.id}>
              <td>{v.produto}</td>
              <td>{v.quantidade}</td>
              <td>R$ {v.valor}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
