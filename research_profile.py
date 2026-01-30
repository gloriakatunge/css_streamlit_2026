#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:55:48 2026
@author: gloria
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np       # <--- Add this line!
# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Gloria Katunge | Research Profile", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
# Step 1: Added "Contact" to this list
selection = st.sidebar.radio("Go to:", ["Home", "Data Lab", "Projects", "Technical Stack", "Contact"])

# --- 🏠 HOME SECTION ---
if selection == "Home":
    st.title("Gloria Katunge | Computational Physicist & Solar Engineer")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("Gemini_Generated_Image_tn8dmwtn8dmwtn8d.png", use_container_width=True)
       
    with col2:
        st.header("About Me")
        st.write("""
        PhD candidate specializing in condensed matter physics, with a focus on computational research. 
        My academic journey in Physics has been deeply intertwined with my passion 
        for solar energy applications. Currently, 
        I am exploring the fascinating realm of optoelectronics,working on computational study to enhance PV performance t
        hrough band gap engineering of novel perovskite materials.
        Beyond my academic pursuits,I am a licensed solar technician with hands-on experience in installing, maintaining, 
        and optimizing solar energy systems. My work in the field combined with my research fuels my mission to 
          bring reliable, clean energy solutions to communities.
        """)
        st.subheader("Research Focus")
        st.write("Optoelectronics, Band Gap Engineering, and PV performance optimization.")
# --- 📊 DATA LAB SECTION ---
elif selection == "Data Lab":
    st.header("Interactive Material Science Lab")
    # 1. Initialize memory with your actual convergence data 
    if 'research_data' not in st.session_state or not st.session_state['research_data']:
        # Real data from your ecut.dat file 
        ecut_data = pd.DataFrame({
            "Energy": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
            "Total Energy": [-280.1081, -281.1406, -281.3417, -281.3639, 
                            -281.3653, -281.3656, -281.3657, -281.3658, 
                            -281.3660, -281.3661, -281.3661, -281.3661]
        })
        st.session_state['research_data'] = [{"name": "Total Energy vs Ecut)", "data": ecut_data}]

    # 2. Upload Section
    with st.expander("📤 Add More Research Data"):
        new_files = st.file_uploader("Upload CSVs", type=["csv", "dat"], accept_multiple_files=True)
        if new_files:
            for f in new_files:
                # Basic parsing for .dat or .csv
                new_df = pd.read_csv(f, sep=r'\s+', names=["Energy", "Total Energy"]) if f.name.endswith('.dat') else pd.read_csv(f)
                st.session_state['research_data'].append({"name": f.name, "data": new_df})
            st.success("Data added to lab memory!")

    # 3. Visualization
    st.subheader("Visualize Convergence OPtimization")
    all_names = [item['name'] for item in st.session_state['research_data']]
    selected_materials = st.multiselect("Select datasets to plot:", options=all_names, default=all_names[0])

    if selected_materials:
        fig, ax = plt.subplots(figsize=(10, 5))
        for item in st.session_state['research_data']:
            if item['name'] in selected_materials:
                df = item['data']
                # Automating axis labels based on column names [cite: 1, 17]
                x_col = df.columns[0]
                y_col = df.columns[1]
                ax.plot(df[x_col], df[y_col], marker='+', label=item['name'], linewidth=2)
                
                ax.set_xlabel("Ecutwfc (Ry)", fontweight='bold')
                ax.set_ylabel("Total Energy (eV)", fontweight='bold')
        
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig)
elif selection == "Projects & Publications":
    st.header("Current Projects & Impact")
    # ... your existing code ...

# --- 📚 PROJECTS & PUBLICATIONS ---
elif selection == "Projects":
    st.header("Current Projects")
    
    with st.expander("🇬🇭 Digitizing Ghana's Parliamentary Registers (Hansard)"):
        st.write("Currently in the prototype stage, this project involves transforming locked PDF Hansards into searchable digital formats.")

    with st.expander("☀️ Solar Water Pump Systems"):
        st.write("Developing technical manuals and training materials for solar training.")

# --- 🛠️ TECHNICAL STACK SECTION ---
elif selection == "Technical Stack":
    st.header("The Computational Stack")
    
    st.subheader("Core Competencies")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Simulation & Physics**")
        st.code("Quantum ESPRESSO\nSolar  PV design, sizing, installation, and maintenance\nDFT Formalism\nPVsyst")
    with col_b:
        st.write("**Data & Deployment**")
        st.code("Python (Pandas,numpy,Matplotlib....)\nLinux/HPC Cluster")

# --- 📞 CONTACT SECTION ---
elif selection == "Contact":
    st.header("Get In Touch")
    st.write("I am open to collaborations in computational materials science, renewable energy research, and data science projects.")
    
    # Using columns for a clean layout
    col_info, col_links = st.columns(2)
    
    with col_info:
        st.subheader("Direct Contact")
        st.write("📧 **Email:** gloriakatunge133@gmail.com")
        st.write("📞 **Phone:** +254 797 334 169") # Insert your number here
        st.write("📍 **Location:** University of Nairobi, Kenya")

    with col_links:
        st.subheader("Professional Network")
        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/gloria-katunge?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BSVf9TIFdRs2fW%2FKg23lX0w%3D%3D)")
       

   
