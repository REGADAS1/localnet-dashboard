
# 🔐 Dashboard de Segurança de Rede Local

Um dashboard web simples e poderoso para **monitorizar tráfego de rede em tempo real**, identificar **comportamentos suspeitos** e visualizar **estatísticas interativas** da rede local.

Desenvolvido com `Python`, `Flask`, `Scapy` e `Chart.js`, este projeto é ideal para **ambientes domésticos** ou **pequenas empresas** que queiram ter visibilidade sobre o que se passa na sua rede, sem necessidade de appliances caros ou infraestruturas complexas.

---

## 🎯 Funcionalidades

✅ **Monitorização de Tráfego**
- Captura pacotes de rede (origem, protocolo e tamanho)
- Guarda informações num banco de dados SQLite

✅ **Visualização Interativa**
- Interface web em tempo real com gráfico de tráfego (Chart.js)
- Histórico dos últimos 100 pacotes
- Lista de alertas gerados automaticamente

✅ **Alertas Automáticos**
- Detecta comportamentos suspeitos (ex: flood de pacotes)
- Gera alertas com timestamp para investigação rápida

✅ **Interface Simples**
- Dashboard web limpo acessível em `http://127.0.0.1:5000`
- Totalmente local (sem envio de dados para a internet)

---

## 🧠 Tecnologias Utilizadas

| Tecnologia     | Finalidade                       |
|----------------|----------------------------------|
| Python         | Lógica principal do sistema      |
| Flask          | Servidor web/API                 |
| Scapy          | Captura e inspeção de pacotes    |
| SQLite         | Armazenamento local              |
| Chart.js       | Gráficos dinâmicos na interface  |
| HTML/CSS/JS    | Interface web simples            |

---

## 🚀 Como Instalar

### 1. Clonar o Repositório

```bash
git clone https://github.com/teu-usuario/network-dashboard.git
cd network-dashboard
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/Mac
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Inicializar Base de Dados

```bash
python
>>> from database import init_db
>>> init_db()
>>> exit()
```

### 5. Iniciar a Aplicação

```bash
python app.py
```

Acede a [http://127.0.0.1:5000](http://127.0.0.1:5000) no browser.

---

## 📸 Capturas de Ecrã

![Dashboard de Tráfego](screenshot_dashboard.png)
> Gráfico interativo e lista de alertas recentes

---

## 📁 Estrutura do Projeto

```
network_dashboard/
├── app.py                 # App Flask
├── database.py            # DB SQLite + funções
├── monitor.py             # Captura de pacotes com Scapy
├── alerts.py              # Lógica de deteção de anomalias
├── templates/
│   └── dashboard.html     # Interface web
├── static/
│   └── charts.js          # Gráfico Chart.js
├── requirements.txt       # Dependências
└── README.md              # Este ficheiro
```

---

## ⚠️ Notas Importantes

- Requer privilégios de administrador para capturar pacotes (no Windows)
- Recomendado instalar o [Npcap](https://nmap.org/npcap/) (modo WinPcap compatible)
- Esta é uma versão de desenvolvimento. Não usar diretamente em produção

---

## 🔮 Roadmap (Futuro)

- [ ] Exportar tráfego para CSV
- [ ] Dashboard com filtros por IP/protocolo
- [ ] Alertas via email ou Telegram
- [ ] Autenticação (login/senha)
- [ ] Empacotar como aplicação desktop (Electron)

---

## 🤝 Contribuição

Pull requests e sugestões são bem-vindos!

---

## 📄 Licença

Distribuído sob a licença MIT. Ver `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Gonçalo Regadas**  
Projeto pessoal de segurança e monitorização de redes locais.
