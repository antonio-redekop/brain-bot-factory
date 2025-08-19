# Work Instructions — Base, Jaeger P2

## Change Log

| ECO Number | Date | Description |
| --- | --- | --- |
| XXXXXX | 6/1/25 | Initial Release  |

## Workmanship Standards

- Avoid fastener and assembly preload during installation.
- Avoid cross-threading fasteners.
- Take special care when installing steel bolts into aluminum (e.g. B3CM)
- Fastener installation to be performed in (2) steps when using hand tools:
    1. Tighten to achieve clamp up
    2. Tighten to achieve clamp up then apply final torque
- Utilize star pattern when tightening and torquing where applicable.
- Screwdriver torque settings:
    - [Makita: 13-15](img/makita.png)
    - [Milwaukee: 13-15](img/milwaukee.png)
- Ensure fasteners are tight, maintaining designed torques. 
- Torque wheel nuts to 25 Nm.
- If no torque is provided in the Drawing or Work Instructions, reference the following table(s):
    
**For dry (unlubricated) A2-70 stainless-steel bolts:**

| Screw Size  | Typical Torque (Nm) | Typical Torque (in-lb) |
| :---------: | :-----------------: | :--------------------: |
|  M2 × 0.40  |    0.2 – 0.4 Nm     |    1.8 – 3.5 in-lb     |
| M2.5 × 0.45 |    0.5 – 0.8 Nm     |    4.4 – 7.1 in-lb     |
|  M3 × 0.50  |    0.4 – 0.6 Nm     |    3.5 – 5.3 in-lb     |
|  M4 × 0.70  |    1.2 – 2.0 Nm     |   10.6 – 17.7 in-lb    |
|  M5 × 0.80  |    2.4 – 3.2 Nm     |   21.2 – 28.3 in-lb    |
|  M6 × 1.00  |    5.6 – 7.2 Nm     |   49.6 – 63.7 in-lb    |

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

## <font color="#e36c09">Sequence: Prep Base</font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                                     | Quantity | Notes |
| ----------- | ------------ | ------------------------------------------------------------- | -------- | ----- |
| FN-6        | 411-00491-01 | Chassis, Jaeger                                               | 1        |       |
| FN-11       | 411-00496-01 | Bracket, Spring Retainer, Jaeger                              | 2        |       |
| FN-31       | 420-00223-01 | Rail, Battery, Jaeger                                         | 2        |       |
| FN-34       | 423-00278-01 | Spacer, Speaker, Jaeger                                       | 1        |       |
| FN-35       | 830-00311-01 | Assy, Battery Lock, Jaeger                                    | 1        |       |
| FN-37       | 442-00474-01 | Swivel Caster, Dual Wheel Polyamide Gray 50mm                 | 4        |       |
| FN-38       | 442-00475-01 | Plate, Caster Mounting Base with Pin 42x42mm                  | 4        |       |
| FN-41       | 442-00572-01 | Holder Strip Brush, Jaeger                                    | 1        |       |
| FN-42       | 442-00573-01 | Strip Brush, Jaeger                                           | 1        |       |
| FN-43       | 442-00574-01 | Bumper, RGB 250-562-4, Rubber, Black                          | 4        |       |
| FN-44       | 442-00575-01 | Hole Grommet, SBR Rubber 1-1/8" Hole Dia x 3/32" Thk          | 2        |       |
| FN-47       | 442-00578-01 | Hole Grommet, SBR Rubber 13/16" Hole Dia x 1/8" Thk, 1/2" ID  | 1        |       |
| FN-68       | 450-00119-01 | Compression Spring, 1.75"L x 0.72"OD x 0.58"ID, 22 lbs/in, Zn | 2        |       |
| FN-108      | 810-00394-01 | Cable Assy, Speaker, Jaeger                                   | 1        |       |

### Fasteners

| BOM Find No | Part Number  | Description                                           | Quantity | Where Used?                                  |
| ----------- | ------------ | ----------------------------------------------------- | -------- | -------------------------------------------- |
| FN-50       | 444-00163-01 | Nut, M4x0.7, Nylon Insert Locknut, Class 10, Zn       | 2        | mounting FN-35 battery lock                  |
| FN-57       | 446-00326-10 | Screw, M4x10mm, Flat Head, Hex, Zn                    | 8        | mounting FN-31 battery rails                 |
| FN-56       | 446-00295-01 | Screw, M3x12mm, SHCS, Zinc-Plated Steel               | 4        | mounting FN-109 battery power and cable assy |
| FN-58       | 446-00326-16 | Screw, M4x16mm, Flat Head, Hex, Zn                    | 2        | mounting FN-35 battery lock                  |
| FN-60       | 446-00370-10 | Screw, M5x10mm, Socket Head, Hex, Zn                  | 16       | mounting FN-38 caster plates                 |
| FN-63       | 446-00378-01 | Screw, M4x10mm, Socket Head, Hex, Zinc Plated Steel   | 4        | mounting FN-11 spring retainer brackets      |
| FN-64       | 446-00387-10 | Screw, M2x10mm, Pan Head, Phillips, Zinc Plated Steel | 4        | mounting FN-108 speaker cable assy           |
| FN-70       | 442-00580-01 | 1/8" Aluminum Blind Rivets                            | 5        | mounting rivet brush assy |

###  Tools

| Tool Name                        | Note                            |
| -------------------------------- | ------------------------------- |
| Battery-powered screw driver     |                                 |
| H3 hex bit                       | For FN-57, FN-63                |
| H4 hex bit                       | For FN-60                       |
| 1/4 drive ratchet and 7mm socket | For FN-50                       |
| PH00x40 screwdriver              | For FN-64                       |
| Snips                            | For edge protection             |
| Long needle nose pliers          | To install strip to strip brush |
| Rivet gun                        | To install strip brush          |

### Instructions


- <input type="checkbox" /> [Install FN-43 bumpers to FN-6 chassis (4) places.](img/base-bumpers.png)
- <input type="checkbox" /> [Install FN-31 battery rails to FN-6 (2) places using (8) FN-57 screws](img/base-rails.png)
- <input type="checkbox" /> [Install FN-37 swivel casters (4) places onto caster studs.](img/base-swivel.png)
- <input type="checkbox" /> [Install FN-109 battery power and data cable assembly to FN-6 chassis using (4) FN-56 screws.](img/base-batpower.png)
- <input type="checkbox" /> Trim the strip brush to length using fixture
- <input type="checkbox" /> Install the strip brush to the base using FN-70 rivets (5) places.
- <input type="checkbox" /> Install FN-38 caster mounting plate to FN-6 chassis (4) places using (16) FN-60 screws.
- <input type="checkbox" /> [Install FN-44 grommets to FN-6 chassis (2) places.](img/base-grommets.png)
- <input type="checkbox" /> [Install FN-47 grommet to FN-6 chassis](img/base-grommet2.png)
- <input type="checkbox" /> [Install edge protection on FN-6 (2) places.](img/base-edge.png)
- <input type="checkbox" /> [Install FN-42 strip brush to FN-41 strip brush holder.](img/base-strip-brush-install.png)
- <input type="checkbox" /> [Install FN-35 battery lock using (2) FN-58 screws and (2) FN-50 nuts.](img/base-batterylock.png)
- <input type="checkbox" /> [Install FN-68 compression springs into FN-11 spring retainer brackets (2) places.](img/base-springs.png)
- <input type="checkbox" /> [Install FN-108 speaker cable assembly with FN-34 spacer using (4) FN-64 screws.](img/base-speaker.png)

---

## <font color="#e36c09">Sequence: Suspension and Motors </font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                                                     | Quantity |
| ----------- | ------------ | ----------------------------------------------------------------------------- | -------- | 
| FN-1        | 275-00252-01 | 5inch, 24V, 3N.m, 270RPM, 4096‐wire encoder, single shaft, 70kg load/2 wheels | 2        |
| FN-12       | 411-00497-01 | Bracket, Left Drive Wheel, Jaeger                                             | 1        |
| FN-13       | 411-00498-01 | Bracket, Right Drive Wheel, Jaeger                                            | 1        |
| FN-14       | 411-00499-01 | Bracket, Left Suspension Stop, Jaeger                                         | 1        |
| FN-15       | 411-00500-01 | Bracket, Right Suspension Stop, Jaeger                                        | 1        |
| FN-25       | 412-00194-01 | Mount, Wheel Pivot, Jaeger                                                    | 4        |
| FN-26       | 414-00196-01 | Pin, Suspension, Jaeger                                                       | 2        |

### Fasteners

| BOM Find No | Part Number  | Description                                     | Quantity | Where Used?                 |
| ----------- | ------------ | ----------------------------------------------- | -------- | --------------------------- |
| FN-50       | 444-00163-01 | Nut, M4x0.7, Nylon Insert Locknut, Class 10, Zn | 4        | FN-14, FN-15 swing arm stop |
| FN-61       | 446-00370-20 | Screw, M5x20mm, Socket Head, Hex, Zn            | 8        | Swing arm assembly to base  |
| None        | None         | Supplied nut                                    | 2        | Wheel assy                  |
| None        | None         | Supplied washer                                 | 2        | Wheel assy                  |

### Tools

| Tool Name                   | Note                         |
| --------------------------- | ---------------------------- |
| Battery-powered screwdriver |                              |
| H4 hex bit                  | For FN-61                    |
| 7mm ratcheting wrench       | For FN-50                    |
| Vice                        | For pressing bronze bushings |
| Torque Wrench               | For wheel nuts               |

### Instructions


- <input type="checkbox" /> [Get (4) FN-25 pivots and (4) FN-48 bushings. ](img/base-pivots-and-bushings.png)
- <input type="checkbox" /> Press the bushings into the pivots using the vice.
- <input type="checkbox" /> [Install (1) FN-26 pin to FN-13 drive wheel bracket](img/base-swingarm-pin-install.png)
- <input type="checkbox" /> Install (1) FN-26 pin to FN-12 drive wheel bracket.
- <input type="checkbox" /> Press the assemblies together using the vice.
- <input type="checkbox" /> [Install swing arm assembly using (4) FN-61 fasteners.  Repeat for the opposite swingarm assembly. ](img/base-pivot-install.png)
- <input type="checkbox" /> [Install FN-1 wheels (2) places using supplied nut and washer](img/base-swingarm.png)
    - Torque nuts to 25 Nm.
- <input type="checkbox" /> [Install FN-14 suspension stop using (2) FN-50 nuts.  Repeat for FN-15 suspension stop](img/base-swingarm.png)
- <input type="checkbox" /> Pass the motor cables through the grommets in the base.

---

## <font color="#e36c09">Sequence: Install B3CM </font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                              | Quantity | Note |
| ----------- | ------------ | -------------------------------------- | -------- | ---- |
| FN-5        | 830-00271-01 | Assy, Gen 3 Brain Control Module, B3CM | 1        |      |
| FN-9        | 411-00494-01 | Plate, B3CM                            | 1        |      |

### Fasteners

| BOM Find No | Part Number  | Description                                         | Quantity | Where Used? |
| ----------- | ------------ | --------------------------------------------------- | -------- | ----------- |
| FN-59       | 446-00330-12 | Screw, M6x12mm, Button Head, Hex, Zn                | 4        | B3CM        |
| FN-63       | 446-00378-10 | Screw, M4x10mm, Socket Head, Hex, Zinc Plated Steel | 3        | B3CM plate  |

### Tools

| Tool Name                   | Note             |
| --------------------------- | ---------------- |
| Screwdriver with H4 hex bit | For FN-59 screws |
| Screwdriver with H3 hex bit | For FN-63 screws |

### Instructions

- <input type="checkbox" /> [Install the FN-9 plate to the FN-5 B3CM using (4) FN-59 fasteners. ](b3cmplate.png)
- <input type="checkbox" /> [Install to the base using (2) FN-63 screws.](b3cmplate.png)

---

## <font color="#e36c09">Sequence: Assemble Upper Base</font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                                   | Quantity | Note           |
| ----------- | ------------ | ----------------------------------------------------------- | -------- | -------------- |
| FN-7        | 411-00492-01 | Bracket, Chassis Back Riser, Jaeger                         | 1        |                |
| FN-8        | 411-00493-01 | Bracket, Chassis Front Riser, Jaeger                        | 2        |                |
| FN-17       | 411-00503-01 | Bracket, Handle Support, Jaeger                             | 2        |                |
| FN-18       | 411-00504-01 | Bracket, Left Handle, Jaeger                                | 1        |                |
| FN-19       | 411-00505-01 | Bracket, Right Handle, Jaeger                               | 1        |                |
| FN-20       | 411-00506-01 | Bracket, Base Hook, Jaeger                                  | 1        |                |
| FN-24       | 412-00193-01 | Base Plate, Tower, Jaeger                                   | 1        |                |
| FN-33       | 442-00575-01 | Hooks                                                       | 2        | From Tower BOM |
| FN-45       | 442-00576-01 | Cable Clamp, Screw Mount 0.203" Dia, Black Nylon, 0.875" ID | 1        |                |
| FN-46       | 442-00577-01 | Cable Clamp, 0.172" Dia, Black Nylon, 0.625" ID             | 1        |                |

### Fasteners

| BOM Find No | Part Number  | Description                                         | Quantity | Where Used? |
| ----------- | ------------ | --------------------------------------------------- | -------- | ----------- |
| FN-59       | 446-00370-10 | Screw, M5x10mm, Socket Head, Hex, Zn                | 4        |             |
| FN-63       | 446-00378-10 | Screw, M4x10mm, Socket Head, Hex, Zinc Plated Steel | 10       |             |
| FN-57       | 446-00326-10 | Screw, M4x10mm, Flat Head, Hex, Zn                  | 4        |             |
| FN-65       | 446-00403-10 | Screw, M3.5X10, Button Head, Hex Drive, SS          | 4        |             |
| FN-60       | 446-00370-10 | Screw, M5x10mm, Socket Head, Hex, Zn                | 16       |             |

### Tools

| Tool Name                   | Note                        |
| --------------------------- | --------------------------- |
| Battery powered screwdriver |                             |
| H4 hex bit                  | For FN-59, FN-60            |
| H3 hex bit                  | For FN-63, FN-57            |
| H2 hex bit                  | For FN-65                   |
| Snips                       | For cutting edge protection |
| Scissors                    | For cutting gaffer tape    |
| Xacto knife                 | For trimming gaffer tape    |

### Instructions

- <input type="checkbox" /> [Install (2) FN-17 brackets to the base using (4) FN-60 fasteners](img/base-fn17.png)
- <input type="checkbox" /> [Get FN-24 plate, (2) FN-8 brackets, (1) FN-7 bracket, and (10) FN-63 screws](img/base-plateassy.png)
- <input type="checkbox" /> Install the FN-7 and FN-8 brackets to the plate.
- <input type="checkbox" /> [Install FN-20 bracket to FN-24 plate using (2) FN-60 fasteners](img/base-basehook.png)
- <input type="checkbox" /> Install (2) FN-33 hooks (from Tower BOM) to FN-20 bracket using (4) FN-65 screws.
- <input type="checkbox" /> [Install FN-45 clamp to FN-24 plate using (1) FN-63 fastener](img/base-clamp.png)
- <input type="checkbox" /> [Install FN-46 clamp to FN-24 plate using (1) FN-63 fastener](img/base-clamp.png)
- <input type="checkbox" /> [Install the (2) FN-8 front risers to the base using (8) FN-63 fasteners](img/base-risers.png)
- <input type="checkbox" /> [Install FN-7 back riser the base using (4) FN-57 fasteners.](img/base-backriser.png)
- <input type="checkbox" /> [Install FN-18 and FN-19 brackets using (8) FN-60 fasteners.](img/base-handlebracket.png)
- <input type="checkbox" /> [Install edge protection (2) places on FN-18 and FN-19.](img/base-protec.png)
- <input type="checkbox" /> Route hub motor cables through the base cut-out.
- <input type="checkbox" /> [Apply a 5.5" width of gaffer tape as shown.](img/base-gaffer-tape.png)
    - Acceptance criteria:  No overlaps allowed.

---

## <font color="#e36c09">Sequence: E-Stop and Safety Interlock</font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                           | Quantity | Note |
| ----------- | ------------ | ----------------------------------- | -------- | ---- | 
| FN-7        | 411-00492-01 | Bracket, Chassis Back Riser, Jaeger | 1        |      |
| FN-16       | 411-00502-01 | Bracket, Estop, Jaeger              | 1        |      |
| FN-36       | 235-00131-01 | SWITCH, PUSHBUTTON, E-STOP, 22mm    | 1        |      |
| FN-71       | 235-00136-01 | Safety interlock switch             | 1        |      |
| FN-112      | 810-00419-01 | Cable Assy, ESTOP & Kill Switch     | 1        |      |

### Fasteners

| BOM Find No | Part Number  | Description                                         | Quantity | Where Used?            |
| ----------- | ------------ | --------------------------------------------------- | -------- | ---------------------- |
| FN-63       | 446-00378-10 | Screw, M4x10mm, Socket Head, Hex, Zinc Plated Steel | 4        | FN-16 bracket          |
| FN-62       | 446-00375-35 | Screw, M4x35mm, Button Head, Hex, Zinc Plated Steel | 2        | FN-71 safety interlock |

### Tools

| Tool Name                   | Note                               |
| --------------------------- | ---------------------------------- |
| Screwdriver with H3 hex bit | For FN-62, FN-63 fasteners         |
| Phillips screwdriver        | For safety interlock switch screws |

### Instructions

- <input type="checkbox" /> [Get the FN-36 E-stop switch, FN-16 E-stop bracket, and the Wake Button Cable Assy.](img/base-estop-assy.png)
- <input type="checkbox" /> Install the Wake Button Cable Assy
    - Reference routing for Wake Button Cable Assy:
        - [View `1`](img/base-wake-button-view-1.png)
        - [View `2`](img/base-wake-button-view-2.png)
- <input type="checkbox" /> Get an FN-112 E-stop and Kill Switch cable assembly.  Install the lugs to the E-Stop Switch (2) places.
- <input type="checkbox" /> [Install the E-Stop switch to the FN-16 bracket](img/base-estop-to-bracket.png).
- <input type="checkbox" /> Install the FN-16 bracket to the base plate using (4) FN-63 fasteners.
    - Reference routing for E-stop and Kill Switch cable assembly:
        - [View `1`](img/base-e-stop-routing.png)
- <input type="checkbox" /> [Get FN-71 safety interlock and open up the door.](img/base-opendoor.png)
- <input type="checkbox" /> [Terminate the `green` wire  to Point 11 and the `yellow/green` wire to Point 12 of the safety interlock.](img/base-interlockwiring.png)
- <input type="checkbox" /> Close the door of the FN-71 safety interlock switch.
- <input type="checkbox" /> [Secure the safety interlock switch to the FN-7 back riser using (2) FN-62 fasteners.](img/base-secure-interlock.png)
- <input type="checkbox" /> [Ensure the kill switch tab is located at the top, not the side as shown](img/base-kill-switch-tab.png)

---

## <font color="#e36c09">Sequence: Complete Distribution PCB-A</font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                  | Quantity |
| ----------- | ------------ | -------------------------- | -------- |
| FN-4        | 820-00509-01 | PCBA, Distribution, Jaeger | 1        |
| FN-101      | 810-00321-02 | Cable Assy, B3CM Power     | 1        |
| FN-103      | 810-00386-01 | Cable Assy, CMC, Jaeger    | 1        |
| FN-104      | 810-00389-01 | Cable Assy, DBPMMC CAN     | 1        |
| FN-106      | 810-00391-01 | Cable Assy, DBPMMC Power   | 1        |
| FN-109      | 810-00395-01 | Cable Assy, Battery Power & Data | 1 |
| FN-110      | 810-00418-01 | Motor Encoder Cable, Left  | 1        |
| FN-111      | 810-00418-02 | Motor Encoder Cable, Right | 1        |

### Fasteners

| BOM Find No | Part Number  | Description                          | Quantity | Where Used?      |
| ----------- | ------------ | ------------------------------------ | -------- | ---------------- |
| FN-50       | 444-00163-01 | Nut, M4x0.7, Nylon Insert Locknut    | 1        | Battery Terminal |
| FN-51       | 444-00174-01 | Nut, M5x0.8, Nylon Insert Locknut    | 1        | Battery Terminal |
| FN-55       | 446-00127-01 | Screw, M3x6 mm SHC                   | 8        | Distribution PCB-A mounting |
| FN-60       | 446-00370-10 | Screw, M5x10mm, Socket Head, Hex, Zn | 1        | Chassis ground   |

### Tools

| Tool Name                   | Note                            |
| --------------------------- | ------------------------------- |
| Battery-powered screwdriver | H2.5 hex bit                    |
| Extension                   | For clearance when installing PCB-A |
| Latex glove                 | To retain screws during install |
| 8mm socket and extension    | for Battery terminal            |
| 10mm socket and extension   | for Battery terminal            |
| H2.5 hex bit                | For FN-55 fasteners
| H4 hex bit                  | For FN-60 fasteners             |

### Instructions

- <input type="checkbox" /> Get FN-4 Distribution PCB-A.
- <input type="checkbox" /> Get FN-110 and FN-111 motor encoder cables and pre-install onto board.
- <input type="checkbox" /> Install the battery terminal to the corresponding post on the Distribution PCB-A using an FN-50 nut.
- <input type="checkbox" /> Install the battery terminal to the corresponding post on the Distribution PCB-A using an FN-51 nut.
- <input type="checkbox" /> Using a ziptie, tie the + and - cables together to prevent interference with fuses.
- <input type="checkbox" /> Connect FN-109 (810-00395-01 battery power and data connector) to Distribution PCB-A J17.
- <input type="checkbox" /> Connect FN-106 (810-00391-01 DBPMMC Power cable assy) to the Distribution PCB-A J2.
- <input type="checkbox" /> Obtain FN-103 (CMC cable assy) and connect main harness to B3CM.
- <input type="checkbox" /> Connect CMC cable end to J7 of Distribution PCB-A.
- <input type="checkbox" /> Connect CMC cable end to J21 of Distribution PCB-A.
- <input type="checkbox" /> Connect CMC cable end to chassis ground using an FN-60 screw.
- <input type="checkbox" /> Connect CMC cable end to 810-00394-01 speaker cable.
- <input type="checkbox" /> Connect FN-104 (810-00389-01 DBPMMC CAN cable assy) to Distribution PCB-A J6.
- <input type="checkbox" /> Connect FN-101 (810-00321-02 B3CM power cable) to Distribution PCB-A J5
- <input type="checkbox" /> Locate and secure the FN-4 Distribution PCB-A using (8) FN-55 screws.
    - Pro-tip: Use a latex glove segment to retain the screws 

---

## <font color="#e36c09">Sequence: Complete DD-TCM</font>

```
Estimated time to complete:
```

### Parts

| BOM Find No | Part Number  | Part Name                                             | Quantity | Note |
| ----------- | ------------ | ----------------------------------------------------- | -------- | ---- |
| FN-10       | 411-00495-01 | Plate, DDTCM, Jaeger                                  | 1 | |
| FN-21       | 411-00507-01 | Bracket, Base Snap-in Catch, Jaeger                   | 1 | |
| FN-106      | 810-00391-01 | Cable Assy, DBPMMC Power, Jaeger                      | 1 | |
| FN-107      | 810-00392-01 | Cable Assy, Wake Button, Jaeger                       | 1 | | 
| FN-110      | 810-00418-01 | Cable Assy, Left Motor Encoder, DBPMMC to Controller  | 1 | |
| FN-111      | 810-00418-02 | Cable Assy, Right Motor Encoder, DBPMMC to Controller | 1 | |
| FN-112      | 810-00419-01 | Cable Assy, Interconnect ESTOP & Kill Switch          | 1 | |

### Fasteners

| BOM Find No | Part Number  | Description                                         | Quantity | Where Used?                     |
| ----------- | ------------ | --------------------------------------------------- | -------- | ------------------------------- |
| FN-60       | 446-00370-10 | Screw, M5x10mm, Socket Head, Hex, Zn                | 8        | Cable encoder terminals, DD-TCM |
| FN-63       | 446-00378-10 | Screw, M4x10mm, Socket Head, Hex, Zinc Plated Steel | 2        | FN-10                           |
| FN-51       | 444-00174-01 | Nut, M5x0.8, Nylon Insert Locknut, Zn               | 2        | DD-TCM                          |

### Tools

| Tool Name  | Note                |
| ---------- | ------------------- |
| H3 hex bit | For FN-63 fasteners |
| H4 hex bit | For FN-60 fasteners |
| 8mm socket | For FN-51 nuts      |

### Instructions

- <input type="checkbox" /> [Get FN-10 base plate for DD-TCM install to base using (2) FN-63 fasteners.](img/base-ddtcm.png)
- <input type="checkbox" /> [Install FN-3 DD-TCM using (2) FN-51 nuts.](img/base-ddtcm-install.png)
- <input type="checkbox" /> Connect right motor encoder cable terminals to the DD-TCM using (3) FN-60 fasteners.
    - Note: Maintain the following order: `Blue --> W, Green --> V, Yellow --> U`
        - [View `1`](img/base-right-motor-encoder-ddtcm.png)
- <input type="checkbox" /> Connect left motor cable encoder terminals to the DD-TCM using (3) FN-60 fasteners.
    - Note:  Maintain the following order:  `Blue --> W, Green --> V, Yellow --> U`
        - [View `1`](img/base-left-motor-encoder-ddtcm.png)
- <input type="checkbox" /> Connect FN-110 (810-00418-01 Cable Assy, Right Motor Encoder) to DD-TCM J9.
- <input type="checkbox" /> Connect FN-111 (810-00418-02 Cable Assy, Right Motor Encoder) to DD-TCM J10.
- <input type="checkbox" /> Connect FN-106 (810-00391-01 DBPMMC Power) to DD-TCM B+ and to DDTCM B-  using (2) FN-60 fasteners.
    - [View `1`](img/base-ddtcm-power.png)
- <input type="checkbox" /> Connect end of FN-103 (810-00389-01 DBPMMC CAN) to DD-TCM J14.
- <input type="checkbox" /> Connect end of FN-105 (810-00390-01 DBPMMC IO) to DD-TCM J21.
- <input type="checkbox" /> Connect FN-107 (810-00392-01 Wake Button Cable Assy) to Distribution PCB-A J16.
    - Reference routing for Wake Button Cable Assy:
        - [View `1`](img/base-wake-button-view-1.png)
        - [View `2`](img/base-wake-button-view-2.png)
- <input type="checkbox" /> Connect FN-102 (810-00332-02, ESTOP Switch Cable Assy) to Distribution PCB-A J3.
- <input type="checkbox" /> [Install FN-21 snap-in catch bracket using (4) FN-60 fasteners.](img/base-snapincatch.png)
- <input type="checkbox" /> [Install push-to-close latch into FN-21 bracket](img/base-catchlatch.png).
- <input type="checkbox" /> Ensure all cables are neat and routed per below reference pictures:
- See pictures for cable routing reference: 
    - [View `1`](img/base-routing-view-1.jpg)
    - [View `2`](img/base-routing-view-2.jpg)
    - [View `3`](img/base-routing-view-3.jpg)
    - [View `4`](img/base-routing-view-4.jpg)
    - [View `5`](img/base-routing-view-5.jpg)

## <font color="#e36c09">Final Quality Check - Base Assembly</font>

>> Owner(s): Maliyah Thompson  

## <font color="#e36c09">Special Rework Instructions</font>

**ZLTech Motor Rework:**

1. Cut back sheathing by 2.5in
2. Loosen heat shrink tube already on cable and move it to cover the newly cut section
3. Apply heat to shrink tube to cover newly cut section
4. Crimp ring terminals on motor phase wires
5. Label motor phase wires (U,V and W)
