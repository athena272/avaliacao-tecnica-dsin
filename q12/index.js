var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// Implementações do comportamento de voo
var VoarComAsas = /** @class */ (function () {
    function VoarComAsas() {
    }
    VoarComAsas.prototype.voar = function () {
        console.log("Estou voando com asas!");
    };
    return VoarComAsas;
}());
var NaoVoar = /** @class */ (function () {
    function NaoVoar() {
    }
    NaoVoar.prototype.voar = function () {
        console.log("Não posso voar.");
    };
    return NaoVoar;
}());
// Classe abstrata Pato
var Pato = /** @class */ (function () {
    function Pato(comportamentoVoo) {
        this.comportamentoVoo = comportamentoVoo;
    }
    Pato.prototype.performarVoo = function () {
        this.comportamentoVoo.voar();
    };
    Pato.prototype.setComportamentoVoo = function (comportamentoVoo) {
        this.comportamentoVoo = comportamentoVoo;
    };
    Pato.prototype.quack = function () {
        console.log("Quack!");
    };
    Pato.prototype.nadar = function () {
        console.log("Estou nadando.");
    };
    return Pato;
}());
// Classes concretas de tipos de pato
var PatoSelvagem = /** @class */ (function (_super) {
    __extends(PatoSelvagem, _super);
    function PatoSelvagem() {
        return _super.call(this, new VoarComAsas()) || this;
    }
    PatoSelvagem.prototype.exibir = function () {
        console.log("Eu sou um pato selvagem.");
    };
    return PatoSelvagem;
}(Pato));
var PatoBorracha = /** @class */ (function (_super) {
    __extends(PatoBorracha, _super);
    function PatoBorracha() {
        return _super.call(this, new NaoVoar()) || this;
    }
    PatoBorracha.prototype.exibir = function () {
        console.log("Eu sou um pato de borracha.");
    };
    PatoBorracha.prototype.quack = function () {
        console.log("Squeak!");
    };
    return PatoBorracha;
}(Pato));
// Usando as classes
var patoSelvagem = new PatoSelvagem();
patoSelvagem.exibir();
patoSelvagem.quack();
patoSelvagem.nadar();
patoSelvagem.performarVoo();
console.log('---');
var patoBorracha = new PatoBorracha();
patoBorracha.exibir();
patoBorracha.quack();
patoBorracha.nadar();
patoBorracha.performarVoo();
// Alterando o comportamento em tempo de execução
patoBorracha.setComportamentoVoo(new VoarComAsas());
patoBorracha.performarVoo();
