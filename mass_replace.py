import os

def replace_in_file(filepath, old_str, new_str):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")


def main():
    start_dir = "src-tauri"
    old_strings = [
        "crate::platforms::traits::PlatformDownloader",
        "crate::platforms::platform::Platform",
        "rand::RngExt",
        "rand::rng().random::<u8>()",
        "rand::rng().random_range",
        "rand::rng()",
    ]
    new_strings = [
        "crate::core::traits::PlatformDownloader",
        "crate::core::traits::Platform",
        "rand::Rng",
        "rand::thread_rng().gen::<u8>()",
        "rand::thread_rng().gen_range",
        "rand::thread_rng()",
    ]
    
    for dirpath, _, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith(".rs"):
                filepath = os.path.join(dirpath, filename)
                for i in range(len(old_strings)):
                    replace_in_file(filepath, old_strings[i], new_strings[i])

if __name__ == "__main__":
    main()
