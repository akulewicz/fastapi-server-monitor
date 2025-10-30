
const url = 'http://192.168.1.6:8000/api/status'
const cpuTemp = document.querySelector('.cpu_temp');
const diskUsage = document.querySelector('.disk_usage');
const memoryUsage = document.querySelector('.memory_usage');
const system = document.querySelector('.system');
const cpu = document.querySelector('.cpu');
const totalMemory = document.querySelector('.memory_total');
const totalDisk = document.querySelector('.disk_total')
const envTemp = document.querySelector('.env_temp');
const envHumidity = document.querySelector('.env_humidity');
const envPressure = document.querySelector('.env_pressure');
const hostname = document.querySelector('.hostname');
const ip = document.querySelector('.ip')

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
    envTemp.textContent = data?.env?.temperature ?? '—';
    envHumidity.textContent = data?.env?.humidity ?? '—';
    envPressure.textContent = data?.env?.pressure ?? '—';
    hostname.textContent = data?.network?.hostname ?? '—';
    ip.textContent = data?.network?.ip ?? '—';

}

const refreshMetrics = async () => {
    const data = await getServerMetrics();
    if (data) updateUI(data);
};

refreshMetrics();
setInterval(refreshMetrics, 5000);