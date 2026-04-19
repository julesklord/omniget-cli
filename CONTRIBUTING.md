# Contributing to OmniGet CLI

Thanks for taking the time to contribute.

## Prerequisites

- [Rust](https://rustup.rs/) 1.70+ (stable toolchain)
- [Git](https://git-scm.com/)

No Node.js, pnpm, or frontend tooling is required for CLI development.

## Building the CLI

```bash
git clone https://github.com/julesklord/omniget-cli.git
cd omniget-cli
cargo build -p omniget-cli
```

Run the CLI directly during development:

```bash
cargo run -p omniget-cli -- --help
cargo run -p omniget-cli -- check
cargo run -p omniget-cli -- download https://example.com/video
```

Build a release binary:

```bash
cargo build -p omniget-cli --release
```

The binary will be at `src-tauri/target/release/omniget-cli` (or `omniget-cli.exe` on Windows).

## Project structure

```
src-tauri/
├── omniget-cli/        # CLI binary crate (clap + indicatif)
│   └── src/
│       ├── main.rs     # Command definitions and dispatch
│       └── reporter.rs # CLI progress bar reporter
├── omniget-core/       # Shared library crate
│   └── src/
│       ├── core/       # Download engine, dependencies, HTTP client, yt-dlp integration
│       │   ├── manager/    # Queue, recovery, download log
│       │   ├── traits.rs   # DownloadReporter trait
│       │   └── ...
│       └── models/     # Data structures (queue items, settings)
└── omniget-lib/        # Platform implementations (YouTube, Instagram, etc.)
```

## Before opening a pull request

Run these checks locally:

```bash
cd src-tauri
cargo fmt --all
cargo clippy --workspace --all-targets
cargo test --workspace
```

All three must pass cleanly before submitting.

## What to work on

- **Bug fixes**: If you find a bug, open an issue first, then submit a fix.
- **New platforms**: Add a new downloader in `src-tauri/omniget-lib/src/platforms/` implementing the `PlatformDownloader` trait.
- **Core improvements**: Enhancements to the download queue, progress reporting, or dependency management in `omniget-core`.
- **Documentation**: Improvements to README, inline docs, or usage examples.

## Commit style

Follow [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`. Keep the subject under 72 characters.

## Security issues

Do not file public issues for security problems. See [SECURITY.md](SECURITY.md).

## License

By contributing you agree that your changes are licensed under [GPL-3.0](LICENSE).
