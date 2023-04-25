import os
from cdktf import TerraformStack
from cdktf_cdktf_provider_cloudflare.provider import CloudflareProvider
from cdktf_cdktf_provider_cloudflare.workers_kv import WorkersKv
from cdktf_cdktf_provider_cloudflare.workers_kv_namespace import WorkersKvNamespace
from constructs import Construct


class WorkersKvNamespaceStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        CLOUDFLARE_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
        CLOUDFLARE_API_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN")

        CloudflareProvider(
            self,
            "CloudflareProvider",
            api_token=CLOUDFLARE_API_TOKEN,
        )

        test_table = WorkersKvNamespace(
            self,
            "WorkersKvNamespace_test-table",
            title="test-table",
            account_id=CLOUDFLARE_ACCOUNT_ID,
        )

        for x in range(1, 4):
            WorkersKv(
                self,
                f"WorkersKv_key-value-pair-{x}",
                account_id=CLOUDFLARE_ACCOUNT_ID,
                namespace_id=test_table.id,
                key=f"test-key-{x}",
                value=f"test-value-{x}",
            )
