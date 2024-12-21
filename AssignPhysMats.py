import unreal
import json
import os


PHYS_MAT_PATH = '/Game/PhysicalMaterials'  # Path to your Physical Materials
JSON_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "material_mapping.json") # Path to your JSON config file (relative to the script's location)



def load_mapping_dict(json_path):

    try:
        with open(json_path, 'r') as f:
            mapping_dict = json.load(f)
        return mapping_dict
    except FileNotFoundError:
        unreal.log_error(f"Error: JSON file not found at {json_path}")
        return {}
    except json.JSONDecodeError:
        unreal.log_error(f"Error: Invalid JSON format in {json_path}")
        return {}
    
mapping_dict = load_mapping_dict(JSON_CONFIG_PATH)


physMats = []
EAL = unreal.EditorAssetLibrary
assetPaths = EAL.list_assets(PHYS_MAT_PATH)  

# Load the actual physical material assets
for assetPath in assetPaths:
    physMat = EAL.load_asset(assetPath)
    if physMat:
        physMats.append(physMat)

print("Physical Materials Detected:")
for pm in physMats:
    print(f"  - {pm.get_name()}")  # Prints the name of each loaded asset



def find_and_set_phys_mats():
    levelActors = unreal.EditorLevelLibrary.get_all_level_actors()
    physMatDict = {pm.get_name().lower().replace("physicalmaterial", ""): pm for pm in physMats}

    for levelActor in levelActors:
        if levelActor.get_class().get_name() == 'StaticMeshActor':
            staticMeshComponent = levelActor.static_mesh_component
            for mat in staticMeshComponent.get_materials():
                if mat is not None:
                    materialName = mat.get_name().lower()
                    mappedMaterial = map_material(materialName, mapping_dict) 
                    currentPhysMat = mat.get_editor_property('phys_material')
                    if mappedMaterial in physMatDict and currentPhysMat is None: 
                        unreal.log(f"Material {mat.get_name()} was set physical material: {physMatDict[mappedMaterial].get_name()}")
                        set_phys_mats(physMatDict[mappedMaterial], mat)
                        

                            

def set_phys_mats(physicalMaterial, material):
    with unreal.ScopedEditorTransaction("Assign Physical Material"):
        material.set_editor_property('phys_material', physicalMaterial) 


def remove_phys_mats():
    selected = unreal.EditorUtilityLibrary.get_selected_assets()  
    for asset in selected:
        if asset.get_class().get_name() == 'Material':
            print(f'Removed physical material from: {asset.get_name()}' )
            asset.set_editor_property('phys_material', None)


def map_material(word, mapping_dict):

    # Sort keys by the length of their longest synonym (descending)
    sorted_keys = sorted(mapping_dict.keys(), key=lambda k: max(len(s) for s in mapping_dict[k]), reverse=True)

    for material in sorted_keys:
        synonyms = mapping_dict[material]
        if any(synonym.lower() in word.lower() for synonym in synonyms):
            return material
    return word

find_and_set_phys_mats()


