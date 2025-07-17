# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdAtdschipTiling(RPackage):
    """Platform Design Info for Affymetrix Atdschip_tiling

    Platform Design Info for Affymetrix Atdschip_tiling
    """

    bioc = "pd.atdschip.tiling"

    version("0.46.0", commit="64c4c6996c169aff81f04db3f1626a577e0adbfe")
    version("0.40.0", commit="6baaf715d75712a1d18796b833541b40a2317ef6")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rsqlite@0.10:", type=("build", "run"))
    depends_on("r-oligoclasses@1.15.58:", type=("build", "run"))
    depends_on("r-oligo@1.17.3:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-biostrings@2.21.11:", type=("build", "run"))
    depends_on("r-iranges@1.11.31:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
