import unreal

def get_selected_assets():
    """Get all currently selected assets in the content browser."""
    editor_util = unreal.EditorUtilityLibrary()
    return editor_util.get_selected_assets()

def duplicate_asset(asset_path, new_name):
    """Duplicate an asset with a new name."""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    original_asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    if original_asset:
        return asset_tools.duplicate_asset(new_name, original_asset.get_path_name(), original_asset)
    return None

def get_asset_dependencies(asset_path):
    """Get all dependencies of an asset."""
    return unreal.EditorAssetLibrary.find_package_referencers_for_asset(asset_path)

def bulk_rename_assets(search_pattern, replace_pattern):
    """Rename multiple assets based on a search and replace pattern."""
    selected_assets = get_selected_assets()
    for asset in selected_assets:
        old_name = asset.get_name()
        new_name = old_name.replace(search_pattern, replace_pattern)
        if new_name != old_name:
            asset_path = asset.get_path_name()
            new_path = asset_path.replace(old_name, new_name)
            unreal.EditorAssetLibrary.rename_asset(asset_path, new_path) 