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

def add_new_menu():
    """Add a new menu"""
    name = click.prompt("Menu Name", type=str)
    menu = Menu(name)
    add_menu(menu)
    click.echo("Menu added successfully.")

def add_new_food():
    """Add a new food"""
    name = click.prompt("Food Name", type=str)
    description = click.prompt("Description", type=str)
    tags = click.prompt("Tags", type=str)
    menu_id = click.prompt("Menu ID", type=int)
    
    food = Food(name, description, tags, menu_id)
    add_food(food)
    click.echo("Food added successfully.")

def list_all_menus():
    """List all menus"""
    menus = get_all_menus()
    if menus:
        for menu in menus:
            click.echo(f"{menu}")
    else:
        click.echo("No menus found.")

def list_all_foods():
    """List all foods"""
    foods = get_all_foods()
    if foods:
        for food in foods:
            click.echo(f"{food}")
    else:
        click.echo("No foods found.")