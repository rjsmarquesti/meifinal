const API_URL = 'https://desenvolvimento-backend.l8qthy.easypanel.host';

function App() {
  const [page, setPage] = useState('dashboard');
  const [clientes, setClientes] = useState([]);
  const [notas, setNotas] = useState([]);
  const [dashboard, setDashboard] = useState({ faturamento_mensal: 0, notas_emitidas: 0, limite_mei: 81000 });
  const [novoCliente, setNovoCliente] = useState({ nome: '', email: '', cpf_cnpj: '', telefone: '' });
  const [novaNota, setNovaNota] = useState({ cliente_id: '', descricao: '', valor: '' });
  const [msg, setMsg] = useState('');

  useEffect(() => {
    if (page === 'dashboard') fetchDashboard();
    if (page === 'clientes') fetchClientes();
    if (page === 'notas') fetchNotas();
  }, [page]);

  async function fetchDashboard() {
    try {
      const res = await fetch(`${API_URL}/dashboard/`);
      const data = await res.json();
      setDashboard(data);
    } catch (e) { setMsg('Erro ao carregar dashboard.'); }
  }

  async function fetchClientes() {
    try {
      const res = await fetch(`${API_URL}/clientes/`);
      const data = await res.json();
      setClientes(data);
    } catch (e) { setMsg('Erro ao carregar clientes.'); }
  }

  async function fetchNotas() {
    try {
      const res = await fetch(`${API_URL}/notas/`);
      const data = await res.json();
      setNotas(data);
    } catch (e) { setMsg('Erro ao carregar notas.'); }
  }

  async function criarCliente(e) {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}/clientes/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(novoCliente)
      });
      if (res.ok) {
        setMsg('Cliente cadastrado com sucesso!');
        setNovoCliente({ nome: '', email: '', cpf_cnpj: '', telefone: '' });
        fetchClientes();
      } else {
        setMsg('Erro ao cadastrar cliente.');
      }
    } catch (e) { setMsg('Erro de conexão com o servidor.'); }
  }

  async function emitirNota(e) {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}/notas/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...novaNota, valor: parseFloat(novaNota.valor), cliente_id: parseInt(novaNota.cliente_id) })
      });
      if (res.ok) {
        setMsg('Nota emitida com sucesso!');
        setNovaNota({ cliente_id: '', descricao: '', valor: '' });
        fetchNotas();
      } else {
        setMsg('Erro ao emitir nota.');
      }
    } catch (e) { setMsg('Erro de conexão com o servidor.'); }
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-blue-600 p-4 text-white shadow-lg">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">MEI Fiscal</h1>
          <div className="space-x-4">
            <button onClick={() => setPage('dashboard')} className={`hover:underline ${page==='dashboard'?'font-bold underline':''}`}>Dashboard</button>
            <button onClick={() => setPage('clientes')} className={`hover:underline ${page==='clientes'?'font-bold underline':''}`}>Clientes</button>
            <button onClick={() => setPage('notas')} className={`hover:underline ${page==='notas'?'font-bold underline':''}`}>Notas Fiscais</button>
          </div>
        </div>
      </nav>

      <main className="container mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
        {msg && <div className="mb-4 p-3 bg-blue-100 text-blue-800 rounded">{msg} <button onClick={()=>setMsg('')} className="ml-2 text-blue-500">✕</button></div>}

        {page === 'dashboard' && (
          <div>
            <h2 className="text-3xl font-semibold text-gray-800 mb-6">Bem-vindo ao seu Gestor MEI</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="p-6 bg-green-100 border-l-4 border-green-500 rounded">
                <h3 className="font-bold text-green-700">Faturamento Mensal</h3>
                <p className="text-2xl">R$ {Number(dashboard.faturamento_mensal || 0).toFixed(2)}</p>
              </div>
              <div className="p-6 bg-blue-100 border-l-4 border-blue-500 rounded">
                <h3 className="font-bold text-blue-700">Notas Emitidas</h3>
                <p className="text-2xl">{dashboard.notas_emitidas || 0}</p>
              </div>
              <div className="p-6 bg-yellow-100 border-l-4 border-yellow-500 rounded">
                <h3 className="font-bold text-yellow-700">Limite MEI</h3>
                <p className="text-2xl">R$ 81.000,00</p>
              </div>
            </div>
            <div className="mt-10 space-x-4">
              <button onClick={() => setPage('clientes')} className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition">+ Novo Cliente</button>
              <button onClick={() => setPage('notas')} className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition">+ Nova Nota Fiscal</button>
            </div>
          </div>
        )}

        {page === 'clientes' && (
          <div>
            <h2 className="text-2xl font-semibold mb-6">Clientes</h2>
            <form onSubmit={criarCliente} className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8 p-4 bg-gray-50 rounded">
              <input required placeholder="Nome" value={novoCliente.nome} onChange={e=>setNovoCliente({...novoCliente, nome: e.target.value})} className="border p-2 rounded" />
              <input required placeholder="Email" value={novoCliente.email} onChange={e=>setNovoCliente({...novoCliente, email: e.target.value})} className="border p-2 rounded" />
              <input required placeholder="CPF/CNPJ" value={novoCliente.cpf_cnpj} onChange={e=>setNovoCliente({...novoCliente, cpf_cnpj: e.target.value})} className="border p-2 rounded" />
              <input placeholder="Telefone" value={novoCliente.telefone} onChange={e=>setNovoCliente({...novoCliente, telefone: e.target.value})} className="border p-2 rounded" />
              <button type="submit" className="md:col-span-2 bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Cadastrar Cliente</button>
            </form>
            <table className="w-full border-collapse">
              <thead><tr className="bg-gray-200"><th className="p-2 text-left">Nome</th><th className="p-2 text-left">Email</th><th className="p-2 text-left">CPF/CNPJ</th><th className="p-2 text-left">Telefone</th></tr></thead>
              <tbody>
                {clientes.length === 0 && <tr><td colSpan="4" className="p-4 text-center text-gray-500">Nenhum cliente cadastrado.</td></tr>}
                {clientes.map(c => <tr key={c.id} className="border-b"><td className="p-2">{c.nome}</td><td className="p-2">{c.email}</td><td className="p-2">{c.cpf_cnpj}</td><td className="p-2">{c.telefone}</td></tr>)}
              </tbody>
            </table>
          </div>
        )}

        {page === 'notas' && (
          <div>
            <h2 className="text-2xl font-semibold mb-6">Notas Fiscais</h2>
            <form onSubmit={emitirNota} className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8 p-4 bg-gray-50 rounded">
              <input required placeholder="ID do Cliente" value={novaNota.cliente_id} onChange={e=>setNovaNota({...novaNota, cliente_id: e.target.value})} className="border p-2 rounded" />
              <input required placeholder="Descrição do Serviço" value={novaNota.descricao} onChange={e=>setNovaNota({...novaNota, descricao: e.target.value})} className="border p-2 rounded" />
              <input required placeholder="Valor (ex: 150.00)" value={novaNota.valor} onChange={e=>setNovaNota({...novaNota, valor: e.target.value})} className="border p-2 rounded" />
              <button type="submit" className="md:col-span-3 bg-green-600 text-white py-2 rounded hover:bg-green-700">Emitir Nota</button>
            </form>
            <table className="w-full border-collapse">
              <thead><tr className="bg-gray-200"><th className="p-2 text-left">ID</th><th className="p-2 text-left">Cliente</th><th className="p-2 text-left">Descrição</th><th className="p-2 text-left">Valor</th><th className="p-2 text-left">Data</th></tr></thead>
              <tbody>
                {notas.length === 0 && <tr><td colSpan="5" className="p-4 text-center text-gray-500">Nenhuma nota emitida.</td></tr>}
                {notas.map(n => <tr key={n.id} className="border-b"><td className="p-2">{n.id}</td><td className="p-2">{n.cliente_id}</td><td className="p-2">{n.descricao}</td><td className="p-2">R$ {Number(n.valor).toFixed(2)}</td><td className="p-2">{n.data_emissao}</td></tr>)}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </div>
  );
}

App;
