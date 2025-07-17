# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbGgallusUcscGalgal5Refgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Ggallus.UCSC.galGal5.refGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Ggallus.UCSC.galGal5.refGene_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Ggallus.UCSC.galGal5.refGene/TxDb.Ggallus.UCSC.galGal5.refGene_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        sha256="387038675be962d6550866e1f72097ca86b4eacb362d811651a15352a39580ba",
    )

    depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
