import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";

// Páginas
import Home from "./pages/home";
import Agenda from "./pages/agenda";
import Financeiro from "./pages/financeiro";
import Vendas from "./pages/vendas";
import Configuracoes from "./pages/configuracoes";

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/agenda" element={<Agenda />} />
          <Route path="/financeiro" element={<Financeiro />} />
          <Route path="/vendas" element={<Vendas />} />
          <Route path="/configuracoes" element={<Configuracoes />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
