# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcsmart(RPackage):
    """Multi sample aCGH analysis package using kernel convolution

    Multi sample aCGH analysis package using kernel convolution
    """

    bioc = "KCsmart"

    version("2.66.0", commit="a9fdcd80f7a146410ebde699b2566688b9ddf940")
    version("2.60.0", commit="cff4f6dea9d84f9fd6c641dc81a3e68749cc0211")

    depends_on("r-siggenes", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
