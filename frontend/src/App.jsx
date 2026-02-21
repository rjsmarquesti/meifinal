import React, { useState } from 'react';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-blue-600 p-4 text-white shadow-lg">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">MEI Fiscal</h1>
          <div className="space-x-4">
            <button className="hover:underline">Dashboard</button>
            <button className="hover:underline">Clientes</button>
            <button className="hover:underline">Notas Fiscais</button>
          </div>
        </div>
      </nav>

      <main className="container mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
        <h2 className="text-3xl font-semibold text-gray-800 mb-6">Bem-vindo ao seu Gestor MEI</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-6 bg-green-100 border-l-4 border-green-500 rounded">
            <h3 className="font-bold text-green-700">Faturamento Mensal</h3>
            <p className="text-2xl">R$ 0,00</p>
          </div>
          <div className="p-6 bg-blue-100 border-l-4 border-blue-500 rounded">
            <h3 className="font-bold text-blue-700">Notas Emitidas</h3>
            <p className="text-2xl">0</p>
          </div>
          <div className="p-6 bg-yellow-100 border-l-4 border-yellow-500 rounded">
            <h3 className="font-bold text-yellow-700">Limite MEI</h3>
            <p className="text-2xl">R$ 81.000,00</p>
          </div>
        </div>
        
        <div className="mt-10">
          <button className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition">
            + Nova Nota Fiscal
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
