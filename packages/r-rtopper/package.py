# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtopper(RPackage):
    """This package is designed to perform Gene Set Analysis across multiple genomic platforms

    the RTopper package is designed to perform and integrate gene set enrichment results across multiple genomic platforms.
    """

    bioc = "RTopper"

    version("1.54.0", commit="d3232c0973d5423bbaf51f5e75c0facbfd808b9a")
    version("1.48.0", commit="7abb24c911fe01875d99d2891a1e6d5ae7f859ac")

    depends_on("r@2.12:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
