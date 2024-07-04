import click
from helpers import (
    create_tables,
    add_menu,
    add_food,
    get_all_menus,
    get_all_foods,
    find_foods_by_tag,
    delete_food,
    update_food
)
from models import Menu, Food

@click.group()
def cli():
    """ Menu CLI """
    create_tables()

@cli.command()
def menu():
    """Display main menu"""
    while True:
        click.echo("\nPlease select an option:")
        click.echo("1. Add a new menu")
        click.echo("2. Add a new food")
        click.echo("3. List all menus")
        click.echo("4. List all foods")
        click.echo("5. Find foods by tag")
        click.echo("6. Delete a food")
        click.echo("7. Update a food")
        click.echo("0. Exit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 0:
            click.echo("Exiting program. Goodbye!")
            break
        elif choice == 1:
            add_new_menu()
        elif choice == 2:
            add_new_food()
        elif choice == 3:
            list_all_menus()
        elif choice == 4:
            list_all_foods()
        elif choice == 5:
            find_foods()
        elif choice == 6:
            delete_food_entry()
        elif choice == 7:
            update_food_entry()
        else:
            click.echo("Invalid choice. Please select a valid option.")
