# SimpleImport

Sublime Text plugin which adds python import statement to the beginning of the current file for selected classes and methods

# Supported Languages

Python

# Dependencies

This plugin requires `ripgrep` which you can install following the instructions here: https://github.com/BurntSushi/ripgrep#installation

# Installation

To enable this plugin do the following: 
1. cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
2. git clone https://github.com/puhtreeseeya/SimpleImport.git
3. In sublime, click the menus Sublime Text → Preferences → Package Settings → Simple Import → Settings - User
4. Replace the file with the following contents 
```
{
    "root_path": $ABSOLUTE_PATH_PROJECT_DIRECTORY,
    "search_paths": []
}
```
5. If you want to omit a directory from the import path then add the directory to search_paths. 

If you have a resource at $ABSOLUTE_PATH_PROJECT_DIRECTORY/src/folder_a/folder_b/example.py and the desired import statement is this format `from folder_a.folder_b import example`, then add the absolute path to the src folder into `search_paths`. It should look like the following:
```
{
  "root_path": $ABSOLUTE_PATH_PROJECT_DIRECTORY,
  "search_paths": [$ABSOLUTE_PATH_PROJECT_DIRECTORY/src]
} 
```

# Usage

1. Highlight the class or method that you want to import
2. Press `cmd+d` 
