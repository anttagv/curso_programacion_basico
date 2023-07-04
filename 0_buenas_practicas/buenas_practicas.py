"""

https://peps.python.org/pep-0008/


Para Python, PEP 8 se erigió como la guía de estilo a la que más proyectos adhirieron; promueve un estilo de
programación fácil de leer y visualmente agradable. Todos los desarrolladores Python deben leerlo en algún
momento; aquí están extraídos los puntos más importantes:

- Usar sangrías de 4 espacios, no tabuladores.

- 4 espacios son un buen compromiso entre una sangría pequeña (permite mayor nivel de sangrado)y una sangría
  grande (más fácil de leer). Los tabuladores introducen confusión y es mejor dejarlos de lado.

- Recortar las líneas para que no superen los 79 caracteres.

- Esto ayuda a los usuarios con pantallas pequeñas y hace posible tener varios archivos de código abiertos,
  uno al lado del otro, en pantallas grandes.

- Usar líneas en blanco para separar funciones y clases, y bloques grandes de código dentro de funciones.

- Cuando sea posible, poner comentarios en una sola línea.

- Usar docstrings.

- Usar espacios alrededor de operadores y luego de las comas, pero no directamente dentro de
  paréntesis: a = f(1, 2) + g(3, 4).

- Nombrar las clases y funciones consistentemente; la convención es usar NotacionCamello para clases y
  minusculas_con_guiones_bajos para funciones y métodos. Siempre usa self como el nombre para el primer
  argumento en los métodos (ver Un primer vistazo a las clases para más información sobre clases y métodos).

- No uses codificaciones estrafalarias si esperas usar el código en entornos internacionales. El default de
  Python, UTF-8, o incluso ASCII plano funcionan bien en la mayoría de los casos.

- De la misma manera, no uses caracteres no-ASCII en los identificadores si hay incluso una pequeñísima chance
  de que gente que hable otro idioma tenga que leer o mantener el código.
"""