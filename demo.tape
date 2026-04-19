# VHS Tape for omniget-cli demo
# https://github.com/charmbracelet/vhs

Output demo.gif

Set Shell "powershell"
Set FontSize 18
Set Width 1000
Set Height 650
Set Theme "Catppuccin Macchiato"
Set Padding 30
Set TypingSpeed 50ms

# Title
Type "# OmniGet CLI v0.1.1-fix — Universal Media Downloader"
Enter
Sleep 1.5s

# 1. Show Help
Type "omniget-cli --help"
Enter
Sleep 4s

# 2. Show Version (About)
Type "omniget-cli about version"
Enter
Sleep 2s

# 3. Download Example (Video)
Type "omniget-cli download https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Enter
Sleep 6s

# 4. Download Example (Audio Only)
Type "omniget-cli download --audio-only https://www.youtube.com/watch?v=5qap5aO4i9A"
Enter
Sleep 6s

# 5. Show configuration
Type "omniget-cli config list"
Enter
Sleep 3s

# Closing message
Type "# Done. One tool, all platforms."
Enter
Sleep 2s
