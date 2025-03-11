import secrets
import time
import sys

def print_colored(text, color):
    """Fungsi untuk mencetak teks dengan warna tertentu."""
    colors = {
        "blue": "\033[94m",
        "green": "\033[92m",
        "red": "\033[91m",
        "end": "\033[0m"
    }
    print(f"{colors[color]}{text}{colors['end']}", end="", flush=True)

def loading_animation():
    """Animasi loading sederhana."""
    for _ in range(3):  # Ulangi 3 kali
        for char in "|/-\\":
            print("\rLoading " + char, end="", flush=True)
            time.sleep(0.1)
    print("\rLoading selesai!", flush=True)

def main():
    # Tampilkan animasi loading
    loading_animation()

    # Generate string heksadesimal acak (32 byte = 64 karakter)
    random_hex = secrets.token_hex(32)

    # Tampilkan hasil dengan animasi warna
    print("\nHasil string heksadesimal acak:")
    for i, char in enumerate(random_hex):
        if i % 3 == 0:
            print_colored(char, "blue")
        elif i % 3 == 1:
            print_colored(char, "green")
        else:
            print_colored(char, "red")
        time.sleep(0.02)  # Delay untuk efek animasi
        sys.stdout.flush()  # Pastikan output langsung terlihat

    print("\n\nSelesai!")

if __name__ == "__main__":
    main()