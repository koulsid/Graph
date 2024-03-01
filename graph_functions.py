import streamlit as st
import networkx as nx


def output_nodes_and_edges(graph:nx.Graph):
    st.write(graph.nodes)
    st.write(graph.edges)


def count_nodes(graph:nx.Graph):
    num_nodes = len(graph.nodes)
    num_nodes = graph.number_of_nodes()
    st.info(f"The graph has {num_nodes} nodes")


def find_density(graph:nx.Graph):
    density=nx.density(graph)
    st.info(f"The density of graph is {density}")


def check_path(graph:nx.Graph):
    node1_col, node2_col = st.columns(2)
    with node1_col:
        node1_select = st.selectbox("Select first node", options=graph.nodes, key="node1_select")
    with node2_col:
        node2_select = st.selectbox("Select second node", options=graph.nodes, key="node2_select")
    if node1_select and node2_select:
        if nx.has_path(graph, node1_select, node2_select):
            st.success(f"There is a path between node {node1_select} and node {node2_select}.")
        else:
            st.error(f"There is no path between node {node1_select} and node {node2_select}.")


def is_empty(graph:nx.Graph):
    is_empty=nx.is_empty(graph)
    if is_empty:
        st.info("The graph is empty.")
    else:
        st.info("The graph is not empty.")


def is_directed(graph:nx.Graph):
    is_directed=nx.is_directed(graph)
    if is_directed:
        st.info("The graph is directed.")
    else:
        st.info("The graph is not directed")
        

def specific_node(graph:nx.Graph):
    node_select = st.selectbox("Select node", options=graph.nodes, key="node_select")
    node=graph.nodes[node_select]
    st.info(node)


def show_shortest_paths(graph: nx.DiGraph):
    # Retrieve graph data from session state
    graph_dict_tree = st.session_state["graph_dict"]

    # Extract node and edge lists from the graph data
    node_list_tree = graph_dict_tree["nodes"]
    edge_list_tree = graph_dict_tree["edges"]

    # Initialize lists to store found nodes and edges related to the shortest paths
    node_list_tree_found = []
    edge_list_tree_found = []

    # Extract the names of nodes from the node list
    node_name_list_tree = [node["name"] for node in node_list_tree]

    # Present a selection box to choose the start node for calculating the shortest paths
    start_node_select_tree = st.selectbox(
        "Select the start node of the shortest paths",
        options=node_name_list_tree
    )
    # Present a selection box to choose the start node for calculating the shortest paths
    target_node_select_tree = st.selectbox(
        "Select the target node of the shortest paths",
        options=node_name_list_tree
    )

    # Present a button to trigger the calculation of shortest paths when clicked
    is_tree_button = st.button("Calculate trees", use_container_width=True, type="primary")

    # If the button is clicked
    if is_tree_button:
        # Calculate the shortest paths using NetworkX's shortest_path function
        tree_list = nx.shortest_path(graph, source=start_node_select_tree, target=target_node_select_tree, weight="dist")

        # Check if any shortest paths exist from the selected start node
        if not tree_list:
            st.write(f"There is no tree starting from {start_node_select_tree}.")
        else:
            # Iterate through each tree in the list of shortest paths
            for tree in tree_list:
                st.write(f"The node {tree} is a member of the tree")
                # For each node in the tree, identify the corresponding node data from the original node list
                for tree_element in tree:
                    for node_element in node_list_tree:
                        if node_element["name"] == tree_element:
                            to_be_assigned_element = node_element
                            # Add the node to the list of found nodes if it's not already there
                            print(node_element)
                            if to_be_assigned_element not in node_list_tree_found:
                                node_list_tree_found.append(node_element)

            # Iterate through each edge in the original edge list
            for edge_element in edge_list_tree:
                for source_node in node_list_tree_found:
                    for sink_node in node_list_tree_found:
                        # Check if both source and sink nodes of the edge are in the list of found nodes
                        if edge_element["source"] == source_node["name"] and edge_element["target"] == \
                                sink_node["name"]:
                            # Add the edge to the list of found edges
                            edge_list_tree_found.append(edge_element)

            # Display the graph without considering the weights of the edges
            show_graph_without_weights(node_list_tree_found, edge_list_tree_found)


# Function to display the graph without considering edge weights
def show_graph_without_weights(nodes, edges):
    def set_color(node_type):
        color = "Grey"
        if node_type=="Person":
            color="Blue"
        elif node_type=="Node":
            color="Green"
        return color
    import graphviz
    graph = graphviz.Digraph()
    for node in nodes:
        node_name = node["name"]
        graph.node(node_name, color=set_color(node["type"]))
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        label = edge["type"]
        graph.edge(source, target, label)
    st.graphviz_chart(graph)


def shortest_path(graph: nx.Graph):
    import graphviz
    node1_col, node2_col = st.columns(2)
    with node1_col:
        node1_select = st.selectbox("Select first node",
        options=graph.nodes,
        key="node1_select")
    with node2_col:
        node2_select = st.selectbox("Select second node",
                                    options=graph.nodes,
                                    key="node2_select")
    try:
        shortest_path_for_graph = nx.shortest_path(graph,node1_select, node2_select)
        st.success(f"The shortest path between {node1_select} "
                   f"and {node2_select} is {shortest_path_for_graph}")
        st.write(shortest_path_for_graph)
        subgraph=graph.subgraph(shortest_path_for_graph)
        graphviz_graph=graphviz.Digraph()
        st.write(subgraph.edges)
        for node in subgraph.nodes:
            graphviz_graph.node(str(node))
            # Add edges to the Graphviz object

        for edge in subgraph.edges:
            graphviz_graph.edge(str(edge[0]), str(edge[1]))
        st.graphviz_chart(graphviz_graph)
    except nx.NetworkXNoPath:
        st.error(f"There is no path between {node1_select} and {node2_select}")