# **Patrones de Diseño**

> 💡 Antes de estudiar los patrones de diseño, te recomendamos repasar los fundamentos de la programación orientada a objetos para aprovechar al máximo esta guía.

---

## **📚 Programación Orientada a Objetos**

### **Conceptos básicos**

- **Clase**: Un plano que define la estructura y comportamiento de los objetos.
- **Atributos**: Las características o propiedades de un objeto.
- **Métodos**: Las funciones que definen el comportamiento del objeto.

---

## **⚙️ Pilares de la Programación Orientada a Objetos**

### **Abstracción**

La capacidad de representar objetos del mundo real en un contexto específico.

### **Encapsulación**

Esconder los detalles internos de un objeto para proteger su estado y comportamiento.

- **Privados**: Solo accesibles dentro de la clase.
- **Protegidos**: Accesibles dentro de la clase y sus subclases.

### **Herencia**

Permite crear nuevas clases a partir de otras existentes, fomentando la reutilización del código.

### **Polimorfismo**

Habilidad de diferentes clases para responder de maneras únicas a un mismo método.

---

## **❓ ¿Qué son los patrones de diseño?**

Los patrones de diseño son soluciones probadas y reutilizables para problemas comunes en el diseño de software. Se pueden comparar con recetas que describen un problema, la solución y los pasos para implementarla.

---

## **🗂️ Clasificación de Patrones**

### 1. **Patrones Creacionales**

- **Formal**: Abordan la creación de objetos, evitando instancias directas.
- **Ejemplo**: Si necesitas fabricar muchas ventanas iguales, este patrón ayuda a producirlas eficientemente.

### 2. **Patrones Estructurales**

- **Formal**: Facilitan la organización y ensamblaje de objetos y clases en estructuras más grandes.
- **Ejemplo**: Conectar habitaciones y ventanas para que tu casa sea funcional.

### 3. **Patrones de Comportamiento**

- **Formal**: Se centran en la comunicación e interacción entre objetos.
- **Ejemplo**: Las reglas para apagar luces automáticamente al salir de una habitación.

---

## **🎯 Principios de Diseño**

### **Encapsula lo que varía**

Identifica y separa los aspectos que pueden cambiar de los que se mantienen constantes. Esto minimiza el impacto de los cambios en el código. El objetivo principal de este principio es minimizar el efecto provocado por los cambios.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Encapsula%20lo%20que%20varia)

---

### **Favorece la composición sobre la herencia**

En lugar de usar la relación "es un/a", utiliza la relación "tiene un/a". Esto reduce el acoplamiento entre clases.

- **Una subclase no puede reducir la interfaz de la superclase**: Tienes que implementar todos los métodos abstractos de la clase padre, incluso aunque no vayas a usarlos.

- **Al sobrescribir métodos debes asegurarte de que el nuevo comportamiento sea compatible con el de base**.

- **La herencia rompe la encapsulación de la superclase**: porque los detalles internos de la clase padre se hacen disponibles
para la subclase.

- **Las subclases estan fuertemente acopladas a superclases**.

Existe una alternativa a la herencia llamada composición. Mientras que la herencia representa la relación “is a” (es un/a) entre clases (un auto es un medio de transporte), la composición se basa en la relación “tiene un/a” (un auto tiene un motor).
Debo mencionar que este principio también se aplica a la agregación, una variante más relajada de la composición en la que un objeto puede contener una referencia al otro pero no gestiona su ciclo vital. Aquí tienes un ejemplo: un auto tiene un conductor pero éste puede utilizar otro auto o caminar sin el auto.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Favorece%20la%20composicion%20sobre%20la%20herencia)

---

### **Programa para una interfaz, no una implementación**

Diseña tu código para depender de abstracciones en lugar de detalles concretos. Esto mejora la flexibilidad y el mantenimiento.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/principios_b%C3%A1sicos/Programa%20a%20una%20interfaz%20no%20una%20implementacion)

---

## **🔑 Principio SOLID**

1. **S - Responsabilidad Única**: Una clase debe tener una sola responsabilidad o razón para cambiar.

   📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/S.%20Principio%20de%20Responsabilidad%20Unica)

2. **O - Abierto/Cerrado**: Las clases deben estar abiertas a la extensión pero cerradas a la modificación. Esto significa que se debe poder extender el comportamiento de una clase sin tener que modificar su código fuente, generalmente utilizando herencia o composición.

    📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/O.%20Principio%20de%20Abierto%20Cerrado)

3. **L - Sustitución de Liskov**: Si tomamos una clase padre y la extendemos con una subclase, la subclase debe seguir comportándose como la clase original. Es decir, un objeto de la subclase debe poder reemplazar a un objeto de la superclase sin que el código que usa esa clase se rompa o funcione de manera inesperada.
El principio de sustitución es un grupo de comprobaciones que ayudan a predecir si una subclase permanece compatible con el código que pudo funcionar con objetos de la superclase. Repasemos esta lista de detalles:

- Los tipos de parámetros en el método de una subclase deben coincidir o ser más abstractos que los tipos de parámetros del método de la superclase.
- El tipo de retorno en el método de una subclase debe coincidir o ser un subtipo del tipo de retorno del método de la superclase.
- Un método de una subclase no debe arrojar tipos de excepciones que no se espere que arroje el método base.
- Una subclase no debe fortalecer las condiciones previas.
- Una subclase no debe debilitar las condiciones posteriores.
- Los invariantes de una superclase deben preservarse.
- Una subclase no debe cambiar los valores de campos privados de la superclase.  
  
   📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/L.%20Principio%20de%20Sustitucion%20de%20Liskov)

1. **I - Segregación de Interfaces**: Divide interfaces grandes en interfaces más específicas para que los clientes solo implementen lo necesario.  

   📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/I.%20Principio%20de%20Segregacion%20de%20la%20Interfaz)

2. **D - Inversión de Dependencias**: Las clases de alto nivel y bajo nivel deben depender de abstracciones.

   📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/principios/SOLID/D.%20Principio%20de%20Inversion%20de%20la%20Dependencia)

---

## **🏭 Patrones Creacionales**

### **Factory Method**

¿Alguna vez has ido a una tienda y notaste que para cada tipo de producto hay un empleado especializado? Por ejemplo, alguien para los lácteos, otro para las frutas, etc. Este es un tipo de “fábrica”: cada área sabe cómo crear o gestionar su propio tipo de producto.

El Factory Method hace algo similar. En lugar de que tu código principal (el cliente) se encargue de crear directamente los objetos que necesita, este patrón delega la tarea a métodos especializados (fábricas). Esto ayuda a que el cliente no tenga que preocuparse de los detalles de cómo se crea el objeto, sino solo de usarlo.

Formalmente: Proporciona una interfaz para crear objetos en una superclase, pero permite que las subclases alteren el tipo de objetos que se crearán.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Creacionales/factory_method)

---

### **Abstract Factory**

¿Alguna vez has armado muebles de una tienda como IKEA? Imagina que compras un juego completo de muebles, pero hay un problema: las sillas vienen de un estilo, la mesa de otro, y el sofá de otro diferente. ¡Un desastre para la decoración! Lo ideal sería que todos los muebles sean del mismo estilo, ¿verdad?

Aquí entra el patrón Abstract Factory, que actúa como un catálogo. Te permite obtener familias de objetos relacionados o dependientes sin preocuparte de cómo se crean. Si eliges "Estilo Moderno", obtendrás todos los muebles modernos. Si eliges "Estilo Clásico", todo será clásico.

La clave: encapsula el proceso de creación de objetos en un único lugar para asegurarte de que todo sea consistente.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Creacionales/abstract_factory)

---

### **Builder**

El patrón Builder es un patrón de diseño creacional que separa la construcción de un objeto complejo de su representación, de modo que el mismo proceso de construcción pueda crear diferentes representaciones del objeto. Es útil cuando un objeto puede configurarse de muchas maneras diferentes o tiene múltiples pasos de construcción.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Creacionales/builder)

---

### **Singleton**

El Patrón Singleton restringe la creación de instancias de una clase a una única instancia. Esto es útil en situaciones donde es importante que solo exista un objeto para coordinar acciones o mantener un estado global./home/abel/Documentos/code/patrones-de-diseño/code/patrones/Estructurales

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Creacionales/singleton)

---

## **🖇️ Patrones de Estructurales**

### **Adapter**

El Patrón Adapter es un patrón de diseño estructural que permite que clases con interfaces incompatibles trabajen juntas. Lo logra transformando la interfaz de una clase en otra que el cliente espera. Este patrón es especialmente útil cuando no puedes modificar las clases originales por restricciones de diseño, legado, o porque no tienes acceso al código fuente.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Estructurales/adapter)

---

## **🗣️ Patrones de Comportamiento**

### **Chain of Responsibility**

Chain of Responsibility es un patrón de diseño de comportamiento que permite pasar solicitudes a lo largo de la cadena de manejadores potenciales hasta que uno de ellos gestiona la solicitud.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Comportamiento/chain_of_responsibility)

### **Mediator**

El Patrón Mediador se utiliza para encapsular las interacciones entre un grupo de objetos. En lugar de que los objetos se comuniquen directamente entre sí, cada uno interactúa con un objeto mediador. Este mediador se encarga de manejar las comunicaciones, delegar tareas y coordinar acciones entre los componentes.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Comportamiento/mediator)

### **Observer**

Este patrón se usa cuando tienes un objeto principal (como un canal de YouTube) que necesita informar cambios a muchos otros objetos (los suscriptores). En lugar de que cada suscriptor pregunte constantemente al canal si hay novedades, el canal notifica automáticamente a todos cuando algo cambia.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Comportamiento/observer)

### **Strategy**

Strategy es un patrón de diseño que permite definir una familia de algoritmos, colocar cada uno de
ellos en una clase separada y hacer sus objetos intercambiables.

¿Has usado alguna vez una aplicación de pago en línea que te deja elegir cómo quieres pagar? Por ejemplo, puedes pagar con tarjeta de crédito, PayPal o transferencia bancaria. Todas estas son formas diferentes de realizar el mismo objetivo: procesar un pago.

Pues bien, el Patrón Strategy funciona exactamente así. Este patrón permite que un objeto (llamémoslo Contexto) pueda ejecutar una acción de diferentes maneras (estrategias), dependiendo de lo que se elija en ese momento. Lo mejor es que puedes cambiar esa estrategia sin modificar el código del contexto. Es como si cambiaras de tarjeta a PayPal sin afectar la app de pagos.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Comportamiento/strategy)

### **Template Method**

El Patrón Template es un patron de diseño que define el esqueleto de un algoritmo en una clase base y delega la implementación de algunos pasos a subclases concretas. Este patrón es ideal para reutilizar código, ya que permite que diferentes implementaciones sigan una estructura común, evitando la duplicación.

📂 **Ejemplo**: [Código](https://github.com/abelcarriizo/patrones-de-diseno/tree/main/code/patrones/Comportamiento/template)
