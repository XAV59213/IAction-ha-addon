document.addEventListener("DOMContentLoaded", function () {
    const adminDiv = document.createElement("div");
    adminDiv.innerHTML = `
        <h1>Administration IAction</h1>
        <p>Gérez les paramètres et visualisez les analyses de la caméra.</p>
        <ul>
            <li><a href="/video">Voir le flux caméra</a></li>
            <li><a href="/api/admin/config">Voir la configuration</a></li>
            <li><a href="#" onclick="fetch('/api/admin/reload', {method: 'POST'}).then(() => alert('Configuration rechargée'));">Recharger la configuration</a></li>
            <li><a href="#" onclick="fetch('/api/admin/restart', {method: 'POST'}).then(() => alert('Redémarrage en cours'));">Redémarrer</a></li>
            <li><a href="/api/admin/mqtt_test">Tester MQTT</a></li>
            <li><a href="#" onclick="fetch('/api/admin/rtsp_test', {method: 'POST'}).then(() => alert('Test RTSP effectué'));">Tester RTSP</a></li>
            <li><a href="/api/admin/ai_test">Tester AI</a></li>
        </ul>
    `;
    document.body.appendChild(adminDiv);

    console.log("Admin JS loaded");
});
