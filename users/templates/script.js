// JS que o Caio me passou
// Exibir campo de locação se "BRB" for selecionado
document.getElementById('exampleInputLocal1').addEventListener('change', function () {
    const locacaoDiv = document.getElementById('locacaoDiv');
    if (this.value === 'brb') {
      locacaoDiv.classList.remove('d-none');
    } else {
      locacaoDiv.classList.add('d-none');
    }
  });
  
  // Máscara para telefone: (00) 000000000
  const telInput = document.getElementById('exampleInputTel1');
  telInput.addEventListener('input', function (e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length > 11) value = value.slice(0, 11);
    const match = value.match(/^(\d{0,2})(\d{0,9})$/);
    if (match) {
      const [, ddd, number] = match;
      let formatted = '';
      if (ddd) formatted += `(${ddd}`;
      if (ddd.length === 2) formatted += `) `;
      if (number) formatted += number;
      e.target.value = formatted;
    }
  });
  
  // Máscara para CPF: 000.000.000-00
  const cpfInput = document.getElementById('exampleInputCPF1');
  cpfInput.addEventListener('input', function (e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length > 11) value = value.slice(0, 11);
    const match = value.match(/^(\d{0,3})(\d{0,3})(\d{0,3})(\d{0,2})$/);
    if (match) {
      const [, part1, part2, part3, part4] = match;
      let formatted = '';
      if (part1) formatted += part1;
      if (part2) formatted += '.' + part2;
      if (part3) formatted += '.' + part3;
      if (part4) formatted += '-' + part4;
      e.target.value = formatted;
    }
  });
  