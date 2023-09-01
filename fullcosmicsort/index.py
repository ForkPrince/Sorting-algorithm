import random
from itertools import permutations
import time
from rich.console import Console
from rich.progress import Progress

console = Console()

def cosmic_sort(arr):
    all_permutations = permutations(arr)
    perms_list = list(all_permutations)

    for i in perms_list:
        create_universe()
        simulate_war()
        simulate_cosmic_sorting(arr)
        extract_sorted_data(list(range(4)))
        if is_sorted(i):
            return i


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i +  1]:
            return False
    return True

def create_universe():
    console.print("[bold green]Initializing the universe...[/bold green]")
    time.sleep(1)

def simulate_war():
    console.print("[bold red]Simulating a war in the universe...[/bold red]")
    time.sleep(2)
    war_intensity = random.uniform(0, 1)

    if war_intensity < 0.3:
        console.print("[bold red]The war is intense![/bold red]")
    elif war_intensity < 0.7:
        console.print("[bold yellow]The war is moderately intense.[/bold yellow]")
    else:
        console.print("[bold green]The war is not intense.[/bold green]")

    time.sleep(1)

def simulate_cosmic_sorting(arr):
    universe = {}
    with Progress() as progress:
        task = progress.add_task("[cyan]Performing cosmic shuffling and sorting...", total=len(arr))

        for i in range(len(arr)):
            universe[arr[i]] = random.uniform(0, 1e30)
            progress.update(task, advance=1)
            time.sleep(0.1)

        progress.stop()

        task = progress.add_task("[cyan]Cosmic convergence...", total=len(arr))
        for i in range(len(arr)):
            universe[arr[i]] = random.uniform(0, 1e30)
            progress.update(task, advance=1)
            time.sleep(0.1)

        progress.stop()

        task = progress.add_task("[cyan]Cosmic frustration detected! Stars explode![/cyan]", total=len(arr))
        for i in range(len(arr)):
            universe[arr[i]] = random.uniform(0, 1e30)
            if random.random() < 0.05:
                progress.stop()
                console.print("[bold red]Cosmic frustration detected! Stars explode![/bold red]")
                time.sleep(1)
                progress.start()
            progress.update(task, advance=1)
            time.sleep(0.1)

        progress.stop()

        task = progress.add_task("[cyan]Stars aligning...", total=len(arr))
        for i in range(len(arr)):
            universe[arr[i]] = random.uniform(0, 1e30)
            progress.update(task, advance=1)
            time.sleep(0.1)

        progress.stop()


def extract_sorted_data(universe):
    with Progress() as progress:
        task = progress.add_task("[green]Extracting sorted data from the universe...", total=len(universe))
        # sorted_data = sorted(universe.keys(), key=lambda star: universe[star])
        progress.update(task, completed=len(universe))
        progress.stop()

        with Progress() as sub_progress:
            sub_task = sub_progress.add_task("[cyan]Extracting stars...", total=len(universe))
            for i in range(len(universe)):
                sub_progress.update(sub_task, advance=1)
                time.sleep(0.1)

if __name__ == "__main__":
    size = input("Array size? ")
    unsorted_array = list(range(int(size)))
    random.shuffle(unsorted_array)
    best_sorted_data = cosmic_sort(unsorted_array)
    console.print("\n[bold green]Best sorted data:[/bold green]\n", best_sorted_data)
