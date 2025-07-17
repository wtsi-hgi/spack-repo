# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedtbdata(RPackage):
    """Curation of existing 49 tuberculosis transcriptomic studies

    The curatedTBData is an R package that provides standardized, curated tuberculosis(TB) transcriptomic studies. The initial release of the package contains 49 studies. The curatedTBData package allows users to access tuberculosis trancriptomic efficiently and to make efficient comparison for different TB gene signatures across multiple datasets.
    """

    homepage = "https://github.com/compbiomed/curatedTBData"
    bioc = "curatedTBData"

    version("2.4.0", commit="01d2f0d038d278e19ffc896eb8298e217735fe48")
    version("1.8.0", commit="7433b35ea15e79aff906c8672a0aeea2f7631e67")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
