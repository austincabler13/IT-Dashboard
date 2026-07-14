# Architecture

IT Dashboard uses a layered architecture so the user interface remains separate from operating-system and hardware access.

## Request Flow

```text
Frontend
    ↓
PyWebView JavaScript API
    ↓
API layer
    ↓
System modules
    ↓
Windows and operating-system data
```

## Layer Responsibilities

### Frontend

The frontend is responsible for rendering the interface, handling navigation, receiving user input, and displaying data returned by the backend.

The frontend never talks directly to hardware or operating-system modules. All requests go through the API layer.

### PyWebView Window Layer

The window layer starts the desktop application, loads the local frontend, and exposes the Python API object to JavaScript.

### API Layer

The API layer is the controlled communication boundary between JavaScript and Python. It receives frontend requests, delegates work to the appropriate backend module, and returns structured results.

### System Modules

System modules collect information from Windows and the operating system. Future modules may cover hardware, networking, storage, services, event logs, devices, and users.

System modules should not contain frontend rendering logic.

### Plugins

The plugin system is a future feature. Plugin interfaces will be designed after the core API and application behavior become stable.

## Data Design

Backend methods should return structured data whenever possible rather than preformatted interface text. The frontend is responsible for deciding how that data is displayed.

Example:

```python
{
    "name": "Example CPU",
    "physical_cores": 6,
    "logical_processors": 12
}
```

## Design Principles

- Keep frontend rendering separate from system-data collection.
- Route frontend requests through the API layer.
- Keep modules focused on one responsibility.
- Prefer structured responses that are easy to test and reuse.
- Consider performance, usability, maintainability, and security when adding features.
