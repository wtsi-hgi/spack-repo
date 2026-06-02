# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlopehunter(RPackage):
    """SlopeHunter is an R package containing tools for correcting for collider bias in conditional Genome-Wide Association Studies (GWAS)."""

    homepage = "https://github.com/Osmahmoud/SlopeHunter/"
    url = "https://github.com/Osmahmoud/SlopeHunter/archive/refs/tags/v1.1.0.tar.gz"

    version("1.1.0", sha256="1d0cc7e5b1e2a0008a25be50a291ca8a8c03c384583fbcc886619aad860b852f")
    version("1.0.1", sha256="cfa7b68e391b350ee0b160461a2d55a3e2edb1982a7b6abe21304318be7a9467")
    version("1.0.0", sha256="18486eb50df63c91a3777312dce24054bb527801df5151211b3d84b874e2e44d")
    version("0.0.2", sha256="646ca030485d3f6ee8ba379e7b48903764645ad90b2d27efce166ad450994521")

    depends_on("r-ggplot2@2.1.0:", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-ieugwasr", type=("build", "run"))
    depends_on("r-data-table@1.14.2:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
