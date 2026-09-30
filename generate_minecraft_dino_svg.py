# -*- coding: utf-8 -*-
"""
Generate Native Animated Minecraft & Chrome Dinosaur SVG
Creates a self-contained SVG animation featuring:
- Pixel Minecraft Steve walking
- Pixel Minecraft Creeper pulsing
- Chrome Dinosaur running & jumping over cacti
- Minecraft Grass/Dirt Block Terrain
100% native vector SVG with CSS animations (never breaks or shows 'CONTENT NOT AVAILABLE')
"""
import os

def generate_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 180" width="660" height="180">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;display=swap');
      .font-mono { font-family: 'Fira Code', monospace; }
      
      /* Ground scrolling animation */
      @keyframes scrollGround {
        0% { transform: translateX(0); }
        100% { transform: translateX(-40px); }
      }
      .ground-track { animation: scrollGround 1.2s linear infinite; }

      /* Chrome Dino Jump Animation */
      @keyframes dinoJump {
        0%, 100% { transform: translateY(0); }
        45%, 55% { transform: translateY(-45px); }
      }
      .dino-runner { animation: dinoJump 2.4s ease-in-out infinite; }

      /* Minecraft Steve Walk Swing Animation */
      @keyframes steveWalk {
        0%, 100% { transform: rotate(-8deg); }
        50% { transform: rotate(8deg); }
      }
      .steve-arm-left { transform-origin: 140px 85px; animation: steveWalk 0.8s ease-in-out infinite; }
      .steve-arm-right { transform-origin: 140px 85px; animation: steveWalk 0.8s ease-in-out infinite reverse; }
      .steve-leg-left { transform-origin: 140px 115px; animation: steveWalk 0.8s ease-in-out infinite reverse; }
      .steve-leg-right { transform-origin: 140px 115px; animation: steveWalk 0.8s ease-in-out infinite; }

      /* Creeper Fuse Glow */
      @keyframes creeperFuse {
        0%, 100% { fill: #00ff55; filter: drop-shadow(0 0 2px #00ff55); }
        50% { fill: #ffffff; filter: drop-shadow(0 0 8px #ffffff); }
      }
      .creeper-body { animation: creeperFuse 2s ease-in-out infinite; }

      /* Cacti Obstacle Scrolling */
      @keyframes scrollCacti {
        0% { transform: translateX(650px); }
        100% { transform: translateX(-60px); }
      }
      .cactus-obstacle { animation: scrollCacti 3.2s linear infinite; }
      
      /* Floating Minecraft Emerald Sparkles */
      @keyframes floatSparkle {
        0%, 100% { transform: translateY(0) scale(0.8); opacity: 0.3; }
        50% { transform: translateY(-12px) scale(1.2); opacity: 1; }
      }
      .sparkle-1 { animation: floatSparkle 2s infinite ease-in-out; }
      .sparkle-2 { animation: floatSparkle 2.5s infinite ease-in-out 0.5s; }
      .sparkle-3 { animation: floatSparkle 1.8s infinite ease-in-out 1s; }
    </style>
  </defs>

  <!-- Container Box -->
  <rect x="5" y="5" width="650" height="170" rx="10" ry="10" fill="#0d1117" stroke="#238636" stroke-width="1.5" />

  <!-- Minecraft Block Ground Line -->
  <g class="ground-track">
    <!-- Dirt & Grass Block Pattern -->
    <rect x="-40" y="145" width="750" height="25" fill="#5c3a21" />
    <!-- Top Grass Line -->
    <rect x="-40" y="145" width="750" height="6" fill="#388e3c" />
    <!-- Grass Pixel Teeth -->
    <path d="M -40 151 L 710 151" stroke="#2e7d32" stroke-width="3" stroke-dasharray="8 6" />
  </g>

  <!-- 1. CHROME DINOSAUR (Left-Center) -->
  <g id="chrome-dinosaur" transform="translate(360, 40)">
    <g class="dino-runner">
      <!-- Pixel Chrome Dino Body -->
      <!-- Head & Eye -->
      <rect x="24" y="20" width="22" height="18" fill="#c9d1d9" />
      <rect x="40" y="24" width="4" height="4" fill="#0d1117" />
      <!-- Mouth/Snout -->
      <rect x="36" y="32" width="10" height="4" fill="#c9d1d9" />
      <!-- Neck & Torso -->
      <rect x="18" y="38" width="16" height="24" fill="#c9d1d9" />
      <rect x="10" y="44" width="28" height="18" fill="#c9d1d9" />
      <!-- Tail -->
      <rect x="2" y="46" width="10" height="8" fill="#c9d1d9" />
      <rect x="-4" y="48" width="8" height="4" fill="#c9d1d9" />
      <!-- Tiny Arms -->
      <rect x="34" y="48" width="6" height="4" fill="#c9d1d9" />
      <rect x="38" y="50" width="2" height="6" fill="#c9d1d9" />
      <!-- Legs -->
      <rect x="14" y="62" width="6" height="14" fill="#c9d1d9" />
      <rect x="14" y="74" width="8" height="4" fill="#c9d1d9" />
      <rect x="26" y="62" width="6" height="14" fill="#c9d1d9" />
      <rect x="26" y="74" width="8" height="4" fill="#c9d1d9" />
    </g>
  </g>

  <!-- Cactus Obstacle scrolling towards Dino -->
  <g class="cactus-obstacle" transform="translate(0, 105)">
    <rect x="0" y="10" width="8" height="30" fill="#2e7d32" />
    <rect x="-6" y="18" width="6" height="12" fill="#2e7d32" />
    <rect x="-6" y="18" width="18" height="4" fill="#2e7d32" />
    <rect x="8" y="22" width="6" height="10" fill="#2e7d32" />
    <rect x="2" y="22" width="10" height="4" fill="#2e7d32" />
  </g>

  <!-- 2. MINECRAFT STEVE (Left Side) -->
  <g id="minecraft-steve" transform="translate(60, 45)">
    <!-- Hair & Head -->
    <rect x="120" y="55" width="20" height="20" fill="#c0a080" /> <!-- Face -->
    <rect x="120" y="55" width="20" height="6" fill="#4a2e16" />  <!-- Hair -->
    <rect x="118" y="58" width="4" height="10" fill="#4a2e16" />  <!-- Side Hair -->
    <rect x="138" y="58" width="4" height="10" fill="#4a2e16" />  <!-- Side Hair -->
    <!-- Eyes & Nose -->
    <rect x="123" y="64" width="4" height="3" fill="#ffffff" />
    <rect x="125" y="64" width="2" height="3" fill="#2b4c7e" /> <!-- Blue Eye -->
    <rect x="133" y="64" width="4" height="3" fill="#ffffff" />
    <rect x="133" y="64" width="2" height="3" fill="#2b4c7e" /> <!-- Blue Eye -->
    <rect x="128" y="67" width="4" height="3" fill="#7a4b2a" /> <!-- Nose -->

    <!-- Cyan Shirt (Torso) -->
    <rect x="120" y="75" width="20" height="25" fill="#00a8a8" />

    <!-- Left & Right Animated Arms -->
    <g class="steve-arm-left">
      <rect x="112" y="75" width="8" height="22" fill="#00a8a8" />
      <rect x="112" y="90" width="8" height="7" fill="#c0a080" />
    </g>
    <g class="steve-arm-right">
      <rect x="140" y="75" width="8" height="22" fill="#00a8a8" />
      <rect x="140" y="90" width="8" height="7" fill="#c0a080" />
    </g>

    <!-- Blue Pants (Legs) -->
    <g class="steve-leg-left">
      <rect x="121" y="100" width="8" height="20" fill="#2a3b8f" />
      <rect x="121" y="116" width="8" height="4" fill="#4a4a4a" /> <!-- Shoe -->
    </g>
    <g class="steve-leg-right">
      <rect x="131" y="100" width="8" height="20" fill="#2a3b8f" />
      <rect x="131" y="116" width="8" height="4" fill="#4a4a4a" /> <!-- Shoe -->
    </g>
  </g>

  <!-- 3. MINECRAFT CREEPER (Right Side) -->
  <g id="minecraft-creeper" transform="translate(520, 50)">
    <!-- Creeper Head -->
    <rect x="10" y="30" width="30" height="30" class="creeper-body" />
    <!-- Creeper Face Expression (Black Pixels) -->
    <!-- Eyes -->
    <rect x="14" y="38" width="7" height="7" fill="#000000" />
    <rect x="29" y="38" width="7" height="7" fill="#000000" />
    <!-- Nose/Mouth -->
    <rect x="21" y="45" width="8" height="10" fill="#000000" />
    <rect x="18" y="50" width="14" height="8" fill="#000000" />

    <!-- Creeper Body & Legs -->
    <rect x="15" y="60" width="20" height="30" class="creeper-body" />
    <rect x="12" y="90" width="12" height="10" fill="#1b5e20" />
    <rect x="26" y="90" width="12" height="10" fill="#1b5e20" />
  </g>

  <!-- Floating Emerald Sparkles -->
  <g class="sparkle-1" transform="translate(240, 50)">
    <polygon points="10,0 14,8 10,16 6,8" fill="#00ff55" />
  </g>
  <g class="sparkle-2" transform="translate(480, 40)">
    <polygon points="10,0 14,8 10,16 6,8" fill="#55ff55" />
  </g>
  <g class="sparkle-3" transform="translate(140, 35)">
    <polygon points="10,0 14,8 10,16 6,8" fill="#00e676" />
  </g>

  <!-- Title Badge Overlay -->
  <rect x="230" y="15" width="200" height="24" rx="12" ry="12" fill="#161b22" stroke="#238636" stroke-width="1" />
  <text x="330" y="31" class="font-mono" font-size="11" font-weight="700" fill="#00ff55" text-anchor="middle">MINECRAFT &amp; DINO RUN</text>

</svg>"""

    output_path = "minecraft_dino_animation.svg"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated Minecraft & Chrome Dino SVG: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    generate_svg()
