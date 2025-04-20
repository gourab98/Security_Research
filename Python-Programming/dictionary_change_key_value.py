
def invert_resource_dict(resource_dictionary):
    new_dictonary = {}
    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictonary:
                new_dictonary[resource].append(resource_group)
            else: new_dictonary[resource]= [resource_group]
    return(new_dictonary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], 
        "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}
