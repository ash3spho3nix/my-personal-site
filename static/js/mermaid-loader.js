import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.js';

mermaid.initialize({ 
  startOnLoad: false, 
  theme: 'neutral'
});

document.addEventListener("DOMContentLoaded", function() {
  const blocks = document.querySelectorAll("pre code.language-mermaid");
  blocks.forEach((block, index) => {
    const rawText = block.innerText;
    const container = document.createElement('div');
    container.className = 'mermaid';
    container.innerText = rawText;

    const preElement = block.parentElement;
    preElement.parentNode.replaceChild(container, preElement);
  });
  mermaid.run();
});