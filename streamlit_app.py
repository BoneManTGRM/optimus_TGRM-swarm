import streamlit as st
import time
import json
from optimus_tgrm_swarm_v2 import NexusSwarm, Agent

st.set_page_config(page_title="Nexus Swarm", page_icon="♻️", layout="wide")

st.title("♻️ Nexus Swarm — Live Demo")
st.markdown("""
**Heterogeneous Self-Repairing Agent Collective**  
*Reparodynamics in action — teacher broadcasting, RYE emergence, skill export.*
""")

with st.sidebar:
    st.header("Simulation Controls")
    n_agents = st.slider("Number of agents", 6, 24, 12, step=2)
    cycles = st.slider("Cycles to run", 5, 40, 15)
    speed = st.slider("Speed (seconds per cycle)", 0.0, 0.5, 0.08, step=0.02)
    run_button = st.button("Run Simulation", type="primary")

col1, col2 = st.columns(2)

if run_button:
    with st.spinner("Running Nexus Swarm..."):
        swarm = NexusSwarm(n_agents=n_agents)
        tasks = ['structural_repair', 'diagnostic_scan', 'coordination_sync', 'preventive_maintenance']

        progress_bar = st.progress(0)
        status_text = st.empty()

        history = []
        for i in range(cycles):
            metrics = swarm.step(tasks)
            history.append(metrics)
            progress_bar.progress((i + 1) / cycles)
            status_text.text(f"Cycle {i+1}/{cycles} | Avg RYE: {metrics['avg_rye']:.1f} | Energy: {metrics['avg_energy']:.1f}")
            time.sleep(speed)

        # Final results
        st.success("Simulation complete")

        # Metrics
        final_avg_rye = sum(a.repair_yield for a in swarm.agents) / len(swarm.agents)
        total_learned = sum(len(a.learned_behaviors) for a in swarm.agents)

        col1.metric("Final Average RYE", f"{final_avg_rye:.1f}")
        col2.metric("Behaviors Learned (Swarm)", total_learned)

        # Show recent history
        st.subheader("Recent Swarm Metrics")
        st.dataframe(history[-8:] if len(history) > 8 else history, use_container_width=True)

        # Export
        exported = swarm.export_skills("high_rye_skills.json")
        with open(exported) as f:
            skills_data = json.load(f)
        st.download_button("Download Exported Skills (JSON)", json.dumps(skills_data, indent=2), file_name=exported)

        st.caption("This swarm improved itself through coordinated repair. The future belongs to systems that do the same.")

else:
    st.info("Adjust parameters in the sidebar and click **Run Simulation** to watch the swarm evolve in real time.")
    st.markdown("""
    ### What you're seeing
    - **Heterogeneous agents** with different roles and specializations  
    - **Teacher broadcasting** of high-value behaviors  
    - **RYE (Repair Yield per Energy)** emergence over time  
    - **Skill export** — the collective wisdom, ready for persistence or transfer
    """)
