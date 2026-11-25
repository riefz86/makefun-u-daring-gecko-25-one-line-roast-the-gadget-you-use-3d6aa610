import os

ROAST = "My robot vacuum mapped my whole house in a day, then wedged itself under the same sofa every day since, beeping for rescue like the floor plan betrayed it."

def main():
    if not (1 <= len(ROAST) <= 200):
        raise ValueError(f"roast must be 1-200 characters, got {len(ROAST)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
