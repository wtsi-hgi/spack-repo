# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbamr(RPackage):
    """Generating SAM file for PSMs in shotgun proteomics data

    Mapping PSMs back to genome. The package builds SAM file from shotgun proteomics data The package also provides function to prepare annotation from GTF file.
    """

    bioc = "proBAMr"

    version("1.42.0", commit="fb3cc99008b04e88b87a647cc21e986f5464a6af")
    version("1.36.0", commit="49db4d211f085c1cb4b7a4c1600647aaf97c2617")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    # Required by DESCRIPTION: txdbmaker (Bioconductor) -> r-txdbmaker in Spack
    depends_on("r-txdbmaker", type=("build", "run"))
