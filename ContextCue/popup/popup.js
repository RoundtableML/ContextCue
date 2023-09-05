document.getElementById("extractButton").addEventListener("click", () => {
    chrome.tabs.query({
        active: true,
        currentWindow: true
    }, (tabs) => {
        const activeTab = tabs[0];

        chrome.scripting.executeScript({
            target: {
                tabId: activeTab.id
            },
            function: extractText
        });
    });
});

function extractText() {
    const text = document.body.innerText;

    chrome.runtime.sendMessage({
        action: "displayText",
        text: text
    });
}

chrome.runtime.onMessage.addListener((message) => {
    if (message.action === "displayText") {
        const outputDiv = document.getElementById("output");
        outputDiv.textContent = message.text;
    }
});