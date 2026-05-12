"""Command-line interface for imas-ambix."""

import click


@click.group()
@click.version_option()
def main() -> None:
    """Ambix — Fusion World Model training framework."""


@main.command()
def status() -> None:
    """Show training pipeline status."""
    click.echo("⚗️  ambix: no active training runs")
