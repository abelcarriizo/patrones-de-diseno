# Patrones de Diseño

> Antes de estudiar los patrones, puedes refrescar tu memoria repasando los términos clave de la programación orientada a objetos.

## Programación Orientada a Objetos

**Clase**: Es un plano que define la estructura de objetos, que son instancias de la clase.

**Atributos**: Características del objeto.

**Métodos**: Comportamiento del objeto.

## Pilares de la Programación Orientada a Objetos

**Abstracción**: Es la capacidad de representar a los objetos del mundo real en un contexto especifico.

**Encapsulacion**: Capacidad de un objeto de esconder sus atributos y métodos.
- **Privados**: Atributos o metodos que  solo pueden ser accedidos dentro de la misma clase.
- **Protegidos**: Es un poco menos restrictivo porque los atributos o metodos ser accedidos por las subclases de una clase.

**Herencia**: Capacidad de crear clases a partir de una existente. Tiene la ventaja de permitir la reutilización del código.

**Polimorfismo**: Capacidad de múltiples clases de objetos distintos de responder de formas distintas a un mismo método.

## ¿Qué son los patrones de diseño?

Los patrones de diseño son soluciones reutilizables a problemas comunes en el diseño de software. Son como una receta, un plan de acción, una descripción de un problema junto con una forma de solucionarlo.

## Clasificación de patrones

1. **Patrones creacionales (Cómo crear cosas)**: 
    - **Formal**: Abordan la creación de objetos, evitando la necesidad de instanciar objetos directamente.
    - **Informal**: Estos patrones son como los métodos que usan los trabajadores para crear las diferentes partes de la casa. Por ejemplo, si necesitas muchas ventanas idénticas, usarías una técnica que permita fabricarlas rápidamente y de manera eficiente.

2. **Patrones estructurales (Cómo construir cosas grandes con piezas pequeñas)**: 
    - **Formal**: Estos patrones te ayudan a ensamblar objetos y clases para formar estructuras más grandes y fáciles de entender.
    - **Informal**: Estos patrones se ocupan de cómo organizar las diferentes partes de la casa para que funcionen bien juntas. Es como decidir cómo conectar las habitaciones, puertas y ventanas para que la casa sea cómoda y eficiente.

3. **Patrones de comportamiento (Cómo hacer que las cosas trabajen juntas)**: 
    - **Formal**: Estos patrones se centran en la comunicación y la interacción entre objetos. Proveen soluciones para delegar responsabilidades entre los objetos y describen patrones de comunicación.
    - **Informal**: Estos patrones son como las reglas y rutinas que seguimos dentro de la casa para mantener todo en orden. Por ejemplo, cómo usamos la calefacción, cómo se apagan las luces automáticamente cuando salimos, etc. 

## Principios de Diseño

### Encapsula lo que varia: 

Identifica los aspectos de tu aplicación que varían y sepáralos de los que se mantienen inalterables.
El objetivo principal de este principio es minimizar el efecto provocado por los cambios.
Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Encapsula%20lo%20que%20varia)

### Favorece la composicion sobre la herencia

- **Una subclase no puede reducir la interfaz de la superclase**: Tienes que implementar todos los métodos abstractos de la clase padre, incluso aunque no vayas a usarlos.

- **Al sobrescribir métodos debes asegurarte de que el nuevo comportamiento sea compatible con el de base**.

- **La herencia rompe la encapsulación de la superclase**: porque los detalles internos de la clase padre se hacen disponibles
para la subclase.

- **Las subclases estan fuertemente acopladas a superclases**.

Existe una alternativa a la herencia llamada composición. Mientras que la herencia representa la relación “is a” (es un/a) entre clases (un auto es un medio de transporte), la composición se basa en la relación “tiene un/a” (un auto tiene un motor).
Debo mencionar que este principio también se aplica a la agregación, una variante más relajada de la composición en la que un objeto puede contener una referencia al otro pero no gestiona su ciclo vital. Aquí tienes un ejemplo: un auto tiene un conductor pero éste puede utilizar otro auto o caminar sin el auto.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Favorece%20la%20composicion%20sobre%20la%20herencia)

### Programa una Interfaz no una implementacion
Fomenta el uso de abstracciones para reducir el acoplamiento entre los componentes de un sistema.
Este principio nos enseña a diseñar nuestros sistemas para que dependan de contratos generales (interfaz o clase abstracta) y no de detalles concretos (clases específicas). Esto hace que el código sea más flexible, reutilizable y fácil de mantener.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Programa%20a%20una%20interfaz%20no%20una%20implementacion)