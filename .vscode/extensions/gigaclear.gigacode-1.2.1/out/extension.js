"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const path_1 = __importDefault(require("path"));
const vscode = __importStar(require("vscode"));
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.encrypt_or_decrypt', (uri) => {
        if (uri && uri.fsPath) {
            // Open terminal
            let terminal_name = "Encryption";
            let terminal = vscode.window.terminals.find(term => term.name === terminal_name);
            if (!terminal) {
                // If the terminal doesn't exist, create a new one
                const customTerminalPath = vscode.workspace.getConfiguration().get('extension.customTerminalPath', vscode.env.shell);
                terminal = vscode.window.createTerminal(terminal_name, customTerminalPath);
            }
            // Get file info
            let file_path = path_1.default.parse(uri.fsPath);
            let file_name = file_path.base;
            let file_tokens_reversed = file_name.split(".").reverse();
            if (file_tokens_reversed[0] != "yaml") {
                vscode.window.showErrorMessage("Expected file formats: `*.yaml`, `*.decrypted.yaml`.  Received " + file_name);
                return;
            }
            let dir_path = file_path.dir;
            let custom_path_separator = vscode.workspace.getConfiguration().get('extension.customPathSeparator', '');
            if (custom_path_separator) {
                dir_path = dir_path.replace(/[\/\\]/g, custom_path_separator);
            }
            let cd_into_file_directory = `cd ${dir_path}`;
            let output_file = "";
            if (file_tokens_reversed[1] == "decrypted") {
                // Encrypting
                // Remove "decrypted" from filename
                file_tokens_reversed.splice(1, 1);
                output_file = file_tokens_reversed.reverse().join(".");
                terminal.sendText(cd_into_file_directory);
                terminal.sendText(`sops --encrypt --pgp D2292430F0B9D023F7A6B792A1577B94F0643A44 --input-type yaml --output-type yaml ` + file_name + ` > ` + output_file);
            }
            else {
                // Decrypting
                // Insert "decrypted" into filename
                file_tokens_reversed.splice(1, 0, "decrypted");
                output_file = file_tokens_reversed.reverse().join(".");
                terminal.sendText(cd_into_file_directory);
                terminal.sendText(`sops --decrypt --input-type yaml --output-type yaml ` + file_name + ` > ` + output_file);
            }
        }
    });
    const updateGigacodeConfig = vscode.commands.registerCommand('extension.gigacode_update_config', async () => {
        const newPath = await vscode.window.showInputBox({
            prompt: 'Enter the custom terminal path'
        });
        if (newPath !== undefined) {
            await vscode.workspace.getConfiguration().update('extension.customTerminalPath', newPath, vscode.ConfigurationTarget.Global);
        }
        const path_separator = await vscode.window.showInputBox({
            prompt: 'Enter custom file path separator'
        });
        if (path_separator !== undefined) {
            await vscode.workspace.getConfiguration().update('extension.customPathSeparator', path_separator, vscode.ConfigurationTarget.Global);
        }
    });
    context.subscriptions.push(disposable);
    context.subscriptions.push(updateGigacodeConfig);
}
exports.activate = activate;
// This method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map