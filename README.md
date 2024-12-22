##Description

Automatically assign physical materials in your UE4 projects, based on a dictionary of materials (keys) and their corresponding synonyms.
Helps save valuable time and mitigate the repetitive task of assigning physical materials to your materials.


What are physical materials?

Physical materials are used to define the response of a physical object when interacting dynamically with the world.
Commonly used for visual responses like bullethole decals, ballistics modeling when shot at, interaction sounds and more.
To learn more about physical materials in Unreal: https://dev.epicgames.com/documentation/en-us/unreal-engine/tutorials-about-physical-materials-in-unreal-engine
 

##Usage

The tools is simple- It assigns physical-materials to materials on existing meshes in your level,
so as long as you give descriptive names to your materials, it will know which physical material to assign to each of your materials.
It pulls key-value pairs from a python dictionary, which conveniently exists in a .json file.
![image](https://github.com/user-attachments/assets/0c2841c9-2831-44c1-83e5-ea1e8efd676c)

The only thing you might need to change is the path to your physical materials directory and the path to your json file. 
By default, the json file should exist where AssignPhysMats.py resides.

DictEditor.exe is a tool I created with PyQt to easily create and edit dictionaries:
![image](https://github.com/user-attachments/assets/2f70fee5-eb86-45cb-a1a2-08d2b5245780)

The Key column is for your physical material name, and the Value column is for the potential material names associated with that physical material.
Once you've created your dictionary, save the .json file and you're done. You or your team can always go back and modify the json file according to your project needs.

I created an Editor Utility Blueprint (EUB) with buttons for assigning physical materials and removing physical materials:
![image](https://github.com/user-attachments/assets/eb80ffb9-2b5f-4e1f-a7fe-f5a83cf7fbf2)

Let's test this out on a demo scene I put together using a free materials pack:
![image](https://github.com/user-attachments/assets/5029bdb8-c4fd-4dd4-86e4-53ff6bc91322)


Note none of these materials currently have a physical material assigned to them.

My physical materials reside in /content/PhysicalMaterials as such:
![image](https://github.com/user-attachments/assets/c4cb19a0-704a-46a5-b17e-f03785056580)






##Important Notes:





