import os, subprocess, sys

# Check Cargo.lock for rapier3d
for lock in [
    r'd:\Minecraft Mod Studio\Minecraft Mod Studio\cang ku\CrossAndOut-Project-main\sable-fork\Cargo.lock',
    r'd:\Minecraft Mod Studio\Minecraft Mod Studio\cang ku\CrossAndOut-Project-main\sable-fork\common\src\main\rust\rapier\Cargo.lock',
]:
    if os.path.exists(lock):
        with open(lock) as f:
            content = f.read()
            idx = content.find('name = "rapier3d"')
            if idx >= 0:
                print("=== rapier3d in Cargo.lock ===")
                print(content[idx:idx+800])
                break

# Search for rapier3d source in cargo registry
cargo_home = os.path.join(os.environ.get('CARGO_HOME', os.path.expanduser('~/.cargo')), 'git', 'checkouts')
print(f"\n=== Cargo git checkouts: {cargo_home} ===")
if os.path.exists(cargo_home):
    for root, dirs, files in os.walk(cargo_home):
        for f in files:
            if f == 'lib.rs' and 'collider' in root.lower():
                path = os.path.join(root, f)
                print(f"Found: {path}")
                with open(path) as fh:
                    content = fh.read()
                    if 'set_scale' in content or 'pub scale' in content or 'fn scale' in content:
                        idx = content.find('pub fn set_scale') if 'set_scale' in content else content.find('pub scale')
                        print(content[max(0,idx-50):idx+200])
                        print("---")
else:
    print("No cargo git checkouts found")
