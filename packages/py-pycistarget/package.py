# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycistarget(PythonPackage):
    """pycistarget is a python module to perform motif enrichment analysis in sets of regions with different tools and identify high confidence TF cistromes."""

    url = "https://github.com/aertslab/pycistarget/archive/refs/tags/v1.0.2.tar.gz"

    version("1.0.2", sha256="71f7d79b17dc8e292e886dc651194dacf68f29ff9726c11cebeb4ca1b417c845")
    version("1.0.1", sha256="43ad36a8b148fca05d4f0130f642910d25f689bf85dcbc14735627616a48d5c8")
    version("1.0.0", sha256="9237d2dc585b88f2aedbe4549fc6a57ede33d36dd4dec3ad5e38ed0075c652ee")

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
