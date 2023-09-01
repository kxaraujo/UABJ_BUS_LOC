const assert = require('assert'); // Importa a biblioteca de assert
const { obterLocalizacao } = require('./script.js'); // Substitua 'seu-arquivo.js' pelo caminho correto para o arquivo onde a função obterLocalizacao está definida

describe('Função obterLocalizacao', function () {
    it('Deve retornar uma localização válida', function () {
        // Simule a função navigator.geolocation.getCurrentPosition
        global.navigator = {
            geolocation: {
                getCurrentPosition: (successCallback, errorCallback) => {
                    // Simule uma posição de exemplo
                    const position = {
                        coords: {
                            latitude: 40.7128, // Latitude de Nova Iorque
                            longitude: -74.0060, // Longitude de Nova Iorque
                        },
                    };
                    successCallback(position);
                },
            },
        };

        // Chame a função obterLocalizacao
        obterLocalizacao((latitude, longitude) => {
            // Verifique se a latitude e longitude são válidas
            assert.strictEqual(latitude, 40.7128);
            assert.strictEqual(longitude, -74.0060);
        });
    });
});
