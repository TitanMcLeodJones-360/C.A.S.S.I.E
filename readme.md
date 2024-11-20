CASSIE/
│
├── main.py                          # Entry point of the application
├── utils/                           # Utilities folder
│   ├── typewriter.py                # Handles typewriter effect
│   └── auth.py                      # Handles user authentication
├── loading/                         # Loading and Configuration Module
│   ├── load_config.py               # Checks and initializes system details
│   ├── dashboard.py                 # GUI dashboard logic
│   └── gui_helpers.py               # Helper functions for GUI loading
├── storage/                         # Data Storage Module
│   ├── storage_management.py        # Manages storage organization
│   ├── perm/                        # Permanent storage
│   ├── ce/                          # Current activities storage
│   └── temp/                        # Temporary storage
├── memory_bank/                     # RAM Management Module
│   ├── ram_usage.py                 # Allocates and monitors RAM
│   ├── ram_check.py                 # Periodic RAM check logic
├── web/                             # Web and Notifications Module
│   ├── notifications_communications.py  # Handles notifications across modules
│   ├── universal_cookie_storage.py  # Manages cookies for browsers
│   ├── web_browser.py               # Browser functionality
│   ├── web_browser_settings.py      # Browser customization settings
├── diagnostics/                     # Diagnostic Module
│   ├── software_diagnostics.py      # Scans software for issues
│   ├── system_diagnostics.py        # System checks for RAM, CPU, etc.
│   ├── hardware_diagnostics.py      # Hardware diagnostics
├── standby/                         # Standby Mode Module
│   └── standby_mode.py              # Monitors and triggers standby mode
├── tools/                           # Tool Manager Module
│   ├── tool_manager.py              # Manages connected devices
│   └── tool_files/                  # Stores device configurations
├── ai/                              # AI and Command Processing
│   └── ai_command_processor.py      # Handles OpenAI command interpretation
├── logging/                         # Logging and Error Handling
│   ├── logging.py                   # Logs all activities
│   ├── error.py                     # Handles and logs errors
└── settings.py                      # Configuration for APIs and paths
