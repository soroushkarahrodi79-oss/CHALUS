import json
import matplotlib.pyplot as plt

r=json.load(open('gate2a_results.json'))
fig,axes=plt.subplots(1,2,figsize=(14,7),sharex=True,sharey=True)
colors={'south':'#d62728','east':'#1f77b4','west':'#2ca02c'}
for ax,field,title in [(axes[0],'base_edges','Baseline 12 Jun 2024'),(axes[1],'closure_edges','Bounded Darband closure')]:
    for key,v in r.items():
        gw,dst=key.split('-')
        # Each edge only contains node ids, recover coordinates from serialized node list via separate graph not available.
        # Plot from edge endpoints is added below by rebuilding node coordinates.
    ax.set_title(title); ax.grid(alpha=.2); ax.set_aspect('equal',adjustable='box')

from gate2a_reconcile import build_graph
h,g=build_graph('june_reconciled_partial.osm')
for ax,field in [(axes[0],'base_nodes'),(axes[1],'closure_nodes')]:
    for key,v in r.items():
        gw,dst=key.split('-')
        xs=[g.nodes[n]['lon'] for n in v[field]]; ys=[g.nodes[n]['lat'] for n in v[field]]
        ax.plot(xs,ys,color=colors[gw],alpha=.55,lw=1.2,label=gw if dst=='chalus' else None)
        ax.scatter([xs[0],xs[-1]],[ys[0],ys[-1]],s=12,color=colors[gw])
for ax in axes: ax.legend(title='Gateway'); ax.set_xlabel('Longitude')
axes[0].set_ylabel('Latitude')
fig.tight_layout(); fig.savefig('gate2a_routes_qa.png',dpi=180)
