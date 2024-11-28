// Definindo a interface para o comportamento de voo
interface ComportamentoVoo {
    voar(): void;
  }
  
  // Implementações do comportamento de voo
  class VoarComAsas implements ComportamentoVoo {
    voar() {
      console.log("Estou voando com asas!");
    }
  }
  
  class NaoVoar implements ComportamentoVoo {
    voar() {
      console.log("Não posso voar.");
    }
  }
  
  // Classe abstrata Pato
  abstract class Pato {
    protected comportamentoVoo: ComportamentoVoo;
  
    constructor(comportamentoVoo: ComportamentoVoo) {
      this.comportamentoVoo = comportamentoVoo;
    }
  
    performarVoo() {
      this.comportamentoVoo.voar();
    }
  
    setComportamentoVoo(comportamentoVoo: ComportamentoVoo) {
      this.comportamentoVoo = comportamentoVoo;
    }
  
    quack() {
      console.log("Quack!");
    }
  
    nadar() {
      console.log("Estou nadando.");
    }
  
    abstract exibir(): void;
  }
  
  // Classes concretas de tipos de pato
  class PatoSelvagem extends Pato {
    constructor() {
      super(new VoarComAsas());
    }
  
    exibir() {
      console.log("Eu sou um pato selvagem.");
    }
  }
  
  class PatoBorracha extends Pato {
    constructor() {
      super(new NaoVoar());
    }
  
    exibir() {
      console.log("Eu sou um pato de borracha.");
    }
  
    quack() {
      console.log("Squeak!");
    }
  }
  
  // Uso das classes
  const patoSelvagem = new PatoSelvagem();
  patoSelvagem.exibir();
  patoSelvagem.quack();
  patoSelvagem.nadar();
  patoSelvagem.performarVoo();
  
  console.log('---');
  
  const patoBorracha = new PatoBorracha();
  patoBorracha.exibir();
  patoBorracha.quack();
  patoBorracha.nadar();
  patoBorracha.performarVoo();
  
  // Alterando o comportamento em tempo de execução
  patoBorracha.setComportamentoVoo(new VoarComAsas());
  patoBorracha.performarVoo();
  