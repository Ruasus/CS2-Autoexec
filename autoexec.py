#+----------------------------------------------------------------------+#
#|                                                                      |#
#|                               AUTOEXEC                               |#
#|                            Made by Ruasus                            |#
#|                                                                      |#
#|                DISCORD: https://discord.gg/TBFrXRKzAb                |#
#|      BUG REPORTS: https://github.com/Ruasus/CS2-Autoexec/issues      |#
#|                                                                      |#
#+----------------------------------------------------------------------+#

import sys
from pathlib import Path



def parse_kv(line: str):
  parts = line.split("\"")
  return (parts[1], parts[3]) if len(parts) >= 4 else (None, None)

def main(steam_path: Path, convars_allows, udc: Path):
  lines = []
  #   CONVARS   #
  for file in [udc / "cs2_machine_convars.vcfg", udc / "cs2_user_convars_0_slot0.vcfg"]:
    if not file.exists():
      print(f"[WARN] Skipped: {file} does not exist. The generated autoexec.cfg may be incomplete and not fully reflect your in-game settings.")
      continue
    convars = False
    for line in file.read_text(encoding = "utf-8").splitlines():
      line = line.strip()
      if line == "{":
        continue
      if line == "\"convars\"":
        convars = True
        continue
      if convars and "\"" in line:
        key, value = parse_kv(line)
        if not key:
          continue
        if not "$" in key and any(key.startswith(prefix) for prefix in convars_allows):
          lines.append(f"{key} \"{value}\"")
        continue
      if line.startswith("}") and convars:
        convars = False
  #   KEYS   #
  sac = steam_path / r"steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg"
  uk = udc / "cs2_user_keys_0_slot0.vcfg"
  if uk.exists():
    defaults = {}
    bindings = False
    analogbindings = False
    for line in (sac / "user_keys_default.vcfg").read_text(encoding = "utf-8").splitlines():
      line = line.strip()
      if line == "{":
        continue
      if line == "\"bindings\"":
        bindings = True
        continue
      if line == "\"analogbindings\"":
        analogbindings = True
        continue
      if bindings and not analogbindings and "\"" in line:
        key, value = parse_kv(line)
        defaults[key] = value
        continue
      if line.startswith("}") and bindings:
        if analogbindings:
          analogbindings = False
        else:
          bindings = False
    bindings = False
    analogbindings = False
    for line in uk.read_text(encoding = "utf-8").splitlines():
      line = line.strip()
      if line == "{":
        continue
      if line == "\"bindings\"":
        bindings = True
        continue
      if line == "\"analogbindings\"":
        analogbindings = True
        continue
      if bindings and not analogbindings and "\"" in line:
        key, value = parse_kv(line)
        if key in defaults and defaults[key] == value:
          continue
        if value == "<unbound>":
          lines.append(f"unbind \"{key}\"")
        else:
          lines.append(f"bind \"{key}\" \"{value}\"")
        continue
      if line.startswith("}") and bindings:
        if analogbindings:
          analogbindings = False
        else:
          bindings = False
  else:
    print(f"[WARN] Skipped: {uk} does not exist. The generated autoexec.cfg may be incomplete and not fully reflect your in-game settings.")
      
  #   SAVE   #
  (steam_path / r"steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg\autoexec.cfg").write_text("\n".join(lines), encoding = "utf-8")
  print("[DONE] autoexec.cfg generated successfully.")



if __name__ == "__main__":
  #   Nếu bạn biết code Python, bạn có thể chỉnh sửa trực tiếp chỗ này. Có thể chỉnh convars_allows theo nhu cầu   #
  #   If you're familiar with Python, you can modify this file directly. Feel free to adjust convars_allows as needed   #
  CONVARS_ALLOWS = [
    "cl_crosshair",
    "cl_debounce_zoom",
    "cl_hud_color",
    "cl_prefer_lefthanded",
    "cl_radar",
    "cl_showloadout",
    "cl_silencer_mode",
    "cl_sniper_auto_rezoom",
    "cl_use_opens_buy_menu",
    "fps_max",
    "fps_max_tools",
    "hud_",
    "m_",
    "rate",
    "sensitivity",
    "snd_gamevolume",
    "snd_headphone_eq",
    "snd_mute_losefocus",
    "snd_voipvolume",
    "viewmodel_",
    "volume",
    "zoom_sensitivity_ratio",
  ]
  STEAM_PATH: Path = None
  UDC: Path = None
  if STEAM_PATH is None or UDC is None:
    if len(sys.argv) >= 3:
      STEAM_PATH = Path(sys.argv[1])
      UDC = STEAM_PATH / fr"userdata\{sys.argv[2]}\730\local\cfg"
      if UDC.exists():
        main(STEAM_PATH, CONVARS_ALLOWS, UDC)
      else:
        print(f"{UDC} does not exist.")
    else:
      while True:
        STEAM_PATH = Path(input("- Enter your Steam path: ").strip())
        if STEAM_PATH.exists():
          break
        else:
          print(f"{STEAM_PATH} does not exist.")
      while True:
        UDC = Path(STEAM_PATH / fr"userdata\{input("- Enter your SteamID32: ").strip()}\730\local\cfg")
        if UDC.exists():
          main(STEAM_PATH, CONVARS_ALLOWS, UDC)
          break
        else:
          print(f"{UDC} does not exist.")
