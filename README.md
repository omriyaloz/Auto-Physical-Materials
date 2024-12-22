
# Auto Physical Materials Assigner for Unreal Engine

This tool automates the process of assigning physical materials to your Unreal Engine materials based on a dictionary of physical materials and their synonyms. It saves time and reduces the repetitive task of manually assigning physical materials to meshes in your level.

### What Are Physical Materials?

Physical materials in Unreal Engine define how an object interacts with the world physically. They affect various behaviors, such as:
- Visual effects like bullet hole decals
- Ballistics modeling (e.g., effects when an object is shot)
- Interaction sounds (e.g., footsteps, impacts)

To learn more about physical materials in Unreal Engine, visit the official [Unreal Engine Documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/tutorials-about-physical-materials-in-unreal-engine).

---

## Features

- Automatically assigns physical materials to materials on existing meshes within your level.
- Uses a dictionary (key-value pairs) stored in a `.json` file to map material names to their corresponding physical materials.
- Simple and flexible—requires only descriptive material names to function properly.
- A PyQt-based tool, **DictEditor.exe**, makes it easy to create and edit the dictionary of physical materials.
- Includes an **Editor Utility Blueprint (EUB)** with buttons to automatically assign and remove physical materials.

---

## Usage

1. **Configure the Tool**:  
   To get started, you’ll need to specify the path to your physical materials directory and the `.json` file containing the material mappings. By default, the `.json` file should reside in the same folder as the script (`AssignPhysMats.py`).

2. **Dictionary Setup**:  
   Use the **DictEditor.exe** tool to create and manage the dictionary of physical materials and their associated material names. The dictionary file should follow this format:
   - **Key**: Physical material name (e.g., `Metal`, `Wood`, `Concrete`).
   - **Value**: Material names that correspond to the physical material.
![image](https://github.com/user-attachments/assets/2f70fee5-eb86-45cb-a1a2-08d2b5245780)
   Once you're done, save the `.json` file.
   

4. **Assigning Physical Materials**:  
   After setting up the dictionary, open your level in Unreal Engine, select the materials in the content browser, and click on the "Auto Physical Materials" button in the EUB. The script will automatically assign the appropriate physical material to each selected material based on the dictionary.

5. **Removing Physical Materials**:  
   To remove the assigned physical materials, select the materials in the content browser and click on the "Remove Physical Materials" button.

---

## Demo

Here’s an example of the tool in action:

1. **Before**:  
   The materials in the level have no physical materials assigned:
   ![image](https://github.com/user-attachments/assets/5029bdb8-c4fd-4dd4-86e4-53ff6bc91322)

2. **Physical Materials Directory**:  
   The physical materials reside in the `/content/PhysicalMaterials` directory:
   ![image](https://github.com/user-attachments/assets/c4cb19a0-704a-46a5-b17e-f03785056580)

3. **Auto Assignment**:  
   After clicking the "Auto Physical Materials" button, the script processes the materials and assigns the correct physical materials. The output log will display the results:
   
   ![image](https://github.com/user-attachments/assets/628ed3b3-6b45-4678-b065-68e14522e861)

   One rock material was *wrongly* assigned the `Metal` physical material:
   ![image](https://github.com/user-attachments/assets/e91d53e4-76f3-4572-9748-7bfa0223cd52)

   The word Iron exists in the material name, so the script couldn't determine which physical material to assign.

---

## Limitations

- **Naming Convention**: The script relies on the material names being descriptive and follows a specific convention. If your material name contains ambiguous keywords (e.g., "Iron" for both metal and stone-like materials), the script may not assign the correct physical material. This may require a more careful naming strategy or manual adjustments.
- **UE4 Only**: This script is currently supported for Unreal Engine 4 (UE4). An update for Unreal Engine 5 (UE5) is planned.
- **Not Foolproof**: The tool works well for most cases but may not be perfect for all project setups. It's designed to save time and handle 80% of the assignment process.

---

## Important Notes

- **Physical Materials Directory**: Ensure the physical materials are placed in the correct directory (`/content/PhysicalMaterials` by default).
- **Editing Dictionary**: You can easily edit the `.json` dictionary at any time to add new mappings or adjust existing ones.
- **Customizing Paths**: The paths to the physical materials directory and dictionary file are customizable within the script. Make sure to adjust them based on your project structure.

---

## Requirements

- Unreal Engine 4
- Python (for running the `AssignPhysMats.py` script)
- PyQt (for the **DictEditor.exe** tool)

---

## License

This tool is open source and free to use for both personal and commercial projects. If you find it useful, feel free to contribute or modify it for your own needs.

---
