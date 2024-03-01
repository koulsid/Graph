metamodel_dict = {
    "nodes" : [
        {
            "type": "Person",
            "edges": ["Friends With", "Parent of", "Child of", "Sibling of", "Colleague of"],
        },
        {
            "type": "Pets",
            "edges": ["owned by"]
        }
    ],
    "edges": ["Friends With", "Parent of", "Child of", "Sibling of", "Colleague of"],
}