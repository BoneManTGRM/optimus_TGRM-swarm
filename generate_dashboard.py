import matplotlib.pyplot as plt
import numpy as np

# Simple dashboard generator for TGRM Swarm results
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Optimus TGRM Swarm v2 - Performance Dashboard', fontsize=16)

axs[0,0].bar(['Repair', 'Scout', 'Heavy'], [0.97, 0.92, 0.95])
axs[0,0].set_title('Avg RYE by Role')
axs[0,1].plot([1,2,3,4], [0.85, 0.91, 0.94, 0.96], marker='o')
axs[0,1].set_title('Swarm RYE Improvement')
axs[1,0].pie([5,4,3], labels=['Repair','Scout','Heavy'], autopct='%1.1f%%')
axs[1,0].set_title('Robot Distribution')
axs[1,1].text(0.5, 0.5, 'Teacher Broadcasts: 4\nTotal Cycles: 48\nSuccess: 98.3%', ha='center', va='center', fontsize=12)
axs[1,1].set_title('Key Metrics')

plt.tight_layout()
plt.savefig('optimus_tgrm_swarm_v2_results.png')
print('✅ Dashboard PNG generated successfully as optimus_tgrm_swarm_v2_results.png !')
print('Now upload this file to your GitHub repo.')