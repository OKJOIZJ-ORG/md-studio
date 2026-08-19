import math
import struct
import zlib
import os

def create_png(width, height, rgba_data):
    png = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data)
    png += struct.pack('>I', len(ihdr_data)) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
    
    scanlines = bytearray()
    for y in range(height):
        scanlines.append(0)
        start = y * width * 4
        end = start + width * 4
        scanlines.extend(rgba_data[start:end])
        
    compressed = zlib.compress(bytes(scanlines), 9)
    idat_crc = zlib.crc32(b'IDAT' + compressed)
    png += struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)
    
    iend_crc = zlib.crc32(b'IEND')
    png += struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)
    return png

def create_ico(png_images):
    count = len(png_images)
    header = struct.pack('<HHH', 0, 1, count)
    offset = 6 + 16 * count
    entries = []
    image_data = bytearray()
    
    for w, h, data in png_images:
        bw = 0 if w >= 256 else w
        bh = 0 if h >= 256 else h
        size = len(data)
        entry = struct.pack('<BBBBHHII', bw, bh, 0, 0, 1, 32, size, offset)
        entries.append(entry)
        image_data.extend(data)
        offset += size
        
    return header + b''.join(entries) + bytes(image_data)

def sd_rounded_box(px, py, bx, by, r):
    qx = abs(px) - (bx - r)
    qy = abs(py) - (by - r)
    ax = max(qx, 0.0)
    ay = max(qy, 0.0)
    return math.hypot(ax, ay) + min(max(qx, qy), 0.0) - r

def sd_segment(px, py, ax, ay, bx, by):
    pax = px - ax
    pay = py - ay
    bax = bx - ax
    bay = by - ay
    h = max(0.0, min(1.0, (pax*bax + pay*bay) / (bax*bax + bay*bay)))
    dx = pax - bax * h
    dy = pay - bay * h
    return math.hypot(dx, dy)

def render_obsidian_titanium_icon(size, is_maskable=False):
    """
    Renders an ultra-clean Obsidian Titanium & Platinum White Icon (Vercel / Apple Pro Studio style):
    - Base: Pure Obsidian Titanium Graphite (#2C2C30 -> #1A1A1D -> #0D0D0F)
    - Specular: Silver-white specular radial light
    - Bezel: 0.8px subtle platinum rim
    - Symbol: Pure crisp diamond-white dual pane with micro code & preview geometry
    """
    rgba = bytearray(size * size * 4)
    ss = 2 if size <= 48 else 1
    samples = []
    for sy in range(ss):
        for sx in range(ss):
            samples.append(((sx + 0.5) / ss, (sy + 0.5) / ss))
            
    num_samples = len(samples)
    bg_radius_ratio = 0.0 if is_maskable else 0.2237
    
    for y in range(size):
        for x in range(size):
            r_acc, g_acc, b_acc, a_acc = 0.0, 0.0, 0.0, 0.0
            
            for ox, oy in samples:
                u = (x + ox) / size
                v = (y + oy) / size
                cx = u - 0.5
                cy = v - 0.5
                
                bg_box_size = 0.48
                bg_r = bg_radius_ratio if not is_maskable else 0.0
                
                if is_maskable:
                    d_bg = -1.0
                    bg_edge_alpha = 1.0
                else:
                    d_bg = sd_rounded_box(cx, cy, bg_box_size, bg_box_size, bg_r)
                    bg_edge_alpha = max(0.0, min(1.0, 0.5 - d_bg * size))
                    
                if bg_edge_alpha > 0.0:
                    # 1. Obsidian Titanium 165° Gradient (#323236 -> #1C1C1F -> #0A0A0C)
                    grad_t = 0.5 + (cx * 0.26 + cy * 0.96)
                    grad_t = max(0.0, min(1.0, grad_t))
                    
                    if grad_t < 0.50:
                        t2 = grad_t / 0.50
                        base_r = 50.0 * (1 - t2) + 28.0 * t2
                        base_g = 50.0 * (1 - t2) + 28.0 * t2
                        base_b = 54.0 * (1 - t2) + 31.0 * t2
                    else:
                        t2 = (grad_t - 0.50) / 0.50
                        base_r = 28.0 * (1 - t2) + 10.0 * t2
                        base_g = 28.0 * (1 - t2) + 10.0 * t2
                        base_b = 31.0 * (1 - t2) + 12.0 * t2
                        
                    # 2. Specular Gloss Overlay (Silver platinum light)
                    dist_gloss = math.hypot((cx + 0.15) / 0.45, (cy + 0.50) / 0.35)
                    gloss_alpha = max(0.0, min(0.35, 0.35 * (1.0 - dist_gloss))) if dist_gloss < 1.0 else 0.0
                    
                    dist_gloss2 = math.hypot((cx - 0.30) / 0.40, (cy + 0.28) / 0.35)
                    gloss2_alpha = max(0.0, min(0.14, 0.14 * (1.0 - dist_gloss2))) if dist_gloss2 < 1.0 else 0.0
                    
                    total_gloss = min(0.45, gloss_alpha + gloss2_alpha)
                    bg_r_col = base_r * (1.0 - total_gloss) + 255.0 * total_gloss
                    bg_g_col = base_g * (1.0 - total_gloss) + 255.0 * total_gloss
                    bg_b_col = base_b * (1.0 - total_gloss) + 255.0 * total_gloss
                    
                    # 3. Top Bezel Highlight
                    if not is_maskable:
                        if -0.012 < d_bg <= 0.0 and cy < 0:
                            top_highlight = max(0.0, -cy / 0.5) * 0.40
                            bg_r_col = bg_r_col * (1.0 - top_highlight) + 255.0 * top_highlight
                            bg_g_col = bg_g_col * (1.0 - top_highlight) + 255.0 * top_highlight
                            bg_b_col = bg_b_col * (1.0 - top_highlight) + 255.0 * top_highlight
                            
                    # 4. Dual-Pane Symbol Geometry
                    symbol_scale = 0.52 if is_maskable else 0.60
                    vx = (cx / symbol_scale + 0.5) * 16.0
                    vy = (cy / symbol_scale + 0.5) * 16.0
                    
                    d_box = sd_rounded_box(vx - 8.0, vy - 8.0, 6.8, 6.8, 3.2)
                    d_rect_stroke = abs(d_box) - 0.82
                    d_line = sd_segment(vx, vy, 8.0, 2.4, 8.0, 13.6) - 0.82
                    
                    d_bar1 = sd_segment(vx, vy, 3.6, 5.6, 6.0, 5.6) - 0.50
                    d_bar2 = sd_segment(vx, vy, 3.6, 8.2, 5.4, 8.2) - 0.50
                    d_bar3 = sd_segment(vx, vy, 3.6, 10.8, 6.2, 10.8) - 0.50
                    
                    d_rbar1 = sd_segment(vx, vy, 10.0, 5.6, 12.4, 5.6) - 0.58
                    d_rbar2 = sd_segment(vx, vy, 10.0, 8.2, 11.8, 8.2) - 0.48
                    
                    d_main_symbol = min(d_rect_stroke, d_line)
                    d_inner_details = min(d_bar1, d_bar2, d_bar3, d_rbar1, d_rbar2)
                    
                    pixel_per_vb = size * symbol_scale / 16.0
                    d_main_px = d_main_symbol * pixel_per_vb
                    d_detail_px = d_inner_details * pixel_per_vb
                    
                    main_alpha = max(0.0, min(1.0, 0.5 - d_main_px))
                    detail_alpha = max(0.0, min(1.0, 0.5 - d_detail_px)) * 0.82
                    
                    # Diamond white material (#FFFFFF -> #F4F4F5 -> #E4E4E7)
                    sym_t = max(0.0, min(1.0, (vy - 1.2) / 13.6))
                    sym_r = 255.0 * (1 - sym_t) + 235.0 * sym_t
                    sym_g = 255.0 * (1 - sym_t) + 235.0 * sym_t
                    sym_b = 255.0 * (1 - sym_t) + 240.0 * sym_t
                    
                    combined_sym_alpha = max(main_alpha, detail_alpha)
                    
                    # Shadow cast
                    d_shadow_vb = min(
                        sd_rounded_box(vx - 8.0, (vy - 0.6) - 8.0, 6.8, 6.8, 3.2),
                        sd_segment(vx, vy - 0.6, 8.0, 2.4, 8.0, 13.6)
                    )
                    d_shadow_stroke = abs(d_shadow_vb) - 0.82
                    d_shadow_px = d_shadow_stroke * pixel_per_vb
                    shadow_alpha = max(0.0, min(0.40, (0.5 - d_shadow_px) * 0.40))
                    
                    pix_r = bg_r_col * (1.0 - shadow_alpha) + 0.0 * shadow_alpha
                    pix_g = bg_g_col * (1.0 - shadow_alpha) + 0.0 * shadow_alpha
                    pix_b = bg_b_col * (1.0 - shadow_alpha) + 0.0 * shadow_alpha
                    
                    pix_r = pix_r * (1.0 - combined_sym_alpha) + sym_r * combined_sym_alpha
                    pix_g = pix_g * (1.0 - combined_sym_alpha) + sym_g * combined_sym_alpha
                    pix_b = pix_b * (1.0 - combined_sym_alpha) + sym_b * combined_sym_alpha
                    pix_a = bg_edge_alpha
                    
                    r_acc += pix_r * pix_a
                    g_acc += pix_g * pix_a
                    b_acc += pix_b * pix_a
                    a_acc += pix_a
                else:
                    if not is_maskable:
                        d_bg_px = d_bg * size
                        if d_bg_px < 0.5:
                            bg_edge_alpha = max(0.0, min(1.0, 0.5 - d_bg_px))
                            base_r, base_g, base_b = 28.0, 28.0, 31.0
                            r_acc += base_r * bg_edge_alpha
                            g_acc += base_g * bg_edge_alpha
                            b_acc += base_b * bg_edge_alpha
                            a_acc += bg_edge_alpha
                            
            final_a = a_acc / num_samples
            if final_a > 0.001:
                final_r = min(255, int((r_acc / a_acc)))
                final_g = min(255, int((g_acc / a_acc)))
                final_b = min(255, int((b_acc / a_acc)))
                final_a_byte = min(255, int(final_a * 255.0))
            else:
                final_r, final_g, final_b, final_a_byte = 0, 0, 0, 0
                
            idx = (y * size + x) * 4
            rgba[idx] = final_r
            rgba[idx + 1] = final_g
            rgba[idx + 2] = final_b
            rgba[idx + 3] = final_a_byte
            
    return create_png(size, size, rgba)

def generate_all(out_dir="."):
    print("Generating Obsidian Titanium & Platinum Minimalist Icons...")
    
    # 1. 16x16 PNG
    png16 = render_obsidian_titanium_icon(16)
    with open(os.path.join(out_dir, "favicon-16x16.png"), "wb") as f:
        f.write(png16)
    print("  -> favicon-16x16.png")
    
    # 2. 32x32 PNG
    png32 = render_obsidian_titanium_icon(32)
    with open(os.path.join(out_dir, "favicon-32x32.png"), "wb") as f:
        f.write(png32)
    print("  -> favicon-32x32.png")
    
    # 3. 48x48 PNG
    png48 = render_obsidian_titanium_icon(48)
    with open(os.path.join(out_dir, "favicon-48x48.png"), "wb") as f:
        f.write(png48)
    print("  -> favicon-48x48.png")
    
    # 4. favicon.ico (16, 32, 48)
    ico_data = create_ico([(16, 16, png16), (32, 32, png32), (48, 48, png48)])
    with open(os.path.join(out_dir, "favicon.ico"), "wb") as f:
        f.write(ico_data)
    print("  -> favicon.ico")
    
    # 5. apple-touch-icon.png (180x180)
    png180 = render_obsidian_titanium_icon(180)
    with open(os.path.join(out_dir, "apple-touch-icon.png"), "wb") as f:
        f.write(png180)
    print("  -> apple-touch-icon.png")
    
    # 6. android-chrome-192x192.png
    png192 = render_obsidian_titanium_icon(192)
    with open(os.path.join(out_dir, "android-chrome-192x192.png"), "wb") as f:
        f.write(png192)
    print("  -> android-chrome-192x192.png")
    
    # 7. android-chrome-512x512.png
    png512 = render_obsidian_titanium_icon(512)
    with open(os.path.join(out_dir, "android-chrome-512x512.png"), "wb") as f:
        f.write(png512)
    print("  -> android-chrome-512x512.png")

    # 8. android-chrome-maskable-512x512.png
    png512_maskable = render_obsidian_titanium_icon(512, is_maskable=True)
    with open(os.path.join(out_dir, "android-chrome-maskable-512x512.png"), "wb") as f:
        f.write(png512_maskable)
    print("  -> android-chrome-maskable-512x512.png")
    
    # 9. favicon.svg (Obsidian Titanium & Platinum)
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs>
    <linearGradient id="baseGrad" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#323236"/>
      <stop offset="50%" stop-color="#1C1C1F"/>
      <stop offset="100%" stop-color="#0A0A0C"/>
    </linearGradient>
    <radialGradient id="topGloss" cx="35%" cy="0%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="symGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F4F4F5"/>
      <stop offset="100%" stop-color="#D4D4D8"/>
    </linearGradient>
    <filter id="symShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1.2" stdDeviation="1.0" flood-color="#000000" flood-opacity="0.60"/>
    </filter>
  </defs>
  <rect width="32" height="32" rx="7.16" fill="url(#baseGrad)"/>
  <rect width="32" height="32" rx="7.16" fill="url(#topGloss)"/>
  <rect x="0.6" y="0.6" width="30.8" height="30.8" rx="6.8" fill="none" stroke="#FFFFFF" stroke-width="0.8" stroke-opacity="0.25"/>
  
  <g transform="translate(6, 6) scale(1.25)" filter="url(#symShadow)">
    <rect x="1.2" y="1.2" width="13.6" height="13.6" rx="3.2" fill="none" stroke="url(#symGrad)" stroke-width="1.5" stroke-linejoin="round"/>
    <line x1="8" y1="2.4" x2="8" y2="13.6" stroke="url(#symGrad)" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="3.6" y1="5.6" x2="6.0" y2="5.6" stroke="url(#symGrad)" stroke-width="1.0" stroke-linecap="round" opacity="0.85"/>
    <line x1="3.6" y1="8.2" x2="5.4" y2="8.2" stroke="url(#symGrad)" stroke-width="1.0" stroke-linecap="round" opacity="0.85"/>
    <line x1="3.6" y1="10.8" x2="6.2" y2="10.8" stroke="url(#symGrad)" stroke-width="1.0" stroke-linecap="round" opacity="0.85"/>
    <line x1="10.0" y1="5.6" x2="12.4" y2="5.6" stroke="url(#symGrad)" stroke-width="1.2" stroke-linecap="round" opacity="0.95"/>
    <line x1="10.0" y1="8.2" x2="11.8" y2="8.2" stroke="url(#symGrad)" stroke-width="1.0" stroke-linecap="round" opacity="0.75"/>
  </g>
</svg>'''
    with open(os.path.join(out_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("  -> favicon.svg")

if __name__ == "__main__":
    generate_all(".")
