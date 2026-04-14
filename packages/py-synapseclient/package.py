# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySynapseclient(PythonPackage):
    """Python client for Synapse, the collaborative research data platform."""

    homepage = "https://www.synapse.org"
    pypi = "synapseclient/synapseclient-4.12.0.tar.gz"

    license("Apache-2.0")

    version("4.12.0", sha256="3c08a5a1eb9454ab5b88c58a25fd7b1119a9d2cd88a1ac1f2fca384e2f534f37")

    depends_on("python@3.10:3.14", type=("build", "run"))
    depends_on("py-setuptools@80.10.1:", type="build")

    depends_on("py-requests@2.22:2", type=("build", "run"))
    depends_on("py-urllib3@2.6.3:", type=("build", "run"))
    depends_on("py-deprecated@1.2.4:1", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.33.0:", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.33.0:", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-http@1.33.0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation-httpx@0.54b0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation-requests@0.54b0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation-threading@0.54b0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation-urllib@0.54b0:", type=("build", "run"))
    depends_on("py-opentelemetry-util-http@0.54b0:", type=("build", "run"))
    depends_on("py-nest-asyncio@1.6:", type=("build", "run"))
    depends_on("py-asyncio-atexit@1.0.1:", type=("build", "run"))
    depends_on("py-httpx@0.27:", type=("build", "run"))
    depends_on("py-httpcore@1.0.9:", type=("build", "run"))
    depends_on("py-tqdm@4.66.2:", type=("build", "run"))
    depends_on("py-async-lru@2.0.4:", type=("build", "run"))
    depends_on("py-psutil@5.9.8:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import synapseclient")
