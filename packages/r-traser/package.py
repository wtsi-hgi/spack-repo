# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraser(RPackage):
    """GWAS trait-associated SNP enrichment analyses in genomic intervals

    traseR performs GWAS trait-associated SNP enrichment analyses in genomic intervals using different hypothesis testing approaches, also provides various functionalities to explore and visualize the results.
    """

    bioc = "traseR"

    version("1.38.0", commit="6f24513677ced75d145904bcf8b033c388ddb4a7")
    version("1.32.0", commit="27f15937a4d96ac319f7c3ddf6dc48a51381747a")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
