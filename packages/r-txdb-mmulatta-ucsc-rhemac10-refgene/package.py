# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmulattaUcscRhemac10Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Mmulatta.UCSC.rheMac10.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmulatta.UCSC.rheMac10.refGene_3.14.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmulatta.UCSC.rheMac10.refGene/TxDb.Mmulatta.UCSC.rheMac10.refGene_3.14.0.tar.gz",
    ]

    version(
        "3.14.0",
        sha256="2b52a9cf4568b128f4cbe9b271626e15f69dc0826701f2460042d053b4d1fd89",
    )

    depends_on("r-genomicfeatures@1.45.2:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
