# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGlimixCore(PythonPackage):
    """Fast inference over mean and covariance parameters for Generalised Linear Mixed Models."""

    homepage = "https://github.com/limix/glimix-core"
    pypi = "glimix-core/glimix-core-3.1.13.tar.gz"

    version("3.1.13", sha256="a382a0f6de89c96b474f4ede9a8549539c9b65d2f1b6877dca4f0738d2d4055d")

    depends_on("python@3.8:3.12", type=("build", "run"))
    depends_on("py-brent-search", type=("build", "run"))
    depends_on("py-liknorm@1.2.8:", type=("build", "run"))
    depends_on("py-ndarray-listener", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numpy-sugar", type=("build", "run"))
    depends_on("py-optimix", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pytest-doctestplus", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
