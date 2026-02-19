# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPartipy(PythonPackage):
    """Pareto Task Inference in Python (ParTIpy)."""

    homepage = "https://github.com/saezlab/ParTIpy"
    url = "https://github.com/saezlab/ParTIpy/archive/refs/tags/v0.2.0.tar.gz"

    license("GPL-3.0-only")

    version("0.2.0", sha256="cde37811bc237e0372d72f731a3fcddbec69200628adbdac3b44000710f1b726")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-decoupler@2.0.0:", type=("build", "run"))
    depends_on("py-dcor", type=("build", "run"))
    depends_on("py-nbformat", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-plotnine", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-pydantic@2.10:", type=("build", "run"))
    depends_on("py-session-info2", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pybiomart", type=("build", "run"))
    depends_on("py-squidpy", type=("build", "run"))
    depends_on("py-liana", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import partipy")
