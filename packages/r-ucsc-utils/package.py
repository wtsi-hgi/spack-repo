# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcscUtils(RPackage):
    """UCSC Utils.

    Utilities for interacting with UCSC genome browser data."""

    bioc = "UCSC.utils"

    license("Artistic-2.0")

    version("1.4.0", sha256="09f372de865600d96885830f78570b6b")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://bioconductor.org/packages/release/bioc/src/contrib/UCSC.utils_{0}.tar.gz"
        return url.format(version)
