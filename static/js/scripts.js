
// CHAT ROOM SENDING AND GETTING MESSAGES BY WEB SOCKET

const protocol = "ws"
const pathUrl = "/ws/chatroom/" + (chatroomId?chatroomId:"")

const ws = configWebSocket(protocol, pathUrl)

$(document).ready(initParams)

function initParams() {
    jQuery(addSendBtnEventListener)
    jQuery(addHandleMessagesFromWS)
    scrollToTheBottom()
}

function handleMessagesFromWS(ev) {
    const data = JSON.parse(ev.data)

    avatar_img = '<div class="rounded-circle d-flex align-self-start me-3 shadow-1-strong" width="60"></div>'
    if (data.avatar_img) {
        avatar_img = '<img src=' + data.avatar_img + '/ alt="avatar" class="rounded-circle d-flex align-self-start me-3 shadow-1-strong" width="60">'
    }

    const msgElement =
        '<li class="d-flex justify-content-between mb-4">' +
        avatar_img +
        '<div class="card">' +
        '<div class="card-header d-flex justify-content-between p-3">' +
        '<p class="fw-bold mb-0 me-3">' + data.username + '</p>' +
        '<p class="text-muted small mb-0"><i class="far fa-clock"></i>' + data.created_date + '</p>' +
        '</div> <div class="card-body"> <p class="mb-0">' + data.message + '</p> </div> </div> </li>'

    $("#message-box").append(msgElement)

    scrollToTheBottom()
}

function sendMessage(ev) {
    ev.preventDefault()
    $textArea = $("#textArea")
    const message = $textArea.val()

    ws.send(JSON.stringify({
            "message": message,
            "username": user
        })
    )
    $textArea.val("")

}

function addSendBtnEventListener(ev) {
    const $sendButton = $("#send-button")
    $sendButton.on("click", sendMessage)
}

function addHandleMessagesFromWS(ev) {
    ws.onmessage = handleMessagesFromWS
}

function configWebSocket(protocol, pathUrl) {
    const url = getUrl(protocol, pathUrl)
    const ws = new WebSocket(url)
    return ws
}

function getUrl(protocol, pathUrl) {
    const url = protocol + "://" +
        window.location.host +
        pathUrl

    return url
}

function scrollToTheBottom() {
    window.scrollTo(0, document.body.scrollHeight);
}