# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdMogene20St(RPackage):
    """Platform Design Info for Affymetrix MoGene-2_0-st

    Platform Design Info for Affymetrix MoGene-2_0-st
    """

    bioc = "pd.mogene.2.0.st"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mogene.2.0.st_3.14.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.mogene.2.0.st/pd.mogene.2.0.st_3.14.1.tar.gz",
    ]

    version(
        "3.14.1",
        sha256="28b2de14d9eda0bd0af25f1c4feabd548661ea34389ca36a5d6564d4cd940508",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
