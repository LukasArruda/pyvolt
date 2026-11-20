import numpy as np


class Componente:
    """Classe base para componentes de um circuito elétrico CC."""

    def __init__(self, nome: str, valor: float):
        self.nome = nome        # Ex.: "R1", "C1", "V1"
        self.valor = valor      # Resistência (Ω), Capacitância (F) ou Tensão (V)

    def obter_item(self) -> str:
        """Retorna uma string com o nome e o valor do componente."""
        return f"{self.nome}: {self.valor}"


class Fonte(Componente):
    """Representa uma fonte de tensão contínua (V)."""

    def __init__(self, nome: str, voltagem: float):
        super().__init__(nome, voltagem)


class Resistor(Componente):
    """Representa um resistor ôhmico (Ω)."""

    def __init__(self, nome: str, resistencia: float):
        super().__init__(nome, resistencia)

    def calcular_potencia(self, corrente: float) -> float:
        """Calcula a potência dissipada no resistor: P = R * I²."""
        return self.valor * (corrente ** 2)


class Capacitor(Componente):
    """Representa um capacitor em circuito RC (F)."""

    def __init__(self, nome: str, capacitancia: float):
        super().__init__(nome, capacitancia)

    def calcular_constante_tempo(self, req: float) -> float:
        """Calcula a constante de tempo tau: τ = Req * C."""
        return req * self.valor

    def tensao_carga(self, t, v_fonte: float, req: float):
        """Calcula a tensão de carga do capacitor no instante t: V(t) = V_fonte * (1 - e^(-t/tau))."""
        tau = self.calcular_constante_tempo(req)
        t_arr = np.asarray(t, dtype=float)

        if tau == 0:
            return np.full_like(t_arr, float(v_fonte), dtype=float)

        return v_fonte * (1.0 - np.exp(-t_arr / tau))