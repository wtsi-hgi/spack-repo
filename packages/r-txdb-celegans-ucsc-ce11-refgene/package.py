# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCelegansUcscCe11Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Celegans.UCSC.ce11.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Celegans.UCSC.ce11.refGene_3.4.6.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Celegans.UCSC.ce11.refGene/TxDb.Celegans.UCSC.ce11.refGene_3.4.6.tar.gz",
    ]

    version(
        "3.4.6",
        sha256="c67e3026fa905784f594a095f18d5c2c56a665ce0d5101f08afc18262c9404ab",
    )

    depends_on("r-genomicfeatures@1.35.11:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
