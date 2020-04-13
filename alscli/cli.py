# -*- coding: utf-8 -*-

"""Console script for alscli."""

import logging
import sys

import click

from .alscli import parse_als


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('-l', '--loglevel', help='Logging level')
@click.pass_context
def cli(ctx, debug, loglevel):
    ctx.obj['DEBUG'] = debug
    if loglevel is not None:
        loglevel = getattr(logging, loglevel.upper(), None)
    else:
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel)


@cli.command()
@click.pass_context
@click.argument('als_path')
def list_plugins(ctx, als_path):
    root = parse_als(als_path)
    plugin_nodes = root.findall('.//PluginDevice')
    plugin_names = set()
    for plugin_node in plugin_nodes:
        plugin_name = plugin_node.find('.//PlugName').attrib['Value']
        plugin_names.add(plugin_name)
    for plugin_name in sorted(plugin_names):
        click.echo(plugin_name)
    return 0


def main():
    sys.exit(cli(obj={}))


if __name__ == '__main__':
    main()
