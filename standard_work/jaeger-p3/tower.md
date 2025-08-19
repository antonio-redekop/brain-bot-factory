# Work Instructions — Tower, Jaeger P2

## Change Log

| ECO Number | Date | Description |
| --- | --- | --- |
| XXXXXX | 6/1/25 | Initial Release  |

## Workmanship Standards

- Take care to avoid fastener preload.
- Take care to avoid cross-threading fasteners.
- Take special care when installing steel bolts into aluminum (e.g. B3CM)
- Utilize star pattern when tightening and torquing where applicable.
- When using hand tools:
    - Fastener installation to be performed in (2) steps when using hand tools:
        1. Tighten to achieve clamp up, without preloading fastener
        2. Apply final torque
- When using electric screwdrivers:
    - Maintain screwdriver torque settings:
        - [Makita: 13-15](img/makita.png)
        - [Milwaukee: 13-15](img/milwaukee.png)
- Note: Apply dry torque values when using fastener with pre-applied Loctite.
- See fastener torque tables for suggested torque values.  Tolerance is 5%.

| Screw Size  | Dry Torque (Nm) | Dry Torque (in-lb) | Lubricated Torque (Nm) | Lubricated Torque (in-lb) |
| :---------: | :-------------: | :----------------: | :--------------------: | :-----------------------: |
|     M2      |      0.13       |        1.1         |         0.09           |           0.8             |
|     M3      |      0.47       |        4.1         |         0.40           |           3.5             |
|    M3.5     |      0.74       |        6.5         |         0.60           |           5.3             |
|     M4      |      1.0        |        8.8         |         0.8            |           7.0             |
|     M5      |      2.1        |       18.6         |         1.7            |          14.9             |
|     M6      |      3.6        |       32.0         |         2.9            |          25.6             |

## Drawing / BOM References

**Drawing**

- [Link to full drawing](<dwg/800-00389-XX - rev 01.pdf>)

| Base                               | Tower                                | Final Assy                           |
| ---------------------------------- | ------------------------------------ | ------------------------------------ |
| [Sheet `1 of 12`](img/sheet1.png)  | [Sheet `7 of 12`](img/sheet7.png)    | [Sheet `12 of 12`](img/sheet12.png)  |
| [Sheet `2 of 12`](img/sheet2.png)  | [Sheet `8 of 12`](img/sheet8.png)    |                                      |
| [Sheet `3 of 12`](img/sheet3.png)  | [Sheet `9 of 12`](img/sheet9.png)    |                                      |
| [Sheet `4 of 12`](img/sheet4.png)  | [Sheet `10 of 12`](img/sheet10.png)  |                                      |
| [Sheet `5 of 12`](img/sheet5.png)  | [Sheet `11 of 12`](img/sheet11.png)  |                                      |
| [Sheet `6 of 12`](img/sheet6.png)  |                                      |                                      |

**BOM (Bill of Materials)**

- Base
    - [830-00309-01](bom/830-00309-01_base.csv)
- Tower
    - [830-00310-01](bom/830-00310-01_tower.csv)
    
---

## <font color="#e36c09">Sequence: Pre-Assemble Sensors</font>

```  
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                        | Quantity | Notes |
| ----------- | ------------ | ------------------------------------------------ | -------- | ----- |
| FN-1        | 290-00148-01 | Bpearl 3D LIDAR, Aviation Connector              | 1        |       |
| FN-2        | 290-00151-01 | UHD Camera, eCon, IMX412, RGB, GMSL2, 2.5 mm     | 1        |       |
| FN-3        | 290-00151-02 | Sense 2.0 Camera, eCon, IMX412, RGB, GMSL2, 6 mm | 4        |       |
| FN-5        | 260-00136-01 | PCB, Bpearl Insulator                            | 1        |       |
| FN-16       | 411-00488-01 | Bracket, Tower Camera 0-deg, Jaeger              | 2        |       |
| FN-17       | 411-00489-01 | Bracket, Tower Camera 5-deg, Jaeger              | 2        |       |
| FN-18       | 411-00490-01 | Bracket, Bpearl, Jaeger                          | 1        |       |

### Fasteners

| BOM Find No | Part Number  | Description                           | Quantity | Where Used?                                                     |
| ----------- | ------------ | ------------------------------------- | -------- | --------------------------------------------------------------- |
| FN-45       | 446-00375-10 | Screw, M4×10 mm, Button Head, Hex, Zn | 3        | Mounting Bpearl insulator (FN-5) and related subcomponents      |
| FN-46       | 446-00406-16 | Screw, M5×16 mm, Button Head, Hex, Zn | 10       | Mounting UHD camera (FN-2) and Sense cameras (FN-3) to brackets |
| FN-49       | 456-00158-01 | Washer, Shoulder #8 (M4) Nylon        | 3        | With FN-45 screws for Bpearl subassembly                        |

### Tools

| Tool Name                | Note                                    |
| ------------------------ | --------------------------------------- |
| H2.5 hex bit             | For FN-45 screws                        |
| H4 hex bit               | For FN-46 screws                        |
| Torque wrench (optional) | To ensure proper torque on M5 fasteners |

### Instructions

**Prepare Bpearl Subassembly**  
- <input type="checkbox" /> [Get (1) FN-1 Bpearl, (1) FN-18 Bpearl bracket, (1) FN-5 Bpearl insulator](tower-bpearl-assy.png)
- <input type="checkbox" /> [Assemble the Bpearl subassembly using (3) FN-49 washers and (3) FN-45 fasteners.](tower-bpearl-assy-2.png)

**Prepare Sense Cameras**  
- <input type="checkbox" /> [Get (4) FN-3 Sense cameras, (2) FN-16 brackets, (2) FN-17 brackets, and (8) FN-46 fasteners.](tower-sense-cameras.png)  
- <input type="checkbox" /> [Mount (2) FN-3 Sense cameras to the (2) FN-16 brackets using (4) FN-46 screws.](tower-sense-bracket-16.png)
- <input type="checkbox" /> [Mount (2) FN-3 Sense cameras to the (2) FN-17 brackets using (4) FN-46 screws.](tower-sense-bracket-17.png)
- <input type="checkbox" /> Get (1) FN-2 UHD camera and (2) FN-46 fasteners.  Set aside for now.

---

## <font color="#e36c09">Sequence: Bottom Fold Tower</font>

```  
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                           | Quantity | Notes |
| ----------- | ------------ | --------------------------------------------------- | -------- | ----- |
| FN-9        | 410-00130-01 | Tube, Bottom Fold Tower, Jaeger                     | 1        |       |
| FN-14       | 411-00486-01 | Plate, Snap-in Keeper                               | 1        |       |
| FN-21       | 412-00203-01 | Mount, Curved Flange Hinge, Jaeger                  | 2        |       |
| FN-28       | 423-00276-01 | Small Insert A, Hinge, Jaeger                       | 1        |       |
| FN-33       | 442-00567-01 | Tight-Hold Draw Latch with Safety Catch, 300 Series | 2        |       |
| FN-35       | 830-00247-01 | Touchscreen Assembly, Gen 3                         | 1        |       |

### Fasteners

| BOM Find No | Part Number  | Description                                        | Quantity | Where Used?                                                       |
| ----------- | ------------ | -------------------------------------------------- | -------- | ----------------------------------------------------------------- |
| FN-40       | 446-00326-10 | Screw, M4×10 mm, Flat Head, Hex, Zn                | 15       | Mounting Sense camera assemblies, Bpearl subassembly, FN-14 plate |
| FN-44       | 446-00404-14 | Screw, M5×14 mm, Flat Head, Hex, Zinc Plated Steel | 4        | Mounting FN-21 curved flange hinges                               |
| FN-45       | 446-00375-10 | Screw, M4×10 mm, Button Head, Hex, Zn              | 2        | Mounting FN-14 plate to FN-9 bottom fold tower                    |
| FN-46       | 446-00406-16 | Screw, M5×16 mm, Button Head, Hex, Zn              | 2        | Mounting UHD camera (FN-2) to FN-9 bottom fold tower              |
| FN-47       | 446-00403-10 | Screw, M3.5×10 mm, Button Head, Hex Drive, SS      | 8        | Mounting FN-33 latches and hooks to FN-9 bottom fold tower        |

### Tools

| Tool Name                       | Note                                      |
| ------------------------------- | ----------------------------------------- |
| H2.5 hex bit                    | For FN-40 and FN-47 fasteners (M4 & M3.5) |
| H3 hex bit                      | For FN-44 fasteners (M5×14 mm)            |
| H4 hex bit                      | For FN-46 fasteners (M5×16 mm)            |
| 1/4 drive ratchet & 7 mm socket | (Optional) for subassembly alignment      |

### Instructions

**Mount Sense Camera Assemblies**  
- <input type="checkbox" /> [Get FN-9 bottom fold tower, (1) Sense camera sub-assy with FN-16 bracket, and (1) Sense camera sub-assy with FN-17 bracket.](img/tower-bottom-1.png)
- <input type="checkbox" /> [Mount the Sense camera assembly with the FN-16 bracket onto FN-9 using (4) FN-40 screws. ](tower-sense-assy_2.png)
- <input type="checkbox" /> [Mount the Sense camera assembly with the FN-17 bracket onto FN-9 using (4) FN-40 screws.](tower-sense-assy.png) 

**Install Draw Latches & Hooks** 
- <input type="checkbox" /> [Install (2) FN-33 draw latches to FN-9 bottom fold tower using (4) FN-47 fasteners.](tower-draw-latch.png)
- <input type="checkbox" /> [Install (2) hooks (supplied with FN-33) to FN-9 using (4) FN-47 screws.](tower-hooks.png)

**Mount Bpearl Subassembly**  
- <input type="checkbox" /> [Mount the Bpearl subassembly to FN-9 bottom fold tower using (3) FN-40 fasteners.](tower-bpearl.png)

**Mount UHD Camera**  
- <input type="checkbox" /> [Mount FN-2 UHD camera using (2) FN-46 fasteners.](tower-uhd-camera-install.png)
    - Verify orientation matches drawing.  

**Install Curved Flange Hinges**  
- <input type="checkbox" /> [Mount (2) FN-21 curved flange hinges to the FN-9 bottom fold tower using (4) FN-44 screws.](img/tower-curved-flange.png)

**Install Push-to-Close Latch & Plate**  
- <input type="checkbox" /> [Install (1) FN-35 push-to-close latch to the FN-14 plate using (2) FN-45 screws.](img/tower-push-to-close.png)
- <input type="checkbox" /> [Mount the FN-14 plate (with latch attached) to FN-9 bottom fold tower using (2) FN-45 screws.](img/tower-bottom-plate.png)

**Install Hinge Insert**  
- <input type="checkbox" /> [Get FN-28 small insert A and (1) FN-38 screw. Mount FN-28 to one FN-21 curved flange hinge using (1) FN-38 screw (H2.5 hex).](img/tower-small-insert.png)
  
**Install Catch Latch**  
- <input type="checkbox" /> [Install the catch latch supplied with Item 35 (push-to-close latch) into FN-9 (align with FN-14 plate).](img/tower-catch-latch.png)

---

## <font color="#e36c09">Sequence: Middle Fold Tower</font>

```  
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                               | Quantity | Notes                       |
| ----------- | ------------ | --------------------------------------- | -------- | --------------------------- |
| FN-4        | 830-00247-01 | Touchscreen Assembly, Gen 3             | 1        |                             |
| FN-10       | 410-00131-01 | Tube, Middle Fold Tower, Jaeger         | 1        |                             |
| FN-12       | 411-00484-01 | Tower Screen Top Bracket, Jaeger        | 1        |                             |
| FN-13       | 411-00485-01 | Tower Screen Lower Bracket, Jaeger      | 1        |                             |
| FN-15       | 411-00487-01 | Plate, Tower Alignment, Jaeger          | 2        |                             |
| FN-17       | 411-00489-01 | Bracket, Tower Camera 5-deg, Jaeger     | 1        | From “Pre-Assemble Sensors” |
| FN-22       | 420-00215-01 | Bezel, Touchscreen, Jaeger              | 1        |                             |
| FN-21       | 412-00203-01 | Mount, Curved Flange Hinge, Jaeger      | 2        |                             |
| FN-32       | 438-00164-01 | LCD Neoprene Seal, Jaeger               | 1        |                             |
| FN-33       | 442-00567-01 | Tight-Hold Draw Latch with Safety Catch | 2        |                             |
| FN-36       | 442-00570-01 | Handle, Pull, Oval 7″ L, Black Aluminum | 1        |                             |

### Fasteners

| BOM Find No | Part Number  | Description                                        | Quantity | Where Used?                                                    |
| ----------- | ------------ | -------------------------------------------------- | -------- | -------------------------------------------------------------- |
| FN-40       | 446-00326-10 | Screw, M4×10 mm, Flat Head, Hex, Zn                | 12       | Mounting FN-15 plates, FN-17 bracket, FN-33 latches, and hooks |
| FN-41       | 446-00326-12 | Screw, M4×12 mm, Flat Head, Hex, Zn                | 4        | Mounting FN-22 touchscreen bezel to FN-10 middle fold tower |
| FN-43       | 446-00330-20 | Screw, M6×20 mm, Button Head, Hex, Zn              | 2        | Mounting FN-36 pull handle to FN-10                            |
| FN-44       | 446-00404-14 | Screw, M5×14 mm, Flat Head, Hex, Zinc Plated Steel | 4        | Mounting FN-21 curved flange hinges to FN-10                   |
| FN-45       | 446-00375-10 | Screw, M4×10 mm, Button Head, Hex, Zn              | 1        | Mounting FN-36 pull handle bracket (if needed)                 |
| FN-47       | 446-00403-10 | Screw, M3.5×10 mm, Button Head, Hex Drive, SS      | 8        | Mounting FN-33 latches and hooks to FN-10                      |
| FN-48       | 446-00405-01 | Screw, M4x10, Round Head, Phillips, Thread Forming, Zinc Plated Steel | 8 | Mounting touchscreen brackets (FN-12 & FN-13) to FN-4 |

### Tools

| Tool Name                 | Note                                                |
| ------------------------- | --------------------------------------------------- |
| H2.5 hex bit              | For FN-40 and FN-47 fasteners (M4 & M3.5)           |
| H3 hex bit                | For FN-44 fasteners (M5×14 mm)                      |
| H4 hex bit                | For FN-41 fasteners (M4×12 mm) and FN-43 (M6×20 mm) |
| Phillips drive bit (PH00) | For FN-48 touchscreen bracket screws                      |

### Instructions

**Prepare Touchscreen Assembly**
- <input type="checkbox" /> [Get FN-4 touchscreen assembly,  FN-12 top bracket, FN-13 lower bracket,  and FN-37 grommet.](img/tower-touchscreen-assy.png)
- <input type="checkbox" /> [Install FN-37 grommet into FN-13 lower bracket.](img/tower-install-grommet.png)
- <input type="checkbox" /> [Install FN-12 top bracket and FN-13 lower bracket to the FN-4 touchscreen using (8) FN-48 thread-forming screws.](img/tower-touchscreen-brackets.png)
    - Torque the fasteners to 5 in-lbs.
    - Verify gasket/seal alignment

**Install Touchscreen Assembly and Bezel**  
- <input type="checkbox" /> [Mount the touchstreen assembly to the FN-10 middle fold tower using (2) FN-40 fasteners.](img/tower-mount-touchscreen.png)
- <input type="checkbox" /> [Install the FN-32 neoprene seal and FN-22 touchscreen bezel to the FN-10 middle fold tower using (4) FN-41 fasteners.](img/tower-touchscreen-bezel.png)
    - Ensure adhesive side of neoprene seal against touchscreen bezel
      
**Mount Sense Camera Assembly**  
- <input type="checkbox" /> [Get the Sense camera subassembly (with FN-17 bracket).  Install onto FN-10 using (4) FN-40 screws.](img/tower-middle-fold-tower-sense.png)
    - Maintain orientation per drawing.

**Install Curved Flange Hinges**  
- <input type="checkbox" /> [Install (1) FN-21 curved flange hinge onto FN-10 middle fold tower.](img/tower-middle-tower-curved-hinge.png)
- <input type="checkbox" /> [Install another FN-21 curved flange hinge onto FN-10 middle fold tower.](tower-middle-tower-curved-hinge-2.png)

**Install Pull Handle**  
- <input type="checkbox" /> Get (2) FN-20 handle mounts and (4) FN-45 screws (for reference; FN-20 is part of the Top Fold Tower sequence but may be staged here if combined).  
- <input type="checkbox" /> Get (1) FN-36 pull handle and (2) FN-43 screws. Mount FN-36 to FN-10 middle fold tower using (2) FN-43 screws (H4 hex).  

**Install Alignment Plates**  
- <input type="checkbox" /> Get (2) FN-15 plates and (4) FN-40 screws. Mount two FN-15 plates to FN-10 using (4) FN-40 screws (H2.5 hex).  

**Install Draw Latches & Hooks**  
- <input type="checkbox" /> Get (2) FN-33 latches and (4) FN-47 screws. Mount both FN-33 latches to FN-10 using (4) FN-47 screws (H2.5 hex).  
- <input type="checkbox" /> Get (2) hooks (supplied with FN-33) and (4) FN-47 screws. Install (2) hooks to FN-10 using (4) FN-47 screws (H2.5 hex).

**Install Push-to-Close Latch & Plate**  
- <input type="checkbox" /> Get (1) FN-35 push-to-close latch and (2) FN-45 screws.  
- <input type="checkbox" /> Get (1) FN-14 plate. Mount latch to plate using (2) FN-45 screws (H2.5 hex).  
- <input type="checkbox" /> Mount the FN-14 plate (with latch attached) to FN-10 using (2) FN-45 screws (H2.5 hex).

---

## <font color="#e36c09">Sequence: Top Fold Tower</font>

```  
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                                   | Quantity | Notes |
| ----------- | ------------ | ----------------------------------------------------------- | -------- | ----- |
| FN-6        | 810-00309-01 | Cable Assy, 3D Lidar, HSD+2 A-Key to LEMO, 1300 mm          | 1        |       |
| FN-7        | 810-00312-01 | Cable Assy, Mini-Fakra Quad Code-B to UHD CAM, 2600 mm      | 1        |       |
| FN-8        | 810-00313-01 | Cable Assy, Mini-Fakra Quad Code-A to Scanning CAM, 2600 mm | 1        |       |
| FN-11       | 410-00132-01 | Tube, Top Fold Tower, Jaeger                                | 1        |       |
| FN-15       | 411-00487-01 | Plate, Tower Alignment, Jaeger                              | 2        |       |
| FN-21       | 412-00203-01 | Mount, Curved Flange Hinge, Jaeger                          | 1        |       |
| FN-33       | 442-00567-01 | Tight-Hold Draw Latch with Safety Catch                     | 2        |       |
| FN-34       | 442-00568-01 | Hinge, Concealed SOSS 212, Satin Chrome                     | 3        |       |

### Fasteners

| BOM Find No | Part Number  | Description                                        | Quantity | Where Used?                                                  |
| ----------- | ------------ | -------------------------------------------------- | -------- | ------------------------------------------------------------ |
| FN-40       | 446-00326-10 | Screw, M4×10 mm, Flat Head, Hex, Zn                | 4        | Mounting FN-15 plates to FN-11                               |
| FN-44       | 446-00404-14 | Screw, M5×14 mm, Flat Head, Hex, Zinc Plated Steel | 10       | Mounting FN-34 hinges and FN-21 curved flange hinge to FN-11 |
| FN-47       | 446-00403-10 | Screw, M3.5×10 mm, Button Head, Hex Drive, SS      | 8        | Mounting FN-33 latches and hooks to FN-11                    |

### Tools

| Tool Name                   | Note                                      |
| --------------------------- | ----------------------------------------- |
| H2.5 hex bit                | For FN-40 and FN-47 fasteners (M4 & M3.5) |
| H3 hex bit                  | For FN-44 fasteners (M5×14 mm)            |
| Slot-head pliers (optional) | For seating cables and aligning hinges    |

### Instructions

**Stage Top Fold Tower Components**  
- <input type="checkbox" /> Get FN-11 top fold tower.  
- <input type="checkbox" /> Get (2) FN-15 plates and (4) FN-40 screws.  

**Install Alignment Plates**  
- <input type="checkbox" /> Mount two FN-15 plates to FN-11 using (4) FN-40 screws (H2.5 hex).  

**Install Draw Latches & Hooks**  
- <input type="checkbox" /> Get (2) FN-33 latches and (4) FN-47 screws. Mount both latches to FN-11 using (4) FN-47 screws (H2.5 hex).  
- <input type="checkbox" /> Get (2) hooks (supplied with FN-33) and (4) FN-47 screws. Install (2) hooks to FN-11 using (4) FN-47 screws (H2.5 hex).  

**Install Curved Flange Hinge**  
- <input type="checkbox" /> Get FN-21 curved flange hinge and (2) FN-44 screws. Mount hinge to FN-11 using (2) FN-44 screws (H3 hex).  

**Install Concealed Hinges**  
- <input type="checkbox" /> Get (3) FN-34 hinges and (10) FN-44 screws. Install three FN-34 hinges to FN-9 (bottom), FN-10 (middle), and FN-11 (top) assemblies using (10) FN-44 screws (H3 hex).  

**Route Cables Through Tower Subassemblies**  
- <input type="checkbox" /> Get FN-6 3D lidar cable, FN-7 UHD camera cable, and FN-8 scanning camera cable.  
- <input type="checkbox" /> With bottom (FN-9), middle (FN-10), and top (FN-11) subassemblies secured together, feed the FN-8 scanning camera cable first from the bottom (Camera 0). Then feed the FN-7 UHD camera cable, followed by the FN-6 3D lidar cable. Snap all subassemblies closed with the latches.  

## <font color="#e36c09">SKU/SN Configuration (Flavor Station)</font>

1. Disconnect Distribution Board J2 (power to DD-TCM )
2. Disconnect DD-TCM J12 and J14
3. Connect ground to DD-TCM J13
4. Connect CAN to DD-TCM J14
5. Connect power to DD-TCM J12
6. In the command line, input the following:
    - `sudo ip link set can0 up type can bitrate 500000`
    - `clear; cd /opt/jaeger_ddtcm_config_station && sudo ./jaeger_config.sh jaeger_config.py BC533T9001 base_standardized.yaml /opt/jaeger_ddtcm_config_station/7CH2DM13_1.1.0_20250529.bvk`
7. Scan Vehicle Serial Number label on the robot when prompted
8. Wait until confirmation that Jaeger DDTCM configuration has completed successfully.
9. Disconnect power (DD-TCM J12)
10. Disconnect CAN (DD-TCM J14).
11. Disconnect ground (DD-TCM J13)
12. Reconnect DD-TCM J14 CAN
13. Reconnect DD-TCM J12 power
14. Reconnect Distribution Board J2 (power to DD-TCM)
