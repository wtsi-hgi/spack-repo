# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLoomxpy(PythonPackage):
    """Python package (compatible with SCope) to create .loom files and extend them with other data e.g.: SCENIC regulons."""

    homepage = "https://github.com/aertslab/LoomXpy"
    pypi = "loomxpy/loomxpy-0.4.2.tar.gz"

    version("0.4.2", sha256="b23f031c3efb6115a2a231de5f554d0c15ae794d661c3daf39d44dd267cce851", expand=False, url="https://files.pythonhosted.org/packages/ef/1c/503108d76021b7f73ed6f445baecbd2bd07e48db8f0f5888bc65c2c7d71c/loomxpy-0.4.2-py3-none-any.whl")

    depends_on("py-loompy@3.0.7", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyscenic@0.12.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.22.2:", type=("build", "run"))
    depends_on("py-ctxcore@0.2.0:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import loomxpy")
