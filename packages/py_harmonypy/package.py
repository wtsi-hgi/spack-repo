# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHarmonypy(PythonPackage):
    """Harmony is an algorithm for integrating multiple high-dimensional datasets."""

    homepage = "https://github.com/slowkow/harmonypy"
    pypi = "harmonypy/harmonypy-0.0.9.tar.gz"

    version("0.0.9", sha256="85bfdd4e6ec6e0fa8816a276639358d3598a40d60ba9f7a5d9dada8706be8c4d")

    depends_on("py-numpy@1.13:", type=("build", "run"))
    depends_on("py-scipy@1.2:", type=("build", "run"))
    depends_on("py-scikit-learn@0.21:", type=("build", "run"))
    depends_on("py-pandas@0.25:", type=("build", "run"))
