# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmadb(RPackage):
    """R wrapper for the OMA REST API

    A package for the orthology prediction data download from OMA database.
    """

    homepage = "https://github.com/DessimozLab/OmaDB"
    bioc = "OmaDB"

    version("2.24.0", commit="810564161ba994b66b864a10f8920760f6615623")
    version("2.18.0", commit="88c9a3a75ac347e0bf6befa62230a47bf253ddb5")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-httr@1.2.1:", type=("build", "run"))
    depends_on("r-plyr@1.8.4:", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
