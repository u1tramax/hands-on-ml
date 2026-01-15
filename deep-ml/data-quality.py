def calculate_data_quality_score(data: list, schema: dict) -> dict:
    """
    Calculate data quality metrics for ML pipeline monitoring.
    
    Args:
        data: list of dictionaries representing rows of data
        schema: dictionary defining expected columns and their types
                {'column_name': {'type': 'numeric'|'categorical'|'boolean', 'nullable': True|False}}
    
    Returns:
        dict with keys: 'completeness', 'type_validity', 'uniqueness_ratio', 'overall_score'
        All values as percentages (0-100), rounded to 2 decimal places.
    """
    data_types = {'numeric': [int, float], 'categorical': [str], 'boolean': [bool]}
    unique = set()
    total_data = 0
    valid = 0
    nulls = 0
    for row in data:
        unique.add(tuple(row.items()))
        for column, validation in zip(row.values(), schema.values()):
            total_data += 1
            if column is None:
                nulls += 1
            if column is None and validation['nullable'] == True:
                valid += 1
            elif validation['type'] == 'numeric':
                if isinstance(column, int) or isinstance(column, float):
                    valid += 1
            elif validation['type'] == 'categorical':
                if isinstance(column, str):
                    valid += 1
            elif validation['type'] == 'boolean':
                if isinstance(column, bool):
                    valid += 1
    completeness = (1 - (nulls / total_data)) * 100
    type_validity = valid / total_data * 100
    uniqueness_ratio = len(unique) / len(data) * 100
    overall_score = completeness * 0.4 + type_validity * 0.4 + uniqueness_ratio * 0.2
    return {
        'completeness': round(completeness, 2),
        'type_validity': round(type_validity, 2),
        'uniqueness_ratio': round(uniqueness_ratio, 2),
        'overall_score': round(overall_score, 2)
    }

print(
    calculate_data_quality_score(
        [
            {'age': 25, 'name': 'Alice', 'active': True}, 
            {'age': 'thirty', 'name': 'Bob', 'active': False}, 
            {'age': None, 'name': None, 'active': True}, 
            {'age': 40, 'name': 'Dave', 'active': 'yes'}], 

        {
            'age': {'type': 'numeric', 'nullable': True}, 
            'name': {'type': 'categorical', 'nullable': True}, 
            'active': {'type': 'boolean', 'nullable': False}
        }
    )
)