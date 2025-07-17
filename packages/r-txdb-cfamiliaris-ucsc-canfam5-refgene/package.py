# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCfamiliarisUcscCanfam5Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Cfamiliaris.UCSC.canFam5.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Cfamiliaris.UCSC.canFam5.refGene_3.14.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Cfamiliaris.UCSC.canFam5.refGene/TxDb.Cfamiliaris.UCSC.canFam5.refGene_3.14.0.tar.gz",
    ]

    version(
        "3.14.0",
        sha256="b26de4e79584660605f69f3daeeabaf03b75f96c1668e55571c86612706c6ac6",
    )

    depends_on("r-genomicfeatures@1.45.2:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
