import { bytesToGB } from "./utils.js";

class Dashboard {
    constructor(url) {

        this.url = url;
        this.elements = {
            cpuTemp: document.querySelector('.cpu_temp'),
            diskUsage: document.querySelector('.disk_usage'),
            memoryUsage: document.querySelector('.memory_usage'),
            system: document.querySelector('.system'),
            cpu: document.querySelector('.cpu'),
            totalMemory: document.querySelector('.memory_total'),
            totalDisk: document.querySelector('.disk_total'),
            envTemp: document.querySelector('.env_temp'),
            envHumidity: document.querySelector('.env_humidity'),
            envPressure: document.querySelector('.env_pressure'),
            hostname: document.querySelector('.hostname'),
            ip: document.querySelector('.ip'),
            users: document.querySelector('.users')
        }
    }

    updateSystemData(data) {
        this.elements.cpuTemp.textContent = data?.cpu?.temp ?? '—';
        this.elements.diskUsage.textContent = data?.disk?.percent ?? '—';
        this.elements.memoryUsage.textContent = data?.memory?.percent ?? '—';
        this.elements.cpu.textContent = data?.cpu?.brand ?? '—';
        this.elements.system.textContent = `${data?.system?.system}, ${data?.system?.release}, ${data?.system?.distro}` ?? '—'; 
        this.elements.totalMemory.textContent = bytesToGB(data?.memory?.total) ?? '—';
        this.elements.totalDisk.textContent = bytesToGB(data?.disk?.total) ?? '—';
        this.elements.users.textContent = data?.users?.connected_users.map( user => {
            return `${user.name} ${user.host}`
        }).join(', ') || '—';
    }

    updateEnvData(data) {
        this.elements.envTemp.textContent = data?.env?.temperature ?? '—';
        this.elements.envHumidity.textContent = data?.env?.humidity ?? '—';
        this.elements.envPressure.textContent = data?.env?.pressure ?? '—';
    }

    updateNetworkData(data) {
        this.elements.hostname.textContent = data?.network?.hostname ?? '—';
        this.elements.ip.textContent = data?.network?.ip ?? '—';
    }

    updateUI(data) {
        if (!data) return;
        this.updateSystemData(data);
        this.updateEnvData(data);
        this.updateNetworkData(data);
    }
 
    async fetchMetrics() {
        try {
            const response = await fetch(this.url);
            if (! response.ok ) throw response.status;
            return await response.json();
        } catch(e) {
            console.error(`Błąd pobierania danych: ${e}`);
            return null;
        }
    }

    async refresh() {
        const data = await this.fetchMetrics();
        this.updateUI(data);
    }

    start(interval = 5000) {
        this.refresh();
        setInterval(() => this.refresh(), interval);
    }
}

const dashboard = new Dashboard('/api/status');
dashboard.start();