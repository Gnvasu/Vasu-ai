
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Open Source AI App</title>
    <style>
        body { font-family: Arial; background: #f4f4f4; padding: 20px; }
        input, button { padding: 10px; margin: 5px; }
        #result { background: white; padding: 15px; border-radius: 5px; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Ask Anything!</h1>
    <input type="text" id="question" placeholder="Ask your question here..." />
    <button onclick="askAI()">Search</button>

    <div id="result"></div>

    <script>
        function askAI() {
            const question = document.getElementById('question').value;
            fetch('http://127.0.0.1:5000/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: question })
            })
            .then(response => response.json())
            .then(data => {
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = `<h3>AI Answer:</h3><p>${data.ai_answer}</p>
                                       <h3>Web Results:</h3>
                                       <ul>${data.web_results.map(link => `<li><a href="${link}" target="_blank">${link}</a></li>`).join('')}</ul>`;
            });
        }
    </script>
</body>
</html>
