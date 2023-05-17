# city = input("Shahar nomini kiriting ")

# city = 'Tashkent'
# import requests
# import json

# url = "https://api.openweathermap.org/data/2.5/weather?q=" 
# + city + "&units=imperial&appid=895284fb2d2c50a520ea537456963d9c"

# sorov = requests.get(url).json()
{
  "include": [
    "src"
  ],
  
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    "src/experimental",
    "src/typestubs"
  ],

  "ignore": [
    "src/oldstuff"
  ],

  "defineConstant": {
    "DEBUG": True
  },

  "stubPath": "src/stubs",
  "venv": "env367",

  "reportMissingImports": True,
  "reportMissingTypeStubs": False,

  "pythonVersion": "3.6",
  "pythonPlatform": "Linux",

  "executionEnvironments": [
    {
      "root": "src/web",
      "pythonVersion": "3.5",
      "pythonPlatform": "Windows",
      "extraPaths": [
        "src/service_libs"
      ]
    },
    {
      "root": "src/sdk",
      "pythonVersion": "3.0",
      "extraPaths": [
        "src/backend"
      ]
    },
    {
      "root": "src/tests",
      "extraPaths": [
        "src/tests/e2e",
        "src/sdk"
      ]
    },
    {
      "root": "src"
    }
  ]
}
import requests







