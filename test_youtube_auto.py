import os
import urllib.request
import xml.etree.ElementTree as ET
import subprocess


# 1. आपके चैनल का RSS फीड लिंक
rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC2sBCYCH6Kb9dgqQN3vVgFw"

# 2. फोल्डर जहाँ नई HTML फाइलें सेव होंगी
target_folder = "shivpuran/2026/10"
os.makedirs(target_folder, exist_ok=True)

# 3. HTML टेम्पलेट
html_template = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>{video_title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #fffdf5; color: #333; text-align: center; padding: 20px; }}
        .container {{ max-width: 800px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #b22222; }}
        .meta {{ font-size: 14px; color: #666; margin-bottom: 20px; }}
        .video-container {{ position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; margin-bottom: 20px; border-radius: 6px; }}
        .video-container iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }}
        .desc {{ font-size: 16px; line-height: 1.6; text-align: left; margin-bottom: 20px; }}
        .footer {{ margin-top: 30px; font-size: 14px; color: #888; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📿 {video_title} 📿</h1>
        <div class="meta">श्री ज्योतिर्लिंग शिवमठ, लखनऊ | कथा व्यास: महंत राजेश कुमार तिवारी "रंजन"</div>
        
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{video_id}" allowfullscreen></iframe>
        </div>
        
        <div class="desc">
            <p>🔱 हर हर महादेव 🔱</p>
            <p>{video_title} का यह पावन प्रसंग श्रद्धा और भक्ति से सुनें। श्री ज्योतिर्लिंग शिवमठ, लखनऊ से प्रस्तुत इस शिवपुराण कथा का आनंद लें और अपने जीवन को धन्य करें।</p>
        </div>

        <div class="footer">
            <a href="https://jyotirlingshivmath.in">🏠 मुख्य पृष्ठ</a> | 
            <a href="https://www.youtube.com/watch?v={video_id}" target="_blank">▶ YouTube पर देखें</a>
        </div>
    </div>
</body>
</html>
"""

try:
    # RSS फीड डेटा पढ़ें
    req = urllib.request.urlopen(rss_url)
    xml_data = req.read()

    # XML पार्स करें
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015'}

    file_created = False

    # वीडियो की सूची पढ़ें
    for entry in root.findall('atom:entry', ns):
        video_id = entry.find('yt:videoId', ns).text
        title = entry.find('atom:title', ns).text
        
        # फाइल का नाम सुरक्षित फॉर्मेट में बनाएं
        safe_filename = "".join([c if c.isalnum() else "_" for c in title])[:40] + f"_{video_id}.html"
        file_path = os.path.join(target_folder, safe_filename)
        
        # यदि यह पेज पहले से नहीं है, तो नया पेज बना दें
        if not os.path.exists(file_path):
            page_content = html_template.format(video_title=title, video_id=video_id)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(page_content)
            print(f"नया पेज जनरेट हुआ: {safe_filename}")
            file_created = True
            break # केवल सबसे नए वीडियो के लिए

    # अगर नई फाइल बनी है, तो उसे गिटहब पर ऑटो-कमिट कर दें
    if file_created:
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"])
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])
        subprocess.run(["git", "add", target_folder])
        subprocess.run(["git", "commit", "-m", "Auto-generate new YouTube video HTML page"])
        subprocess.run(["git", "push"])
        print("फाइल सफलतापूर्वक गिटहब पर सेव हो गई है!")
    else:
        print("कोई नई फाइल नहीं बनी, क्योंकि वह पहले से मौजूद है।")

except Exception as e:
    print(f"त्रुटि आई: {e}")
