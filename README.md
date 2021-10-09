An automation script to sync local folders with youtube playlists.

# HOW TO USE
After the setup run ```batser.py``` or ```sync_all.bat```     

# HOW TO SETUP
* Download and install youtube-dl.   
* Set the following path variables accordingly:    

| yps-mp3.py                     | sync_all.bat                       | yps.json | batser.py |
| ---                            | ---                                | --- | --- |
| YOUTUBE_DL_PATH = 'youtube-dl' | set PY_PATH= X:\PATH\TO\python.exe | "youtube_playlist": "PLAYLIST_URL_HERE" | path = "X:\PATH\TO\TOP\FOLDER" |
| CONFIG_FILENAME = 'yps.json'   | set SCRIPT_PATH= X:\PATH\TO\batser.py |                                      |     |
   
| sync.bat                           | 
| ---                                | 
| set PY_PATH= X:\PATH\TO\python.exe | 
| set SCRIPT_PATH= Y:\PATH\TO\yps-mp3.py |

* File structure:
```
 /top_folder/
            |-- sync_all.bat
            |-- batser.py
            |-- yps-mp3.py
            |
            |-- playlist_name_0/
            |                  |-- sync.bat
            |                  `-- yps.json
            |-- playlist_name_1/
            |                  |-- sync.bat
            |                  `-- yps.json
            |-- playlist_name_2/
                               |-- sync.bat
                               `-- yps.json
```
