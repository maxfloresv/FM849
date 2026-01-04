# 💻 Programación Científica para Proyectos de Inteligencia Artificial (IA)

Bienvenid@s al repositorio oficial del curso FM849, dictado en la Escuela de Verano de la Universidad de Chile. [[Realizaciones del curso en U-Cursos, plataforma oficial de comunicación](https://www.u-cursos.cl/escverano/FM849/datos_ramo/)].

## 📄 Licencia

Este proyecto está bajo la licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Para más detalles, revisa el archivo [LICENSE](LICENSE).

## 📋 Descripción del curso

Este curso nace como una iniciativa presentada a la Escuela de Verano de la Universidad de Chile para introducir conocimiento básico sobre Inteligencia Artificial en estudiantes de Educación Media (1.° a 4.° medio). 

El curso fue diseñado en julio de 2024, bajo el nombre "Proyecto de Ciencia de Datos" con el objetivo de concretar un proyecto, y posteriormente fue renombrado a "Programación Científica para Proyectos de Inteligencia Artificial (IA)" para fortalecer los contenidos.

> ❗ **Importante**: Las carpetas sufijadas por un `1` (p. ej., `20261`) corresponden al **semestre de verano**, donde el curso tiene 20 cátedras en total. Aquellas sufijadas por `2` corresponden al **semestre de invierno**. En este último, se dicta una versión alternativa de 10 cátedras. El material se actualiza semestre a semestre.

## 👷 Equipo docente

**Profesores de Cátedra**
- Máximo Flores Valenzuela [[Correo electrónico](mflores@dcc.uchile.cl)] [[GitHub](https://github.com/maxfloresv)].
- Héctor Jiménez Orellana [[Correo electrónico](hector.jimenezor@gmail.com)] [[GitHub](https://github.com/hectorjimenez12)].

## ⚙️ Ejecución del material

En la realización actual del curso (`20261/`), hay una carpeta llamada `scripts`, donde se crea material complementario de las cátedras (p. ej., Jupyter Notebooks, gráficos, etc.).

Para ejecutar el material, es necesario que clones previamente el repositorio en tu máquina local, y accedas a la carpeta mencionada. Desde allí, debes instalar los paquetes indicados en `requirements.txt`:
```sh
pip install -r requirements.txt
```
Se recomienda altamente la creación y uso de un entorno virtual, y usar **Python 3.10**.

Para que los gráficos sean renderizados correctamente, también es necesario que instales la fuente CMU Sans Serif y todas sus variantes (_bold_, _italic_, etc.) en tu sistema. Éstas puedes descargarlas desde la página [FontLibrary](https://fontlibrary.org/es/font/cmu-sans-serif).

También, existe una carpeta `source` donde está el código fuente de las cátedras. Para la compilación, es necesario instalar una distribución de LaTeX (p. ej., [TeX Live](https://www.tug.org/texlive/)) y aprovechar el _pipeline_ creado en `.vscode/settings.json` para compilar los archivos `.tex` directamente desde el editor [Visual Studio Code](https://code.visualstudio.com/). 

Antes de la compilación, se debe instalar el paquete `sansmathaccent` para renderizar correctamente las fuentes matemáticas de Beamer. En TeX Live, esto se logra con el siguiente comando:
```sh
tlmgr install sansmathaccent
```

## 🏗️ Código abierto

Este proyecto es de código abierto. Si deseas contribuir, puedes hacer un _fork_ del repositorio y enviar un _Pull Request_ con tus mejoras o correcciones. Agradecemos cualquier aporte que ayude a mejorar el material del curso, y los créditos serán debidamente reconocidos. 

**Al enviar un _Pull Request_ a este repositorio, aceptas que tu contribución se licencie bajo los mismos términos (CC BY-NC-SA 4.0).**