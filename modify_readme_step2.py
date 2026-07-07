import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

dedicated_list = """- **[LosslessCut](https://github.com/mifi/lossless-cut)** [![GitHub stars](https://img.shields.io/github/stars/mifi/lossless-cut?style=social&color=white)](https://github.com/mifi/lossless-cut/stargazers)  
  Extremely fast open-source tool for lossless cutting and trimming of YouTube footage.

- **[Blender Video Sequence Editor](https://github.com/blender/blender)** [![GitHub stars](https://img.shields.io/github/stars/blender/blender?style=social&color=white)](https://github.com/blender/blender/stargazers)  
  Powerful open-source 3D suite with a capable video editor for complex YouTube projects.

- **[Shotcut](https://github.com/mltframework/shotcut)** [![GitHub stars](https://img.shields.io/github/stars/mltframework/shotcut?style=social&color=white)](https://github.com/mltframework/shotcut/stargazers)  
  Cross-platform open-source editor with native timeline editing and hardware acceleration support.

- **[Olive Video Editor](https://github.com/olive-editor/olive)** [![GitHub stars](https://img.shields.io/github/stars/olive-editor/olive?style=social&color=white)](https://github.com/olive-editor/olive/stargazers)  
  Modern open-source non-linear video editor aiming for professional features.

- **[OpenShot](https://github.com/OpenShot/openshot-qt)** [![GitHub stars](https://img.shields.io/github/stars/OpenShot/openshot-qt?style=social&color=white)](https://github.com/OpenShot/openshot-qt/stargazers)  
  User-friendly open-source video editor with excellent animation and title tools for YouTubers.

- **[Kdenlive](https://github.com/KDE/kdenlive)** [![GitHub stars](https://img.shields.io/github/stars/KDE/kdenlive?style=social&color=white)](https://github.com/KDE/kdenlive/stargazers)  
  Professional open-source video editor with timeline editing, effects, and strong YouTube export options.

- **[Flowblade](https://github.com/jliljebl/flowblade)** [![GitHub stars](https://img.shields.io/github/stars/jliljebl/flowblade?style=social&color=white)](https://github.com/jliljebl/flowblade/stargazers)  
  Fast and efficient open-source multitrack video editor designed for Linux.

- **[Pitivi](https://github.com/GNOME/pitivi)** [![GitHub stars](https://img.shields.io/github/stars/GNOME/pitivi?style=social&color=white)](https://github.com/GNOME/pitivi/stargazers)  
  GNOME-based open-source video editor with a focus on simplicity and GStreamer integration.

- **[DaVinci Resolve Free Version](https://www.blackmagicdesign.com/products/davinciresolve)**  
  Industry-leading free professional editor with full color, audio, and VFX capabilities.

- **[Cinelerra](https://github.com/cinelerra)** (and forks)  
  Long-standing open-source video editing and compositing software."""

additional_list = """- **[FFmpeg](https://github.com/FFmpeg/FFmpeg)** [![GitHub stars](https://img.shields.io/github/stars/FFmpeg/FFmpeg?style=social&color=white)](https://github.com/FFmpeg/FFmpeg/stargazers) scripts and GUIs for batch processing and optimization.
- **[HandBrake](https://github.com/HandBrake/HandBrake)** [![GitHub stars](https://img.shields.io/github/stars/HandBrake/HandBrake?style=social&color=white)](https://github.com/HandBrake/HandBrake/stargazers) — Open-source video transcoder for YouTube-ready exports.
- **[Krita](https://github.com/KDE/krita)** [![GitHub stars](https://img.shields.io/github/stars/KDE/krita?style=social&color=white)](https://github.com/KDE/krita/stargazers) with animation tools for thumbnails and motion graphics.
- **[Natron](https://github.com/NatronGitHub/Natron)** [![GitHub stars](https://img.shields.io/github/stars/NatronGitHub/Natron?style=social&color=white)](https://github.com/NatronGitHub/Natron/stargazers) — Open-source compositing software for VFX in YouTube videos.
- **[GIMP](https://github.com/GNOME/gimp)** [![GitHub stars](https://img.shields.io/github/stars/GNOME/gimp?style=social&color=white)](https://github.com/GNOME/gimp/stargazers) with video plugins for image-based YouTube assets."""

content = re.sub(r"### Dedicated Video Editing Tools for YouTubers.*?### Additional Strong Open-Source Options", "### Dedicated Video Editing Tools for YouTubers\n\n" + dedicated_list + "\n\n### Additional Strong Open-Source Options", content, flags=re.DOTALL)
content = re.sub(r"### Additional Strong Open-Source Options.*?\*\*Recommended Toolchains\*\*:", "### Additional Strong Open-Source Options\n\n" + additional_list + "\n\n**Recommended Toolchains**:", content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
