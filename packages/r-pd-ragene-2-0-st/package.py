# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdRagene20St(RPackage):
    """Platform Design Info for Affymetrix RaGene-2_0-st

    Platform Design Info for Affymetrix RaGene-2_0-st
    """

    bioc = "pd.ragene.2.0.st"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.ragene.2.0.st_3.14.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.ragene.2.0.st/pd.ragene.2.0.st_3.14.1.tar.gz",
    ]

    version(
        "3.14.1",
        sha256="e92f0d14d395b444f1d32aafd86c6bdf3d47745d364b92fd1d051d10f68e04e7",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
