# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafdbExacR10NontcgaHs37d5(RPackage):
    """Minor allele frequency data from ExAC release 1.0 subset of nonTCGA exomes for hs37d5

    Store minor allele frequency data from the Exome Aggregation Consortium (ExAC release 1.0 subset of nonTCGA exomes) for the human genome version hs37d5.
    """

    bioc = "MafDb.ExAC.r1.0.nonTCGA.hs37d5"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.ExAC.r1.0.nonTCGA.hs37d5_3.10.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MafDb.ExAC.r1.0.nonTCGA.hs37d5/MafDb.ExAC.r1.0.nonTCGA.hs37d5_3.10.0.tar.gz",
    ]

    version(
        "3.10.0",
        sha256="a507120e7d266dee30a339fb3e5db0b6094e3c9c25d5cdf18d34829e6c623ceb",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.ExAC.r1.0.nonTCGA.hs37d5_3.10.0.tar.gz",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicscores@1.9.6:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
