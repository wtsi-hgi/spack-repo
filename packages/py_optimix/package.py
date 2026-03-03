# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptimix(PythonPackage):
    """Abstract function optimisation."""

    homepage = "https://github.com/limix/optimix"
    pypi = "optimix/optimix-3.0.4.tar.gz"

    version("3.0.4", sha256="9f051d3ab947f7ad7c79439242426f53310bee298b3a53413f923f361f13c6c6")

    depends_on("py-brent-search@2.0.1:", type=("build", "run"))
    depends_on("py-ndarray-listener@2.0.1:", type=("build", "run"))
    depends_on("py-numpy@1.14.3:", type=("build", "run"))
    depends_on("py-pytest@6.0.0:", type=("build", "run"))
    depends_on("py-scipy@1.0.1:", type=("build", "run"))
    depends_on("py-tqdm@4.23.4:", type=("build", "run"))
