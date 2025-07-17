# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomewidesnp5crlmm(RPackage):
    """Metadata for fast genotyping with the 'crlmm' package

    Package with metadata for fast genotyping Affymetrix GenomeWideSnp_5 arrays using the 'crlmm' package. Annotation build is hg19.
    """

    bioc = "genomewidesnp5Crlmm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/genomewidesnp5Crlmm_1.0.6.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/genomewidesnp5Crlmm/genomewidesnp5Crlmm_1.0.6.tar.gz",
    ]

    version(
        "1.0.6",
        sha256="e86e0b6be47f61b654feea5e3e4c2bd47d2cc4ad4d806c8d1f65bde1a5e5b519",
    )
