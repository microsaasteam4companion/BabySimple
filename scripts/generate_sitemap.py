import re
import os
from datetime import datetime

def generate_sitemap():
    base_url = "https://babysimple.entrext.in"
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Static routes
    routes = [
        {"loc": "/", "changefreq": "weekly", "priority": "1.0"},
        {"loc": "/privacy", "changefreq": "monthly", "priority": "0.5"},
        {"loc": "/terms", "changefreq": "monthly", "priority": "0.5"},
        {"loc": "/blog", "changefreq": "daily", "priority": "0.8"},
        {"loc": "/dashboard", "changefreq": "monthly", "priority": "0.5"},
    ]
    
    # Extract slugs from src/blogContent.ts and src/generatedBlogs.ts
    slugs = set()
    
    files_to_scan = [
        "src/blogContent.ts",
        "src/generatedBlogs.ts"
    ]
    
    for file_path in files_to_scan:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Match single quoted slugs: slug: 'slug-name'
                found_single = re.findall(r"slug:\s*'([^']+)'", content)
                slugs.update(found_single)
                # Match double quoted slugs: "slug": "slug-name"
                found_double = re.findall(r'"slug":\s*"([^"]+)"', content)
                slugs.update(found_double)
    
    # Add blog posts to routes
    for slug in sorted(list(slugs)):
        if slug:
            routes.append({
                "loc": f"/blog/{slug}",
                "changefreq": "monthly",
                "priority": "0.7"
            })
            
    # Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for route in routes:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{base_url}{route["loc"]}</loc>')
        xml_lines.append(f'    <lastmod>{today}</lastmod>')
        xml_lines.append(f'    <changefreq>{route["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{route["priority"]}</priority>')
        xml_lines.append('  </url>')
        
    xml_lines.append('</urlset>')
    
    # Write to public/sitemap.xml
    output_path = "public/sitemap.xml"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(xml_lines))
        
    print(f"Sitemap generated with {len(routes)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
