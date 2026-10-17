import os
from datetime import datetime

base_url = "https://jyotirlingshivmath.in"
sitemap_filename = "sitemap-today.xml" 

# 1. मुख्य होमपेज के साथ sitemap शुरू करें
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_content += f"  <url>\n"
sitemap_content += f"    <loc>{base_url}/</loc>\n"
sitemap_content += f"    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>\n"
sitemap_content += f"    <changefreq>daily</changefreq>\n"
sitemap_content += f"  </url>\n"

# 2. पूरी रिपॉजिटरी के सभी फोल्डर्स और फाइलों को स्कैन करें
for root, dirs, files in os.walk("."):
    # .git या venv जैसी गुप्त/सिस्टम फ़ोल्डर को छोड़ दें
    if ".git" in root or "venv" in root or ".github" in root:
        continue
        
    for file in files:
        if file.endswith('.html') and not file.startswith('404'):
            # फाइल का सही पाथ बनाएं
            rel_path = os.path.join(root, file).replace("\\", "/")
            if rel_path.startswith("./"):
                rel_path = rel_path[2:]
            
            # sitemap में यूआरएल जोड़ें
            sitemap_content += f"  <url>\n"
            sitemap_content += f"    <loc>{base_url}/{rel_path}</loc>\n"
            sitemap_content += f"    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>\n"
            sitemap_content += f"    <changefreq>weekly</changefreq>\n"
            sitemap_content += f"  </url>\n"

sitemap_content += '</urlset>'

# फाइल में सेव करें
with open(sitemap_filename, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Sitemap '{sitemap_filename}' updated successfully with all pages!")
