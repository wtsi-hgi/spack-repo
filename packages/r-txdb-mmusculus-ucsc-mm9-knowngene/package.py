# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm9Knowngene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Mmusculus.UCSC.mm9.knownGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm9.knownGene_3.2.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm9.knownGene/TxDb.Mmusculus.UCSC.mm9.knownGene_3.2.2.tar.gz",
    ]

    version(
        "3.2.2",
        sha256="a2d760206336d0c1ba48108ba3e23b201aa429a6b88a19437270980180ef7299",
    )

    depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
