
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
        return data
    } catch(e) {
        console.log(`Błąd pobierania danych: ${e}`)
    }

}

const bytesToGB = bytes => (bytes / (1024 ** 3)).toFixed(2);

const updateUI = (data) => {
    cpuTemp.textContent = data?.cpu?.cpu_temp ?? '—';
    diskUsage.textContent = data?.disk_usage.percent ?? '—';
    memoryUsage.textContent = data?.memory_usage?.percent ?? '—';
    cpu.textContent = data?.cpu?.cpu_info?.brand ?? '—';
    system.textContent = `${data?.system_info?.system}, ${data?.system_info?.release}, ${data?.system_info?.distro}` ?? '—'; 
    totalMemory.textContent = bytesToGB(data?.memory_usage?.total) ?? '—';
    totalDisk.textContent = bytesToGB(data?.disk_usage?.total) ?? '—';
}

const refreshMetrics = async () => {
    const data = await getServerMetrics();
    if (data) updateUI(data);
};

refreshMetrics();
setInterval(refreshMetrics, 5000);