# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbDrerioUcscDanrer10Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Drerio.UCSC.danRer10.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Drerio.UCSC.danRer10.refGene_3.4.6.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Drerio.UCSC.danRer10.refGene/TxDb.Drerio.UCSC.danRer10.refGene_3.4.6.tar.gz",
    ]

    version(
        "3.4.6",
        sha256="d3ba3c965e6bf1006e4bd71c0cbac4dc06460b67c01c9c73dcd425b85b244dc7",
    )

    depends_on("r-genomicfeatures@1.35.11:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
