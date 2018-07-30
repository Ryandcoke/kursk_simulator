Kursk Simulator:  1943
=====================

![main_menu](https://raw.githubusercontent.com/wiki/Ryandcoke/kursk_simulator/main_menu.PNG)

Table of Contents
-----------------
1. [Introduction](#introduction)
2. [A Brief History](#a-brief-history)
3. [Weapon Performance](#weapon-performance)
    - [Historical Data](#historical-data)
    - [Penetration Functions](#penetration-regression)
4. [Armor Model](armour-model)
5. [Armor Overmatch Mechanics](#armor-overmatch-mechanics)
6. [Data and References](#data-and-references)


Introduction
------------
**Kursk Simulator: 1943** is a 2D tank gunnery simulator built in Python. The
simulator's armor overmatch mechanics (how armor penetration is modeled) are
based on a stylized model that was calibrated to closely match historical shell
penetration data. Tanks are reduced to simple polygons. The line segments in
the polygon chain capture the thickness and angle of the glacis plates, mantlet
and other hull surfaces.

A Brief History
---------------
The Battle of Kursk was the largest tank battle in history (perhaps the Battle
of Brody/Dudno was larger).

Weapon Performance
------------------
##### Historical Data
Shell penetration data was obtained from Rexford Bird and Livingston's book,
*World War II Ballistics: Armor and Gunnery*. This source provides normalized
penetration tables for different shells against RHA, at a perpendicular strike
angle, with a 50% success rate. The data tables give millimeters of penetration
at different ranges.

##### Penetration Functions
In order to map the discrete penetration data onto a continuous function, we
estimate each shell's penetration function. The penetration function for shell
*i* takes the following quadratic form:

*P<sub>i</sub>*&nbsp; = α<sub>*i*</sub> + β<sub>1*i* </sub>*x* + β<sub>2*i* </sub>*x*<sup>2</sup>

P is penetration <br>
*x* is distance, from the gun to target <br>
α is a constant <br>
β<sub>1</sub> and β<sub>2</sub> are coefficients

These penetration functions are estimated with a simple multiple regression.
Using STATA, we regress penetration on distance and distance squared to
estimate α, β<sub>1</sub> and β<sub>2</sub>.

Armor Models
------------
Tank 'hitboxes' are a polygon chain which represents the tank in 2D space. Each
line segment in the polygon has an associated thickness. These simplified
models simulate the thickness and angle of a tank's glacis plates, gun mantlet,
and other surfaces. Smaller details such as hatches and ports are not currently
modeled.

Armor Overmatch Mechanics
--------------------------
If a shell hits armor, it will penetrate if its penetration value is greater
than the armor's armor value.

Shell's penetration value = *f*(shell_type, range_to_target)

Armor's armor value = *g*(thickness, angle_of_incidence)

Penetration ⟺ *f* > *g*

Data and References
-------------------
This
[spreadsheet](https://docs.google.com/spreadsheets/d/1NiQnLE_kk3XM-1OGkv_seddDS9wuO5e36ZYBHDHRMOI/edit?usp=sharing)
contains the collected data that was used to model the attributes of the tanks
and their guns in-game.

Weapon penetration data was collected from the book *World War II Ballistics:
Armor and Gunnery*, which is available from
[scribd](https://www.scribd.com/doc/219173969/WWII-Ballistics-Armor-and-Gunnery)
and [MediaFire](http://www.mediafire.com/file/30f70hhd55ipvbp/WWII+Ballistics-+Armor+and+Gunnery.pdf).

> Rexford Bird, L., & Livingston, R. D. (2001). *World War II Ballistics: Armor
and Gunnery*. Overmatch Press.

Historical information comes from articles written on
[German](http://blog.tiger-tank.com/incombat/german-tanks-kursk/) and
[Soviet](http://blog.tiger-tank.com/incombat/soviet-tanks-kursk/) tanks at
Kursk by the staff of [The Tank Museum](http://www.tankmuseum.org/home).
