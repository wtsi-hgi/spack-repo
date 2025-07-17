# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHugene21St(RPackage):
    """Platform Design Info for Affymetrix HuGene-2_1-st

    Platform Design Info for Affymetrix HuGene-2_1-st
    """

    bioc = "pd.hugene.2.1.st"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hugene.2.1.st_3.14.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.hugene.2.1.st/pd.hugene.2.1.st_3.14.1.tar.gz",
    ]

    version(
        "3.14.1",
        sha256="1065a1666ec9d241c0a6518c0b2cb4fcbee13dcbdc098aaaa3713303043a8a1e",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
