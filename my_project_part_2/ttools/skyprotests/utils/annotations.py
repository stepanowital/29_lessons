from typing import Dict, List, Union


def get_union_annotations(
    *args: Dict[str, Union[str, List[Union[str, list]]]]
) -> Dict[str, List[str]]:
    base_annotation = args[0]
    annotations_count = len(args)
    for key in base_annotation:
        base_annotation[key] = [
            base_annotation[key],
        ]
    for index in range(1, annotations_count):
        next_annotation = args[index]
        for annotation in next_annotation:
            base_annotation[annotation].append(next_annotation[annotation])
    return base_annotation
