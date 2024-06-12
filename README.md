# LSP-actions

GitHub Actions support for Sublime's LSP plugin. Basically a fork of [sublimelsp/LSP-yaml](https://github.com/sublimelsp/LSP-yaml).

Uses [@actions/languageserver](https://github.com/actions/languageservices) to provide validation, formatting, and other features for GitHub Actions YAML files. See the linked repository for more information.

By default, schemas are automatically retrieved from [schemastore.org](https://schemastore.org/).

## Install

1. Open the command palette and run `Package Control: Install Package`, then select [`LSP`](https://packagecontrol.io/packages/LSP)
2. Install `LSP-actions` from Package Control
3. Restart Sublime Text

## Configuration

Open the configuration file using the command palette with the `Preferences: LSP-actions Settings` command or by opening it from the Sublime menu (`Preferences > Package Settings > LSP > Servers > LSP-actions`).

## Development

Clone this repository into your `Packages` directory. Open the command palette and run `Package Control: Satisfy Dependencies.`
