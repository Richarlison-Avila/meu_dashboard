import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home.jsx";
import Agenda from "./pages/agenda.jsx";
import Financeiro from "./pages/financeiro.jsx";
import Vendas from "./pages/vendas.jsx";
import Configuracoes from "./pages/configuracoes.jsx";
import Login from "./pages/login.jsx";
import Register from "./pages/register.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
        <Route path="/agenda" element={<Agenda />} />
        <Route path="/financeiro" element={<Financeiro />} />
        <Route path="/vendas" element={<Vendas />} />
        <Route path="/configuracoes" element={<Configuracoes />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
