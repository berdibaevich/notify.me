const notification_count = document.getElementById("notification");
const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/notifications/`;
const socket = new WebSocket(wsEndpoint);

socket.addEventListener("message", (event) => {
    try {
        const messageData = JSON.parse(event.data);
        console.log(messageData)
        localStorage.setItem("notificationCount", messageData.count);

        if (messageData.count > 0){
            notification_count.textContent = messageData.count;
            notification_count.classList.remove("d-none");
        }else{
            notification_count.classList.add("d-none")
        }

    } catch (e) {
        console.error('Notification Error:', e);
    }
});