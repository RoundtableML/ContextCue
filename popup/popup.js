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
    // TO GET ONLY ARTICLE TEXT FROM PAGE (NOT WORKING)
    // const documentClone = document.cloneNode(true);
    // const article = Readability(documentClone).parse();
    // const text = article.textContent;

    const text = document.body.innerText;
    var doc = nlp(text);
    var nouns = doc.match('#Noun').not('#Pronoun').out('array');
    chrome.runtime.sendMessage({
        action: "displayText",
        nouns
    });
}

chrome.runtime.onMessage.addListener((message) => {
    if (message.action === "displayText") {
        const outputDiv = document.getElementById("output");
        outputDiv.textContent = message.nouns.join(", ");
    }
});