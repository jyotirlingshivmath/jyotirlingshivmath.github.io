import os
from datetime import datetime

base_url = "https://jyotirlingshivmath.in"
sitemap_filename = "sitemap-today.xml" 

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

target_folder = "shivpuran/2026/10"

if os.path.exists(target_folder):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file.endswith('.html') and not file.startswith('404'):
                rel_path = os.path.join(root, file).replace("\\", "/")
                
                sitemap_content += f"  <url>\n"
                sitemap_content += f"    <loc>{base_url}/{rel_path}</loc>\n"
                sitemap_content += f"    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>\n"
                sitemap_content += f"    <changefreq>weekly</changefreq>\n"
                sitemap_content += f"  </url>\n"

sitemap_content += '</urlset>'

with open(sitemap_filename, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Sitemap '{sitemap_filename}' updated successfully!")
