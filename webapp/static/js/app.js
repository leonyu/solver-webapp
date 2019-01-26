document.addEventListener('DOMContentLoaded', () => {
  const $form = document.querySelector('form');
  const $textarea = document.querySelector('textarea');
  const $submitButton = document.querySelector('input[type="submit"]');

  updateViewState($form, $textarea, $submitButton);

  $textarea.addEventListener('input', (evt) => {
    updateViewState($form, $textarea, $submitButton);
  })

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

function updateViewState($form, $textarea, $submitButton) {
  const textContent = $textarea.value ? $textarea.value.trim() : '';
  if (/^\S.*=.*\S$/.test(textContent)) {
    $form.classList.remove('is-number');
    $form.classList.add('is-formula')
    $form.action = '/api/solve';
    $submitButton.disabled = false;
  } else if (/^\d+$/.test(textContent)) {
    $form.classList.remove('is-formula');
    $form.classList.add('is-number')
    $form.action = '/api/is_prime';
    $submitButton.disabled = false;
  } else {
    $form.classList.remove('is-formula', 'is-number');
    $form.action = '';
    $submitButton.disabled = true;
  }
}

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
