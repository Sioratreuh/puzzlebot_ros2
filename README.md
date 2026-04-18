# Integración de Navegación y SLAM para Puzzlebot en ROS 2

Este repositorio contiene la estructura inicial y la integración formal del robot diferencial **Puzzlebot** al stack de navegación de ROS 2. El proyecto abarca la descripción del robot, la simulación del entorno y la configuración de los modos de mapeo (SLAM) y navegación (Nav2).

# Integrantes del Equipo
* Ezzat Alzahouri Campos A0176 - DrearyLand
* Jose Angel Huerta Ríos A0176 - Sioratreuh
* Juan Pablo A. Curiel Nava A01748818 - JPCN33

# Estructura del Proyecto

El proyecto está segmentado en tres paquetes principales para mantener una arquitectura modular y escalable:

1. **`puzzlebot_description`**: Contiene la definición del robot. Incluye el modelo URDF, las mallas (meshes) en formato STL y las configuraciones de visualización en RViz para el modelo estático.
2. **`puzzlebot_gazebo`**: Encargado de la simulación. Contiene el mundo o laberinto del proyecto (`maze.world`), las configuraciones del bridge de Gazebo y los archivos launch para hacer spawn del robot en el simulador.
3. **`puzzlebot_navigation`**: Contiene el stack de navegación. Aquí se alojan las configuraciones YAML para `slam_toolbox` y `nav2`, los mapas generados (`my_map.yaml` / `.pgm`), perfiles de RViz específicos para mapeo y navegación, y los launch files principales.

## Prerrequisitos y Entorno
* **SO:** Ubuntu 22.04 (Recomendado)
* **ROS 2:** Humble
* **Simulador:** Gazebo Classic