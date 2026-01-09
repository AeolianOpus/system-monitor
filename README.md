# Project structure
```
system_monitor/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── monitor/
│ ├── init.py
│ ├── system_monitor.py
│ └── stats.py
└── utils/
  ├── init.py
  ├── logger.py
  ├── ascii_graph.py
  ├── file_handler.py
  └── plotter.py
```

## Description

A Python CLI tool that displays your cpu, gpu, ram and disk usage. It includes functions as live auto refresh mode, both file and terminal logging, report export to file and configuration handling. Added some ascii graphics as well to make it look cooler.

## Installation

python -m venv venv  
source venv/bin/activate  (Windows: venv\Scripts\activate)  
pip install -r requirements.txt

## Run

python main.py