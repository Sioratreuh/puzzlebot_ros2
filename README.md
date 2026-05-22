# Integración de Navegación y SLAM para Puzzlebot en ROS 2 (Simulación y Hardware Físico)

Este repositorio contiene la arquitectura de software y la integración del robot diferencial **Puzzlebot** con el ecosistema de **ROS 2 (Humble)**. El proyecto abarca desde la descripción física y simulación en entornos controlados, hasta la migración total hacia el hardware real utilizando el stack de **Nav2** para la planificación de trayectorias y **SLAM Toolbox** para el mapeo simultáneo.

---

## Integrantes del Equipo

| Nombre | Matrícula | Usuario de GitHub |
| :--- | :--- | :--- |
| Ezzat Alzahouri Campos | A01710709 | [@DrearyLand](https://github.com/DrearyLand) |
| Jose Angel Huerta Ríos | A01710607 | [@Sioratreuh](https://github.com/Sioratreuh) |
| Juan Pablo A. Curiel Nava | A01748818 | [@JPCN33](https://github.com/JPCN33) |

---

## Estructura de Paquetes Modulares

El proyecto está diseñado de forma modular para separar estrictamente los elementos de simulación del hardware físico:

1.  **`puzzlebot_description`**: Contiene la definición URDF del robot, mallas `.stl` y configuraciones de RViz para el modelo estático.
2.  **`puzzlebot_gazebo`**: Encargado de la simulación pura, conteniendo el laberinto (`maze.world`) y configuraciones para Gazebo Classic.
3.  **`puzzlebot_navigation`**: El núcleo lógico. Aloja configuraciones YAML base para SLAM Toolbox y Nav2, así como herramientas generales del stack.
4.  **`puzzlebot_real_robot`**: Actúa como la capa de abstracción de hardware, reemplazando al entorno simulado para inicializar los componentes físicos del robot.

### Detalles del paquete `puzzlebot_real_robot`

* **`config/`**: Almacena parámetros ajustados para la física real, desactiva el reloj de simulación y adapta las tolerancias de los costmaps.
* **`launch/`**: Contiene orquestadores en cascada (`real_robot_core`, `slam_real`, `nav2_real`) para evitar inicializaciones manuales.
* **`maps/`**: Repositorio dedicado a los mapas físicos generados por el LiDAR RPLIDAR A1.
* **`scripts/`**: Nodos en Python para calcular la cinemática directa e inversa a partir de la telemetría de los encoders reales.

---

## Diferencias Clave: Simulación vs Realidad

Para operar en el mundo físico, la arquitectura implementa los siguientes ajustes críticos:
* **Sincronización de Tiempo**: El parámetro `use_sim_time = false` está configurado globalmente para depender estrictamente del reloj interno del sistema operativo (Hardware Clock).
* **Tolerancia de Latencia**: En `nav2_params_real.yaml`, el parámetro `transform_tolerance` se aumentó de 0.5 a 1.0 para mitigar retrasos físicos de Wi-Fi o procesamiento.
* **Odometría Real**: Los actuadores simulados fueron reemplazados por cálculos matemáticos alimentados por las lecturas crudas `/VelocityEncL` y `/VelocityEncR`.
* **Seguridad**: El lanzador de navegación incluye un comando de apagado seguro que publica velocidad cero (`linear: 0.0, angular: 0.0`) en `/cmd_vel` al cancelarse la ejecución.

---

## Ejecución en el Robot Físico

### A) Proceso de Ejecución de SLAM (Mapeo)

1.  En la terminal 1, inicializa el hardware (Micro-ROS, sensores, odometría y TFs):
    ```bash
    ros2 launch puzzlebot_real_robot real_robot_core.launch.xml
    ```
    *Nota: Este comando incluye una transformada estática (`static_transform_publisher`) automática para alinear el frame nativo del lidar `laser` con `laser_frame` del URDF*.

2.  En la terminal 2, inicia el nodo de SLAM, RViz y teleoperación:
    ```bash
    ros2 launch puzzlebot_real_robot slam_real.launch.xml
    ```
3.  Conduce suavemente al robot usando el teclado para mapear la pista.

### B) Proceso de Ejecución de Navegación Autónoma

1.  En la terminal 1, energiza la capa de hardware físico:
    ```bash
    ros2 launch puzzlebot_real_robot real_robot_core.launch.xml
    ```

2.  En la terminal 2, ejecuta Nav2 apuntando al mapa generado:
    ```bash
    ros2 launch puzzlebot_real_robot nav2_real.launch.xml map_path:=/ruta/al/map_maze_real.yaml
    ```

3.  En RViz, usa la herramienta **2D Pose Estimate** para indicar la posición inicial del robot y hacer converger las partículas de AMCL.
4.  Utiliza la herramienta **Nav2 Goal** para instruir una coordenada final y comenzar la navegación.

---

## Solución de Problemas (Troubleshooting)

* **Desincronización Temporal (Clock Drift):** Si Nav2 descarta paquetes por fechas inválidas, asegúrate de que tanto el robot como la estación base tengan instalado y configurado **Chrony** (cliente NTP) para sincronizar los relojes en red local.
* **Falta de Tópicos en RViz (Bloqueo DDS):** Si RViz está "ciego" a la telemetría, deshabilita temporalmente el firewall de la base para permitir tráfico UDP Multicast y verifica que ambos equipos exporten el mismo `ROS_DOMAIN_ID`.
* **Modelos 3D Invisibles:** Actualmente existe un conflicto visual de baja prioridad que impide la carga completa gráfica de los `.stl` en RViz. Esto no afecta la funcionalidad del robot, ya que los ejes matemáticos y de navegación operan con normalidad.