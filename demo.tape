# VHS Tape for omniget-cli demo
# https://github.com/charmbracelet/vhs

Output demo.gif

Set Shell "powershell"
Set FontSize 14
Set Width 900
Set Height 500
Set Theme "Dracula"
Set Padding 20
Set TypingSpeed 40ms

# Title
Type "# OmniGet CLI v0.1.0 — Demo"
Enter
Sleep 1s

# Show help
Type "cargo run -p omniget-cli -- --help"
Enter
Sleep 3s

# Check dependencies
Type "cargo run -p omniget-cli -- check"
Enter
Sleep 5s

# Show version info
Type "cargo run -p omniget-cli -- about version"
Enter
Sleep 2s

# Config list
Type "cargo run -p omniget-cli -- config list"
Enter
Sleep 3s

# Info command (inspect a URL)
Type "cargo run -p omniget-cli -- info https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Enter
Sleep 8s

# Show roadmap
Type "cargo run -p omniget-cli -- about roadmap"
Enter
Sleep 2s

# Closing
Type "# omniget-cli — Paste a link. Get your file."
Enter
Sleep 2s
