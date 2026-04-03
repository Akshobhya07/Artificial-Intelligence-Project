document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('textInput');
    const generateBtn = document.getElementById('generateBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const outputCode = document.getElementById('outputCode');
    const elementCountBadge = document.getElementById('elementCount');
    const copyBtn = document.getElementById('copyBtn');

    generateBtn.addEventListener('click', async () => {
        const inputText = textInput.value;
        if (!inputText.trim()) {
            outputCode.innerHTML = '<span style="color: #ef4444;">Please provide requirement statements first.</span>';
            return;
        }

        // Setup loading state
        generateBtn.disabled = true;
        generateBtn.style.opacity = '0.5';
        loadingIndicator.classList.remove('hidden');
        outputCode.textContent = 'Evaluating constraints and generating scenarios...';

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: inputText })
            });

            const data = await response.json();

            if (data.success) {
                // Update UI: Show markdown followed by Python stubs
                outputCode.textContent = data.markdown + "\n\n" + data.python;
                elementCountBadge.textContent = `Completed`;
                elementCountBadge.style.color = '#fff';
                elementCountBadge.style.background = 'rgba(16, 185, 129, 0.4)';
                elementCountBadge.style.boxShadow = '0 0 10px rgba(16, 185, 129, 0.4)';
            } else {
                outputCode.textContent = `Error: ${data.error}`;
                elementCountBadge.textContent = 'Error';
                elementCountBadge.style.background = 'rgba(239, 68, 68, 0.4)';
            }
        } catch (error) {
            outputCode.textContent = `Network Error: ${error.message}`;
            elementCountBadge.textContent = 'Failed';
            elementCountBadge.style.background = 'rgba(239, 68, 68, 0.4)';
        } finally {
            // Revert loading state
            loadingIndicator.classList.add('hidden');
            generateBtn.disabled = false;
            generateBtn.style.opacity = '1';
        }
    });

    copyBtn.addEventListener('click', () => {
        const text = outputCode.textContent;
        navigator.clipboard.writeText(text).then(() => {
            const originalText = copyBtn.innerHTML;
            copyBtn.innerHTML = '✅ Copied!';
            setTimeout(() => {
                copyBtn.innerHTML = originalText;
            }, 2000);
        });
    });

    if (!textInput.value) {
        textInput.value = "User needs to be able to login with email and password.";
    }
});
