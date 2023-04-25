import cdktf
from stacks.workers_kv_namespace_stack import WorkersKvNamespaceStack

app = cdktf.App()

WorkersKvNamespaceStack(
    app,
    "WorkersKvNamespaceStack",
)

app.synth()
