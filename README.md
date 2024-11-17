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

### Principios Básicos

#### Encapsula lo que varia

Identifica los aspectos de tu aplicación que varían y sepáralos de los que se mantienen inalterables.
El objetivo principal de este principio es minimizar el efecto provocado por los cambios.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Encapsula%20lo%20que%20varia)

#### Favorece la composicion sobre la herencia

- **Una subclase no puede reducir la interfaz de la superclase**: Tienes que implementar todos los métodos abstractos de la clase padre, incluso aunque no vayas a usarlos.

- **Al sobrescribir métodos debes asegurarte de que el nuevo comportamiento sea compatible con el de base**.

- **La herencia rompe la encapsulación de la superclase**: porque los detalles internos de la clase padre se hacen disponibles
para la subclase.

- **Las subclases estan fuertemente acopladas a superclases**.

Existe una alternativa a la herencia llamada composición. Mientras que la herencia representa la relación “is a” (es un/a) entre clases (un auto es un medio de transporte), la composición se basa en la relación “tiene un/a” (un auto tiene un motor).
Debo mencionar que este principio también se aplica a la agregación, una variante más relajada de la composición en la que un objeto puede contener una referencia al otro pero no gestiona su ciclo vital. Aquí tienes un ejemplo: un auto tiene un conductor pero éste puede utilizar otro auto o caminar sin el auto.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Favorece%20la%20composicion%20sobre%20la%20herencia)

#### Programa una Interfaz no una implementacion

Fomenta el uso de abstracciones para reducir el acoplamiento entre los componentes de un sistema.
Este principio nos enseña a diseñar nuestros sistemas para que dependan de contratos generales (interfaz o clase abstracta) y no de detalles concretos (clases específicas). Esto hace que el código sea más flexible, reutilizable y fácil de mantener.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Programa%20a%20una%20interfaz%20no%20una%20implementacion)

### Principio SOLID

#### S: Principio de Responsabilidad Única

Este principio establece que una clase debe tener una sola responsabilidad o razón para cambiar. En otras palabras, una clase debe enfocarse en realizar una tarea específica y no hacerse cargo de varias responsabilidades que podrían cambiar de forma independiente.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/S.%20Principio%20de%20Responsabilidad%20Unica)

#### O: Principio de Abierto/Cerrado

Las clases deben estar abiertas a la extensión pero cerradas a la modificación. Esto significa que se debe poder extender el comportamiento de una clase sin tener que modificar su código fuente, generalmente utilizando herencia o composición.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/O.%20Principio%20de%20Abierto%20Cerrado)

#### L: Principio de Sustitucion de Liskov

Si tomamos una clase padre y la extendemos con una subclase, la subclase debe seguir comportándose como la clase original. Es decir, un objeto de la subclase debe poder reemplazar a un objeto de la superclase sin que el código que usa esa clase se rompa o funcione de manera inesperada.

El principio de sustitución es un grupo de comprobaciones que ayudan a predecir si una subclase permanece compatible con el código que pudo funcionar con objetos de la superclase. Repasemos esta lista de detalles:

- Los tipos de parámetros en el método de una subclase deben coincidir o ser más abstractos que los tipos de parámetros del método de la superclase.
- El tipo de retorno en el método de una subclase debe coincidir o ser un subtipo del tipo de retorno del método de la superclase.
- Un método de una subclase no debe arrojar tipos de excepciones que no se espere que arroje el método base.
- Una subclase no debe fortalecer las condiciones previas.
- Una subclase no debe debilitar las condiciones posteriores.
- Los invariantes de una superclase deben preservarse.
- Una subclase no debe cambiar los valores de campos privados de la superclase.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/L.%20Principio%20de%20Sustitucion%20de%20Liskov)

#### I: Principio de Segregacion de la Interfaz

Intenta que tus interfaces sean lo suficientemente estrechas para que las clases del cliente no tengan que implementar comportamientos que no necesitan.
Según el principio de segregación de la interfaz, debes desintegrar las interfaces “gruesas” hasta crear otras más detalla-
das y específicas. Los clientes deben implementar únicamente aquellos métodos que necesitan de verdad. De lo contrario, un
cambio en una interfaz “gruesa” descompondrá incluso clientes que no utilizan los métodos cambiados.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/I.%20Principio%20de%20Segregacion%20de%20la%20Interfaz)

#### D: Principio de Inversion de Dependencia

Las clases de alto nivel no deben depender de clases de bajo nivel. Ambas deben depender de abstracciones. Las abstracciones no deben depender de detalles. Los detalles deben depender de abstracciones.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/D.%20Principio%20de%20Inversion%20de%20la%20Dependencia)

## Patrones de Diseño

### Patrones Creacionales

#### Factory Method

¿Alguna vez has ido a una tienda y notaste que para cada tipo de producto hay un empleado especializado? Por ejemplo, alguien para los lácteos, otro para las frutas, etc. Este es un tipo de “fábrica”: cada área sabe cómo crear o gestionar su propio tipo de producto.

El Factory Method hace algo similar. En lugar de que tu código principal (el cliente) se encargue de crear directamente los objetos que necesita, este patrón delega la tarea a métodos especializados (fábricas). Esto ayuda a que el cliente no tenga que preocuparse de los detalles de cómo se crea el objeto, sino solo de usarlo.

Formalmente: Proporciona una interfaz para crear objetos en una superclase, pero permite que las subclases alteren el tipo de objetos que se crearán.

Ejemplo: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Creacionales/factory_method)
