# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm39Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Mmusculus.UCSC.mm39.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm39.refGene_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm39.refGene/TxDb.Mmusculus.UCSC.mm39.refGene_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="bb79c5dfaca582f2d8436777afc0b94c7f7b2be7bb37ed6442a4b49f9848e338",
    )

    depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
