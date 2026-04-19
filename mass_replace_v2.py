import os
import re

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

def regex_replace_in_file(filepath, pattern, new_str):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, count = re.subn(pattern, new_str, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated (regex): {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")


def main():
    start_dir = "src-tauri"
    
    # First, fix all the trait paths.
    # The script was correct, but my diagnosis was wrong. The traits are in a SUBMODULE now.
    regex_pattern = r'use crate::platforms::traits::(\w+);'
    replacement = r'use crate::core::traits::\1;'

    for dirpath, _, filenames in os.walk(os.path.join(start_dir, "omniget-core", "src")):
        for filename in filenames:
            if filename.endswith(".rs"):
                filepath = os.path.join(dirpath, filename)
                regex_replace_in_file(filepath, regex_pattern, replacement)

    # Now fix instagram specific issues
    insta_path = os.path.join(start_dir, "omniget-core", "src", "platforms", "instagram", "mod.rs")
    replace_in_file(insta_path, 
        'use crate::core::traits::PlatformDownloader;', 
        'use crate::core::traits::PlatformDownloader;\nuse crate::core::direct_downloader;')
    
    # Fix the missing `html` variable
    with open(insta_path, 'r', encoding='utf-8') as f:
        insta_content = f.read()

    # This is complex, need to add the html variable to multiple functions
    # Let's target the get_media_info_impl
    media_info_impl_pattern = r'async fn get_media_info_impl\(&self, url: &str\) -> anyhow::Result<MediaInfo> {'
    replacement = r'async fn get_media_info_impl(&self, url: &str) -> anyhow::Result<MediaInfo> {\n        let response = self.client.get(url).send().await?;\n        let html = response.text().await?;'
    insta_content, _ = re.subn(media_info_impl_pattern, replacement, insta_content)
    
    # For get_auth_headers
    auth_headers_pattern = r'async fn get_auth_headers\(&self\) -> anyhow::Result<reqwest::header::HeaderMap> {'
    replacement = r'async fn get_auth_headers(&self) -> anyhow::Result<reqwest::header::HeaderMap> {\n        let response = self.client.get("https://www.instagram.com/").send().await?;\n        let html = response.text().await?;\n        let csrf = Self::extract_csrf_from_html(&html)?;'
    insta_content, _ = re.subn(auth_headers_pattern, replacement, insta_content)


    with open(insta_path, 'w', encoding='utf-8') as f:
        f.write(insta_content)
    print("Patched instagram downloader")


if __name__ == "__main__":
    main()
