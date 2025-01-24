from funpdbe_validator.validator import Validator
from funpdbe_validator.residue_index import ResidueIndexes

def run(filepath : str, resource_name : str = 'auto', verbose : bool = True) -> bool:
    """
    Basic example of running the PDBe-KB/FunPDBe validator
    :return:
    """
    validator = Validator(resource_name) # Same as in the JSON
    validator.load_schema()
    validator.load_json(filepath)
    if resource_name == 'auto':
        validator.resource = validator.json_data['data_resource']
    if not validator.basic_checks():
        if verbose: print("Did not pass the basic checks:\n" + validator.error_log)
        return False
    if not validator.validate_against_schema():
        if verbose: print("Did not pass the schema validation:\n" + validator.error_log)
        return False
    residue_indexes = ResidueIndexes(validator.json_data)
    if not residue_indexes.check_every_residue():
        if verbose: print("Did not pass the index validation:\n" + "\n".join(residue_indexes.mismatches))
        return False
    return False
