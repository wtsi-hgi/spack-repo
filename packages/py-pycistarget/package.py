# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycistarget(PythonPackage):
    """pycistarget is a python module to perform motif enrichment analysis in sets of regions with different tools and identify high confidence TF cistromes."""

    git = "https://github.com/aertslab/pycistarget.git"

    version("1.0.2", tag="v1.0.2")
    version("1.0.1", tag="v1.0.1")
    version("1.0.0", tag="v1.0.0")

    depends_on("py-setuptools", type="build")

    depends_on("py-ctxcore", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandoc", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyranges", type=("build", "run"))
    depends_on("py-pybiomart", type=("build", "run"))
    depends_on("py-ray", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    #depends_on("py-typing", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))
    depends_on("py-nbsphinx-link", type=("build", "run"))
    depends_on("py-numpydoc", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
