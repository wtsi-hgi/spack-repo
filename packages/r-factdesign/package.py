# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactdesign(RPackage):
    """Factorial designed microarray experiment analysis

    This package provides a set of tools for analyzing data from a factorial designed microarray experiment, or any microarray experiment for which a linear model is appropriate. The functions can be used to evaluate tests of contrast of biological interest and perform single outlier detection.
    """

    bioc = "factDesign"

    version("1.84.0", commit="0026802a444e74858c262c527f4cf8626e159242")
    version("1.78.0", commit="ca661fab167781d4cfc3c62a89bbb781e605290a")

    depends_on("r-biobase@2.5.5:", type=("build", "run"))
