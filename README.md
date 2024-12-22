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

I simply click on Auto Physical Materials button, which calls the function find_and_set_phys_mats()

![image](https://github.com/user-attachments/assets/7c962496-5a7d-44ea-a2cb-a955bec3754a)

Output Log:

![image](https://github.com/user-attachments/assets/628ed3b3-6b45-4678-b065-68e14522e861)

![image](https://github.com/user-attachments/assets/27378a08-2317-4489-92f4-41789f0462bb)


Notice how one rock material was set a metal physical material:
![image](https://github.com/user-attachments/assets/e91d53e4-76f3-4572-9748-7bfa0223cd52)

That's the main flaw in this tool- the word Iron exists in the material name and so the script couldn't determine which physical material to assign.
In this case, either a more careful naming convention is required, or manual tweak.
The tool isn't 100% foolproof and it is designed to take you 80% of the way.

To easily remove physical materials (for whatever reason)- select the materials *in the content browser* and click the remove button:

![image](https://github.com/user-attachments/assets/0873cef4-533e-40eb-87ad-7f277d47afb6)





##Important Notes:

This script is currently only supported for UE4. 
I plan to update for UE5 soon.

As mentioned, the script isn't foolproof and uses a simple algorithm that heavily relies on your file naming conventions. Use with caution.




