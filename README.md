# Packet Labs AppConfig

This is a very simple web tool to build iPXE templates for various complex applications that can be deployed on Packet. There is a small list of applications currently supported:

## esxicfg

*Configuration Tool for ESXi*

Currently the only application. Has some work left. Allows customizing an ESXi installation based on a few questions. Currently supports changing SSH configuration, and Network options.

TODO:

- URLs of files to download into the default datastore during install
- Ability to choose different ESXi versions

## About iPXE at Packet

Packet supports passing custom iPXE scripts during provisioning, which allows you to install a custom operating system manually, or via automated kickstart. For details, see the [Custom iPXE](https://support.packet.com/kb/articles/custom-ipxe) 
article in the Packet knowledgebase.
