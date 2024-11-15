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

**Encapsula lo que varia**: 

Identifica los aspectos de tu aplicación que varían y sepáralos de los que se mantienen inalterables.
El objetivo principal de este principio es minimizar el efecto provocado por los cambios.

## Favorece la Composicion sobre la herencia