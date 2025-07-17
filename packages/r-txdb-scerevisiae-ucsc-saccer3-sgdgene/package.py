# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbScerevisiaeUcscSaccer3Sgdgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Scerevisiae.UCSC.sacCer3.sgdGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Scerevisiae.UCSC.sacCer3.sgdGene_3.2.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Scerevisiae.UCSC.sacCer3.sgdGene/TxDb.Scerevisiae.UCSC.sacCer3.sgdGene_3.2.2.tar.gz",
    ]

    version(
        "3.2.2",
        sha256="6dac0b4f88ce54c8543bb0ce236507cd46dd78ff7b3e3457ef7fd0b1dca15cea",
    )

    depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
