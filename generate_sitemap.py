import os
from datetime import datetime

base_url = "https://jyotirlingshivmath.in"
sitemap_filename = "sitemap-today.xml" 

# sitemap की शुरुआत करें
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# यदि आप मुख्य होमपेज को भी साइटमैप में रखना चाहते हैं, तो यह लाइन रहने दें (नहीं तो इसे हटा भी सकते हैं)
sitemap_content += f"  <url>\n"
sitemap_content += f"    <loc>{base_url}/</loc>\n"
sitemap_content += f"    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>\n"
sitemap_content += f"    <changefreq>daily</changefreq>\n"
sitemap_content += f"  </url>\n"

# सिर्फ इस विशिष्ट फोल्डर को टारगेट करें
target_folder = "shivpuran/20
