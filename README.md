# IFC to OBJ Converter

This Python script is designed for converting IFC (Industry Foundation Classes) files, commonly used in the construction and architecture industry, into OBJ (Wavefront Object) files, a versatile 3D model format. This conversion is valuable for tasks like 3D visualization, analysis, or integration with other 3D software.

## How it works

- The script starts by searching for IFC files in the specified directory and its subdirectories using the `print_found_ifc_files` function. It compiles a list of discovered IFC file paths.

- For each found IFC file, the script performs the following conversion:

  - It uses the `ifcopenshell` library to open and read the IFC file.
  
  - Geometric settings are configured, including the use of world coordinates.
  
  - The script iterates through the IFC entities, checks for representation data, and extracts relevant 3D geometry information.
  
  - This geometry data is converted into a 3D mesh using the `trimesh` library.
  
  - The 3D mesh is further processed and converted to an Open3D mesh.
  
  - The OBJ file format is used to save the 3D mesh in a new directory named after the IFC file.

## Key Features

- Handles the entire conversion process from IFC to OBJ, including directory creation and file naming.
  
- Organizes OBJ files in separate directories for each IFC file, ensuring a structured output.
  
- Detects IFC files in the specified directory and its subdirectories, making it versatile for various project structures.
  
- The code is well-documented and provides clear functions for finding IFC files and performing the conversion.

## Usage

1. Place your IFC files in the specified directory.
  
2. Set the `directory_path` variable to the path where your IFC files are located.
  
3. Run the script, and it will process the IFC files and generate OBJ files in separate directories for each IFC file.

This script can be a valuable tool for individuals or teams working with IFC data who need to convert it into a more widely supported 3D format.
