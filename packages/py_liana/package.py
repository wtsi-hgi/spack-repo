# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLiana(PythonPackage):
    """LIANA+: a one-stop-shop framework for cell-cell communication."""

    homepage = "https://github.com/saezlab/liana-py"
    pypi = "liana/liana-1.7.1.tar.gz"

    license("BSD-3-Clause")

    version("1.7.1", sha256="85cc3bf19e7562eb76d396e8318cf13ec884998b15188791aadfce9cadd598dd")

    depends_on("python@3.10:3.13", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-anndata@0.7.4:", type=("build", "run"))
    depends_on("py-mudata", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-tqdm@4.0:", type=("build", "run"))
    depends_on("py-docrep@0.3.1:", type=("build", "run"))
    depends_on("py-plotnine@0.10.1:", type=("build", "run"))
    depends_on("py-session-info2", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import liana")
