import os
from rich.console import Console
from rich.panel import Panel
import dns.resolver
import string
import secrets
import hashlib

console = Console()

# Terminal Clear Function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Title Function
def title():
    print("$$$$$$$$\                               $$$$$$\   $$$$$$\  ")
    print("\____$$  |                             $$  __$$\ $$  __$$\ ")
    print("    $$  / $$$$$$\  $$$$$$$\   $$$$$$\  $$ /  $$ |$$ /  \__|")
    print("   $$  / $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |\$$$$$$\  ")
    print("  $$  /  $$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ | \____$$\ ")
    print(" $$  /   $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$\   $$ |")
    print("$$$$$$$$\\$$$$$$  |$$ |  $$ |\$$$$$$$\  $$$$$$  |\$$$$$$  |")
    print("\________|\______/ \__|  \__| \_______| \______/  \______/ ")

# Main Menu Function
def main_menu():
    while True:
        console.print(Panel("[bold cyan]Welcome To ZoneOS![/bold cyan]\n1. DNS Lookup[green]            ( ** Available ** )[/green]\n2. Port Scanner[bold red]          ( ** Not Available For Now ** )[/bold red]\n3. Subdomain Scanner[bold red]     ( ** Not Available For Now ** )[/bold red] \n4. Ping[bold red]                  ( ** Not Available For Now ** )[/bold red]\n5. Website Information[bold red]   ( ** Not Available For Now ** )[/bold red]\n6. Hash Generator[green]        ( ** Available ** )[/green]\n7. Password Generator[green]    ( ** Available ** )[/green]\nq/exit: Exit", title="Main Menu"))
        
        selection = input("Choose an option: ").lower()

        if selection == '1':
            print("\n--- DNS Lookup Module Has Been Choosed! ---\n")
            dns_lookup()
        elif selection == '2':
            print("\n--- Port Scanner Module Is Coming Soon... ---\n")
        elif selection == '3':
            print("\n--- Subdomain Scanner Module Is Coming Soon... ---\n")
        elif selection == '4':
            print("\n--- Ping Module Is Coming Soon... ---\n")
        elif selection == '5':
            print("\n--- Website Information Module Is Coming Soon... ---\n")
        elif selection == '6':
            print("\n--- Hash Generator Option Has Been Choosed! ---\n")
            hash_generator()
        elif selection == '7':
            print("\n--- Password Generation Option Has Been Choosed! ---\n")
            generate_password()
        elif selection == '8':
            print("\n--- System Information Module Is Coming Soon... ---\n")
        elif selection == 'exit' or selection == 'q':
            console.print("[bold red]Exiting from the program... See ya![/bold red]")
            break
        else:
            console.print("[yellow]Unrecognized option, try again.[/yellow]")

# DNS Lookup Function
def dns_lookup():
    clear()
    console.print("\n[bold green]--- DNS Lookup ---[/bold green]")
    domain = input("Enter the domain to lookup: (Example: google.com) ")
    if not domain:
        return
    
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            console.print(f"\n[yellow1]{record} Records:[/yellow1]")
            
            for rdata in answers:
                console.print(f" [white]>[/white] {rdata.to_text()}")

        except dns.resolver.NoAnswer:
            continue
        except dns.resolver.NXDOMAIN:
            console.print(f"\n[bold red]Error: The domain '{domain}' does not exist :)[/bold red]")
            break
        except Exception as e:
            continue

        input("\nPress Enter to continue...")

# Password Generator Function
def generate_password():
    clear()
    console.print("\n[bold green]--- Password Generator ---[/bold green]")
    try:
        length = int(input("Enter the password length (Example: 16): "))
        punctuation = input("Include punctuation? (y/n): ").lower()

        if punctuation == 'y':
            alphabet = string.ascii_letters + string.digits + string.punctuation
        else:
            alphabet = string.ascii_letters + string.digits
        
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        
        clear()
        console.print(f"\n[bold yellow]Generated Password:[/bold yellow] [white]{password}[/white]\n")
    except ValueError:
        console.print("[bold red]Error: Please enter a valid number![/bold red]")

# Hash Generator Function
def hash_generator():
    clear()
    console.print("\n[bold green]--- Hash Calculator ---[/bold green]")
    text = input("Enter the text to hash: ")

    # MD5
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    
    # SHA-1
    sha1_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    
    # SHA-256
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

    clear()
    console.print(f"\n[bold cyan]Target Text:[/bold cyan] {text}")
    console.print(f"\n[bold cyan]MD5   :[/bold cyan] {md5_hash}")
    console.print(f"[bold cyan]SHA-1 :[/bold cyan] {sha1_hash}")
    console.print(f"[bold cyan]SHA-256:[/bold cyan] {sha256_hash}\n")

if __name__ == "__main__":
    title()
    main_menu()
