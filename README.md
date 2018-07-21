Kursk Simulator:  1943
=====================

![battleofkursk](https://raw.githubusercontent.com/wiki/Ryandcoke/kursk_simulator/title_image.jpg)

Table of Contents
-----------------
1. [Introduction](#introduction)
2. [A Brief History](#a-brief-history)
3. [Weapon Performance](#weapon-performance)
    - [Historical Data](#historical-data)
    - [Penetration Regression](#penetration-regression)
4. [Armour Model](armour-model)
5. [Armour Overmatch Mechanics](#armour-overmatch-mechanics)
6. [Data and References](#data-and-references)


Introduction
------------
**Kursk Simulator: 1943** is a 2D tank gunnery simulator built in Python. The simulator's armor overmatch mechanics (how armor penetration is modeled) are based on a stylized model that was calibrated to closely match historical shell penetration data. Tanks are reduced to simple polygons. The line segments in the polygon chain capture the thickness and angle of the glacis plates, mantlet and other hull surfaces.

A Brief History
---------------
The Battle of Kursk was the largest tank battle in history (perhaps the Battle of Brody/Dudno was larger).

Weapon Performance
------------------
Weapon performance is based on historical shell penetration data from Rexford Bird and Livingston's book, *World War II Ballistics: Armor and Gunnery*.

Armour Models
------------
Tank armor layouts are based on historical data. The simplified models capture the thickness and angle of glacis plates and the gun mantlet. Smaller details such as hatches and ports are not currently modeled.

Armour Overmatch Mechanics
--------------------------
If a shell hits armor, it will penetrate if its penetration value is greater than the armor's armor value.

Shell's penatration value = *f*(shell_type, range_to_target)

Armour's armor value = *g*(thickness, angle_of_incidence)

Penetration iff *f* > *g*

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
