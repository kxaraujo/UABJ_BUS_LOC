describe('Teste da função obterDistancia', function() {
  it('Deve testar a função obterDistancia', function() {
    
    // Simular os valores de posição de geolocalização
    const position = {
      coords: {
        latitude: 37.7749,
        longitude: -122.4194,
      },
    };

    // Simular o objeto do navegador
    globalThis.navigator = {
      geolocation: {
        getCurrentPosition: (successCallback, errorCallback) => {
          successCallback(position);
        },
      },
    };

    // Simular o elemento HTML onde você deseja exibir as coordenadas
    const coordenadasElement = document.createElement('div');
    coordenadasElement.id = 'coordenadas';
    document.body.appendChild(coordenadasElement);

    // Chamar a função a ser testada
    obterDistancia();

    // Verificar se o elemento contém as coordenadas esperadas
    const resultado = document.getElementById('coordenadas').textContent;
    chai.expect(resultado).to.include('Latitude 37.7749, Longitude -122.4194');
  });
});
