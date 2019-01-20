document.addEventListener('DOMContentLoaded', ()=>{
  const form = document.querySelector('form');

  form.addEventListener('submit', (evt) => {
    evt.preventDefault();
    const data = new FormData(evt.target);
    const result = fetch(form.action, { method: form.method, body: data });
    result.then((res) => res.json()).then((json) => {
      document.querySelector('.message').textContent = json.message;
      document.querySelector('.solutions').textContent = json.solutions;
    });
  });
});

