# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafdb1kgenomesPhase1Grch38(RPackage):
    """Minor allele frequency data from 1000 Genomes Phase 1 for GRCh38

    Store minor allele frequency data from the Phase 1 of the 1000 Genomes Project for the human genome version GRCh38.
    """

    bioc = "MafDb.1Kgenomes.phase1.GRCh38"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.1Kgenomes.phase1.GRCh38_3.10.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MafDb.1Kgenomes.phase1.GRCh38/MafDb.1Kgenomes.phase1.GRCh38_3.10.0.tar.gz",
    ]

    version(
        "3.10.0",
        sha256="8ce616ff5abb70795d818c959b048d0ce84a4c82904c853d15e3c6be6b18e514",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.1Kgenomes.phase1.GRCh38_3.10.0.tar.gz",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicscores@1.9.6:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
