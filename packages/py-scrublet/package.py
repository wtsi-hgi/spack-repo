# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScrublet(PythonPackage):
    """https://files.pythonhosted.org/packages/bf/f8/52cecc93d2ac7b7ffe53662b60c34b2ad7f97eed7360e3d264080f8b1608/scrublet-0.2.3.tar.gz"""

    homepage = "https://github.com/swolock/scrublet"
    pypi = "scrublet/scrublet-0.2.3.tar.gz"

    version("0.2.3", sha256="2185f63070290267f82a36e5b4cae8c321f10415d2d0c9f7e5e97b1126bf653a")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-annoy", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
