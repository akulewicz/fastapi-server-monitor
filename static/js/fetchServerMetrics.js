
const url = 'http://127.0.0.1:8000/status'
const cpuTemp = document.querySelector('.cpu_temp');
const diskUsage = document.querySelector('.disk_usage');
const memoryUsage = document.querySelector('.memory_usage');
const system = document.querySelector('.system');
const cpu = document.querySelector('.cpu');
const totalMemory = document.querySelector('.memory_total');
const totalDisk = document.querySelector('.disk_total')

const getServerMetrics = async () => {
    try {
        const response = await fetch(url)
        if (! response.ok ) throw response.status
        const data = await response.json()
          console.log(data)
        return data
    } catch(e) {
        console.log(`Błąd pobierania danych: ${e}`)
    }

}

const bytesToGB = bytes => (bytes / (1024 ** 3)).toFixed(2);

const updateUI = (data) => {
    cpuTemp.textContent = data?.cpu?.temp ?? '—';
    diskUsage.textContent = data?.disk?.percent ?? '—';
    memoryUsage.textContent = data?.memory?.percent ?? '—';
    cpu.textContent = data?.cpu?.brand ?? '—';
    system.textContent = `${data?.system?.system}, ${data?.system?.release}, ${data?.system?.distro}` ?? '—'; 
    totalMemory.textContent = bytesToGB(data?.memory?.total) ?? '—';
    totalDisk.textContent = bytesToGB(data?.disk?.total) ?? '—';
}

const refreshMetrics = async () => {
    const data = await getServerMetrics();
    if (data) updateUI(data);
};

refreshMetrics();
setInterval(refreshMetrics, 5000);