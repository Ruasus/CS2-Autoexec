# CS2-Autoexec

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Game](https://img.shields.io/badge/Game-Counter--Strike%202-orange)

> Tired of managing multiple Counter-Strike 2 accounts and struggling to keep settings in sync?  
> **CS2-Autoexec** lets you export a master account's CS2 settings and instantly share them across all your accounts — no more manual copying.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1 — Prepare your master account](#step-1--prepare-your-master-account)
  - [Step 2 — Run the tool](#step-2--run-the-tool)
  - [Step 3 — Apply to other accounts](#step-3--apply-to-other-accounts)
- [Output](#output)
- [License](#license)

---

## Features

- 🎯 Export **convars** (crosshair, HUD, radar, sensitivity, volume, etc.) from a master account
- ⌨️ Export and sync **keybindings** across multiple accounts
- ⚙️ Auto-generates a ready-to-use `autoexec.cfg`
- 🪶 Minimal setup — fully Python-based, no external dependencies

---

## Requirements

| Requirement | Details |
|---|---|
| Python | 3.6 or higher |
| OS | Windows |
| Steam | Access to your `userdata` folder for CS2 accounts |

---

## Installation

**Option A — Clone with Git:**

```bash
git clone https://github.com/Ruasus/CS2-Autoexec.git
cd CS2-Autoexec
```

**Option B — Download ZIP:**

Download the project as a ZIP from GitHub, extract it, and open the extracted folder.

---

## Usage

### Step 1 — Prepare your master account

Launch CS2 on your **master account**, then open the in-game console and run:

```
host_writeconfig
```

This saves all your current settings to disk so the tool can read them.

---

### Step 2 — Run the tool

You can run the script in three ways:

#### 1. Command-line mode

Pass your Steam path and SteamID32 directly as arguments:

```bash
python autoexec.py "STEAM_PATH" SteamID32
```

**Example:**

```bash
python autoexec.py "D:\Steam" 898215518824185888
```

#### 2. Interactive mode

Run without arguments and the script will guide you step by step:

```bash
python autoexec.py
```

You will be prompted to enter your `STEAM_PATH` and `SteamID32` interactively.

#### 3. Dev mode

If you're comfortable with Python, you can hardcode `STEAM_PATH` and `UDC` directly in the source file. This mode also lets you customize the `CONVARS_ALLOWS` list to control which convars are exported.

---

### Step 3 — Apply to other accounts

Launch CS2 on each of your **other accounts**, open the console, and run:

```
exec autoexec.cfg
```

Your master settings will be applied instantly.

---

## Output

The generated config file is saved to:

```
<STEAM_PATH>\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg
```

---

## License

This project is licensed under the [MIT License](LICENSE).
