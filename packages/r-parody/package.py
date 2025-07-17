# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParody(RPackage):
    """Parametric And Resistant Outlier DYtection

    Provide routines for univariate and multivariate outlier detection with a focus on parametric methods, but support for some methods based on resistant statistics.
    """

    bioc = "parody"

    version("1.66.1", commit="8529446f16f7b62fa7051209db872c050c3fb205")
    version("1.60.0", commit="5b848de0055495dcb6398fd8b990684cc00a2d32")

    depends_on("r@3.5:", type=("build", "run"))
