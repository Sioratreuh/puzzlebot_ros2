# Integración de Navegación y SLAM para Puzzlebot en ROS 2

Este repositorio contiene la arquitectura de software y la integración del robot diferencial **Puzzlebot** con el stack de navegación de **ROS 2 (Humble)**. El proyecto abarca desde la descripción física del robot y su simulación en entornos controlados, hasta la configuración de los modos de mapeo (SLAM) y la sintonización de parámetros de navegación autónoma (Nav2).

---

## Integrantes del Equipo

| Nombre | Matrícula | Usuario de GitHub |
| :--- | :--- | :--- |
| Ezzat Alzahouri Campos | A01710709 | [@DrearyLand](https://github.com/DrearyLand) |
| Jose Angel Huerta Ríos | A01710607 | [@Sioratreuh](https://github.com/Sioratreuh) |
| Juan Pablo A. Curiel Nava | A01748818 | [@JPCN33](https://github.com/JPCN33) |

---

## Estructura del Proyecto

El proyecto se divide en tres paquetes modulares para facilitar la escalabilidad y el mantenimiento:

1.  **`puzzlebot_description`**: Contiene la definición del robot. Incluye el modelo **URDF**, las mallas (meshes) en formato `.stl` y las configuraciones de visualización en **RViz** para el modelo estático.
2.  **`puzzlebot_gazebo`**: Encargado del entorno de simulación. Contiene el mundo o laberinto (`maze.world`), las configuraciones del bridge de Gazebo y los archivos *launch* para instanciar (spawn) al robot.
3.  **`puzzlebot_navigation`**: El núcleo del sistema de navegación. Aloja las configuraciones YAML para **SLAM Toolbox** y **Nav2**, los mapas generados (`.yaml` / `.pgm`), perfiles de RViz específicos y los lanzadores principales del stack.

---

## 🛠️ Prerrequisitos y Entorno

* **Sistema Operativo:** Ubuntu 22.04 LTS
* **ROS 2:** Humble Hawksbill
* **Simulador:** Gazebo Classic
* **Paquetes Clave:** `rviz2`, `slam_toolbox`, `nav2`.

---

## 🚀 Inicialización y Ejecución

Sigue estos comandos en tu terminal para poner en marcha el proyecto:

1. **Clonar el repositorio:**
   ```bash
   cd ~/tu_workspace_ws/src
   git clone <url_del_repositorio>```

2. **Compilar el espacio de trabajo:**
   ```bash
   cd ~/tu_workspace_ws
    colcon build```

3. **Cargar el entorno:**
   ```bash
   source install/setup.bash```

4. **Lanzar la simulación y navegación:**
   ```bash
   ros2 launch puzzlebot_navigation nav2.launch.xml use_sim_time:=true```
   
