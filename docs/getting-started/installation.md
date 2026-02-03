# Installation

EnergyAtlas is available in multiple formats to suit different workflows and preferences.

## Web Application

The EnergyAtlas web application requires no installation and runs directly in your browser.

**Access**: [EnergyAtlas.io](http://EnergyAtlas.io/)

**Requirements**:
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- JavaScript enabled

## Standalone Executable

Desktop applications for Windows and macOS provide offline access and enhanced performance.

### Windows

**Download**: Available from [EnergyAtlas.io](http://EnergyAtlas.io/)

**Installation Steps**:
1. Download the Windows installer (.exe)
2. Run the installer
3. Follow the installation wizard
4. Launch EnergyAtlas from the Start menu

**System Requirements**:
- Windows 10 or later
- 4 GB RAM minimum (8 GB recommended)
- 500 MB free disk space

### MacOS

**Download**: Available from [EnergyAtlas.io](http://EnergyAtlas.io/)

**Installation Steps**:
1. Download the macOS installer (.dmg)
2. Open the disk image
3. Drag EnergyAtlas to Applications folder
4. Launch from Applications

**System Requirements**:
- macOS 10.15 (Catalina) or later
- 4 GB RAM minimum (8 GB recommended)
- 500 MB free disk space

**Note**: You may need to allow the application in System Preferences > Security & Privacy if you see a security warning.

## Rhino Grasshopper

EnergyAtlas is available as a plugin for Rhino 3D's Grasshopper visual programming environment.

**Get Rhino**: [Free 90-day trial](https://www.rhino3d.com/)

**Installation Steps**:
1. Install Rhino 3D (version 7 or later)
2. Open Grasshopper in Rhino
3. Install EnergyAtlas plugin via Package Manager:
   - Tools > Package Manager
   - Search for "EnergyAtlas"
   - Click Install
4. Restart Rhino/Grasshopper

**Documentation**: See [Technical References](../technical-references/technical-references.md) for Grasshopper-specific documentation.

## QGIS

*Coming soon*: EnergyAtlas plugin for QGIS

QGIS is a free and open-source Geographic Information System.

**Get QGIS**: [Download for free](https://qgis.org/)

**Status**: The QGIS plugin is currently in development. Check [EnergyAtlas.io](http://EnergyAtlas.io/) for updates.

## Python Package

*Coming soon*: EnergyAtlas Python API

Install via pip (when available):

```bash
pip install energyatlas
```

**Status**: The Python package is currently in development. Check [EnergyAtlas.io](http://EnergyAtlas.io/) for updates.

## RESTful API

*Coming soon*: Public RESTful API

Access EnergyAtlas functionality programmatically via HTTP requests.

**Status**: The public API is currently in development. Check [EnergyAtlas.io](http://EnergyAtlas.io/) for updates.

**For API access**: Contact us through [EnergyAtlas.io](http://EnergyAtlas.io/)

## Troubleshooting

### Installation Issues

**Windows**:
- Ensure you have administrator privileges
- Disable antivirus temporarily if installation is blocked
- Check Windows Event Viewer for error details

**macOS**:
- If you see "EnergyAtlas cannot be opened", go to System Preferences > Security & Privacy and click "Open Anyway"
- Ensure Gatekeeper allows applications from identified developers

**Grasshopper**:
- Verify Rhino version compatibility
- Check Grasshopper is up to date
- Restart Rhino after installation

### Getting Help

- **[FAQ](../resources/faq.md)** - Common questions and solutions
- **[GitHub Issues](https://github.com/Chengxuan-Li/EnergyAtlasWiki/issues/new)** - Report installation problems
- **[EnergyAtlas.io](http://EnergyAtlas.io/)** - Contact support

---

*Last updated: {{ version }}*
