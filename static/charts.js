async function fetchTraffic() {
    const res = await fetch('/api/traffic');
    const data = await res.json();
    return data;
}

async function fetchAlerts() {
    const res = await fetch('/api/alerts');
    return await res.json();
}

async function drawChart() {
    const traffic = await fetchTraffic();
    const labels = traffic.map(t => t.timestamp);
    const bytes = traffic.map(t => t.bytes);

    new Chart(document.getElementById('trafficChart'), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Tráfego (bytes)',
                data: bytes
            }]
        }
    });
}

async function showAlerts() {
    const alerts = await fetchAlerts();
    const list = document.getElementById('alertList');
    alerts.forEach(alert => {
        const li = document.createElement('li');
        li.textContent = `${alert.timestamp} - ${alert.alert}`;
        list.appendChild(li);
    });
}

drawChart();
showAlerts();
