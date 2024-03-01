import streamlit as st
import json
from streamlit_option_menu import option_menu
from tabs import (upload_graph,
                  create_nodes,
                  create_relations,
                  store_graph,
                  visualize_graph,
                  analyze_graph, export_graph)

if __name__ == '__main__':
    if "node_list" not in st.session_state:
        st.session_state["node_list"] = []
    if "edge_list" not in st.session_state:
        st.session_state["edge_list"] = []
    if "graph_dict" not in st.session_state:
        st.session_state["graph_dict"] = []
    tab_list = [
        "Import Graph",
        "Create Nodes",
        "Create Relations",
        "Store the Graph",
        "Visualize the Graph",
        "Analyze the Graph",
        "Export the Graph"
     ]

    st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    with st.sidebar:
        selected_tab = option_menu("Main Menu",
                                   tab_list,
                                   icons=['house', 'gear', "arrow-clockwise"],
                                   menu_icon="cast",
                                   default_index=0,
                                   orientation="vertical"
                                   )

    #selected_tab = option_menu("Main Menu",
     #                  tab_list,
      #                 icons=['house', 'gear', "arrow-clockwise"],
       #                menu_icon="cast",
        #               default_index=1,
         #                      orientation = "horizontal"
          #                  )

    st.title("PyInPSE Tutorial 1")

    if selected_tab == "Import Graph":
        upload_graph()

    if selected_tab == "Create Nodes":
        create_nodes()

    if selected_tab == "Create Relations":
        create_relations()

    if selected_tab == "Store the Graph":
        store_graph()

    if selected_tab == "Visualize the Graph":
        visualize_graph()

    if selected_tab == "Analyze the Graph":
        analyze_graph()

    if selected_tab == "Export the Graph":
        export_graph()









