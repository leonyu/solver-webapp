document.addEventListener('DOMContentLoaded', () => {
  const $form = document.querySelector('form');

  $form.addEventListener('submit', (evt) => {
    evt.preventDefault();
    const data = new FormData(evt.target);
    const result = fetch($form.action, { method: $form.method, body: data });
    result.then((res) => res.json()).then((json) => {
      renderSolution(json.solutions);
    }).catch((error) => {
      renderError(error)
    });
  });
});

function renderSolution(solutions) {
  const $errorMessage = document.querySelector('.error-message');
  const $solution = document.querySelector('.solution');

  let message = '';
  if (solutions.length == 0) {
    message = 'No solutions';
  } else if (solutions.length > 1) {
    message = 'There are multiple solutions';
  }
  $errorMessage.textContent = message;
  $solution.innerHTML = '';
  for (const solution of solutions) {
    const li = document.createElement('li');
    li.textContent = solution;
    $solution.append(li);
  }
}

function renderError(error) {
  const $errorMessage = document.querySelector('.error-message');
  const $solution = document.querySelector('.solution');

  $errorMessage.textContent = `${error}`;
  $solution.innerHTML = '';
}
