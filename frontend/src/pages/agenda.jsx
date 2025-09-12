import React from "react";
import "../styles/Agenda.css";

export default function Agenda() {
  const eventos = [
    { id: 1, titulo: "Reunião equipe", inicio: "2025-09-12 10:00", status: "pendente" },
    { id: 2, titulo: "Entrega relatório", inicio: "2025-09-12 15:00", status: "concluído" },
    { id: 3, titulo: "Call cliente", inicio: "2025-09-13 09:00", status: "pendente" },
  ];

  return (
    <div className="agenda">
      <h1>Agenda</h1>
      <table>
        <thead>
          <tr>
            <th>Título</th>
            <th>Início</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {eventos.map((evento) => (
            <tr key={evento.id}>
              <td>{evento.titulo}</td>
              <td>{evento.inicio}</td>
              <td>{evento.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
