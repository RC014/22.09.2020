import plotly.graph_objects as go

a=True
b=False
c=True
d=False

and1=a and a
and2=b and a
and3=a and b
and4=b and b

or1=a or a
or2=b or a
or3=a or b
or4=b or b

notx1=not a
notx2=not b
notx3=not a
notx4=not b

noty1=not a
noty2=not a
noty3=not b
noty4=not b

fig = go.Figure(data=[go.Table(header=dict(values=['X', 'Y', 'AND', 'OR', 'NOT X', 'NOT Y']),
                 cells=dict(values=[[a,b,a,b], [a,a,b,b], [and1,and2,and3,and4],[or1,or2,or3,or4],[notx1,notx2,notx3,notx4],[noty1,noty2,noty3,noty4]]))
                     ])
fig.show()
