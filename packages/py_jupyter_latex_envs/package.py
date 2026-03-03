# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJupyterLatexEnvs(PythonPackage):
    """Jupyter notebook extension adding LaTeX environments, theorem-style
    blocks, bibliography support, cross referencing, and custom exporters."""

    homepage = "https://github.com/jfbercher/jupyter_latex_envs"
    pypi = "jupyter_latex_envs/jupyter_latex_envs-1.4.6.tar.gz"

    license("BSD-3-Clause")

    version("1.4.6", sha256="070a31eb2dc488bba983915879a7c2939247bf5c3b669b398bdb36a9b5343872")

    depends_on("py-setuptools", type="build")
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-jupyter-core", type=("build", "run"))
    depends_on("py-nbconvert", type=("build", "run"))
    depends_on("py-notebook@4.0:", type=("build", "run"))
    depends_on("py-traitlets@4.1:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import latex_envs")
