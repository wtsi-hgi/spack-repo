# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdFelgene10St(RPackage):
    """Platform Design Info for Affymetrix FelGene-1_0-st

    Platform Design Info for Affymetrix FelGene-1_0-st
    """

    bioc = "pd.felgene.1.0.st"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.felgene.1.0.st_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.felgene.1.0.st/pd.felgene.1.0.st_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        sha256="06c24498fd8c6d43e463b857fb4f83c71b29e49eb7392ba2e52e5ff9c7a5c3d1",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
