# -*- coding: utf-8 -*-

"""Console script for alscli."""

import xml.etree.cElementTree as etree
import logging
import sys

import click

from .alscli import (
    extract_als,
    parse_als,
)


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
        pname_node = plugin_node.find('.//PlugName')
        if pname_node is None:
            pname_node = plugin_node.find('.//Name')
        plugin_name = pname_node.attrib['Value']
        if plugin_name:
            plugin_names.add(plugin_name)
    for plugin_name in sorted(plugin_names):
        click.echo(plugin_name)
    return 0


@cli.command()
@click.pass_context
@click.argument('als_path')
def dump(ctx, als_path):
    sys.stdout.write(extract_als(als_path).decode('utf-8'))
    return 0


def main():
    sys.exit(cli(obj={}))


if __name__ == '__main__':
    main()
