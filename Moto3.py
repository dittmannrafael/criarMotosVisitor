# Componentes da moto
class MotoComponent:
    def accept(self, visitor):
        pass


class Motor(MotoComponent):
    def accept(self, visitor):
        visitor.visit_motor(self)

    def __str__(self):
        return "Motor"


class Rodas(MotoComponent):
    def accept(self, visitor):
        visitor.visit_rodas(self)

    def __str__(self):
        return "Tipo de rodas"


class Tanque(MotoComponent):
    def accept(self, visitor):
        visitor.visit_tanque(self)

    def __str__(self):
        return "Tanque"


class Quadro(MotoComponent):
    def accept(self, visitor):
        visitor.visit_quadro(self)

    def __str__(self):
        return "Quadro"


class ParaLamas(MotoComponent):
    def accept(self, visitor):
        visitor.visit_para_lamas(self)

    def __str__(self):
        return "Para-lamas"


class Guidao(MotoComponent):
    def accept(self, visitor):
        visitor.visit_guidao(self)

    def __str__(self):
        return "Guidão"


class Freios(MotoComponent):
    def accept(self, visitor):
        visitor.visit_freios(self)

    def __str__(self):
        return "Tipo de freios"


# Visitor 
class MotoVisitor:
    def visit_motor(self, motor):
        pass

    def visit_rodas(self, rodas):
        pass

    def visit_tanque(self, tanque):
        pass

    def visit_quadro(self, quadro):
        pass

    def visit_para_lamas(self, para_lamas):
        pass

    def visit_guidao(self, guidao):
        pass

    def visit_freios(self, freios):
        pass


# Implementação
class ImprimirVisitor(MotoVisitor):
    def visit_motor(self, motor):
        print("Motor:", motor)

    def visit_rodas(self, rodas):
        print("Tipo de rodas:", rodas)

    def visit_tanque(self, tanque):
        print("Tanque:", tanque)

    def visit_quadro(self, quadro):
        print("Quadro:", quadro)

    def visit_para_lamas(self, para_lamas):
        print("Para-lamas:", para_lamas)

    def visit_guidao(self, guidao):
        print("Guidão:", guidao)

    def visit_freios(self, freios):
        print("Tipo de freios:", freios)


# Cliente
class Moto:
    def __init__(self, freios, rodas):
        self.componentes = [
            Motor(),
            Rodas(),
            Tanque(),
            Quadro(),
            ParaLamas(),
            Guidao(),
            Freios()
        ]
        self.tipo_freios = freios
        self.tipo_rodas = rodas

    def accept(self, visitor):
        for componente in self.componentes:
            componente.accept(visitor)

    def __str__(self):
        return f"Moto: tipo_freios={self.tipo_freios}, tipo_rodas={self.tipo_rodas}"

moto = Moto("Freios a disco", "Rodas de liga leve")

imprimir_visitor = ImprimirVisitor()
moto.accept(imprimir_visitor)
