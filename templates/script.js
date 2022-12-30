$(document).ready(() => {


    const protocol = document.location.protocol.startsWith('https') ? 'wss://' : 'ws://';
    const webSocket = new WebSocket(protocol + location.host);

    webSocket.onmessage = function onMessage(message) { 

    
    }

    })