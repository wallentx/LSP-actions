from __future__ import annotations

import os
from lsp_utils import NpmClientHandler, ClientConfig
from sublime_plugin import WindowCommand
from typing import Optional, Dict, Any, List

def plugin_loaded() -> None:
    LspActionsPlugin.setup()

def plugin_unloaded() -> None:
    LspActionsPlugin.cleanup()

class LspActionsPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = "language-server"
    server_binary_path = os.path.join(
        server_directory,
        "dist",
        "cli.js"
    )

    @classmethod
    def on_pre_start(
        cls,
        window: sublime.Window,
        initiating_view: sublime.View,
        workspace_folders: List[Dict[str, Any]],
        configuration: ClientConfig
    ) -> Optional[ClientConfig]:
        if not configuration:
            return None

        configuration.command = ["npx", "tsx", cls.server_binary_path, "--stdio"]
        print("Executing command:", configuration.command)
        print("Server binary path:", cls.server_binary_path)
        return configuration
