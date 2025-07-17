# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbDmelanogasterUcscDm6Ensgene(RPackage):
    """Annotation package for TxDb object(s)

    Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
    """

    bioc = "TxDb.Dmelanogaster.UCSC.dm6.ensGene"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Dmelanogaster.UCSC.dm6.ensGene_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Dmelanogaster.UCSC.dm6.ensGene/TxDb.Dmelanogaster.UCSC.dm6.ensGene_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        sha256="042317df9bddefa7979c815a8b88e17b5b55947b42e784c608b9d689fd3f327a",
    )

    depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
