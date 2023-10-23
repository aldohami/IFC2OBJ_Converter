import ifcopenshell
import os
import trimesh
import open3d as o3d
from ifcopenshell import geom



def print_found_ifc_files(directory_path):
    found_ifc_files = []
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.ifc'):
                ifc_file_path = os.path.join(root, file)
                found_ifc_files.append(ifc_file_path)
                
    return found_ifc_files



def ifc_to_obj(ifc_file_path):
    ifc_file = ifcopenshell.open(ifc_file_path)

    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)

    # Extract the name of the IFC file (excluding the extension)
    ifc_file_name = os.path.splitext(os.path.basename(ifc_file_path))[0]

    # Create a new directory for OBJ files
    obj_dir = os.path.join(os.path.dirname(ifc_file_path), f"{ifc_file_name}_obj")
    os.makedirs(obj_dir, exist_ok=True)

    for index, entity in enumerate(ifc_file):
        if hasattr(entity, "Representation") and entity.Representation:
            coordinates = []

            shape = ifcopenshell.geom.create_shape(settings, entity)
            geo = shape.geometry

            ifc_vertices = geo.verts
            ifc_edges = geo.edges
            ifc_faces = geo.faces

            a = 0
            while a < len(ifc_vertices):
                local_coord_vertices = [ifc_vertices[a], ifc_vertices[a + 1], ifc_vertices[a + 2]]
                coordinates.append(local_coord_vertices)
                a += 3

            edges = [ifc_edges[i: i + 2] for i in range(0, len(ifc_edges), 2)]
            faces = [tuple(ifc_faces[i: i + 3]) for i in range(0, len(ifc_faces), 3)]

            mesh = trimesh.Trimesh(vertices=coordinates, faces=faces, process=False)

            mesh_o3d = mesh.as_open3d
            obj_name = os.path.join(obj_dir, f"entity_{index:04d}.obj")
            o3d.io.write_triangle_mesh(obj_name, mesh_o3d)


if __name__ == "__main__":
    directory_path = r"C:\Users\omar\Documents\omar_pcd_segmentation\bridge_examples\Finished\IFC\test"
    found_files = print_found_ifc_files(directory_path)
    
    for ifc_file_path in found_files:
        print("Processing:", ifc_file_path)
        ifc_to_obj(ifc_file_path)
